#!/usr/bin/env bash
# Check the assemble-knots/ submodule out at the assembler version we want to
# reproduce with -- by default the head of assemble-deriv PR #3 ("Honor
# --skip-update-check for CHECK-LAST lines"), which this branch exists to
# exercise.
#
# This replaces the historical per-spec pin (which followed the spec commit's
# submodule pointer to whatever driver the Knots maintainer used at the time).
# A Knots maintainer states the latest assembler is backwards-compatible with
# every historical spec, so a single assembler can build any release; this
# branch verifies that for PR #3 specifically, with the CHECK-LAST workaround
# removed from run-driver.sh.
#
# Override the ref with KNOTS_ASSEMBLER_REF -- e.g. `master` once the PR is
# merged, or any branch/tag/SHA reachable from the submodule's origin
# (bitcoinknots/assemble-deriv).

set -euo pipefail
. "$(dirname "$0")/lib.sh"

ASSEMBLER_REF="${KNOTS_ASSEMBLER_REF:-pull/3/head}"

# Idempotent submodule init for a fresh local clone without
# --recurse-submodules.
sub_path="$(basename "$ASSEMBLE")"
if [ ! -e "$ASSEMBLE/.git" ]; then
  say "initialising $sub_path submodule"
  git -C "$TMP" submodule update --init -- "$sub_path"
fi

say "fetching assembler ref '$ASSEMBLER_REF' from origin (bitcoinknots/assemble-deriv)"
git -C "$ASSEMBLE" fetch --quiet origin "$ASSEMBLER_REF"
git -C "$ASSEMBLE" -c advice.detachedHead=false checkout FETCH_HEAD
say "$sub_path HEAD -> $(git -C "$ASSEMBLE" rev-parse HEAD)"
