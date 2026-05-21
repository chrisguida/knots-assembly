#!/usr/bin/env bash
# After the fetch step in the CI workflow brings all required commits into
# the object database, this script forces every branch ref to match its
# release-time SHA, taken from the second parent of each merge commit on
# the first-parent chain of the target release.
#
# Why:
#   luke-jr/bitcoin feature branches are MUTABLE. Luke continues advancing
#   them after a release is tagged. Fetching the current tip gives newer
#   commits than what Luke actually merged at release time; the driver
#   then merges the newer tip, produces a diverging tree, and downstream
#   merges hit conflicts the recorded autoresolvers don't match.
#
#   For historical reproduction, the authoritative source for branch tips
#   is the release tag itself: each "Merge <prnum> via <branch>" commit on
#   the first-parent chain has the branch's release-time tip as its second
#   parent. We walk every such commit and update-ref accordingly.
#
# Ported from knots-knowledge/scripts/15-synthesize-refs.sh.

set -euo pipefail
. "$(dirname "$0")/lib.sh"

[ -d "$BITCOIN/.git" ] || die "$BITCOIN is not a git clone"

BASE_TAG="$(resolve_base_tag)"
git -C "$BITCOIN" rev-parse --verify --quiet "$RELEASE_TAG" >/dev/null \
  || die "$RELEASE_TAG not present; fetch it first"
git -C "$BITCOIN" rev-parse --verify --quiet "$BASE_TAG" >/dev/null \
  || die "$BASE_TAG not present; fetch it first"

mkdir -p "$OUT"

# Auto-generated spec overrides: sed substitutions for cherrypick sources
# Luke has kept only in his local working repo. For each spec line
# `(cherrypick=X) Y` where X is not in our object database, Y is the
# previous release's equivalent commit; find the current release's
# equivalent commit Z and substitute X with Z. Two strategies, in order:
#
#   1. parent2-of-merge: works when the driver wraps the cherrypick in a
#      merge commit with parent2 == Y (drivers v29.2+).
#   2. file-set match: works when the cherrypick landed as a plain
#      non-merge commit (older drivers). Matches by the file-set the
#      commit touches relative to its first parent.
AUTO_SED="$OUT/${TAG_SHORT}.auto-overrides.sed"
: > "$AUTO_SED"

file_set_of() {
  git -C "$BITCOIN" diff --name-only "$1^1" "$1" 2>/dev/null \
    | sort \
    | tr '\n' '|'
}

# Resolve a short SHA prefix (typically 11 chars, as stored in spec
# `last=` fields) to its full 40-char SHA via GitHub's REST API.
# Echoes the full SHA on success, nothing on failure.
#
# Why: the spec records `last=<sha>` as short prefixes for readability.
# When the referenced branch has drifted past that tip (normal
# upstream-PR maintenance per MAINTAINER.md S3 / NOTES F13), the
# recorded SHA becomes orphaned: still preserved as an object on
# GitHub's servers, but no longer reachable from any current ref.
#
# GitHub keeps orphan commits queryable for as long as it retains
# them, and they remain fetchable via `git fetch <remote> <sha>` IF
# the wire protocol's allowReachableSHA1InWant is on (it is, for
# bitcoin / bitcoinknots / luke-jr) -- BUT the git protocol requires
# the FULL 40-char SHA. Anything shorter is interpreted as a ref name
# and returns `fatal: couldn't find remote ref`. GitHub's REST API,
# by contrast, accepts any unambiguous prefix on `/repos/<owner>/<repo>/commits/<sha>`.
# We use it to expand short -> full, then hand the full SHA to git.
#
# This adds api.github.com as a runtime dependency on top of the
# existing github.com clone dependency. The whole pipeline already
# requires GitHub-the-service to exist (every remote URL is
# github.com); the marginal cost of an additional REST endpoint is
# small. If GitHub ever stops being the canonical home for these
# repos, the whole pipeline needs rethinking regardless.
#
# Args: <short_sha> <remote-name-in-bitcoin-clone>
expand_short_sha_via_rest_api() {
  # Defensive: runs under `set -euo pipefail`. This function MUST
  # `return 0` on every path -- a non-zero return propagates through
  # the caller's `resolved=$(...)` assignment (a simple command) and
  # trips set -e, killing the whole run.
  local short="$1" remote="$2"
  local url owner_repo resp
  url=$(git -C "$BITCOIN" remote get-url "$remote" 2>/dev/null) || return 0
  # Reduce the remote URL to <owner>/<repo>. Parsed with case +
  # parameter expansion rather than a regex: POSIX ERE has no
  # reliable non-greedy quantifier, so a pattern like
  # `([^/]+/[^/]+?)(\.git)?` lets group 1 swallow the `.git` suffix.
  case "$url" in
    https://github.com/*) owner_repo="${url#https://github.com/}" ;;
    http://github.com/*)  owner_repo="${url#http://github.com/}" ;;
    git@github.com:*)     owner_repo="${url#git@github.com:}" ;;
    *) return 0 ;;
  esac
  owner_repo="${owner_repo%.git}"
  [ -n "$owner_repo" ] || return 0
  command -v curl >/dev/null 2>&1 || return 0
  resp=$(curl -sf --max-time 15 \
    "https://api.github.com/repos/$owner_repo/commits/$short" 2>/dev/null) \
    || return 0
  # The top-level "sha" is the first 40-hex value in the response.
  if [[ "$resp" =~ \"sha\"[[:space:]]*:[[:space:]]*\"([a-f0-9]{40})\" ]]; then
    printf '%s\n' "${BASH_REMATCH[1]}"
  fi
  return 0
}

declare -A PARENT2_TO_COMMIT
while IFS='|' read -r csha cpar; do
  p2=$(printf '%s\n' "$cpar" | awk '{print $2}')
  [ -n "$p2" ] || continue
  PARENT2_TO_COMMIT[$p2]="$csha"
done < <(git -C "$BITCOIN" log --first-parent --merges --pretty='%H|%P' "$BASE_TAG..$RELEASE_TAG")

declare -A FILESET_TO_COMMIT
while read -r csha; do
  fs=$(file_set_of "$csha")
  [ -n "$fs" ] || continue
  FILESET_TO_COMMIT[$fs]="$csha"
done < <(git -C "$BITCOIN" log --first-parent --pretty='%H' "$BASE_TAG..$RELEASE_TAG")

cherrypick_fixed=0
while IFS=$'\t' read -r cherry lastapply; do
  if git -C "$BITCOIN" cat-file -e "$cherry" 2>/dev/null; then
    continue
  fi
  if ! git -C "$BITCOIN" cat-file -e "$lastapply" 2>/dev/null; then
    say "  WARN: cherrypick=$cherry has unreachable lastapply $lastapply; cannot auto-substitute"
    continue
  fi
  substitute=""
  for p2key in "${!PARENT2_TO_COMMIT[@]}"; do
    if [ "${p2key#$lastapply}" != "$p2key" ]; then
      substitute="${PARENT2_TO_COMMIT[$p2key]}"
      break
    fi
  done
  if [ -z "$substitute" ]; then
    fs=$(file_set_of "$lastapply")
    if [ -z "$fs" ]; then
      say "  WARN: empty file-set for lastapply $lastapply (cherrypick=$cherry); cannot auto-substitute"
      continue
    fi
    substitute="${FILESET_TO_COMMIT[$fs]:-}"
    if [ -z "$substitute" ]; then
      say "  WARN: no release commit matches file-set of lastapply $lastapply for cherrypick=$cherry"
      continue
    fi
  fi
  printf 's/cherrypick=%s/cherrypick=%s/\n' "$cherry" "$substitute" >> "$AUTO_SED"
  cherrypick_fixed=$((cherrypick_fixed+1))
done < <(perl -ne '
  s/\s*#.*//;
  next unless /\(cherrypick=([a-f0-9]+)\)\s+([a-f0-9]+)/;
  print "$1\t$2\n";
' "$SPEC")

say "walking $BASE_TAG..$RELEASE_TAG merges, pinning refs to release-time SHAs"
printf '%s\t%s\t%s\t%s\n' branch release_sha current_sha_at_run status > "$DRIFT_LOG"

match=0; drift=0; created=0; skipped_nm=0; skipped_unparsed=0; caret=0; directpin=0

while IFS='|' read -r sha subject parents; do
  is_null=0
  case "$subject" in
    "NULL-Merge "*) is_null=1 ;;
  esac

  if [[ "$subject" =~ ^(NULL-|Tree-)?Merge\ ([a-zA-Z0-9#]+\ via\ )?(.+)$ ]]; then
    branch="${BASH_REMATCH[3]}"
  else
    skipped_unparsed=$((skipped_unparsed+1))
    continue
  fi

  caret_suffix=""
  if [[ "$branch" == *"^"* ]]; then
    caret_suffix="${branch#*^}^"
    branch="${branch%%^*}"
  fi

  if [ "$is_null" = "1" ]; then
    skipped_nm=$((skipped_nm+1))
    continue
  fi

  parent2=$(printf '%s\n' "$parents" | awk '{print $2}')
  [ -n "$parent2" ] || continue

  # Direct remote merge: the driver refuses to merge any slash-form remote
  # ref without a `last=` pin (unpinned slash-form merges are
  # non-deterministic). Old specs frequently omit the pin since it was
  # ambient at authoring time. parent2 IS the release-time tip, so emit a
  # spec rewrite appending `last=<parent2>` to that line when it has none.
  if [[ "$branch" == */* ]]; then
    needs_pin=$(perl -ne '
      s/\s*#.*//;
      next unless /^\s*(?:NM|TM|[am]*)\t\s*(?:[a-z]?\d+|\-|n\/a)\s+(\S+)/;
      next unless $1 eq "'"$branch"'";
      print "yes" unless /last=/;
      exit;
    ' "$SPEC")
    if [ "$needs_pin" = "yes" ]; then
      printf 's#%s#%s last=%s#\n' "$branch" "$branch" "$parent2" >> "$AUTO_SED"
      printf '%s\t%s\t%s\t%s\n' "$branch" "$parent2" "-" "direct-pin" >> "$DRIFT_LOG"
      directpin=$((directpin+1))
    fi
  fi

  case "$branch" in
    */*) ref="refs/remotes/$branch" ;;
    *)   ref="refs/heads/$branch"   ;;
  esac

  if [ -n "$caret_suffix" ]; then
    last_sha=$(perl -ne '
      s/\s*#.*//;
      next unless /^\s*(?:NM|TM|[am]*)\t\s*([a-z]?\d+|\-|n\/a)\s+(\S+)/;
      my ($pr, $br) = ($1, $2);
      next unless $br eq "'"$branch$caret_suffix"'";
      if (/last=([a-f0-9]+)/) {
        print $1;
        exit;
      }
    ' "$SPEC")
    if [ -z "$last_sha" ]; then
      say "  WARN: caret branch $branch$caret_suffix has no last= in spec; skipping"
      continue
    fi
    # Default to using last_sha as-is. If we resolve it to full via
    # the REST API below, use that full form for the update-ref so
    # git doesn't have to re-resolve the prefix later.
    full_sha="$last_sha"
    if ! git -C "$BITCOIN" cat-file -e "$last_sha" 2>/dev/null; then
      say "  resolving orphan $last_sha for caret branch $branch$caret_suffix"
      fetched=0
      for remote in luke-jr upstream origin-pull origin-pull-g origin-pull-k origin; do
        if ! git -C "$BITCOIN" remote | grep -qxF "$remote" 2>/dev/null; then
          continue
        fi
        # GitHub's git wire protocol rejects short SHAs as fetch
        # targets. If last_sha is a prefix, resolve it to the full
        # 40-char SHA via the REST API first. See
        # expand_short_sha_via_rest_api() above.
        target="$last_sha"
        if [ "${#target}" -lt 40 ]; then
          resolved=$(expand_short_sha_via_rest_api "$last_sha" "$remote" || true)
          if [ -n "$resolved" ]; then
            target="$resolved"
            say "    $remote: REST API resolved $last_sha -> $target"
          fi
        fi
        if git -C "$BITCOIN" -c protocol.version=2 fetch "$remote" "$target" 2>/dev/null; then
          fetched=1
          full_sha="$target"
          say "    $remote: fetched $target"
          break
        fi
      done
      if [ "$fetched" = "0" ]; then
        say "  WARN: could not fetch $last_sha for caret branch $branch$caret_suffix"
        continue
      fi
    fi
    git -C "$BITCOIN" update-ref "$ref" "$full_sha"
    printf '%s\t%s\t%s\t%s\n' "${branch}${caret_suffix}" "$full_sha" "-" "caret-fetched" >> "$DRIFT_LOG"
    caret=$((caret+1))
    continue
  fi

  current=$(git -C "$BITCOIN" rev-parse --verify --quiet "$ref" 2>/dev/null || true)
  if [ -z "$current" ]; then
    git -C "$BITCOIN" update-ref "$ref" "$parent2"
    printf '%s\t%s\t%s\t%s\n' "$branch" "$parent2" "-" "created" >> "$DRIFT_LOG"
    created=$((created+1))
  elif [ "$current" = "$parent2" ]; then
    match=$((match+1))
  else
    git -C "$BITCOIN" update-ref "$ref" "$parent2"
    printf '%s\t%s\t%s\t%s\n' "$branch" "$parent2" "$current" "drift" >> "$DRIFT_LOG"
    drift=$((drift+1))
  fi
done < <(git -C "$BITCOIN" log --first-parent --merges --pretty='%H|%s|%P' "$BASE_TAG..$RELEASE_TAG")

say "synthesis complete"
say "  match:     $match branches already at release-time SHA"
say "  drift:     $drift branches overwritten (pre-drift SHA logged)"
say "  created:   $created new refs (no prior fetch target)"
say "  skipped:   $skipped_nm NULL-merges (parent2 is a runtime-generated revert)"
say "  caret:     $caret caret-suffix merges resolved via last=<sha> fetch"
say "  directpin: $directpin unpinned direct-remote merges given synthesized last="
say "  crp-fix:   $cherrypick_fixed cherrypick sources auto-substituted"
[ -s "$AUTO_SED" ] && say "  auto-overrides file: $AUTO_SED"
[ "$skipped_unparsed" -eq 0 ] || say "  unparsed: $skipped_unparsed merge subjects I couldn't match"
say "drift log: $DRIFT_LOG"

if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  {
    echo "## Synthesized release-time refs"
    echo
    echo "Branch refs rewritten to the SHAs that were current when \`$RELEASE_TAG\` was tagged."
    echo
    echo "| metric | count |"
    echo "|--------|-------|"
    echo "| already at release-time SHA | $match |"
    echo "| drift (overwritten)         | $drift |"
    echo "| new refs created            | $created |"
    echo "| NULL-merges skipped         | $skipped_nm |"
    echo "| caret-suffix resolutions    | $caret |"
    echo "| direct-pin synthesis        | $directpin |"
    echo "| cherrypick substitutions    | $cherrypick_fixed |"
  } >> "$GITHUB_STEP_SUMMARY"
fi
