timestamp 2025-03-05 03:27:08
lastapply no-merge

#.. checked up to PR #31992 / gui #855

checkout v29.0rc3
@28.x-syslibs
# BUILD BUGS:
	#29.xTODO# Triage: g841 furszy-g/2024_gui_rpconsole_walletmodel_dependency
	#29.xTODO# If needed? 30997 hebasto/240928-qt6
# SYSLIBS:
	2241  sys_leveldb							91af8d0c4ea
	5416  sys_libsecp256k1						3d441102525
	# TODO: sys_crc32c ??
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	n/a   rm_minisketch-29+syslibs				723ceffb7b7
		# Implicitly includes most of #18818
		#30.xTODO# sys_libminisketch
	15155 test_external_bcli					7d6366b5659
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	n/a   (delete_release_notes_fragments)
@28.x-knotsfixes
# TESTS:
	# If needed: -     ci_knots-26							e2099d64846
	# If needed: -     lint_relaxer-28+knots					efeece9f031
	# If needed: -     nowarn_unreachable-code				ad6a12d7bbc
	# If needed: -     nowarn_unused-function				45a2e5951ce
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
	# If needed: -     ci_i686mp_clang15						955f1eeed99
# FIXES:
	13789 asm_bypass_cxxflags					22df203e4cd
	32217 fix_gitdir_foreign
		# Was part of #18902
	-     relsrc_embed_tagname-29+knots
		# Was part of #18902
	18427 2020mingwthrd-mini					da1e5f9ffae	 # Latest code now
	18490 bugfix_symcheck_pe_case				d2d3b434b08
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 http_bind_error						def0d7f8f83	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					d0f65e2f2e4
		# NOTE: libevent-copied code more-or-less up to date as of 2025-04-04 112421c8fa4840acd73502f2ab6a674fc025de37 (upstream has added more portable TCP keepalive, setting keepalive interval to 5min, failure if setting keepalive or reusable fail, and merged 1a6dd1ff1b8 but not e8461128b8d,5a067073d77,45dd91f71f4)
	 9524  rpc_pruneblkchain0					85dc1e1fc32	last=88883ae13d
	10731 log_more_uacomment					cbfa6e5b9be
	29614 bufferedfile_fclose					4be2187282d
	14485 fadvise-29+knots						efcc7b7a087  # Latest code now
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					cfdde513b64
	-     fix_rpc_arg_multiname					3b0c1f0add6
	-     bugfix_rpc_getbalance_hacky			ccf3424296e
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted -OR- 27539 Empact/2023-04-minimum-file-descriptor-18911
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	18194 bugfix_gui_edit_sendaddr-mini			e9d0a3182b0	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				12d357c6255	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect OR 27245 fjahr/202303-pr19434 OR 27909
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	g152  gui_notify_setup_bg					f81eeca008a
	-     bugfix_gui_drop_abc_confusing_hack	85e32c93b2b
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	g236  gui_init_walleterror_cont				d40c1220043
	-     rpc_addconnection_mainnet				72ac99f48a5
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	30756 subproc_closefds						fd30be38f53
		# Replaces #22417 (Boost::Process variant)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				159d9c36b05
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs work: 23502 achow101/tr-low-fee-est
		# "rebase" in #26573 for post-#26567 refactor
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	g506  qt_qrcode_sizefixes					36c41fed21b
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs review: 24066 whitslack/openrc-daemonwait
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				7dc92f9cc9f
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-28+knots			bea0c626a1a	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	# Needs review: 24972 hebasto/220425-no-libtool
	# Needs review: 24994 hebasto/220426-consensus
	g595  qt_handle_autostart_errors-0.15		3da9f0c4b0b	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	-   gui_psbt_error_msgbox					5a1384386db
		# WAS: g599  ts_20220515-partial-25				5191aa16ac2	last=d9411324066 ts_20220515
			# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
			#TsTODO# Update with other commit (unit translations) when translations supported again
	29868 hww_windows-29						301886f3d0e	last=5541ef02f71 hebasto/240414-win-subprocess
		# Replaces: -     hww_windows-27						e1f9c1bbde8
			# Reverts #29489 & #28967
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
	# Needs review: 25380 darosior/fee_estimator_disable_cpfp
	# Check on #25561
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	# Needs review: 25698 -  # crypto: avoid potential buffer overread in ChaCha20::SetKey
	g633  -										2b6dec6757f	last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	# Needs review: 25938 mzumsande/202208_fixed_cjdns
	g662  qt_fix_txview_202209					0e9150347ec
		# Includes gui#368
	# TODO: Needs review: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	# TODO: Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	# TODO: Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	# TODO: Sane fix for #24049
	g677 fix_qt_peers_na						db82f05cfd3
	# Needs work/review: 26426 fjahr/202210-coinstatsindex-overflow
	# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs review: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-28+knots	f182f096cf2	last=a6f567590b7
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	# TODO: CAUTION: #27307 was merged, but "this appears to possibly show a higher balance than the user actually has for sure??" - investigate
	# Alternative to: 27434 pinheadmz/chaintips-invalid
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#28.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	-     qafix_assert_debug_log_create			8d840e79471
	-     acceptstalefeeestimates_mainnet_opt	04db65df5ea
		# Currently (28.1) needs qafix_assert_debug_log_create
	# Needs review: 27684 hebasto/230516-punish OR ???
	#28.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 forbid_nohelp-29						387a5cf295c	last=bfc2bb6a270
	# Needs review: 27820 -  # Sanitizing ports of -rpcconnect and -rpcport.
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	# Needs review: 27912 -  # net: run disconnect in I2P thread
	# Needs work: 27973 maflcko/2306-byte-span-
	# Needs work: 27991 fanquake/instrument_libsecp
	28029 fix_zmq_errhandling_202307-mini		24565dab864	last=ba28af94bd5 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err		52de30f4845
	# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Needs concept: 28205 theStack/202308-netprocessing-reallow_fetching_of_genesis_block
	# 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	# Triage #28248
	28345 fix_bytespersigop_checks-mini			8e36b819288	last=6f627727739 fix_bytespersigop_checks
		#29.xTODO# NOTE: Excludes removal of buggy wrapper for diff-minimisation; needs checking manually (to ensure wrapper doesn't get used even in final/complete merge of all PRs) when assembly done; known issues: stash 172d7d7a9
		# Related bug in #18479
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	#29.xTODO# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	28616 Sjors/2023/10/assume-unconfirmed		f7e50a7e3f3	last=3e281590c7d  # assumeutxo_unconfirmed_ux_Sjors-28
	-     assumeutxo_unconfirmed_ux-29			46c7684bc14
	-     qt_recomm_confirms-0.9				3a77d04cbd5
		# NOTE: Un-hardcoding 6 already taken care of in assumeutxo_unconfirmed_ux above (956546a1f2f)
	# Needs review & triage: 28678 sipa/202310_miniscript_assume
	# Needs review: 28776 BrandonOdiwuor/gui_overview_page_add_used_balance
	# -- Needs review: g775 -  # gui: add used balance to overview page
	# Needs review: 28780 -  # log: torcontrol opt checks
	-     fix_keep_notmy_cookie					16aacf2a6f8
		# Originally part of #28784, but regressed in d95dde9441f...7cb9367157e
	# Needs review: 28824 fix_asm_nodecimals-23								last=fde11cb0fa3 willcl-ark/asm-full-hex
		# FIXME: disambiguate opcodes too?
	28944 ishaanam/sendall_anti_fee_sniping		25117369373	last=b11d00d54ed  # rpc_sendall_anti_fee_sniping-27
	29141 fix_rpcauth_blank						3ad996f41bb
	# Needs review: 29124 achow101/fix-double-keypath
	# Needs work: 29147 guix_attachable_sigs					ad4fe4b83a4
		# GPG discourages clearsign signatures!
		#29.xTODO# but windows has lots of problems with existing style...
		#29.xTODO# but deviating from Core signing may reduce participants?
	# Needs review: 29155 -  # wallet: move lock at the top of ReleaseWallet
	29175 -										5f08e7fee5b	last=be8ae64b82e  # rpc: validate fee estimation mode case insensitive (fix_rpc_estmode_unset_case-24)
	# Needs review: g786  -  # FIX:When opening or autoloading wallets there should be clear messages about rescanning in progress and wallets' names.
	29307 AutoFile_error_check-29				17291246d08	last=dba78353868 vasild/AutoFile_error_check
	# Needs work: g792 -  # Correct tooltip wording for watch-only wallets
	# Nothing to fix? 29589 -  # tests: fix OP_1NEGATE handling in CScriptOp
	#28.xTODO# Needs review? 29640 -  # Fix tiebreak when loading blocks from disk (and add tests for comparing chain ties)
	#28.xTODO# Needs review: 29652 ryanofsky/pr/noloc
	#28.xTODO# Needs review: 29664 mzumsande/202403_near_tip_stalling
	29678 fix_init_lowdisk_warning_reqd^		8c4f8f40807	last=c452d6c1efe fix_init_lowdisk_warning_reqd
	# Needs review: 29680 -  # wallet: fix unrelated parent conflict doesn't cause child tx to be marked as conflict
	# Needs review: 29770 fjahr/2024-03-check-undo-index
	# Needs review: 29796 fanquake/depends_0g_debug_flags
	-     fix_rpc_warnings_all-28				6fb830e0d2d
	# Needs review: 29913 furszy/2024_fix_reconsiderblock_bestheader
	g815  fix_qt_privacy_before_open-23			20bc0e347cd	last=0dc337f73d0
		# Rewrote myself due to overcomplication and race bug in PR
	# Not worth it? 29963 hebasto/240425-guess-cc
	#28.xTODO# Needs review: 30079 ismaelsadeeq/05-2023-ignore-transactions-with-parents
	-     jonatack/2024-05-fix-cjdns-detection-in-AddNode	0a3e577e9e8	last=be4541abe59 jonatack/2024-05-fix-cjdns-detection-in-AddNode  # fix_cjdns_addnode_detect2-27+knots
	# Needs review: 30155 mzumsande/202405_replay_blocks
	#29.xTODO# Revert or semi-revert #30157 ?? (Mempool-influenced fee estimation)
	# Needs review & diff-minimising: 30207 mzumsande/202405_invalid_chains
	# Needs review & maybe wallet format finalization: 30221 achow101/wallet-no-chainstateflushed
	# Needs work: g823 -  # wallet: Improve error log color in the console
	-     detect_clang_bug96267					6da92446b43
	# Needs review: 30359 -  # Correct Error Code in OP_IF/OP_NOTIF Empty Stack Check
	# Needs review: 30465 hebasto/240716-deps-cmake
	# Needs review: 30469 fjahr/2024-07-csi-overflow-2
	# Needs review: 30479 mzumsande/202407_fix_resetfailure
	# If needed? 30489 theuni/depends-zmq-patch
	# Needs review: 30972 BrandonOdiwuor/wallet-listreceivedby-fix
	# Needs review: 31135 jonatack/2024-10-verification-progress or 31177 polespinasa/verificationProgress
	31275 -										ad6c4570514	last=49ffbc6077d  # fix_rpc_example_quoting_pr31275-24
	# Needs work? (adds overhead) 31298 -  # rpc: combinerawtransaction now rejects unmergeable transactions
	# Needs work: 31349 vasild:test_log_internet_traffic
	# Needs work: 31378 furszy/2024_wallet_migration_multisig_crash
	# Needs review: 31404 furszy/2024_descriptors_infer_multisig
	# Needs review: 31405 mzumsande/202411_stricter_invalidblock_handling
	# Needs review: 31423 furszy/2024_migration_watch-only_migration
	# Needs review/correctness per branch: Diff-minimise: 31449 -  # coins,refactor: Reduce getblockstats RPC UTXO overhead estimation
	31453 macos_exfat_warning-29+knots			25f0359c100	last=df1ba101419 willcl-ark/macos-exfat
		# Dropped doc change (links to Core github)
		# Added warning before leaving GUI firstrun screen
	# Needs review: 31492 -  # Execute Discover() when bind=0.0.0.0 or :: is set
	# Needs review: 31514 -  # wallet: allow lable for external descriptor & disallow label for ranged descriptors
	# Needs work: 31603 brunoerg/2025-01-descriptor-pk
	# Needs work? 31610 l0rinc/l0rinc/gettransaction-rpc-doc
	# Needs work: 31615 -  # Ensure assumevalid is always used during reindex
	# Needs review: 31622 achow101/psbt-sighashes
	# Needs review? 31727 darosior/2501_miniscript_nonfatal
	# Needs review? 31734 -  # miniscript: account for all StringType variants in Miniscriptdescriptor::ToString()
	# Needs review? 31774 -  # crypto: Use secure_allocator for AES256_ctx
	# Needs work & importance: 31775 -  # rpc: collect transaction fees on generateblock
	# Needs review: 31785 Sjors/2025/02/create_new_block
	# Needs review: 31807 theuni/fix-dupe-kernel-symbols
	31912 workaround_buggy_rndrrs-28			36e11bb93cc	last=2498dd8dbd5  # random: Check GetRNDRRS is supported in InitHardwareRand to avoid infinite loop
		# Held back 585aba6eec8..2498dd8dbd5 (2x diff for basically the same thing)
	# Needs review: 31835 -  # validation: set BLOCK_FAILED_CHILD correctly
	# Needs work: 31888 midnightmagic/fix-linearize-gjpyn
	# Needs review: 31929 hodlinator/2025/02/stop_http_robust
	31958 -										ee76cf26ae7	last=32dcec269bf  # rpc: add cli examples, update docs  # docfix_rpc_wallet_cf_psbt-24
	31979 -										056c95b3ff8	last=f708498293c  # torcontrol: Limit reconnect timeout to max seconds and log delay in whole seconds  # tor_backoff_max-26
	-     fix_rpccookieperms_early				dec38cfcc7b
	-     qt_intro_nojumpy						4ee79cc6ff2
	-     restore_guix_ppc64le-28				72fda2e9327
	-     qt_dialogs_less_modal					2822662e04d
	-     docfix_getorphantxs_vsize
		# Originally bundled in Knots with #30793 rpc_getorphantxs
	#28.xTODO# "Knots feature request: system notification for a txn should show the net wallet balance delta assuming the txn confirms, not whatever it does now that gives me a heart attack every time I use a large-ish UTXO lol" -Jason (currently only the first send of a sendmany is shown) https://github.com/bitcoin-core/gui/issues/853
	# TODO: prunenotify to run a command after each prune (eg, for fstrim or such)
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	# FIXME: https://twitter.com/tchjntr/status/1788332365887995925
		# weird bitcoin.conf results in:
		#	ASSERT failure in QList<T>::operator[]: "index out of range", file /bitcoin/depends/x86_64-w64-mingw32/include/QtCore/qlist.h, line 575
	# TODO: ensure that rejecting a tx also rejects dependents in the orphan pool
	#28.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
#@28.x-knots-lts-deps
	#28.xTODO# FIXME -     depends_qt5kde
@28.x-knots
# PERFORMANCE:
	# Needs review: 24158 JeremyRubin/epoch-mempool-reorg-updates
	# Needs review: 24589 -  # sha512.cpp improvements
	# Probably a bad idea: 24712 -  # wallet: reduce coin selection iterations
	# Knots doesn't support MSVC builds: 24773 Enable AVX2 implementation of SHA256 for MSVC builds
	# Needs work: 24901 -  # mempool: reduce lookups, insertions to cache in UpdateForDescendants
	# Needs review: 24926 -  # mempool: use mapNextTx.lower_bound in removeRecursive
	# Needs review: 25232 -  # rpc: Faster getblock API
	# Needs review: 25236 -  # wallet: use vector instead of list for transactions
	# Needs review & diff-minimising: 25297 -  # wallet: speedup transactions sync, rescan and load not flushing to db constantly
	# Needs review: 25968 sipa/202208_headerssync_optimize
	# Unclear benefit: 26375 zmq_optimise_duplread-27+k			3f9e56d77af	last=7b631dc9b19 andrewtoth/no-read-zmq
		# Several improvements in Knots branch
		# Post-#26415(merged), it's unclear if this is an improvement or potentially a performance loss: we either readback raw (from OS cache), or serialize CBlock
	# Needs review: 26486 sipa/202211_batchnotfound
	# Opt-in & needs review: 26951 pstratem/2023-01-23-gcsfilter
	# Needs review: 26966 furszy/2022_parallelize_blockfilter_index_2
	# Needs review: 27006 furszy/2022_reduce_cs_main_scope_blockindex_nfile
	# Needs concept/review: 27050 -  # p2p, validation: Don't download witnesses for assumed-valid blocks when running in prune mode
	# Needs review: 27427 -  # validation: Replace MinBIP9WarningHeight with MinBIP9WarningStartTime
	# Needs review? Part of? 28226 martinus:2023-08-more-CBufferedFile
	-     dbcache_1TB-29						2ed340330f1
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 -										5b3fb3eeb0f	last=42b25bbd939  # opti_merkle_mutation-0.17
	28592 -										88f7b4153a1 last=b81f37031c8  # txrelayrate_14txps-26
		# TODO: Make configurable? Or is that even sane?
	# MSVC: Needs review: 29036 theuni/msvc_fast_byteswap
	# Needs review?? 29159 -  # Update net.h bigger TCP socket using larger buffer
	# Needs review: 29473 -  # optimization: Speed up Base58 encoding by 400% by 64-bit preliminary byte packing
	# Needs review: 29491 fjahr/2024-02-batch-validation-updated
	# Needs review: 29578 brunoerg/2024-03-addrman-getaddr
	# Needs review: 29602 -  # refactor: Optimize IsSpace function for common non-whitespace characters
	# TODO: Revert #29815 ? (ie, use OS provided optimised timingsafe_bcmp)
	30059 dbfilesize_param-29+knots				add2386fdc7	last=c283a572145 dbfilesize_param
	-     dbfilesize_64-29+knots				6d097aed47f
	# Needs review: 30317 -  # WIP Simplify SipHash
	# Needs review: 30325 -  # optimization: Switch CTxMemPool::CalculateDescendants from set to vector to reduce transaction hash calculations
	# Needs review: 30370 fjahr/2024-07-pr28945
		# Was (never in Knots) #28945
	# Needs review? 30442 paplorinc/paplorinc/siphash
	# Needs review: 30610 sipa/202408_force_sync
	# Needs review: 30611 andrewtoth/write-chainstate-every-hour
	# Needs diff-minimise: 30987 davidgumberg/zero_after_free_allocator_change
	# Needs review: 31132 andrewtoth/threaded-inputs
	# Needs review: 31144 l0rinc/l0rinc/optimize-xor
	31179 ismaelsadeeq/10-2024-add-reserve-to-univalue	fd9df84d86b	last=5d82d92aff7  # opti_rpc_uv_reserve-25
	# Needs review: 31539 l0rinc/l0rinc/buffered-block-read-write OR 31551 l0rinc/l0rinc/bulk-block-read-write
	31645 l0rinc/l0rinc/utxo-dump-batching		ef2cf259a11	last=868413340f8  # opti_dbbatchsize_64-0.15
		# TODO: Test even higher or incrementing-as-we-flush
	# Needs review: 31682 l0rinc/l0rinc/optimize-CheckBlock-input-duplicate-check
	# Needs Review? 31714 mzumsande/202501_simpler_segwit_check
	# Needs review: 31875 l0rinc/l0rinc/sorted-BatchWrite
# SOFTFORK:
	# TODO: 31989 CheckTemplateVerify
		# Was #21702 (never in Knots)
	# TODO: 28550 jamesob/2023-09-covtools-softfork
	# TODO: 29050 stevenroose/txhash
	# TODO: 29198 reardencode/lnhance
	# TODO: 29221 -  # Implement 64 bit arithmetic op codes in the Script interpreter
	# TODO: 29247 -  # Reenable OP_CAT
	# TODO: 29269 -  # Add OP_INTERNALKEY for Tapscript
	# TODO: 29270 -  # Implement OP_CHECKSIGFROMSTACK(VERIFY)
	# TODO: 29280 -  # Implement OP_CHECKTEMPLATEVERIFY
	# TODO? 30018 -  # Implement BIP 118 validation (SIGHASH_ANYPREVOUT)
# FUNCTIONALITY:
	#-     rm_kernel_lib							84b7c6adf43
		# TODO: Support libbitcoinkernel (see 9da0bc3eba7 history for incomplete attempt)
			# When restoring libbitcoinkernel support, adjust libbitcoinconsensus reverts to make it interact with --with-libs (see 7ad32d39d76)
	# Broken: 24448 guix_linux_i686_compat				e8a7da94969	last=c76ac9d57f2 guix_linux_i686
		# test2: export of symbol _IO_stdin_used not allowed!
		# test2: libutil.so.1 is not in ALLOWED_LIBRARIES!
		#'test2: failed EXPORTED_SYMBOLS LIBRARY_DEPENDENCIES
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonasschnelli/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# not ready: 9745 [RPC] Getting confirmations command
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# Needs copyright header: 17311 RandyMcMillan:fix-background-svg
	# Needs fixing/review: 17303 maflcko:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					0a4470afd87	last=47b2ba29df2 !origin-pull/12911/head
		# Dropped rel notes file
		# NOTE: Originally #12911
		#28.xTODO# FIXME: "feerate" fails to account for sigops (see 21d85b5c0e); most of a fix in stash 835c2d3afba
	# Needs review and care (new index): 13014 jonasschnelli/2018/04/txindex_prune
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram+pr15836_api				b891a04599d	last=b94292a7cb jonasschnelli/2019/04/feeinfo
	(CHECK-LAST)	last=c5e53d0d21f origin-pull/21422/head
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ? (or not, since it's been abandoned...)
		# TODO: Drop ec2326304e0 since it's not needed with changes made in 998c34d27e7
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
		# TODO: https://twitter.com/RandyMcMillan/status/1490107008443457538?t=Qc4LO63rRuWxErtRel06EQ&s=19
		# 			aka 4613c88c91f4f3846aa62c929ad73d1a3e6ac70e
	22693 getaddressinfo_txids					1bd683de231
	g562  wallet_warn_reuse_gui					ea957a557d1
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				a5e45fc1e04	last=a0d0807abc2 neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		91423f64d13
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-27+knots		c0fdaeab4d3	last=409c2e34522 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonasschnelli/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr					3f3877f4745	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								4d64e9e4a9d
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							d8114ff1102
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							2fc6668792f
		# TODO: LevelDB flushing causes burst of memory usage; consider that here; see #31645
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			ad22a24eb7f	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-28+knots				a22e5867430	last=1002e2d0d7f jonatack/setfeerate
	# OR (evaluate): 31278 -  # wallet, rpc: Settxfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
		# TODO? Reduce internal changes and move to Knots compat??
	20407 rpcauthfile-29+knots					59ccec74959	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						1a80144445f	last=cf940f0e5f5
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					34b69da3162	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	g363  qt_peers_directionarrow-25+knots		e5d5a5f6965	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						d6140f3cc84	last=1af20831806 Sjors/2021/05/hww-toggle
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21260 rpcwallet_tx_in_mempool-28+knots		3be97e6ce15	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					27405046523
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						97b67babbee	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex							6e151c3f60d	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt				86efc23e6b0	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
		# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							73691fbf13a
	24963 rpc_walletprocesspsbt_options-26		7c2fb8de207	last=40143bafb52 rpc_walletprocesspsbt_options
		# Diff-minimised (and uses merge for rpcarg_type_per_name)
		# Held back f43f992b731...40143bafb52:
			#* 40143bafb52 QA: rpc_psbt: Test that the wrong type cannot be given to named params
			#* 7cd0315bc40 RPC: Strictly enforce the type of parameters passed by name
	-     rpc_descriptorprocesspsbt_opts		3537e02c19c
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	# TODO? 25621 -  # rpc/wallet: Add details and duplicate section for simulaterawtransaction
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Only if Core merges (alternative makes more sense): 22776 kallewoof:202108-getbalances-tx
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs work: g410  benthecarman/uppercase-uri
	# Needs API review: 23330 JeremyRubin/header-fetch
	23362 importfromcoldcard					98b55ac8e6d	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates					f20be3bb5b5	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06 (FlushFeeEstimates lock on m_cs_fee_estimator)
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			3b46e6081b7	last=ad431ff5d18
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip					1b0204cba37	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	g820  qt_fontsel_qrcodes-27+knots			ce838070845	last=b14c9d0572e qt_fontsel_qrcodes
	# TODO: qt_fontsel_console
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	-     verifymsg_bip137_and_electrum			07d4bdba104
		# NOTE: Fully reverts gui#819 in anticipation of #24058
	24058 bip322-29+knots						c7dd00c6de5	last=29b28d07fa9 kallewoof/202201-bip322
		# gui#819 fully reverted above in anticipation of this
	#29.xTODO# signmessagewithprivkey updates for BIP137+Electrum+BIP322
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-29			d9cb2a45b96	last=97a69e232be
		# +RPC doc fix
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
	# Needs work & complex test rebasing: 24539   # Add a "tx output spender" index
		# Partial rebase w/ stash at a1237c9a1851a8fc431467a0861c1d37b61566af
		# NOTE: When rebasing (now that #21726 is merged), need to restore AllowPrune func ?
	# Not worth it? 24615/24569/24556 guix on non-x86
	# Needs review: 24824 -  # net: create IP to ASN database from file - makeseeds.py
	# TODO? BIP 179 (tho... Lightning) - upstream first to get translations?
	# Needs work: 24897 w0xlt/silent_payment_021
	# Needs work: 24950 -  # Add config option to set max debug log size
	# Needs work: 24952 -  # rpc: Add sqlite format option for dumptxoutset
	# Concept NACK? 25026 -  # rpc: Make pruneblockchain fetch old blocks if height is lower than pruned height
	# Needs triage & review: 25038 glozow/package-rbf
	# TODO? Needs careful review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku ???
	25183 rpc_fundraw_segwitonly				938e4a0ff02	last=9e7fd5c0fe3
		# Currently just an old version for Knots 23.0 compatibility (held back 1c5cfd84b3d...9e7fd5c0fe3)
		# Fixed tests with inspiration from 9e7fd5c0fe3
		# TODO: update without breaking compatibility? (new code looks buggy tho - needs rewrite?) (also, filtering by "input type" doesn't really make sense, though segwit filtering does)
	# Needs concept: 25261 -  # rpc: fetch multiple headers in getblockheader()
	#28.xTODO# 25269 -  # wallet: re-activate the not triggered "AmountWithFeeExceedsBalance" error
	# Needs concept review: 25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
		# Concept unsure: Hides logline by default; but maybe we want that with more info included?
	# TODO: 25366 w0xlt/desc_rpc
		# Besides the private key issue (removed; conceptual issues), RPC doc also has "addresses" where there would be a single address (in a details Object)
	# Needs work: 25434 w0xlt/bypass-timelocks
		# NOTE: Was #21413 glozow/2021-03-bypass-timelocks (never in Knots)
		# Also #25570 ?
	# Needs completion & review: 25718 fjahr/2022-07-allowinbound
	# Needs concept/review: 25747 w0xlt/desc_file
	# Needs work: 25776 1440000bytes/bumpfee-inputs
	# Needs concept/review: 25907 achow101/upgrade-to-tr-2
	# Needs work: 25923 jonatack/2022-08-statestats
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	# Needs review (or leave external?): 26052 -  # contrib: Add script to colorize logs
	# Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	# Minimised: 26162 Sjors/2022/09/taproot
	#28.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	# Needs review: 26174 w0xlt/list_address_book
	-     whitelist_outgoing_auto				ec174daacb5
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme	a7335c387e0	last=d8434da3c14
	# Needs option/work: 26454 petertodd/2022-feebump-without-optin
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 rpc_disconnectnode_subnet				dfea58ac00a	last=23f4c2cb452 brunoerg/2022-11-disconnectnode-subnet
		# Refactored tests (to be more deterministic) and added support for disconnecting a single IP without subnet specified
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	27034 rpc_importaddr_for_descwallet-27+k	3422369f448	last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
		# Diff-minimised & tweaked to avoid breaking #23362
	# Needs review: 27052 LarryRuane/2023-02-getpeerinfo (maybe GUI port too?)
	27216 rpc_getaddressinfo_isactive			707ebbb6788	last=85f83339dda pinheadmz/used-addr-ui
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-29+knots						64f3666c9e7	last=91771366a3d apoelstra/2023-03--codex32
		# Diff-minimised, doc bug fixed & tweaked to avoid breaking #23362
	# Needs work: 27409 ryanofsky/pr/1data
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	27600 p2p_forceinbound-28+knots				99edcfd9930	last=8c2026848da pinheadmz/whitebind-evict
		# Reverted forceinbound limit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27770 rpc_getblockfileinfo-28+knots			a31727f8451	last=5090771f326 furszy/2023_rpc_getblockfileinfo
	#28.xTODO# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
	# Needs review & BIP finality & might have wallet changes: 28202 josibake/implement-bip352-receiving
		# Note alternative (approach NACK'd) in #28453
	# Needs review & BIP finality: 27827 josibake/silent-payments-base-pr-slim-down
	# Needs review & concept: 28241 Sjors/2023/08/silent-index
	# Needs work & maybe removing an anti-feature?: 27836 furszy/2023_rpc_fetchblock_improvements
	# Needs review: 27837 furszy/2023_introduce_block_request_tracker
	# Needs work: 27854 -  # [WIP] add a stratum v2 template provider
		# OR #28983 OR #29432 OR #30315+???
	# Needs review & compat checking: 27859 -  # Mempool: persist mempoolminfee accross restarts
	# Needs review: g753 -  # Add new "address type" column to the "receiving tab" address book page
	# Needs review and concept: 28463 mzumsande/202308_increase_block_relay
		# Why not just increase inbound capacity to max anyway?
	# Needs concept/review? 28806 ajtowns/202311-depinfo-scriptflags
	# Needs work: g777 -  # gui: getrawtransaction implementation
	# Needs concept/review: 28926 willcl-ark/2023-07-getnetmsgstats
		# Was #27534 -  # rpc: add 'getnetmsgstats', new rpc to view network message statistics
	# Needs concept/review: 28930 -  # wallet: Add scan_utxo option to getbalances RPC
	# Needs review and/or optionality: 28977 murchandamus/2023-11-gutter-guard-selector
	29016 rpc_listmempooltxs-29+knots			8bc551ae426	last=07008477b81 niftynei/nifty/listmempoolentry
		# Includes typo fixup in comment that annoys linter
	# Needs review? 29054 achow101/descriptor-sethdseed
	# Needs concept + review: 29129 brunoerg/2023-12-externalsigner-account-parameter
	# Needs review or minimal impact: 29136 achow101/sethdseed-void-descriptor
	# Needs final interface: 29163 rpc_help_detail-22								last=c6b68c29707 LarryRuane/2024-01-help-detailed
	# or (newer): 29163 rpc_helpdetail-24									last=56830469303 LarryRuane/2024-01-help-detailed
		# Left off top commit changing rpc_help test behaviour
	# Needs concept & review: 29278 -  # RPC: Wallet: Add maxfeerate and maxburnamount startup option
	# Needs work: 29396 -  # rpc: getdescriptorinfo also returns normalized descriptor
	# Needs review: 29415 vasild/private_broadcast
	# Buggy & maybe waste of RAM? Needs review?? 29418 vasild/getnetmsgstats
	# Needs concept & work: 29468 -  # rpc: method removeprunedfunds should take an array of txids
	-     manpages_seealso_notself				b4f685cd288
		# Originally bundled into #29585
	# Needs review & wallet compat check: 29675 achow101/musig2
	#29.xTODO# 29954 rpc_getmpinfo_policy_pr29954-28+knots				last=d165ac8779b kristapsk/getmempoolinfo-permitbaremultisig-maxdatacarriersize
		# Or maybe this is unnecessary with a get/set policy RPC method?
	#29.xTODO# -     rpc_getmpinfo_policy_coreetc-28+knots
	# TODO: 29959 laanwj/2024-04-qtsowrap-wayland (needs also #29923)
	# Needs review: 30080 -  # wallet: add coin selection parameter add_excess_to_recipient_position for changeless txs with excess that would be added to fees
	# Needs review & Core release (wallet format): 30243 -  # Tr partial descriptors
	#29.xTODO# Needs concept? 30341 willcl-ark/psbt-strip-derivs-combine
	#29.xTODO# Needs concept? 30381 willcl-ark/addnode-failure
	# Needs review? g832 -  # Improve user dialog when signing multisig psbts
	# Needs review/optional? 30572 ariard/reject-unsolicited-txn
		# Was #21224
	#28.xTODO# Needs rewrite? 30635 Sjors/2024/08/waitforblock
	# Needs review: 30685 hebasto/240820-control-flow
	30713 tdb3/relevant_blocks_in_scanblocks_status	15e73d0eb8f	last=5b2d0216d87  # rpc_scanblocks_status_results-28
	#29.xTODO# Mitigate #30717 breaking compatibility with no-longer-debug opts
	# Needs work? 30727 jonatack/2024-08-add-address-type-to-getaddressinfo
	30860 bashcomp_bcli_generate-29				7a279182b1f	last=abf6ad42bdb BrandonOdiwuor/bash-completion
		# Bugfix + Left off re-generation until later
	30886 rpc_descrprocesspsbt_prevtxs-28+knots	1764e95f94c	last=87ceb610a72 instagibbs/2024-09-updateutxo_psbt
		# Avoided doc-code move
	# Needs work: 31086 dnsseed_cdecker-28								last=5b823920836 cdecker/202442-re-add-bitcoinstats-seed
	# Needs work? 31252 rpc_TxToUniv_witScript-28								last=4e128d4f9b2
		# Alternative: 31256 naiyoma/feature/rpc-show-redeemscript-in-P2WSH-and-P2SH
	# Needs concept ACK: 31353 jonatack/2024-11-total-wallet-balance
	31560 rpc_dumptxoutset_fifo-29+knots		27874e8290b	last=4c8e9b4f35b theStack/202412-dumptxoutset-allow_write_to_named_pipe
		# Only the FIFO capability, left out the bundled scripts
	# Needs work? 31668 -  # Added rescan option for import descriptors
	31672 peer_cpu_load-29+knots				dee920da09d	last=0f68c47e931 vasild/peer_cpu_load
	31845 pruneduringinit-29+knots				a219cacbf55	last=d4a3abf6d43 pruneduringinit
	31886 jonatack/2025-02-netinfo-services		bed89007671	last=724546e28a5  # netinfo_local_svcs-28+knots
	# Needs work: 31936 -  # rpc: Support v3 raw transactions creation
	# Needs review & fullrbf-enabled check: 31953 maflcko/2502-fullrbf-follow-up
	# TODO: Some RPC way to report if settings are default?
	# TODO: sats/vB feerate in GUI: https://x.com/billsmith4lyfe/status/1869097896823713819?t=DH2Z02nl6V_nTQp5znmbgA&s=09
	# TODO: "I have a UPS" mode to avoid flushing frequently even while pruning
	
	# TODO: GUI block template view
	# TODO: Build next-block template from mempool + N MB txs (to replace empty blocks for local miner)
	# TODO: Extend IsUnspendable safely
		# eg based on https://github.com/bitcoin/bitcoin/pull/29981
	# TODO: IPv6 Pinholing (see #30005)
# Non-progress functionality:
	8751  sort-multisigs-28+knots				ffec05ceed7	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					17e4ef3f960	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys-29+knots					647dcf1fe7c
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245 ionice									20f5b5a0563
		# low prio: p2p requests, loading/verifying blocks on disk
		# normal prio: connecting blocks, indexes, user requests
	-    ionice_win								990ff83c56d
	8501  old_stats_rpc-28						8646f7adcf9	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-28+knots					2872a2809b7	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504  rpc_dumpmasterprivkey					66ac57716a1	last=07fc81109a
	g444  gui_netwatch-28+knots					9feaec422dd	 # Latest code now
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-28+knots				962511f17b4  # latest code now
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet to wallet-restricted users for now
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
	10554 zmq_wtx-28+knots						560ef5631a7	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
		# Extended doc/zmq a bit to match additions from #14060 and #23471
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					fbc15697b73
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment				79e3ebd76a0
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
		# TODO: Consider rebasing on #29575 (NOW MERGED) ?
	10350 filtered_witblock-28				eb6c081439c	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				5182926cb3a	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								e74bda85570	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			5f71b8ff12b
	12965 scriptthreads-28+knots				44636605244	last=dfab6c6866 jonasschnelli/2018/04/svt
	13203 dsha256_power8-27						f79f994ac5c	last=3b402e0738 TheBlueMatt/2018-05-asm
		# NOTE: Stripped out benchmark change
		#29.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	-     dsha256_power8_asm_pragmas-27			9a6be594a70
	15218 postibd_flush-28						f6400ffc581	last=8887d28a014  andrewtoth/flush-after-ibd
	15428 tor_gui_pairing-28+knots				ea31fd84e38	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-28+knots				0ef06937110	# Latest code now
		# FIXME: fix automatic tor outbound using subprocess
		# FIXME: -netinfo doesn't show tor if inbound-only?
	# TODO: tor guix bundle!
	#29.xTODO# 16490 maflcko/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support TRUC & Knots policies
	17795 gui_console_ctrl_d-26+knots			114b7254d11
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					637b1c54da5
	n/a   rpc_compat_error_index-25+knots		1ebc7d004d3
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos						a574710c9f4
	17636 guisettings-0.21						c9fcd4a9cf5	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					612e113fcd4	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						9468bae9ef4	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances-28+knots		e937882a240	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-28+knots	0e6607f372d	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=71bfa1fb715 cli_getinfo_mw_total_balance-26
	19117 rpc_getrpcwhitelist					fcb36072f90
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-28+knots		a7aa33ccc74
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-28+knots		8f9f124c11f
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	# Needs concept & review: Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
	30951 v2onlyclearnet-28+knots				8bcb122421f	last=5e3fa6758ba
	# TODO: validaterawtransaction with UTXO lookup (and fee calc) ?
	# TODO: Guix: When glibc 2.36+ is required, use -Wl,-z,pack-relative-relocs
# Non-upstreamed functionality:
	TODO: 366c9c53308 build: Exclude CI from release tarball
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	29.xTODO: Restore NAT-PMP/UPNP removed in MERGED #30043 ?
	29.xTODO# revert #31130+#31157+#31198?+#31916? to restore miniupnpc support
		TODO? Needs review: 30301 theuni/miniupnp-228-bump
	n/a   restore_feefilter_opt					cf49d58bff4
	-     gui_payreq_textedit					b487f357bb4
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				2e8254fc98f
	-     walletnotify_w_win-27+knots			c892f8b6dbf	# Latest code now
	14137 win_taskbar_progress-28+knots			87fe75f61fc	last=18eb4dbb8a
		# NOTE: Could drop /official_releases/archive/ change, but keeping it ensures a conflict when the version gets bumped, so we can update the sha256 hash
	-     restore_blockmaxsize					a0a7a60212a
	7107  qtnetworkport-28+knots				77f2e52bf26	last=1f37c87d8f2 origin-pull/7107/head
		# FIXME: Unbind IPv6 on the other port, if its IPv4 bind failed
	7533  sendraw_force-28+knots				9d121259d75 last=2627c0937f8 sendraw_force
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532,#29060 if merged
		# TODO: 1d3fdc1adde Support ignoring various rejection reasons in PackageMempoolChecks
			# error message change impacts a bunch of functional tests; and submitpackage currently lacks support for ignore_rejects anyway
	11082 rwconf-27+knots						c90495c624f # Latest code now
		#29.xTODO# Squash fixes
		#28.xTODO# Deprecate with settings.json better?
	7510  rwconf_gui-28+knots					3c18bc835f5
		#29.xTODO# Squash fixes
		#29.xTODO# Move blockreconstructionextratxn (and others?) from rwconf_policy?
		# TODO: when we can enable block filters post-pruning, revert 81d696e132c
	559   accept_nonstdtxn						e72688bf354
		#29.xTODO# Revert or redefine #29843 if it got merged
	 929 tbc									fe176fa7028
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
		# TODO: Qt6 drops QRegExpValidator
	 553 bugfix_qt_uri_amount_parser			55e55d6819c
		 TODO: Merge in 561be93aad0 GUI: Mention BIP 20 URI support in command-line options (earlier versions included with #29686, now merged) - ensure knots-next-28.spec gets a check-last too
	-     mining_priority						07464b13214	# Latest code now
		#28.xTODO# FIXME: Lots of lock warnings from clang! (did I already fix these?)
		#28.xTODO# FIXME: Should blockmintxfee apply to blockprioritysize??
		# If mempool-knots.dat is ever extended to store easily manipulatable data, port Xor stuff over
		# Reverts (needed and better performance & memusage): d0cd2e804ec [refactor] rewrite BlockAssembler inBlock and failedTx as sets of txids
	5861 gui_restore_addresses					39668f36473
	5891  qt_console_history_persist			76638518995	last=0cd5fc301d6 qt_console_history_persist
	7219  rbf_opts-28+knots						a1e42756c14	# Latest code now
		29.xTODO: Revert #30592
	-     truc_opts-28+knots					7b898f1d017
	# TODO? -     net_identify_librerelay
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					b7643238b1f
		# TODO: Split out legacy address preference to be more explicit
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname_wo_dat			1d45ac88ee0	# Latest code now
	-     gui_request_payment_label-0.19		11a5aae7341
	-     gui_peers_sort_network-23				d69b756c939
	-     gui_peers_no_net_column				56925da3aeb
	# 22439 guix_in_gitian-23+knots				2014b1271e3	last=ebda0463748 achow101/guix-in-gitian
		# FIXME: If restoring, test that this still works (WIP fixes in stash fa8517a9112 but need rebase too)
	-     rpc_getblockfrompeer_future			e7c08467524
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		b7fb698aa73
		# Prior Knots bundled this in with #20295
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
	-     gbt_rpc_options-28+knots				dc8fc35fc01
		#29.xTODO# Ensure BlockAssembler::Options::operator== is updated to include any new settings
	# TODO: pre-cache GBT call after new block?
	#28.xTODO# RPC to get/set policy configs
	#29.xTODO# -     miningcbtag-27+knots
		# TODO: add to rwconf_policy: 4b38a3031ab GUI/Options: Add miningcbtag via settings
	-     blockview-28.1+knots					d69357dcf51
		# NOTE: if #31897 is merged, need to revert or find alternative source for fee info
	#-     mapport_default_on-27+knots			a32f282230d
		# Re-disabled in light of continued security issues
	#28.xTODO# Look into making the patches tarball in guix
	-     restore_libconsensus-28+knots			57d68d7c5cb
		TODO: When restoring libbitcoinkernel support, adjust libbitcoinconsensus reverts to make it interact with --with-libs (see 7ad32d39d76)
	# TODO: bump dbcache to 1 TB on systems we can detect memory pressure! - after testing
	-     rpccookieperms_log_improvements-28+k	ec34bd875d1
	# Needs work: n/a   macos_dmg-27							d26ae740b99
		# Reverts #28432, #28932, and #28973, and includes fix_dmg_openfinder
		# 28.xTODO: revert macos ZIP only: #29733
		# TODO: Investigate if we can compress again by reverting #24031 using patches in https://bugzilla.mozilla.org/show_bug.cgi?id=935237
		# FIXME: Probably incompatible with MERGED #31407 macos_notarization ?
	# Needs review: 31065 danielabrozzoni/20241008_rest_broadcast
# Non-upstreamed policy options (default off):
	30232 refactor_isstandardtx_mpopts-28+knots	5ba611afd07
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	29309 permitbarepubkey-28+knots				22193cca113	last=1dfe27e49ab
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     bytespersigopstrict-28+knots			9d18c6ea473
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	9749  unique_spk_mempool-28+knots			84eff5944da
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     dustdynamic-28+knots					5dd1f1ee25e
	28408 match_more_datacarrier-28+knots		570cb5cb1dc	last=4d2ec0671a3 match_more_datacarrier
		#29.xTODO# TODO: Delete TBD "maxdatacarriersize" from #29954 (see b02aab950af) (or at least fix the description)
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
		# TODO? Revise byte counting to consider input/output waste
	-     datacarriercost-28+knots				42ecf3bfb75
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		#28.xTODO# Add tests and make sure boundaries are correct
	# TODO: Filter for output value < tx fee * N - https://twitter.com/DoctorBuzz1/status/1741622696327205176
	# TODO: Impose accurately-calculated (not just guessing witness size) dust limit on Taproot _spends_ (only Taproot because there should be a more sensible spend path available in theory)
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     acceptnonstddatacarrier-28+knots		48c848e044a
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     rejecttokens-28+knots					39ec1308346
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Currently filters just Runes
	k78   rejectparasites-28+knots				6c5ca3ed56c	last=d978324923a
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Currently filters just CAT-21
		# GUI component & default-on moved into rwconf_policy below
		# Rewrote unit test to be more comprehensive
	# TODO: #30964 & LR alternative options
	# TODO: NO APPARENT USAGE: filter HG: https://pbs.twimg.com/media/GDV-H8UWkAAsckl?format=jpg&name=large
	# TODO: CBRC-20 https://twitter.com/bitoordileone/status/1734654996539457666 - INSCRIPTION-WRAPPED: https://mempool.space/tx/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9
	# TODO? All-ASCII data storage (inefficient)
	# TODO? If any input is dust, limit output count to < input count? (or lower?)
	# TODO: Stacks (OP_RETURN X2... - most are 80 bytes long, some 55, few 19)
	# TODO: "OLGA" file storage: https://github.com/mikeinspace/stamps/blob/main/OLGA.md https://github.com/CounterpartyXCP/Forum/blob/1e362f7f8668654d0241fe5b1f1c1c330a8b4368/cip-0033.md
	# TODO? Procedural approve/deny/discount/penalize policy scripting?
	# Needs concept ACK: 29843 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	-     maxscriptsize-28+knots				574d3ab59c1
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Alternate to(?) #29769
	# Needs concept & impl: Policy: limit script sigops to N (default to MAX_OPS_PER_SCRIPT which is consensus pre-taproot)
	# Needs concept & impl: Policy: limit any witness stack items to N elements (like MAX_STANDARD_P2WSH_STACK_ITEMS)
	# TODO? Ordislow??
	# TODO? Spam filter for stuff like https://mempool.space/tx/4ec38548aa67f6a2efbbc3cf34ab49dc5c275d9701ab0b58696baee9f555c45a
	# TODO: Whitelisting model for non-SPK scripts
	# TODO: -blockpreference=smaller|larger,lessdata|moredata (or match our own policies?)
	# TODO: allow txs from reorg'd-out blocks to bypass policy?
	# TODO: prioritise txs from reorg'd-out blocks?
	# TODO: some way to prioritise Lightning channel activity?
	TODO? https://github.com/petertodd/bitcoin/commit/04c8e449a34e74e048bf5751d13592a22763ff7e (see email dated 2025-03-19 8:27pm)
# Non-upstreamed Knots compatibility:
	-     compat_rpc_dumptxoutset_hr
		TODO: Compatibility with Knots 0.20.0-28.1 positional params
	-     compat_jsonrpc_weirdversions			d50d30bf835
	29530 rpc_getpeerinfo_misbehaving_score-28	66b8c669e38	last=87efb6f0cfd
		# NOTE: Held back 976d61c974e...87efb6f0cfd which degrades docs and adds a test incompatible with Knots
		# Deprecated in Knots 28.0
	-     rpccookieperms_octal_compat-28+knots	cbd3aa51b74
	-     zmq_ipc_uri_compat					85f09aa4af0	last=0b1762c90d1 origin-pull/28020/head
		# Backward compatibility with #28020 URI format supported by Knots 25.1+
	#29.xTODO# Check on #29942 removal of -datacarrier, possibly revert?
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-26			dd9a275a37b
		# Effectively reverts #24505, #27869, #28597, and gui#764
		#29.xTODO# revert #28710  Remove the legacy wallet and BDB dependency
		#29.xTODO# revert #31250  wallet: Disable creating and loading legacy wallets
	14641 fundraw_min_conf_deprecated-25+knots	9e0533bb2c0	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			74f7c944e91
	-     netperms_implicit_addr				9ffb23bb848
	# IMPOSSIBLE with v2transport param: 12674 rpc_onetry_nonpriv-25+knots			ecaf5bf309f
	-     rpc_getblockfrompeer_nodeid_compat	925240d6f71
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-25+k		05258006a0a
		#29.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	-    1day_default_conftarget				c189a5677d3
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	-     bloom_default-28+knots				401f2f03e86
	-     wallet_avoid_newerchange				5962a67e5f5
	-     enforce_checkpoints					254fabebf5a
		#29.xTODO# Revert #31649
	n/a   checkpoint_update-28					41c985132c9
		#29.xTODO# Revert #25725 (Remove mainnet checkpoints)
	10282 timebomb_knots						40f673fe63e
	-     rwconf_policy-28+knots				6fd67aa463d
		# Includes Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: Get GUI settings for dustdynamic to select ratio box & focus text area when you click their labels
		#29.xTODO# QTreeWidget or similar for GUI Options dialog?
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
	# Needs review/options: 26348 -  # Make P2SH redeem script "IF .. PUSH <x> ELSE ... PUSH <y> ENDIF CHECKMULTISIG .. " standard
	# Needs refactoring to only happen for -acceptnonstdtxn(?): 26398 instagibbs/relax_too_small_tx_equality
	# Needs review/concept: 29001 instagibbs/2023-12-ephemeral-anchors
		# Problematic: 26403 instagibbs/ephemeral-anchors
	# Needs review & optionality: 26451 sdaftuar/2022-11-fixrbf
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		d4c1e555559
	7483  svg_icon-28+knots						5b18d9e534b
		# Consider: https://github.com/bitcoinknots/bitcoin/pull/54
	n/a   tbc_font-28+knots						458c5339ceb
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/ But depends on the build-for-release-source code from svg_icon...
# BRANDING:
	n/a   copyright_2025-28						19e67dd9efa
	n/a   knots_branding-28						f58950aab87
		#28.xTODO# Review security policy
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#29.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
# TODO: Check that we aren't deprecating anything in Core
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
# TODO: Check that no git Author lines are a mix due to GIT_AUTHOR_NAME no longer allowing emails: git log v27.1.. | grep '^Author.*luke-jr' | grep -v Dashjr
	n/a   (cherrypick=6ee0b3ec0fc)				db9ec3a8f5f	# doc/{bips,files}
		# TODO: Update with bump_version below !!!!
	n/a  (bump_version=Knots:20250305)			ba223403bbc
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist		45b084a111f
	n/a   (cherrypick=b5bdee81b14)				df2512ca90f  # release notes: write/update, including change log and credits
		# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge [gk]?\d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# When re-added, #28824 notes in 9db5d23d559
	n/a  (cherrypick=20338f1e833)				5f8256608fc  # update manpages (build first)
		# also example bitcoin.conf and bitcoin-cli bash-completion
	#29.xTODO# n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: Upload to Transifex with * d9411324066 (ts_20220515, origin-pull-g/599/head) GUI: Support translating Bitcoin units
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

TODO: Close Knots issue 98

# TODO: @28.x-knots-android

@28.x-knots-extratests
	31367 dergoegge/2024-11-ci-ulimit-s
	31410 hebasto/241203-multiwallet
