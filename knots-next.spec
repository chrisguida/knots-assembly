timestamp 2022-09-20 14:00:13
lastapply no-merge

#.. checked up to PR #26140 / gui #669

checkout origin/24.x
@24.x-syslibs
# BUILD BUGS:
	# Needs review: 23609 hebasto/211126-reduce
	24051 config_utils_drop_extra_deps			7aaf200af71
	5872 subdir_incl_compat						3a646ac6a6b
	24295 -										f4ae5e430d7	last=faf7a61483a  # Remove std::move from fs wrapper to work around -D_LIBCPP_DEBUG=1 bug
		# 24.xTODO: Can this go away?
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb							a96a241ab69
	5416  sys_libsecp256k1						f4a59d2a40f
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	#25.xTODO: sys_libminisketch
	13789 bugfix_asm_pragmas					5caf7787338
	15155 test_external_bcli					b020b0febcf
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	# ---- BEGIN qt6 SUPPORT, TODO ----
	# NOTE: Partial qt6 backport in WIP_qt6-23
	# Needs review: 24813 hebasto/220409-appcheck        # Qt 6 (4/n)
	# TODO: tbc uses QRegExpValidator
	# Needs work/splitting-up: 24798 hebasto/220406-qt6
	# Needs review: 25191 hebasto/220523-qt6-mac
	# ---- END qt6 SUPPORT ----
	n/a   (delete_release_notes_fragments)
@24.x-knotsfixes
# TESTS:
	#24.xTODO#-     lint_relaxer							c6a96c5159d
		# Add back as needed:
		#	* 16e78207523 Bugfix: lint: Tolerate explicit hidden-only args
		#	* 76fc5a93eab QA: Don't require coverage of all RPC methods
		#	* 041efdee0d3 lint/includes: Don't fail for new boost usage
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
# FIXES:
	18818 guix_reltar_autogen_distclean			04ef73ac671	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again						fe1576ba2d8
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					06b2e2cae97	last=df5ece3e064 2020mingwthrd
	18490 bugfix_symcheck_pe_case				5ef693738d0
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 http_bind_error						f61e704deeb	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					524a221b075
		# NOTE: libevent-copied code up to date as of 2021-07-16 c29f1dbe116c88434e77721ca215b8d2082b247f
	9524  rpc_pruneblkchain0					b327b038e9d	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					e94a07f681b
	14485 fadvise								d13637180c8
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					894b5b40dfc
	-     bugfix_rpc_getbalance_hacky			60f5367f46a
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	18194 bugfix_gui_edit_sendaddr-mini			3e18bb2be29	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	g658  intro_dont_change_user_prune			bbc927c3c8e
		# Was #18729
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				68bd18dadc7	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19888 getblockstats_utxo_actual-24+knots	02627b9a519	last=7232bd27184
		# Diff-minimised incl test changes
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	g152  gui_notify_setup_bg					05368bdfa90
	-     bugfix_gui_drop_abc_confusing_hack	10a38703175
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				3a6e53d4b5b
	-     rpc_addconnection_mainnet				3f030489ee0
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22417 bpchild_closefds						05121d01966
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
		# NOTE: Currently uses ENABLE_EXTERNAL_SIGNER in place of USE_BOOST_PROCESS (not defined until #15421 merged)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				32caa7dec63
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs work: 23502 achow101/tr-low-fee-est
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	g506  qt_qrcode_sizefixes					d036a08f614
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs review: 24066 whitslack/openrc-daemonwait
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049
	# Needs work: 24313 Sjors/2022/02/displayaddress						last=803387f054d
		# TODO: make sure this doesn't break compatibility (and fix review bugs)
	22087 validate_port_opts-24+knots			5bdf4c61815	last=1dae86bfd22  # Validate port-options
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				1ae167e21ee
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	# TODO: Triage KDE patches for Qt5
		# NOTE: WIP list of KDE patches in 202204-KDEQtPatchesForBitcoin
	24718 fix_rpc_docs_pr24718-24+knots			1ce1a6ef90b	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Simpler version of? 24845 -  # wallet: createTransaction, return proper error description for "too-long-mempool-chain" + introduce generic Result classes
	# Needs work: 24851 -  # init: ignore BIP-30 verification in DisconnectBlock for problematic blocks
	# Needs review: 24858 mruddy/issue_21379  # reindex, log, test: incorrect blk file size calculation during reindex results in undesirable blk file malformedness
	# Needs review: 24912 mruddy/nchaintx_type
	24957 fix_prune_during_loadblock-22			c2e6976a79f	last=da8e95c0140 mruddy/issue_23852_import_prune
	# Needs review: 24972 hebasto/220425-no-libtool
	# Needs review: 24994 hebasto/220426-consensus
	g595  qt_handle_autostart_errors-0.15		e467470fa8b	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	g599  ts_20220515-partial-24				5a4ab415cfe	last=7ec30cf0127 ts_20220515
		# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
		#24.xTODO# Update with other commits that are beneficial
	-     rpcdoc_sendmany_dummy_opt-23			9ddbb6e5a61
		# Just the bugfix from #25093 rpc: Check for omitted, but required parameters
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
	# Needs concept ACK/review: 25158 -  # rpc, wallet: add abandoned field for all categories of transaction in ListTransaction
	# Needs review: g605  hebasto/220522-splash
		# NOTE: Simpler alternative in https://github.com/bitcoin/bitcoin/issues/25146#issuecomment-1129356954
		# Less impact on Knots since we let the user proceed... and only affects builds w/ partial wallet support
	# Needs review: 25193 -  # indexes: Read the locator's top block during init, allow interaction with reindex-chainstate
	# Needs review: 25227 -  # Return empty vector on invalid hex encoding
	# Not clear this fixes anything: 25273 achow101/use-preset-tx-things
	# Needs review: 25380 darosior/fee_estimator_disable_cpfp
	25548 readlink_overflow_check
	#24.xTODO# Check on #25561
	# Needs concept review: 25574 -  # validation: Skip VerifyDB checks of level >=3 if dbcache is too small
	# Needs work: 25595 instagibbs/verify_psbt_input
	# When translations exist, or correct mistaken old translations: 25666 -  # refactor: wallet, do not translate init options names
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	# Needs review: 25698 -  # crypto: avoid potential buffer overread in ChaCha20::SetKey
	g633  -													last=5fde8fbe085  # qt: Fix shortcut ambiguities
	25727 -													last=019e02cb26d  # util, config: error on startup if conf or reindex are set in config file
	# Needs review: 25729 -  # wallet: Check max transaction weight in CoinSelection
	# Meh: 25854 -  # tracing.md trivial English fixes
	# Needs review: Either 25856 or 25858 to fix PSBTs with empty tap_tree
	# Needs work/concept: 25867 -  # lint: enable E722 do not use bare except
		# NOTE: Fixes Ctrl-C being caught/ignored
	#24.xTODO# Needs work/concept: g653 achow101-g/show-bal-send
	25880 -													last=4b0dbc0f3eb  # p2p: Increase BLOCK_STALLING_TIMEOUT timeout during IBD
	#24.xTODO# Needs review: 25935 dist_bitcoinconf_as_example
	# Needs review: 25938 mzumsande/202208_fixed_cjdns
	g662  qt_fix_txview_202209
		# Includes gui#368
	# Needs work: 25950 theStack/202208-test-fix_high_timeout_values
	#24.xTODO# 25964 fanquake/fixup_mingw_cflags						last=1a332c78dbc
	#24.xTODO# Needs review: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	26032 wallet_extsigner_feerate_nogrind-24+k				last=b133ab9b1ee Sjors/2022/09/external-signer-feerate
		# Diff-minimised
		#24.xTODO# Remake on latest branch after review is addressed
	25737 rpc_type_error-24+knots							last=e68d3807979
		# Diff-minimised, including leaving off top commit
	g665 w0xlt-g/load_wallet_signal							last=b8b59ff9fea
	26067 -										73087e7c75b	last=fa2b8ae0a22  # util: improve bitcoin-wallet exit codes
		# NOTE: Was #24428
		#24.xTODO# Diff-minimise??
	# If BSD depends support matters: 26073 fanquake/_BSD_bdb_compilation
	#24.xTODO# Needs review? Are all fixes? 26109 jonatack/2022-09-getpeerinfo-netinfo-updates
	26116 -													last=2c03465dfa1  # rpc: Allow importmulti watchonly imports with locked wallet
	26124 fanquake/24.0rc2_backports^						last=59b154ac443 fanquake/24.0rc2_backports
	26149 fanquake/24.0rc2_backports						last=9dfccb40acc fanquake/24.0rc2_backports
	26130 fix_descrwallet_signmsg_deadlck
	26132 -  # wallet: Fix nNextResend data race in ResubmitWalletTransactions
	Needs review: 26138 -  # test: Avoid race in disconnect_nodes helper
	Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	TODO: coincontrol sort is backward ? (all columns!)
	#24.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
@24.x-knots
# PERFORMANCE:
	# Needs reivew: 24158 JeremyRubin/epoch-mempool-reorg-updates
	n/a   rm_minisketch-24+k					5ddaa57ea1b	last=4e2d2910342 rm_minisketch-23+k
		#25.xTODO# Probably need to drop this
	# Needs review: 24589 -  # sha512.cpp improvements
	# Probably a bad idea: 24712 -  # wallet: reduce coin selection iterations
	# Knots doesn't support MSVC builds: 24773 Enable AVX2 implementation of SHA256 for MSVC builds
	# Needs review: 24814 -  # refactor: improve complexity of removing preselected coins
	# Needs work: 24901 -  # mempool: reduce lookups, insertions to cache in UpdateForDescendants
	# Needs review: 24926 -  # mempool: use mapNextTx.lower_bound in removeRecursive
	# Needs review: 25221 -  # Improve CMedianFilter algorithm - useless? see comments
	# Needs review: 25232 -  # rpc: Faster getblock API
	# Needs review: 25236 -  # wallet: use vector instead of list for transactions
	# Needs review & diff-minimising: 25297 -  # wallet: speedup transactions sync, rescan and load not flushing to db constantly
	Needs review: 25957 theStack/202208-speedup_descriptor_wallet_rescan_with_block_filters
	# Needs review: 25968 sipa/202208_headerssync_optimize
	# Consider: 25985 fanquake/revert_slow_macos_sqlite
	Needs review: 26008 achow101/improve-many-desc-ismine
# SOFTFORK:
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	24448 guix_linux_i686_compat				e8a7da94969	last=c76ac9d57f2 guix_linux_i686
		TODO: Revert #24639, #26075
	25111 hww_windows-23+knots					cd6a088a2ec	last=2a53dce0b66 hww_windows
		# NOTE: Carries commit 209018f4275 for compaibility with #22417
		# NOTE: Being replaced by #25696 ?
		TODO: revert #25723 if needed
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# not ready: 9745 [RPC] Getting confirmations command
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# Needs copyright header: 17311 RandyMcMillan:fix-background-svg
	# Needs fixing/review: 17303 MarcoFalke:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	22049 rpc_fundtx_minmaxconf-23+knots		e80afead907	last=7f4c9039f71  # rpc: allow specifying min chain depth for inputs in fund calls
	(CHECK-LAST)	last=9652e0a2faa rpc_fundtx_minmaxconf
	(CHECK-LAST)	last=1e14aeacd3a origin-pull/25375/head
		# Was #14641 (moved to Knots compat)
		# TODO: Once #25375 is merged, include its strings/tests
		TODO? gcp 46de5347b7a RPC/Wallet: Deprecate FundTransaction min_conf (14641) and replace with minconf from 22049
		TODO? gcp 1d8db4ee846 QA: Minor updates for testing minconf parameter in fund calls
		TODO? gcp cd52287b586 (fundraw_minconf-0.21) RPC/Wallet: Check for negative min_conf in FundTransaction
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					58494ba48db	last=47b2ba29df2 !kallewoof/sign-show-fees
		# Dropped rel notes file
		# NOTE: Originally #12911
	# Needs review and care (new index): 13014 jonas/2018/04/txindex_prune
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	g119  rm_send2self-mini						5f0c6043003	last=2bb4e307634 rm_send2self
		# NOTE: Originally #15115
		TODO? gcp 1c73f0e94e3 (rm_send2self-mini-21) Bugfix: GUI: Correct format specifier for Date sort key
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	Merged: 15423 tor_socks_port						ef0037b9519
		TODO: gcp d0f18ffbc6f torcontrol: Fallback to 127.0.0.1 if resolving the torcontrol-provided host fails
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram+pr15836_api				d001a8627f4	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ?
		FIXME: f93da695638 Bugfix: QA: Ensure mempool_fee_histogram expected feerates rounded down
		BUG: 'with_fee_histogram' compat param (as bool) will be rejected by type check
		TODO? gcp f93da695638 (fee_histogram-21) Bugfix: QA: Ensure mempool_fee_histogram expected feerates rounded down
	(CHECK-LAST)	last=f34072a4d4f origin-pull/21422/head
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
		# TODO: https://twitter.com/RandyMcMillan/status/1490107008443457538?t=Qc4LO63rRuWxErtRel06EQ&s=19
		# 			aka 4613c88c91f4f3846aa62c929ad73d1a3e6ac70e
	22693 getaddressinfo_txids					cf21d8928be
	g562  wallet_warn_reuse_gui					1fe81821269
		# NOTE: Was #15987
	# Needs review/fixes? 16037 / 24865 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs review: 16981 LarryRuane:reindex-speedup
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				b2999f33de0	last=a3300c6b200 neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		055826bebb2
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	0bb929ebf49	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr-23+knots			196de74322c	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202/files#r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								c6fa3b51229
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							120c96e9b59
		TODO? gcp 5630127ef8c (prune_locks-0.21) Bugfix: blockstorage: Delete persistent lock updating to temporary in UpdatePruneLock even with sync=true
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	19762 ryanofsky/pr/named					48e58c13311	last=894c414dafb
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							a6c4444899c
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			30a7f0f9263	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
	-     rpc_getblockfrompeer_wo_header		b89d300855f
		# Prior Knots bundled this in with #20295
		TODO? gcp 008f768dbea Bugfix: RPC/blockchain: Add missing newline to getblockfrompeer help
		TODO? gcp e796abe55ee test: check pre-segwit peer error in `getblockfrompeer` RPC
		TODO? gcp cbf6569da3a (rpc_getblockfrompeer_wo_header-21) rpc: warn that nodes ignore requests for old stale blocks
	TODO? * 61a204efbe1 rpc: Add note on guarantees to getblockfrompeer
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-23						7fd4e8a1563	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20407 rpcauthfile							accabd6d59e	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid-23					01f67fb5b69	last=75aff9e0ff7 intro_assumevalid
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	23549 rpc_scanblocks						83bd74cf3d4	last=e1c89184cd3 jamesob/2021-11-scanblocks
		# NOTE: Was #20664
		# NOTE: Includes lots of additional fixes/doc improvements
		TODO? gcp 0c06258c1e9 RPC/blockchain: Unify result documentation language between scantxoutset and scanblocks
		TODO? gcp 4281973214f RPC/blockchain: Consolidate scan_result_* RPCResults and strings between scan{txoutset,blocks} help
		TODO? gcp 0a8858dbf8f Revert "RPC/blockchain: Document scantxoutset status key when no ongoing scan"
		TODO? gcp 731d77a7e8d RPC/blockchain: Trivially improve scanblocks doc for relevant_blocks
		TODO? gcp 4fbe38f4ebf Bugfix: RPC/blockchain: Document scanblocks only requires scanobjects for "start" action
		TODO? gcp d4e89bd7e33 (rpc_scanblocks-21+knots) rpc: remove scantxoutset EXPERIMENTAL warning
	(CHECK-LAST)	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
	20702 rpc_getblocklocations					1f12d13fadf	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							7135a8a2aec
	Merged: g543  qt_peers_age_column-23				0bdf2c4b51a  # peers-tab: add connection age column to tableview
		# NOTE: Left off top commit enabling ResizeToContents; instead, calculated size is added in local g363-included commit
	g363  qt_peers_directionarrow-23+knots		418d63d0c21	last=4e2fe6b9878 qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
		TODO? gcp 7992ff04a5e (qt_peers_directionarrow-0.21+knots) GUI/Peers: Shorted "Received" header to "Recv'd" so it fits the column
	# Needs review: 21006 -  # rpc: reduce LOCK(cs_min) scope in rest_block: ~5 times as many requests per second
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	# ---- BEGIN HWI SUPPORT, TODO ----
	21576 rpc_bumpfee_signer-23+knots			bc251bca880	last=2c07cfacd17 Sjors/2021/04/signer_bumpfee
		# Simply dropped misc comment changes in first commit
	21928 rpc_hww_toggle-23						d4e05c2df25	last=1af20831806 Sjors/2021/05/hww-toggle
	# ---- END HWI SUPPORT ----
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise						bcf986d0d05
		# Context: 17529 rpc: Faster getblock using PureBlock
	# Needs API finalisation: 21158 -  # lib: Add Taproot support to libconsensus
		#TODO: minimise
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 rpcwallet_tx_in_mempool-23+knots		00751692d11	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					6a47e2cd43b
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						7ac16e22ad6	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 -										a2f94dca829	last=602f4da9178  # autoreindex-0.21
	22159 conf_append_cxxflags-23				fd74eb4a20a	last=fa14c6818f4 marco/2106-buildPattern
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt-22				b94a0f57896	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							7edb7a43520
	24963 rpc_walletprocesspsbt_options-23		7ebcda357a1	last=31ffd7782bf rpc_walletprocesspsbt_options
		# Diff-minimised
		BUG: 'sign' compat param will be rejected by type check
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	# Needs review: 22729 vasild/torbind
	Merged: 22751 simulaterawtransaction-23				ba547c13c56	last=bd520345f7a kallewoof/202108-analyzerawtransaction
		See new competing(?) PR #25621
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Only if Core merges (alternative makes more sense): 22776 kallewoof:202108-getbalances-tx
	# Needs BIP? 22838 achow101:multipath-descs
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs work: g410  benthecarman/uppercase-uri
	# Needs review: 23319 -  # rpc: Return fee and prevout (utxos) to getrawtransaction
		# Rebase of 2c56d72acac in a662191612c w/ failing test :/ (had to replace hard-coded fee assumption too)
	# Needs API review: 23330 JeremyRubin/header-fetch
	23362 importfromcoldcard-23					8d8aa6dc195	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates-23				d2ca24d7dc1	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs concept review: 23395 -  # util: Add -shutdownnotify option
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs work: 23578 Sjors/2021/11/taproot_signer
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			d5f647c9615	last=ad431ff5d18
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip-23+knots			190259f05c2	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour
	g497  qt_fontsel-23+knots					63f1348f70c	last=ca6e29df02e qt_fontsel
	-     qt_fontsel_qrcodes-23+knots			b9996e59773	last=3bfdd05fcfd qt_fontsel_qrcodes
	# TODO: qt_fontsel_console
	# Needs work? g505  -  # RPCConsole: add hidePeersDetail() button and functionality
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	# Needs review & BIP changes: 24058 kallewoof/202201-bip322
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-23			b53beb352aa	last=97a69e232be kallewoof/202201-deriveaddr-nochecksum
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	Merged: 24198 rpc_wtx_wtxid-23+knots				847b30e73d3	last=7abd8b21ba3
		TODO? gcp 1ad918ff517 (rpc_wtx_wtxid-0.20) RPC/Wallet: Provide an actual description of wtxid field
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
	# Needs concept ack: g553 w0xlt-5/change_error_background
		# CAUTION: requires theming changes for gui#537
	# Needs work & complex test rebasing: 24539   # Add a "tx output spender" index
		# Partial rebase w/ stash at a1237c9a1851a8fc431467a0861c1d37b61566af
		# NOTE: When rebasing post-#21726, need to restore AllowPrune func ?
	# Needs review: 24545 -  # BIP324: Enable v2 P2P encrypted transport
	# Not worth it? 24615/24569/24556 guix on non-x86
	# Not worth it: 24611 -  # Add fish completions
	# Needs review: 24824 -  # net: create IP to ASN database from file - makeseeds.py
	# TODO? BIP 179 (tho... Lightning) - upstream first to get translations?
	# Needs work: 24897 w0xlt/silent_payment_021
	# Needs work: 24950 -  # Add config option to set max debug log size
	# Needs work: 24952 -  # rpc: Add sqlite format option for dumptxoutset
	# Concept NACK? 25026 -  # rpc: Make pruneblockchain fetch old blocks if height is lower than pruned height
	# Needs triage & review: 25038 glozow/package-rbf
	# Needs licensing/review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku
	25183 rpc_fundraw_segwitonly-23				68789264835	last=1c5cfd84b3d
	Merged: # TODO: g602  ryanofsky-g/pr/qtsopt
		# +gui#603 ?
	Needs work? 25261 -  # rpc: fetch multiple headers in getblockheader()
	25269 -  # wallet: re-activate the not triggered "AmountWithFeeExceedsBalance" error
	25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
	Needs review: 25287 -  # logging: threshold log level
	Needs review: 25315 Empact/disk-space-check
	Needs work?/review: 25344 -  # New extra_outputs argument for bumpfee/psbtbumpfee
	Needs concept review: 25366 w0xlt/desc_rpc
	Needs work: 25412 brunoerg/2022-06-rest-deploymentinfo
	Needs work? 25434 w0xlt/bypass-timelocks
		# NOTE: Was #21413 glozow/2021-03-bypass-timelocks (never in Knots)
		Also #25570 ?
	Needs review? g626 -  # gui: Showing Local Addresses in Node Window
	At least part of (RPC results) 25634 achow101/desc-import-unset-blank
	Needs work & applicability check: 25680 -  # rpc, docs: Add note for commands that supports only legacy wallets
	Needs completion & review: 25718 fjahr/2022-07-allowinbound
	Needs work: 25730 -  # RPC: listunspent, add "include immature coinbase" flag
	Needs concept/review: 25742 -  # Use change amount as tiebreaker for SelectionResults
	Needs concept/review: 25747 w0xlt/desc_file
	Needs work: 25776 1440000bytes/bumpfee-inputs
	Needs review.. or not? 25796 -  # rpc: add descriptorprocesspsbt rpc
	Needs concept/review: 25907 achow101/upgrade-to-tr-2
	Needs work: 25923 jonatack/2022-08-statestats
	Needs review: 25934 brunoerg/2022-08-add-label-listsinceblock
	Needs concept & review: 25939 -  # rpc: In utxoupdatepsbt also look for the tx in the txindex
	Needs review: g655 -  # Persist "mask values" in gui
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	Needs work/review/concept: 25943 -  # rpc: Add a parameter to sendrawtransaction which sets a maximum burned output for OP_RETURN transactions.
	Needs concept & review: 26026 -  # log: Colorize logs
		and/or #26052
	Needs work? 26077 fanquake/guix_shell_over_environment
	Needs review: 26088 -  # init: Add option for rpccookie permissions
	Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	Needs work: 26131 jamesob/jamesob-22-09-log-rpc-port
# Non-progress functionality:
	8751  sort-multisigs-23						c42c63f0c5c	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					614547cdc59	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys							7b2398d7c36
	9245 ionice									0a0ecc14783
	-    ionice_win								c5ef9ca0e30
	8501  old_stats_rpc-23						9936cf72d91	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-23						b784f359eea	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-23					95035ce6202	last=07fc81109a
	g444  gui_netwatch-23+knots					a44e7b33409	last=524665c116a gui_netwatch
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-23+knots				664cc4b0fb1  # latest code now
		# CAUTION: Be extra careful rebasing - diff/patch default context moves code around between RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-23+knots						ad1bcb2928e	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
		# Extended doc/zmq a bit to match additions from #14060 and #23471
		TODO? gcp 8509de1d91d Bugfix: doc/zmq: Minor typo
		TODO: add validation like #22087 (gcp 86d091852f1 / 08778898b0a)
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					edca5b8af00
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment				432fae20806
		# Squash "QA: Use addconnection rather than addnode onetry" ?
	10350 filtered_witblock-22				abf017ad612	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				9add7811b6d	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								1cc702fa199	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
		# Fixed a minor bug in conf_target range check
		TODO: gcp 5d5b2fb8442 QA: Exercise REST interface in feature_fee_estimation | 71375ee91ac
	11803 bugfix_dumpwallet_hdkeypath			fea9d68f84d
	12965 scriptthreads							0345cf11100	last=dfab6c6866 jonas/2018/04/svt
	13203 dsha256_power8-23						7610e2e0b16	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8_asm_pragmas-23			3ba39b15ebb
	15218 postibd_flush-23						e194bb9b731	last=d2ecb70d64  # validation: Flush state after initial sync
		# TODO: Rewrite after #17487 is ready/safe to merge
	15428 tor_gui_pairing-23+knots				723c1c46950	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-23+knots				6992e4922ed	# Latest code now
		TODO: gcp e545fa438bb Revert Boost Process workaround for mingw-w64 compiler, in context where mingw-w64 compiler never builds
		TODO: gcp b0c7d431f30 Include -torcontrol in hidden_args when building without Boost Process
	# TODO: tor guix bundle!
	15633 nohbcbfornonwit						552d3dfab5b
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
		NOTE: replaced by #20799 & #25147
	# TODO: 16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					bf517f7cdd2
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					5c81646f647
	n/a   rpc_compat_error_index-23+knots		84cf91ccb21
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos-23+knots			5bdd6ed25cb last=539beeaae85 gui_bech32_errpos
	17636 guisettings-0.21						c8db2908604	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					45249322ccb	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						b2b9c2f14a5	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances				03994a2e5e3	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance			91193606e68	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock-23+k	c363d978f97	last=1e868bbbb1b
		TODO: Bump to #26094 (at least check for fixes)
	19117 rpc_getrpcwhitelist					bdbf8ecf130
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-23+knots		7a2a3bc75cd
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-23+knots		7f46d1a059e	last=36cc299baee whitelist_outgoing
		# NOTE: Originally #10594
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-23+knots		6c8fdc9a690
	# Needs careful review: 22702 martinus:2019-08-bulkpoolallocator
		# OR 25325 martinus:2022-06-very-not-scary-NodePoolResource
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan/1643263956-network-graph-issue-532
	Needs work? g650 -  # qt, refactor: Add Import to Wallet GUI
# Non-upstreamed functionality:
	TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	n/a   restore_feefilter_opt					b0a928d3f25
	-     gui_payreq_textedit					e2018a567ae
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				5ba35244a0b
	-     walletnotify_w_win-23+knots			2d3f0b887c9	# Latest code now
	14137 win_taskbar_progress					6b06461d6b8	last=18eb4dbb8a
	-     restore_blockmaxsize					ed77d9b99c2
	7107  qtnetworkport-23+knots				c37c20d1ca7	last=1f37c87d8f2 origin-pull/7107/head
	7533  sendraw_force							9746cd166d6
		# NOTE: partial re-PR in #20753 by Marco
		TODO: Compatibility with #25532 if merged
	11082 rwconf-23+knots						dbc972ce598 # Latest code now
	7510  rwconf_gui-23+knots					7342e194bdb
		TODO? gcp 0c9ffa1de8c (rwconf_gui-0.21) GUI/Options: Add tooltips for addresstype choices
		FIXME: s/P2SH-SegWit/P2SH Segwit/ (dash->space & lowercase W)
	 559 accept_nonstdtxn						2ad1e272d70
	 929 tbc									65ace212fac
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
	 553 bugfix_qt_uri_amount_parser			f110cdc6b5d
	-    mining_priority						79de7fcebc8  # NOTE: now the latest code, rebased
		#24.xTODO# Revert #24934 ?
	5861 gui_restore_addresses					d435b0e1596
	5891  qt_console_history_persist			aaedbe6c41a	last=0cd5fc301d6 qt_console_history_persist
	7219  fullrbf-23+knots						4eea3457d1a	last=5d58ebcc60f fullrbf # missing 91786d16ccc + revert34ae6640174
		149b286b44e (fullrbf-23+knots) rebased onto branch-23: 9e79f188695
		9e79f188695 rebased onto master: 08ebca8e0fc
		08ebca8e0fc..7e8cdb9eeea: Add fixups, diff-heavy refactoring, remove never-rebase
		7e8cdb9eeea squash fixups (but not ^diff-heavy+removal): c6decd62837 = #25373
		eb6bb1e3528 squash the rest: fe474794513
		fe474794513 rebased onto master: 5647bc061a2
		NOTE: Above work still needs:
			149b286b44e (fullrbf-23+knots) Advertise temporary REPLACE_BY_FEE service bit (when appropriate)
			dd77f450ee4 Recognise temporary REPLACE_BY_FEE service bit
		MISSING IN 22.x & 23.0? c10e54ecb54 (rbf_opts-0.21+knots) QA: feature_rbf: Test full-RBF service bit
			aka 7f5e66db399 Bugfix: Enable full RBF service bit by default
		NOTE: Competing PR now in #25353 +#25575
		TODO: Compatibility with #25353 ?
		NOTE: #25600 has RBF service bit
		24.xTODO: Update doc/policy/mempool-replacement.md
		NOTE: #25626 has -mempoolreplacement on Core - including new RPC getmempoolinfo values (be sure to backport as feature)
		TODO? gcp c10e54ecb54 QA: feature_rbf: Test full-RBF service bit
		TODO? rename to match Core?
		TODO? gcp a57bf40ca0c Document -mempoolreplacement=fee,-optin configuration
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					2a61c92f17e
		# TODO: Split out legacy address preference to be more explicit
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			f3109a9759d	# Latest code now
	-     gui_request_payment_label-0.19		45064c919be
	-     gui_peers_sort_network-23				d851c7b5730
	-     gui_peers_no_net_column				6d7c55fa917
	22439 guix_in_gitian-23+knots				b3670947f2d	last=ebda0463748 achow101/guix-in-gitian
	#24.xTODO# revert #23927  rpc: Pruning nodes can not fetch blocks before syncing past their height
	# TODO: revert #24031  build: don't compress macOS DMG
	TODO: * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		See #25922, backported with this in 21.x
# Non-upstreamed Knots compatibility:
	TODO: -netinfo and other version checks might need to be more flexible?
	#24.xTODO# revert? #24505  wallet: Add a deprecation warning for newly created legacy wallets
	14641 fundraw_min_conf_deprecated-23+knots	67bb2fae2cb	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			2b802cfbcf9
	-     netperms_implicit_addr				3ec6f62de90
	12674 rpc_onetry_nonpriv-23+knots			1ac3b6f764a
		BUG: 'privileged' compat param will be rejected by type check
	-     rpc_getblockfrompeer_nodeid_compat-23	f41b36c5abe
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-23+k		a71fc4dd708
		#24.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				d3686b812ea
	-     bytespersigopstrict-23+knots			1a34431caca
	9749  unique_spk_mempool-23+knots			68175ac94c1
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	-     bloom_default-0.21+knots				4910b8c3600
	-     wallet_avoid_newerchange				a5e70c68636
	24.xTODO: Revert #25725
	-     enforce_checkpoints					840dddd5a6e
	n/a   checkpoint_update-23					ec23e329857	last=70996dfdd9b checkpoint_update-0.21
	10282 timebomb_knots						28c6dff687b
	-     rwconf_policy-23+knots				85b37875e50
		# Includes Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
		TODO? gcp 3281bf5d1ae Add compatibility with -mempoolfullrbf option
		TODO? gcp 8a228791457 (rwconf_policy-0.21+knots) GUI/Options: When changing mempoolreplacement, update config file with mempoolfullrbf too
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		7502bba0dc8
	7483  svg_icon-23+knots						edbcba95282
	n/a   tbc_font								9929a597b3d
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/
# BRANDING:
	n/a   update_security_policy-21
		TODO: Review security policy
	n/a   knots_branding-23						0ef366334de
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Check calls to RPCConsole::clear(bool) get expected behaviour
	n/a  (cherrypick=165f473d4d068ee31a)		f6260178fc7	# doc/{bips,files}
	n/a  (bump_version=Knots:20220529)			3d04837ba68
#	n/a  knots_historical_relnotes				61100a2
	TODO: Ensure NSIS doesn't bundle _Core_ relnotes either! See #25809; also see #26139
	n/a   rm_historical_relnotes_from_dist		91954f0400c
	n/a  (cherrypick=7c9f28557be)				500a43eca75  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=e176316e332)				dd99e2b4305  # update manpages (build first)
		BELOW TODO: ensure 26117 is fixed
	n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @24.x-knots-android
