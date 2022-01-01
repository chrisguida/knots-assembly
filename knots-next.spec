timestamp 2021-12-13 10:39:46
lastapply no-merge

#.. checked up to PR #23762 / gui #506

checkout origin/master
@22.x-syslibs
# BUILD BUGS:
	# Not needed (depends only): 22380 fanquake/set_std_c_version_depends
	23607 -													last=c62d763fc31  # evhttp_connection_get_peer compatibility with possible-future libevent
	# Needs review: 23609 hebasto/211126-reduce
	5872 subdir_incl_compat						a218f649f67
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb							8cb438ae8ca
	5416  sys_libsecp256k1						6bb55432d3d
	-     sys_univalue
	7485 sys_univalue_def						1d03ddd0d67
	13789 bugfix_asm_pragmas					2fffe355376
	-     bugfix_asm_leveldb_check				74ba4e0ac1f
	15155 test_external_bcli					0c5868df17b
	-     opt_bdb_extracare						27c4d454903
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
@22.x-knotsfixes
# TESTS:
	-     lint_relaxer							f351877c154
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
# FIXES:
	22318 hebasto/210623-random					19e3a797c2c	last=35aab4f0c0b
	-     fix_gitian_gcc8						17e23cf927b
	-     gitian_reverttobionic-22				7a70cb930d8
		# Revert everything to bionic:
		# - avoids GCC 9 (memcmp bug)
		# - avoids GCC bug 102993 (cf-protection=full segfaults in generated Win32 code)
		# - avoids dependency on newer glibc symbols
	18818 fix_gitian_src_202004-22+knots		e8914fe7cab	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again						48e994efd24
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					55e20380c66	last=570ac855612 2020mingwthrd
	18490 bugfix_symcheck_pe_case				be8f2d388ea
	17828 p2p_log_categories					037303a8383	last=04960621582 practicalswift/log-categories
	# Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
	14968 http_bind_error						2d0253e07a7	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					e22b19f9462
		# NOTE: libevent-copied code up to date as of 2021-07-16 c29f1dbe116c88434e77721ca215b8d2082b247f
	9524 marco/Mf1701-qaPruning					5d299ba2a6b	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					93e8f48f027
	14485 fadvise								9c2d09f9515
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	13608 -										2be248b0a77	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	-     rpcarg_type_per_name					d40fdba46d8
	-     bugfix_rpc_getbalance_hacky			b783debf686
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
	g404  bugfix_qvalidlineedit					6174a01aa1a
		# Was #18133
	18194 bugfix_gui_edit_sendaddr-mini			39f0ee79b01	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18729 intro_dont_change_user_prune			39b2462ba7b
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				03d0ef69ca2	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19888 getblockstats_utxo_actual-22+knots	d0fceeac30a	last=6cd78060c8e
		# Diff-minimised incl test changes
	# Needs review: 20196 vasild/fix_GetListenPort
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					6d5fc327268
	-     bugfix_gui_drop_abc_confusing_hack	0ac70704c08
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				9859a56089a
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	-     rpc_addconnection_mainnet				d7d29e53ba2
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	# Needs review: 22362 marco/2106-addrdb  # Drop (only) invalid entries when reading banlist
	22417 bpchild_closefds						95725111d52	last=3b6153ba336 bpchild_closefds
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
	# FIXME: When upgrading any guix/gitian to GCC 9: Ensure #20005 "memcmp with constants that contain zero bytes are broken in GCC" gets addressed
	22834 bugfix_onlynet-22						22f55e6b0b5	last=051c2554ca1 vasild/onlynet
		# Refactored to be less optimised in favour of being more obviously correct
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				162911e79ab
	# Needs review: 22798 MarcoFalke:2108-docRpc
	# Needs review (& diff minimisation?): 22817 MarcoFalke:2108-testRaceConnect
	# Needs review: 22834 vasild:onlynet
	# TODO? 22836 sipa:202108_bipvec5
	# Not worth added build overhead? 22840 fanquake:fix_depends_lib_optimisation
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review: 22929 S3RK/fix_19856
	# Needs review and diff minimisation: 22932 jonatack:require-GetBlockPos-to-hold-cs_main
	# Needs review & concept check: 23074 Package-aware fee estimation
	# TODO: 23139 jonatack/fix-rpc-trusted-field-help
	# Needs review: 23140 sipa/202109_addrmanbias
	# Not sure about this: 23142 meshcollider:202109_no_assert_corruption
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs review: 23197 jonatack/fix-netaddress-UB-and-banman-fuzz-crash
	# Needs review: 23227 marco/2110-ToIntegral
	# Needs review of backport-rewrite in qt_catch_rpc_index_overflow-0.18 [alt to g446  marco/2110-qtRpcCons]
	# TODO: 23268 prayank23/dns-seed-fqdn
	-    gui_revert_g296						b6869ae3ee7
	# TODO: 23253 marco/2110-utilTxSeqId
	# Needs careful work: 23277 -  # wallet: Add size check on meta.key_origin.path
	# Needs care/review: 23304 achow101/inactivehd-derive-keypath-string
	# Maybe just the docs from #23341 ?
	# Needs review: 23365 -  # index: Fix backwards search for bestblock
	# Needs review + diff minimisation: 23380 jnewbery:2021-10-addrman-add-logging
		# + fix in #23434 ???
	# Needs work/diff-minimisation: 23418 marco/2111-txPoolPrioOverflow
	# Needs review/diff-minimisation: 23486 marco/2111-rpcScript
	# Needs work: 23502 achow101/tr-low-fee-est
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	# Needs review: 23628 -  # Check descriptors returned by external signers
	# Needs review: 23631 -  # p2p: Don't use timestamps from inbound peers for Adjusted Time
	# Needs review: 23673 hebasto/211204-native
	g506  qt_qrcode_sizefixes
		TODO: Allow customising the font with g497
@22.x-knots
# SOFTFORK:
	22016 Sjors/2021/05/versionbits_period_start	32dd1d34493	last=70d7e0812a7
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	-     gitian_linux32						95d78266cd4
	-     guix_linux_i686						d7cabad678b
		FIXME: symbol __divmoddi4 from unsupported version GCC_7.0.0
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
	14641 fundraw_minconf						1699bed43a1	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					3981f3114b6	last=47b2ba29df2 !kallewoof/sign-show-fees
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
	# wait for Core?: 14707  # [RPC] Include coinbase transactions in receivedby RPCs
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	g119  rm_send2self-mini						12909b036b0	last=aa744e4382e rm_send2self
		# NOTE: Originally #15115
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						07f2e143d73	last=d37d95a9ea2 tor_socks_port
		# Held back 962f168a014..398df42f449
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram+pr15836_api				855210e5045	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ?
	(CHECK-LAST)	last=f2ca3d35ee9 origin-pull/21422/head
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
	22693 getaddressinfo_txids					a2dd1687f06
	15987 wallet_warn_reuse_gui					3cd9339e389
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	MERGED: 22918 rpc_getblock_prevouts_fees-22			74d372ceec3	last=5c34507ecbb
		# Was originally #16083, then #21245
		# Left off release notes & variable rename (last 2 commits)
		# + docs from #23320 (left off refactor commit)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	16795 rpc_inferred_output_descriptors		c5703402a3d	last=5e256883651 instagibbs/decode_descriptor
	# Needs review: 16981 LarryRuane:reindex-speedup
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs review: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options? (watch out for send RPC)
		# TODO: Diff-minimise
		# Cleanups in #23188; fix in #23200
	18972 neutrino_whitelist-mini				90b945d9f21	last=a3300c6b200 neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	MERGED: g319  gui_openuri_pastebtn-22				ec5bceab101	last=dbde0558ce7
		# NOTE: Used to be #17955
		FIXME: Missing Alt+P shortcut key
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	65bdd6b4b43	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	18689 rpc_dumptxoutset_hr					63bd42e0546	last=65d0697fe34
		# Fixed bugs (eg, scoping of ascii_types)
		# NOTE: Moved rpc/client lines to avoid conflict with #20664
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								2b7b1f97f42
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							05583647cd3	last=1ad45edbfeb prune_locks
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	19762 ryanofsky/pr/named					387e706f17f	last=894c414dafb
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							ef44bb829e6
	# Needs work: 20154 kallewoof/202010-bip322
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			6af482d58f7	last=1f373f93a60  # Enlarge Network Traffic Graph
		# TODO: src/qt/forms/debugwindow.ui:696: Recieved ==> Received
		# WAS gui#90
		# Removed dialog size change
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
	MERGED: 20295 rpc_getblockfrompeer_wo_header-22		42a76849c19	last=9181e2e2179 Sjors/2020/11/getblockfrompeer
		# Left out code movement
		# Re-enabled fetching blocks w/o already having header (from older version of PR)
		# Moved code to avoid conflict with 22577
		TODO: gcp 15f7d87c757 RPC: Ensure getblockfrompeer errors if the peer doesn't exist, even if we already have the block
		TODO: +#23706
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-22						237cdcaf3ee	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20407 rpcauthfile							aea95ce8fe7	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						aa633c92306
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20664 rpc_scanblocks						7c0065a63e4	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
		# Added return value documentation (needed for QA to pass)
		TODO: migrate to #23549
	20702 rpc_getblocklocations					aa48cd06cbd	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							fae2ccbd3f9
	g363  qt_peers_directionarrow-22+knots		63d06a67ec1	last=217d1051c8b qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		TODO: 21.x aligns the direction column on the right side
	# Needs review: 21006 -  # rpc: reduce LOCK(cs_min) scope in rest_block: ~5 times as many requests per second
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	# ---- BEGIN HWI SUPPORT, TODO ----
	21576 rpc_bumpfee_signer-22					b8b2d2d9baa	last=25aa986a53c Sjors/2021/04/signer_bumpfee
		# Simply dropped misc comment changes in first commit
	21928 Sjors/2021/05/hww-toggle				c1697fa9595	last=9fcf3025aae
	# ---- END HWI SUPPORT ----
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise						90e42283f94
		# Context: 17529 rpc: Faster getblock using PureBlock
	# Needs API finalisation: 21158 -  # lib: Add Taproot support to libconsensus
		#TODO: minimise
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 -										3fedb585da1	last=46bf0b7b5d8  # rpcwallet_tx_in_mempool-0.21
		TODO: Merge fixes from rpcwallet_tx_in_mempool-21.1+knots
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	g368  bugfix_gui_restored_columns_stretch	7b17ac26a1f
	g230  gui_backup_formats					8d2249823b3
	# TODO? 21413 glozow/2021-03-bypass-timelocks
	# Needs Concept ACK: 21500 S3RK:listdescriptors_private
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
	# Needs review: 21528 amitiuttarwar:2021-03-addr-defer2
		# + 22616 + 22618?
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rpc_maxmempool						de6aa3acf24	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Too many conflicts: 21832 cli_color_getinfo-0.21							last=14cb2e0fe13
		# Needs fix 22959 -  # cli: Display all proxies in -getinfo
	# Needs reivew: 21841 rebroad/SteadierFeefilter
	# Needs completion: 21851 fanquake/m1_support_depends
		# +22070 (MERGED UPSTREAM)
	# Needs review/optionality: 22009 achow101:cs-waste-2
	# Duplicate (of #14641): 22049 -  # rpc: allow specifying min chain depth for inputs in fund calls
	22072 -										98ae86d5a81	last=602f4da9178  # autoreindex-0.21
	22159 marco/2106-buildPattern				6c70dc6bc61	last=fa14c6818f4 marco/2106-buildPattern
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt-22				74d6f3d34c6	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Needs review: g342 hebasto-g/210521-wallet
		# NOTE: Will require newer changes from gui#409 above
	# Needs review: jonatack/ProtectEvictionCandidatesByRatio-perf-enhancements
	# Needs review: 22340 -  # Use legacy relaying to download blocks in blocks-only mode
		# NOTE: Rebased in 0e3b643ba55
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							05053cd7598
	# TODO: 22609 theStack/202107-gettransaction_remove_lock
		# TODO: Check for safety
	MERGED: 22513 rpcwallet_psbt_no_finalize-22+knots	51cac865a4d	last=a99ed898655 achow101/psbt-no-finalize
		# Modified to use a new options object instead of an additional bool positional param
	# Needs review: 22514 achow101/psbt-sighash-default
	# TODO: Minimal 22539 darosior/fee_est_rbf
	# Needs more careful security review: 22541 Add a new RPC command: restorewallet
		# TODO: restrict access in multiwallet_rpc
	# Needs work: g471 -  # Add Wallet Restore in the GUI
	# TODO? 22546 hebasto:210725-deploy
	# TODO: 22547 -  # cli: Add progress bar for -getinfo
	# Needs review: 22558 achow101:taproot-psbt
	# Needs review: 22563 vasild:addrman_per_group_bucketing
	# TODO? Diff-minimised 22604 jonatack:rate_limit_addr_follow-ups
	# Needs review: 22674 glozow:package-child-with-parents
	# Needs review: vasild:torbind
	22751 kallewoof/202108-analyzerawtransaction		364c0507238	last=b269f1bb0d6  # simulaterawtx
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Only if Core merges (alternative makes more sense): 22776 kallewoof:202108-getbalances-tx
	# TODO? 22777 jnewbery/2021-08-feeler-no-frelay
	# TODO: 22778 jnewbery:2021-02-tx-relay-init
	# Needs BIP? 22838 achow101:multipath-descs
	# TODO? 22894 jonatack/netinfo-clarify-client-and-server-versions
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs review: 22934 -  # Add verification to Sign, SignCompact and SignSchnorr
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs work: g410  benthecarman/uppercase-uri
	# Needs Core release (wallet format change): 23065 meshcollider/202109_lockunspent_persistence
	# Needs work: 23077 vasild/cjdns
		# Followup in #23175
	# Why merge this before Core? (last commit only?) 23115 fanquake:18985_rebased (note: merged in master already)
	# Needs work: 23152 fanquake/experiment_with_lto
	# TODO: 23155 jamesob/2021-10-au-rpc-fixes #diff-minimise
	# Needs review (& bumpfee fix?): 23201 achow101/ext-input-weight
	# Needs review: 23319 -  # rpc: Return fee and prevout (utxos) to getrawtransaction
		# Rebase of 2c56d72acac in a662191612c w/ failing test :/ (had to replace hard-coded fee assumption too)
	# Needs API review: 23330 JeremyRubin/header-fetch
	23362 importfromcoldcard-22					ba52f717337	last=8076f8d4c2a hebasto/211025-cc
		# Needed fs::Path{To,From}String rebasing
		# Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 greenaddress/dump_fee_estimates		ec0f6c01a85	last=d5b41e6b2ed  # savefeeestimates
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work: g459 Sjors-g/2021/10/taproot_gui
	# Needs concept review: 23395 -  # util: Add -shutdownnotify option
	# Needs careful review: 23397 hebasto/211030-contention
	23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs review/walletsafety checks: 23480 sipa/202110_untweakedtr
	# Needs diff-minimisation and de-removal: 23508 ajtowns/202111-getforkinfo
	# Not worth it? 23510 -  # doc: Fixed dead link in build-unix.md
	# Diff-minimised? 23512 marco/2111-policyTaprootActive
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs work: 23578 Sjors/2021/11/taproot_signer
	# Needs work: 23611 fanquake/lto_in_depends
	Review: 23624 -  # zmq: add rawmempooltx publisher
	TODO: Alternative to g459 Add Taproot checkbox to receive tab
	g469  achow101-g/b64-psbt-gui
	g473  rebroad-g/NonLinearTraffic
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	# Needs concept (performance hit?): 23662 theStack:202112-rpc-improve_getreceivedby_performance
	# Needs review: 23718 darosior/psbt_preimages_fields
	g492  rebroad-g/NetworkGraphTooltip
	g497  qt_fontsel
	# idk 23724 -  # build: add systemtap's sys/sdt.h as depends for GUIX builds with USDT tracepoints
	# Needs work? g505  -  # RPCConsole: add hidePeersDetail() button and functionality
# Non-progress functionality:
	8751  sort-multisigs-22						6923385f2e0	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152 sweepprivkeys							a11d2d5c91d
	9245 ionice									f3b535766d2
	-    ionice_win								370875f21a3
	8501  old_stats_rpc-22						2f51ef3fa07	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-22						48a7702ab96	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-22					e7951b8f304	last=07fc81109a
	g444  gui_netwatch-22+knots					921c47226f3	last=b227e4db46f gui_netwatch
		# NOTE: Was #9849
	10615 multiwallet_rpc-22+knots			a0cae660051	last=5a10f8307a5 multiwallet_rpc
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-22+knots						27d1ffd6d18	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					898fc5bf686
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment				f582f6c385f
	10350 filtered_witblock-22				1540619da62	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				344d8477765	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								c79b2dd3914	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			48684964394
	12965 scriptthreads							cc6dca5b8d6	last=dfab6c6866 jonas/2018/04/svt
	13203 dsha256_power8-0.20					7a7804cd627	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		8ef3c1cb910
	15218 postibd_flush-22+knots				5a11498f7df	last=d2ecb70d64  # validation: Flush state after initial sync
		# TODO: Rewrite after #17487 is ready/safe to merge
	15428 tor_gui_pairing-22+knots				b0cfbb9f68f	last=16cb2ae1fe0 tor_gui_pairing-0.21+knots
		FIXME: Revert 4a881554991 (buggy) in favour of g506
	15421 tor_subprocess-22+knots				db4dd219005	last=58c6cafd3a1 tor_subprocess
	# TODO: tor gitian bundle! /guix
	15633 nohbcbfornonwit						8e9e203c847
		FIXME: Revisit why f5e4f1650fe is necessary in 22.x, but not in 21.x where the same code exists
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# TODO: 16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					20a8f506a89
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					115213e2bd8
	MERGED: 16807 old_bech32_error_detection			09c2d5f6fd5	last=88cc4810926 meshcollider/201909_bech32_error_detection
		# Held back rewrite 3bc568d6753..974227bb457 for now; when updating, add in #23577
		# Held back comment drop 974227bb457..88cc4810926
	n/a   rpc_compat_error_index-22+knots		733deba4309
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	-     gui_bech32_errpos-22+knots			b0efb7af93b  # Latest code
	17636 guisettings-0.21						b7ca66c8205	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					c59bc862411	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						7865582eebd	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances				539b445c55f	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance			5db2713785a	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock-22+k	76f79fc7494	last=1e868bbbb1b
	# TODO: g441 achow101-g/create-unsigned-sendconfdialog
		#TODO: Resolve conflict with wallet_warn_reuse_gui
		#OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	19117 rpc_getrpcwhitelist					e889e17cb9c
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-22+knots		b54d2969e2d
		TODO: Use .requires_wallet instead of manual creation of default wallet?
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-22+knots		569c4bc343f	last=81622ba1229 whitelist_outgoing
		# NOTE: Originally #10594
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-22+knots		1450e955bea
	# Needs careful review: 22702 martinus:2019-08-bulkpoolallocator
	# Needs work: 22708 hebasto:210815-wayland
	# TODO (needs concept review?): 23093 meshcollider:202109_keypoolrefill
# Non-upstreamed functionality:
	n/a   restore_feefilter_opt					bf9a6597726
	TODO: Determine whether #22260 (wallet Bech32m default) is good or should be reverted
	-     gui_payreq_textedit					55bd287346d
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				d995448a23d
	-     walletnotify_w_win-22+knots			edd33a2d427	last=a291491d2fd walletnotify_w_win
	14137 win_taskbar_progress					e9dc3bcac3d	last=18eb4dbb8a
	-     restore_blockmaxsize					9db4529dde0
	7107 qtnetworkport							d73a95d8da0	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							960c792aa3c
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								107ed46704d
	7510  rwconf_gui							7271f785252
	 559 accept_nonstdtxn						4f7dc7b3613
	 929 tbc									3f84a3b048c
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
	 553 bugfix_qt_uri_amount_parser			864d90dc093
	-    mining_priority						aeb54b4fc8f  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					8f11d2dcae3
	5891  qt_console_history_persist			189074c6a1a	last=0cd5fc301d6 qt_console_history_persist
	7219  fullrbf-22+knots						5c5190476b9	last=5d58ebcc60f fullrbf # missing 91786d16ccc + revert34ae6640174
		FIXME: Why isn't service bit 26 present?
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					901c180339a
		TODO: Revert(?) #23731 - but maybe n/a since it's for descriptor wallets which are explicit for all types?
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			5b753d4e201	# Latest code now
	-     gui_request_payment_label-0.19		1bc559e14c5
	-     gui_peers_sort_network-22				6c709ff6846
	-     gui_peers_no_net_column				42faba73091
	22439 guix_in_gitian						6f8b29bd9f8	last=ebda0463748 achow101/guix-in-gitian
		FIXME: Add i686-pc-linux-gnu
# Non-upstreamed Knots compatibility:
	-    preserve_unsupported_keyflags			d61bb3c22e9
	-     netperms_implicit_addr				3ab6318c892
	12674 rpc_onetry_nonpriv-22+knots			527c9a13cae
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-22+k		94e73baadff
		# TODO: Each release, see if we need to bump setting names for GUI states
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				b8136f8bc93
	-     bytespersigopstrict-22+knots			efeaa4d511c
	9749  unique_spk_mempool-22+knots			1e69a9eb689
	-     bloom_default-0.21+knots				bfd460431a0
	-     enforce_checkpoints					9bd94bf5d54
	n/a   checkpoint_update-22					197ba14f3ca	last=531aaa286d3 checkpoint_update-0.21
	10282 timebomb_knots						4c57977383e
	-     rwconf_policy-22+knots				4c9a3ad0147
		# Include Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (cherrypick=eaa9f92b50b)				dc7e4b0d473  # delete release notes fragments
	7483  svg_icon-22+knots						22cb29a7fa3
	n/a   tbc_font								552c253ac34
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/
# BRANDING:
	n/a   knots_branding-22						2778d0743d1
#FIXME: check there's no univalue push_back(bool) - see #20424 and stash 8724e2fae4
#FIXME: Check there are no menu icons
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Check calls to RPCConsole::clear(bool) get expected behaviour
	n/a  (cherrypick=0ed7b3b85d3f618838)		9fa4d038aaa	# doc/{bips,files}
	n/a  (bump_version=Knots:20211213)			bcc3f6e8502
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=c22129a3cec)				b31ddd5021f  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=59fae184489)				06a4bf467f6  # update manpages (build first)
	n/a  (cherrypick=0b0a1a14592)				b2c9337cfd7  # translation update
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

@22.x-knots-android
	#23478
