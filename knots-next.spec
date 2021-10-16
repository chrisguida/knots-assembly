timestamp 2021-10-16 01:09:19
lastapply no-merge

#.. checked up to PR #23289 / gui #454

checkout v22.0
@22.x-syslibs
# BUILD BUGS:
	21882 hebasto/210507-fuzz32					d994684b569	last=e4c8bb62e4a hebasto/210507-fuzz32
		# NOTE: Has improvements/fixes
	# Not needed (depends only): 22380 fanquake/set_std_c_version_depends
	22390 fanquake/netbsd_dont_set_locale					last=fdd71448e78
	# Needs review: 23030 -  # src/randomenv.cpp: fix uclibc build
	# OR: 23082 fanquake/remove_weak_auxval
	23045 fix_crc32c_arm64_detect-0.20						last=f2747d1602e laanwj/2021-09-arm64-crc32
	# Needs followup fix? 23182 fanquake/python_3_10_configure
# SYSLIBS: (and old build bugs)
	5872 subdir_incl_compat						f2e1e41e817
	2241 sys_leveldb							5e9497a8ed7
	5416  sys_libsecp256k1						c2e8d067f0b
	22412 bugfix_pushback_bool
	7485 sys_univalue_def						663a72e6a12
	13789 bugfix_asm_pragmas					82ab60f2428
	-     bugfix_asm_leveldb_check				741060d31b8
	15155 test_external_bcli					251dcff7eee
	-     opt_bdb_extracare						3d26b04ad0f
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	# TODO: system crc32c
@22.x-knotsfixes
# TESTS:
	-     lint_relaxer							9afa5d8517a
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
# FIXES:
	22318 hebasto/210623-random								last=35aab4f0c0b
	-     gitian_linux_reverttobionic-22
	18818 fix_gitian_src_202004					e7ae473f644
	18902 fix_gitdir_again						48e2ecb874f
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					51d41a3ea10	last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case				b9b3f3bd5c0
	17828 p2p_log_categories					bab13c46b9b	last=04960621582 practicalswift/log-categories
	# Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
	14968 http_bind_error						e75ff7b9323	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					81ed4fe33fa
		# NOTE: libevent-copied code up to date as of 2021-07-16 c29f1dbe116c88434e77721ca215b8d2082b247f
	9524 marco/Mf1701-qaPruning					ae3444d7950	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					3cee4ceb1b1
	14485 fadvise								e87f5a4c952
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	13608 -										bdb644e5423	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	-     rpcarg_type_per_name					7a602d396d9
	-     bugfix_rpc_getbalance_hacky			2fc80cecb4c
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	g404  bugfix_qvalidlineedit					7933a2d752b
		# Was #18133
	18194 bugfix_gui_edit_sendaddr-mini			64ebfdfb0a1	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18729 intro_dont_change_user_prune			25f70064ec8
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				a0f6d94c0b9	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19888 getblockstats_utxo_actual-22+knots	37dd20ac3a1	last=6cd78060c8e
		# Diff-minimised incl test changes
	# Needs review: 20196 vasild/fix_GetListenPort
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					e7a792e44b6
	-     bugfix_gui_drop_abc_confusing_hack	c0f258de92f
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				37fc886f39f
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	-     rpc_addconnection_mainnet
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22359 fix_wallet_pr22359-22					3244e0d002f	last=fa6fd3dd6a4
		# Semi-diff-minimised
	# Needs review: 22362 marco/2106-addrdb  # Drop (only) invalid entries when reading banlist
	22417 bpchild_closefds									last=3b6153ba336 bpchild_closefds
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
	g379  qt_reset_bad_settingsjson-0.21
	# FIXME: When upgrading any guix/gitian to GCC 9: Ensure #20005 "memcmp with constants that contain zero bytes are broken in GCC" gets addressed
	22577 fix_race_pr22577-22
	22591 missing_settings_err-0.21
	22834 bugfix_onlynet-22									last=0ea0de64385 vasild/onlynet
		# Refactored to be less optimised in favour of being more obviously correct
	# Needs review: 22665 darosior:rbf_optin_nomempool
	22722 fix_estsfee_minrelay-22							last=ea31caf6b4c  # rpc: update estimatesmartfee to return max of CBlockPolicyEstimator::estimateSmartFee, mempoollMinFee and minRelayTxFee
	23027 bugfix_util_test_config
	22781 fix_ishdenabled-0.21
	# Needs review: 22798 MarcoFalke:2108-docRpc
	# Needs review (& diff minimisation?): 22817 MarcoFalke:2108-testRaceConnect
	22820 fix_config_qtinputsupport-22
	# Needs review: 22834 vasild:onlynet
	# TODO? 22836 sipa:202108_bipvec5
	# Not worth added build overhead? 22840 fanquake:fix_depends_lib_optimisation
	22875 parseopcode_threadsafe-22							last=d5e006c84a1
	22879 fix_addrman_err_format-22							last=fab0b55cf06	marco/2109-testPeersDat
	22895 fix_RBFD_lock_pr22895-22
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review: 22929 S3RK/fix_19856
	# Needs review and diff minimisation: 22932 jonatack:require-GetBlockPos-to-hold-cs_main
	g399  fix_load_psbt_wo_wallet-22
	g409  fix_gui_walletop_titlebar-22						last=01bff8f0494
		# Held back trivial comment change f86fe193329..01bff8f0494
	g418  mac_platform_metadata-0.20						last=3765c486ef5 jarolrod-g/applesilicon-categorization
	23050 bugfix_pr23050-0.15  # log: change an incorrect fee to fee rate, and vice-versa
	23061 fix_argparse_persistmempool-22
	# Needs review & concept check: 23074 Package-aware fee estimation
	23106 fix_unlock_before_psbtsign-22
	# TODO: 23139 jonatack/fix-rpc-trusted-field-help
	# Needs review: 23140 sipa/202109_addrmanbias
	# Not sure about this: 23142 meshcollider:202109_no_assert_corruption
	g430 gui_txlinks_g430-22
		# NOTE: Left off trivial string change
	g439 gui_hide_unused_icons-0.20
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	Just fix from 23148 dongcarl/2021-09-fix-loader-quick (copy out of #23276)
	# Needs review: 23197 jonatack/fix-netaddress-UB-and-banman-fuzz-crash
	# Needs review: 23227 marco/2110-ToIntegral
	# Needs review of backport-rewrite in qt_catch_rpc_index_overflow-0.18 [alt to g446  marco/2110-qtRpcCons]
	# TODO: 23268 prayank23/dns-seed-fqdn
	-    gui_revert_g296
	# TODO: 23253 marco/2110-utilTxSeqId
	# Needs careful work: 23277 -  # wallet: Add size check on meta.key_origin.path
@22.x-knots
# SOFTFORK:
	21934 rpc_getblockchaininfo_lockedin_statistics	fe4dfbf3f33	last=2b19f3443ef rpc_getblockchaininfo_lockedin_statistics
	22016 rpc_gbci_period_start-22+knots		4910107f0d1	last=70d7e0812a7 Sjors/2021/05/versionbits_period_start
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	-     restore_win32-22						d37803a84cc	last=3e30ae0514e restore_win32
	# TODO: guix win32
	-     gitian_linux32						efa9ee85ed6
	-     guix_linux_i686
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
	14641 fundraw_minconf						fde6c8132bc	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	12677 listunspent_ancestorinfo				28b3902be59
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					4d67400f273	last=47b2ba29df2 !kallewoof/sign-show-fees
		# NOTE: Originally #12911
	# Needs review and care (new index): 13014 jonas/2018/04/txindex_prune
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# wait for Core?: 14707  # [RPC] Include coinbase transactions in receivedby RPCs
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	g119  rm_send2self-mini						f97c6773966	last=aa744e4382e rm_send2self
		# NOTE: Originally #15115
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						67bfe9cad94	last=d37d95a9ea2 tor_socks_port
		# Held back 962f168a014..398df42f449
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram+pr15836_api				82829beb890	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ?
	(CHECK-LAST)	last=f2ca3d35ee9 origin-pull/21422/head
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
	15987 wallet_warn_reuse_gui					7515d038c84
	22693 getaddressinfo_txids					01bfbd88472
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	22918 rpc_getblock_prevouts_fees-22			5b3f15dcda3	last=5c34507ecbb
		# Was originally #16083, then #21245
		# Left off release notes & variable rename (last 2 commits)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	16795 rpc_inferred_output_descriptors		5de05c6c9f6	last=5e256883651 instagibbs/decode_descriptor
	# Needs review: 16981 LarryRuane:reindex-speedup
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs review: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options? (watch out for send RPC)
		# TODO: Diff-minimise
		# Cleanups in #23188; fix in #23200
	18972 neutrino_whitelist-mini				892d210d2eb	last=a3300c6b200 neutrino_whitelist
		# NOTE: Diff-minimised
	17034 psbt_ver_proprietary_xpub-22-mini		8cfa229a8e4	last=7f066240654 achow101/bip174-extensions
		# NOTE: Diff-minimised
		# NOTE: Now includes 16463 bip174_xpub-0.21+knots				8e6f8d3cc9c	last=9926a387eab achow101/bip174-xpub
	17631 rest_blockfilter-22					31a7b2798a2	last=7cf4e220801 matt/2019-11-filter-rest
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	g319  gui_openuri_pastebtn-22				3cb5fcd37dd	last=dbde0558ce7
		# NOTE: Used to be #17955
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	996d632f395	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	18689 rpc_dumptxoutset_hr					86a235cbd1f	last=65d0697fe34
		# NOTE: Moved rpc/client lines to avoid conflict with #20664
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								0501a4912b2
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							7688250cdac	last=1ad45edbfeb prune_locks
	# Needs review: 18000 -  # Coin Statistics Index
	22047 pr22047-22
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	19762 ryanofsky/pr/named					06d0b03981c	last=894c414dafb
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							d629ab65bcc
	# Needs work: 20154 kallewoof/202010-bip322
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			088733fcf9a	last=1f373f93a60  # Enlarge Network Traffic Graph
		# TODO: src/qt/forms/debugwindow.ui:696: Recieved ==> Received
		# WAS gui#90
		# Removed dialog size change
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
	20295 rpc_getblockfrompeer_wo_header-22		947c37b0b52	last=9181e2e2179 Sjors/2020/11/getblockfrompeer
		# Left out code movement
		# Re-enabled fetching blocks w/o already having header (from older version of PR)
		# Moved code to avoid conflict with 22577
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-22						ed17a7d8d62	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20407 rpcauthfile							0726f132d9d	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						8979d48f938
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20664 rpc_scanblocks						ad927cbdb4c	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
	20702 rpc_getblocklocations					8db5bda17bd	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							1dcbfaca3b6
	g363  qt_peers_directionarrow-22+knots		4c6de52a7fc	last=217d1051c8b qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
	# Needs review: 21006 -  # rpc: reduce LOCK(cs_min) scope in rest_block: ~5 times as many requests per second
	15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
	# ---- BEGIN HWI SUPPORT, TODO ----
	21576 rpc_bumpfee_signer-22								last=25aa986a53c Sjors/2021/04/signer_bumpfee
		# Simply dropped misc comment changes in first commit
	21928 hww_toggle-22+knots								last=8a4eaafe271 Sjors/2021/05/hww-toggle
	# ---- END HWI SUPPORT ----
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise						b79a8d71419
		# Context: 17529 rpc: Faster getblock using PureBlock
	# Needs API finalisation: 21158 -  # lib: Add Taproot support to libconsensus
		#TODO: minimise
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 -										28ec9283de6	last=46bf0b7b5d8  # rpcwallet_tx_in_mempool-0.21
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	21327 p2p_ignore_tx_in_ibd-22				093927be571	last=648c5c73aef  # p2p_ignore_tx_in_ibd-0.21
		# NOTE: Resolved silent conflict FromHex->from_hex
	g368  bugfix_gui_restored_columns_stretch	6facbfb184d
	g230  gui_backup_formats					557904a49bb
	# TODO? 21413 glozow/2021-03-bypass-timelocks
	# Needs Concept ACK: 21500 S3RK:listdescriptors_private
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
	# Needs review: 21528 amitiuttarwar:2021-03-addr-defer2
		# + 22616 + 22618?
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rpc_maxmempool						0bc176fa910	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Too many conflicts: 21832 cli_color_getinfo-0.21							last=14cb2e0fe13
		# Needs fix 22959 -  # cli: Display all proxies in -getinfo
	# Needs reivew: 21841 rebroad/SteadierFeefilter
	# Needs completion: 21851 fanquake/m1_support_depends
		# +22070 (MERGED UPSTREAM)
	# Needs review/optionality: 22009 achow101:cs-waste-2
	# Duplicate (of #14641): 22049 -  # rpc: allow specifying min chain depth for inputs in fund calls
	22072 -										66d83231979	last=602f4da9178  # autoreindex-0.21
	22159 marco/2106-buildPattern				deede4f8965	last=fa14c6818f4 marco/2106-buildPattern
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt-22				7d9f56d4c76	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	g318  gui_peers_copyaddr-22					172639c9e05	last=3ec061d9da0 jarolrod-g/copy-addr-peer
	# Needs review: g342 hebasto-g/210521-wallet
		# NOTE: Will require newer changes from gui#409 above
	# Needs review: jonatack/ProtectEvictionCandidatesByRatio-perf-enhancements
	22288 torcontrol_dnslookup-0.21				d8f8412dcc4	last=cdd51e8ee15
		# Diff-minimised
	# Needs review: 22340 -  # Use legacy relaying to download blocks in blocks-only mode
		# NOTE: Rebased in 0e3b643ba55
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
	# Needs work: 22350 -  # Log rotation
	22372 multinotify
	22383 -													last=78f4c8b98ea  # rpc: Prefer to use txindex if available for GetTransaction
	# TODO: 22609 theStack/202107-gettransaction_remove_lock
		# TODO: Check for safety
	22407 -													last=20edf4bcf61
		# NOTE: promag's own branch is not up to date
	22501 netinfo_addr_stats-22								last=218862a0184 jonatack/netinfo-addr-statistics
	22513 rpcwallet_psbt_no_finalize-22+knots				last=a99ed898655 achow101/psbt-no-finalize
		# Modified to use a new options object instead of an additional bool positional param
	# Needs review: 22514 achow101/psbt-sighash-default
	g384  -													last=ab1461d5d36  # add copy subnet action for banned peer
	# TODO: Minimal 22539 darosior/fee_est_rbf
	# Needs more careful security review: 22541 Add a new RPC command: restorewallet
		# TODO: restrict access in multiwallet_rpc
	# TODO? 22546 hebasto:210725-deploy
	# TODO: 22547 -  # cli: Add progress bar for -getinfo
	# Needs review: 22558 achow101:taproot-psbt
	# Needs review: 22563 vasild:addrman_per_group_bucketing
	# TODO? Diff-minimised 22604 jonatack:rate_limit_addr_follow-ups
	# Needs review: 22674 glozow:package-child-with-parents
	# Needs review: vasild:torbind
	22751 simulaterawtx-22									last=b269f1bb0d6 kallewoof/202108-analyzerawtransaction
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Only if Core merges (alternative makes more sense): 22776 kallewoof:202108-getbalances-tx
	# TODO? 22777 jnewbery/2021-08-feeler-no-frelay
	# TODO: 22778 jnewbery:2021-02-tx-relay-init
	22789 extsigner_pr22789-22								last=d047ed729f1  # external_signer: improve fingerprint matching logic (stop on first match)
		# Rewritten to diff-minimise and simplify
	# Needs BIP? 22838 achow101:multipath-descs
	# TODO? 22894 jonatack/netinfo-clarify-client-and-server-versions
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs review: 22934 -  # Add verification to Sign, SignCompact and SignSchnorr
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	g390  gui_defopt_subfeefromamt-22
	g391  -													last=0b869df1c91  # Add cancel button to configuration options popup
	g408  gui_mnemonics_g408-22  # Add missing mnemonics in menu bar options
	# Needs work: g410  benthecarman/uppercase-uri
	g416  gui_rpcserver_opt-0.18							last=bd5c826a963 Sjors-g/2021/09/rpc_setting
		# NOTE: Includes gui#449
	g419  gui_dbcache_s.threads_tooltips-0.9				last=9bd168bf545 jarolrod-g/options-tooltips
	# Needs Core release (wallet format change): 23065 meshcollider/202109_lockunspent_persistence
	# Needs work: 23077 vasild/cjdns
		# Followup in #23175
	23113 rpc_multisig_uncomp_warnings-0.21					last=29a78ac4319 meshcollider/202109_createmultisig_warnings
		# Left off final commit with relnotes
	# Why merge this before Core? (last commit only?) 23115 fanquake:18985_rebased (note: merged in master already)
	# Needs work: 23152 fanquake/experiment_with_lto
	# TODO: 23155 jamesob/2021-10-au-rpc-fixes #diff-minimise
	g436  gui_coinctrl_copyoutpoint-22
	# Needs review (& bumpfee fix?): 23201 achow101/ext-input-weight
# Non-progress functionality:
	8751  sort-multisigs-22						e06c15ceea1	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152 sweepprivkeys							9d6360908e1
	9245 ionice									52ed64216eb
	-    ionice_win								22b1c9241e8
	8501  old_stats_rpc-22						2fa33c1f65c	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-22						24601755a13	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-22					f9192d9a751	last=07fc81109a
	g444  gui_netwatch-22+knots					539fa817d21	last=2db813077d1 gui_netwatch
		# NOTE: Was #9849
	10615 multiwallet_rpc-22+knots			cc2b14bbbcf	last=5a10f8307a5 multiwallet_rpc
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-22+knots						dad75802d23	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					7a1723439c5
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment				040052148d5
	10350 filtered_witblock-22				5cb7a4a645a	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				e40fcaeb7fe	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								d2f6a3d7d5d	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			3b64c7195f0
	12965 scriptthreads							8d959f05d3c	last=dfab6c6866 jonas/2018/04/svt
	13203 dsha256_power8-0.20					9703ce00ee9	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		6ceb71baa4c
	15218 postibd_flush-22+knots				84b38613864	last=d2ecb70d64  # validation: Flush state after initial sync
		# TODO: Rewrite after #17487 is ready/safe to merge
	15428 tor_gui_pairing-22+knots				e509f51807e	# latest code now
	15421 tor_subprocess-22+knots				3de8ab01bf5	last=58c6cafd3a1 tor_subprocess
	# TODO: tor gitian bundle! /guix
	15633 nohbcbfornonwit						c48ce12aa19
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# TODO: 16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					ca0940d77b6
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					43dad5a3906
	16807 old_bech32_error_detection			47e52930e8f	last=88cc4810926 meshcollider/201909_bech32_error_detection
		# Held back rewrite 3bc568d6753..974227bb457 for now
		# Held back comment drop 974227bb457..88cc4810926
	n/a   rpc_compat_error_index-22+knots		c0b669d2000
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	-     gui_bech32_errpos-22+knots			63858cb48e1  # Latest code
	17636 guisettings-0.21						d4da7377cb0	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					95572de08a2	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						fbe06449a10	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances				19e9d705f4c	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance			aedba84cdb0	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock-22+k	a03387247fb	last=1e868bbbb1b
	# TODO: g441 achow101-g/create-unsigned-sendconfdialog
		#TODO: Resolve conflict with wallet_warn_reuse_gui
		#OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	19117 rpc_getrpcwhitelist					4e5e20bd9ec
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-22+knots		bfaf26b19f1
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-22+knots		d6b39ef5628	last=81622ba1229 whitelist_outgoing
		# NOTE: Originally #10594
	# Needs purpose: 21815 prayank23:max-out-full-relay
	# FIXME: text below QR Code doesn't fit bech32 with Console font!
	-     wallettool_dump_warning-22+knots
	# Needs careful review: 22702 martinus:2019-08-bulkpoolallocator
	# Needs work: 22708 hebasto:210815-wayland
	# TODO (needs concept review?): 23093 meshcollider:202109_keypoolrefill
# Non-upstreamed functionality:
	n/a   restore_feefilter_opt
	# 23.0 TODO: Determine whether #22260 (wallet Bech32m default) is good or should be reverted
	-     gui_payreq_textedit					4a9c6fc46e5
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				011b11763f6
	-     walletnotify_w_win-22+knots			0fafbd4a598	last=a291491d2fd walletnotify_w_win
	14137 win_taskbar_progress					35568cf34dd	last=18eb4dbb8a
	-     restore_blockmaxsize					7cf11b880fc
	7107 qtnetworkport							dd2ad9343f6	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							1c4e51255a4
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								9eefbf8c5fb
	7510  rwconf_gui							31da64c50bc
	 559 accept_nonstdtxn						854677f3a98
	 929 tbc									b92159120bd
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
	 553 bugfix_qt_uri_amount_parser			2bef446009c
	-    mining_priority						c1b36c3197d  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					8fa52dc8120
	5891  qt_console_history_persist			7ed83221a81	last=0cd5fc301d6 qt_console_history_persist
	7219  fullrbf-22+knots						ec4af75863b	last=5d58ebcc60f fullrbf # missing 91786d16ccc + revert34ae6640174
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					c84af5db7d7
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			71cc4a727ef	# Latest code now
	-     gui_request_payment_label-0.19		bd9ec2f9431
	-     gui_peers_sort_network-22				a3e6f0ec5e2
	-     gui_peers_no_net_column
	22439 guix_in_gitian									last=ebda0463748 achow101/guix-in-gitian
# Non-upstreamed Knots compatibility:
	-    preserve_unsupported_keyflags			8c461dcdced
	11413 rpc_feemode_explicit_compat-22		ca8dbc1e33d
	-     netperms_implicit_addr				14687738e62
	12674 rpc_onetry_nonpriv-22+knots			b235a94b1ba
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-22+k
		# TODO: Each release, see if we need to bump setting names for GUI states
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				66fa127a85b
	-     bytespersigopstrict-22+knots			42fef5047e8
	9749  unique_spk_mempool-22+knots			6f7822ceed3
	-     bloom_default-0.21+knots				d714d612b62
	-     enforce_checkpoints					d41dcd18f7c
	n/a   checkpoint_update-22					79d59f9403e
	10282 timebomb_knots						c8b2793aff0
	-     rwconf_policy-22+knots				bae9992c73c
		# Include Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (cherrypick=eaa9f92b50b)  # delete release notes fragments
	7483  svg_icon-22+knots						469d40983b1
	n/a   tbc_font
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
# BRANDING:
	n/a   knots_branding-22						1ee7ca43f35
#FIXME: check there's no univalue push_back(bool) - see #20424 and stash 8724e2fae4
#FIXME: Check there are no menu icons
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Check calls to RPCConsole::clear(bool) get expected behaviour
	n/a  (cherrypick=0ed7b3b85d3f618838)		c7a144c218c	# doc/{bips,files}
	n/a  (bump_version=Knots:20211016)			0a9a4537a5d
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=5248e288238)				f1cc3f1e0b1  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=15212a98dd3)				6addc3eccab  # update manpages (build first)
	n/a  (cherrypick=f06522e8aa9)				a886811721c  # translation update
		# TODO: git grep '＆\|％\|&amp;amp;'
# NOTE: use git diff --minimal for patches!

@22.x-knots-android
