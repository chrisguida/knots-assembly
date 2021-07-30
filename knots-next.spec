timestamp 2021-07-22 08:01:09
lastapply no-merge

#.. checked up to PR #22525 / gui #384

checkout origin/22.x
@22.x-syslibs
	22534 fanquake/22_x_backports  last=34f9f88bc95  # TEMPORARY HACK
# BUILD BUGS:
	21882 hebasto/210507-fuzz32					d994684b569	last=e4c8bb62e4a hebasto/210507-fuzz32
		# NOTE: Has improvements/fixes
	# Not needed (depends only): 22380 fanquake/set_std_c_version_depends
	22390 fanquake/netbsd_dont_set_locale					last=fdd71448e78
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
	g216  optional_font
	#Maybe restore: 7339  opt_libevent
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
	15103 lightsword/getentropy-weak			d61ba875650	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	18133 bugfix_qvalidlineedit					7933a2d752b
	18194 bugfix_gui_edit_sendaddr-mini			64ebfdfb0a1	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18729 intro_dont_change_user_prune			25f70064ec8
	TODO: MERGED UPSTREAM: 18766 blocksonly_no_feeest-0.21				e46a9d86ca1	last=4e28753f606
		# diff-minimised
		# HELD BACK 33ca3590243...4aaad74c4c8 due to refactor complication
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data-0.21+knots	a0f6d94c0b9	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19888 getblockstats_utxo_actual-0.21+knots	37dd20ac3a1	last=0af88a85e59
		# modified
	# Needs review: 20196 vasild/fix_GetListenPort
	g87   hebasto-g/200910-mono					13002cb08f2	last=2e386cd3dd3
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					e7a792e44b6
	-     bugfix_gui_drop_abc_confusing_hack	c0f258de92f
	TODO: MERGED UPSTREAM W/O FIX??: g164 hebasto-g/201224-signal
		# +gui#375 fix
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				37fc886f39f
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	TODO: MERGED UPSTREAM: 19315 rpc_addconnection-0.21				1e691e1fff6
		# PARTIAL: Only the actual addconnection RPC method
		# NOTE: Modified to allow use on non-regtest networks
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22359 fix_wallet_pr22359-0.21				3244e0d002f	last=fa6fd3dd6a4
		# Semi-diff-minimised
	# Needs review: 22362 marco/2106-addrdb  # Drop (only) invalid entries when reading banlist
	22417 bpchild_closefds									last=3b6153ba336 bpchild_closefds
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
	Needs review: g379 ryanofsky/pr/badset
@22.x-knots
# SOFTFORK:
	21934 rpc_getblockchaininfo_lockedin_statistics	fe4dfbf3f33	last=2b19f3443ef rpc_getblockchaininfo_lockedin_statistics
	22016 rpc_gbci_period_start-0.21.1+knots	4910107f0d1	last=04ce309840f Sjors/2021/05/versionbits_period_start
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	TODO: MERGED UPSTREAM: g275  gui_darkmode-0.21_pt1					8939a4a109b
		# NOTE: Fixed bug in gui#330 a simpler way b942216a1a7
	-     restore_win32-0.21+knots				d37803a84cc	last=3e30ae0514e restore_win32
	-     restore_linux32						efa9ee85ed6
		# NOTE: gitian only
		TODO: guix
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
	14641 fundraw_minconf-0.21					fde6c8132bc	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
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
	15836 fee_histogram							82829beb890	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: removed extraneous Bitcoin-Qt.* files
		# NOTE: Backported some features/test from #21422 (but not API incompatibilities)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 ? See also git diff b1f9af22425..9d16921553b -w
	(CHECK-LAST)	last=36f5e224f5f origin-pull/21422/head
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
	17463 gui_custom_sendyes					998dd492930
	15987 wallet_no_reuse-0.21+knots			7515d038c84
		# TODO: Rewrite based on bugfix_gui_bumpyes (g#148) + non-superconstructor #17463
	-     rpc_gai_txids-0.21+knots				01bfbd88472
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	21245 rpc_getblock_prevouts_fees-0.21		5b3f15dcda3	last=7fc316e2c9f
		# Was originally #16083
		# Held back change of verbosity to class enum, and generally kept #16083 base
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	16795 rpc_inferred_output_descriptors		5de05c6c9f6	last=3038f944a6d instagibbs/decode_descriptor
		# Fixes: 478a4da04e77ca4438929909fafdbb0e57614577
	# Needs review: 16981 LarryRuane:reindex-speedup
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs review: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options? (watch out for send RPC)
		# TODO: Diff-minimise
	18972 neutrino_whitelist-mini				892d210d2eb	last=339fe189eb9
		# NOTE: Diff-minimised
	17034 psbt_ver_proprietary_xpub-0.21		8cfa229a8e4	last=cc2644ffc6e achow101/bip174-extensions
		# NOTE: Held back `gdd 078abaac27e dc93052363d` comment correction
		# NOTE: Diff-minimised
		# NOTE: Now includes 16463 bip174_xpub-0.21+knots				8e6f8d3cc9c	last=9926a387eab achow101/bip174-xpub
	17631 rest_blockfilter-0.21					31a7b2798a2	last=16d8d2da598 matt/2019-11-filter-rest
		# NOTE: Dropped unrelated extra commits
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	g319  -										3cb5fcd37dd	last=5062565e112  # gui_openuri_pastebtn-0.21
		# NOTE: Used to be #17955
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	996d632f395	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	18689 rpc_dumptxoutset_hr					86a235cbd1f	last=65d0697fe34
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	TODO: MERGED UPSTREAM: 19137 wallettool_dump-0.21+knots			71d5c75689e	last=23cac24dd3f achow101/dumpwalletrecords
		# NOTE: Disabled for BDB wallets since it doesn't dump/restore wallet id yet
		# NOTE: Changed to print warnings to stderr instead of stdout
		# NOTE: Diff-minimised
		# If bdb is reenabled, need #20267 49797c3ccfb
	19242 uaappend								0501a4912b2
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
	19463 prune_locks							7688250cdac	last=1ad45edbfeb prune_locks
	# Needs review: 18000 -  # Coin Statistics Index
	TODO: MERGED UPSTREAM: # Needs review: 19521 # Coinstats Index (without UTXO set hash)
		# +22047
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
	TODO: MERGED UPSTREAM: 21277 listdescriptors_normalized-0.21+knots	a45c8b5634a
		# TODO: Drop 0.21.0 compatibility "desc" when return format is updated or 21329 (MERGED UPSTREAM) is ready
	g291  gui_trafficgraph_vert-0.21			088733fcf9a	last=1f373f93a60  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
	20254 i2p_static-0.21						b1aec3e913f	last=8b4a3714b91 vasild/i2p_static
		MERGED UPSTREAM: # + a4693f44cfe from #20685
		MERGED UPSTREAM: # TODO: +21825 ? (needs 21560?)
		MERGED UPSTREAM: #TODO: +21914
		MERGED UPSTREAM: #TODO: +21407+21631
		# TODO??? 21514 vasild:ignore_port_in_i2p
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
	TODO: MERGED UPSTREAM: 20275 list_unsupported_wallets-0.21+knots	4db68baa351	last=f3d870fc227 ryanofsky/pr/exist
		# Mostly rewritten?
	20295 Sjors/2020/11/getblockfrompeer		947c37b0b52	last=d0b537458d9 Sjors/2020/11/getblockfrompeer
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-0.21					ed17a7d8d62	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20407 rpcauthfile-0.21+knots				0726f132d9d	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bug, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						8979d48f938
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20664 rpc_scanblocks-0.21					ad927cbdb4c	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
		# Held back insignificant API changes ab315e5294b...71b7cdb460e
	20702 rpc_getblocklocations-0.21			8db5bda17bd	last=9b03c654eb3
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							1dcbfaca3b6
	g180  gui_peer_relay_detail-0.21+knots		f76dd90768b	last=79a2576af1e jonatack-g/peer-details-connection-type-followups
		TODO: MERGED UPSTREAM: # +g203  Display plain "Inbound" in peer details
		# NOTE: Carries commit from g163 since it messes with the string anyway
		# NOTE: Left off final doxygen commit
	g363  qt_peers_directionarrow-0.21+knots	4c6de52a7fc	last=41c881c8a78 qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
	g162  gui_peers_detail_network-0.21+knots	ce1628bb816
		# NOTE: Left out Peers table column & misc formatting changes
	# Needs review: 21006 -  # rpc: reduce LOCK(cs_min) scope in rest_block: ~5 times as many requests per second
	15129 benthecarman/remove_watch_only_address	423fd4425f4	last=fdbd01b50e0 benthecarman/remove_watch_only_address
	# ---- BEGIN HWI SUPPORT, TODO ----
	21576 ???
	# TODO: 21928 Sjors/2021/05/hww-toggle
		# TODO: Avoid wallet format changes
	# ---- END HWI SUPPORT ----
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise						b79a8d71419
		# Context: 17529 rpc: Faster getblock using PureBlock
	TODO: MERGED UPSTREAM: # TODO: 15946 jonas/2019/05/prune_blockfilter
		#NOTE: When merging, update GUI neutrino stuff to allow pruning+filters!
		#NOTE: Integrate prune locks
	# Needs API finalisation: 21158 -  # lib: Add Taproot support to libconsensus
		#TODO: minimise
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 -										28ec9283de6	last=46bf0b7b5d8  # rpcwallet_tx_in_mempool-0.21
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	21327 -										093927be571	last=648c5c73aef  # p2p_ignore_tx_in_ibd-0.21
	TODO: MERGED UPSTREAM: g205  gui_save_txview_reqview_columns-0.19	6facbfb184d
		# +gui#368
		# NOTE: Diff minimised
		# NOTE: gui#229 not applicable to backport
	g230  gui_backup_formats-0.21+knots			557904a49bb	last=e91a3f39d01 gui_backup_formats
		# NOTE: To avoid conflict with wallettool_dump-0.21+knots, added 5ab50bc98db GUI: Omit DbDump option for backup of BDB wallets
	TODO: MERGED UPSTREAM: # Needs review & wallet format impact eval: 21365 sipa/202102_taproot_sign
		# +22275 (_NOT_ MERGED UPSTREAM) +22342 (MERGED UPSTREAM)
	TODO? 21413 glozow/2021-03-bypass-timelocks
	# Needs Concept ACK: 21500 S3RK:listdescriptors_private
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
	# Needs review: 21528 amitiuttarwar:2021-03-addr-defer2
	TODO: MERGED UPSTREAM: 21595 cli_addrinfo-0.21+knots				409d1d8be73
		# NOTE: Adapted error message for Knots
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rpc_maxmempool-0.21					0bc176fa910	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Too many conflicts: 21832 cli_color_getinfo-0.21							last=14cb2e0fe13
	# Needs reivew: 21841 rebroad/SteadierFeefilter
	# Needs completion: 21851 fanquake/m1_support_depends
		# +22070 (MERGED UPSTREAM)
	# Needs review/optionality: 22009 achow101:cs-waste-2
	# Duplicate (of #14641): 22049 -  # rpc: allow specifying min chain depth for inputs in fund calls
	22072 -										66d83231979	last=602f4da9178  # autoreindex-0.21
	22159 marco/2106-buildPattern				deede4f8965	last=fa14c6818f4 marco/2106-buildPattern
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  hebasto-g/210501-stripes				7d9f56d4c76	last=fdf80937d1c hebasto-g/210501-stripes
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	g318  gui_peers_copyaddr-0.14				172639c9e05	last=65d1d351786 jarolrod-g/copy-addr-peer
		# NOTE: Added keyboard shortcut
		# NOTE: Fixed Qt5.5 compatibility
	# Needs review: g342 hebasto-g/210521-wallet
	# Needs review: jonatack/ProtectEvictionCandidatesByRatio-perf-enhancements
	22288 torcontrol_dnslookup-0.21				d8f8412dcc4	last=cdd51e8ee15
		# Diff-minimised
	# Needs review: 22340 -  # Use legacy relaying to download blocks in blocks-only mode
		# NOTE: Rebased in 0e3b643ba55
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
	# Needs work: 22350 -  # Log rotation
	22372 multinotify
	22383 -  # rpc: Prefer to use txindex if available for GetTransaction
	22407 promag/2021-07-getblockchaininfo-time
	22501 jonatack/netinfo-addr-statistics
	22513 achow101/psbt-no-finalize
		FIXME: options object
	Needs review: 22514 achow101/psbt-sighash-default
	g384  -  # add copy subnet action for banned peer
# Non-progress functionality:
	8751  sort-multisigs-0.21					e06c15ceea1	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152 sweepprivkeys							9d6360908e1
	9245 ionice									52ed64216eb
	-    ionice_win								22b1c9241e8
	8501  old_stats_rpc-0.21					2fa33c1f65c	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-0.21						24601755a13	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-0.21					f9192d9a751	last=07fc81109a
	9849 gui_netwatch-0.21+knots				539fa817d21	last=3c8fe76f6ee gui_netwatch
	10615 multiwallet_rpc-0.21+knots			cc2b14bbbcf	last=5a10f8307a5 multiwallet_rpc
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-0.21+knots					dad75802d23	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					7a1723439c5
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment-0.21+knots	040052148d5	last=a06d916c75a relax_invblk_punishment
	10350 filtered_witblock-0.21				5cb7a4a645a	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				e40fcaeb7fe	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.21							d2f6a3d7d5d	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			3b64c7195f0
	12965 scriptthreads-0.20					8d959f05d3c	last=dfab6c6866 jonas/2018/04/svt
	13203 dsha256_power8-0.20					9703ce00ee9	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		6ceb71baa4c
	15218 postibd_flush							84b38613864	last=d2ecb70d64  # validation: Flush state after initial sync
		# TODO: Rewrite after #17487 is ready/safe to merge
	15428 tor_gui_pairing-0.21+knots			e509f51807e	# latest code now
	15421 tor_subprocess-0.21+knots				3de8ab01bf5	last=58c6cafd3a1 tor_subprocess
	# TODO: tor gitian bundle! /guix
	15633 nohbcbfornonwit-0.21+knots			c48ce12aa19	last=ac897f0bd3a nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# TODO: 16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					ca0940d77b6
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning-0.21+knots		43dad5a3906	last=f016cd420df restore_vbits_warning
	16807 meshcollider/201909_bech32_error_detection	47e52930e8f	last=3bc568d6753 meshcollider/201909_bech32_error_detection
	n/a   rpc_compat_error_index-0.21+knots		c0b669d2000
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	-     gui_bech32_errpos-0.21.1+knots		63858cb48e1  # Latest code
	17636 guisettings-0.21						d4da7377cb0	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo-0.21+knots			95572de08a2	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0-0.19					fbe06449a10	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances-0.21+knots		19e9d705f4c	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-0.21+knots	aedba84cdb0	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock-0.21+k	a03387247fb	last=1e868bbbb1b
	# TODO: 18789 achow101/create-unsigned-sendconfdialog
		#TODO: Resolve conflict with wallet_no_reuse
		#OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	19117 rpc_getrpcwhitelist					4e5e20bd9ec
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.21+knots	bfaf26b19f1
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-0.21+knots	d6b39ef5628	last=81622ba1229 whitelist_outgoing
		#TODO: Split this up?
		# NOTE: d756d0a01a6 needs legacyWhitelisted in minified version!
		# NOTE: Originally #10594
	TODO: MERGED UPSTREAM: g165  gui_peers_splitter_ss-0.21+knots		8ea7e7fbc3f
		# +g194 (MERGED UPSTREAM) Save/restore RPCConsole geometry only for window
		# NOTE: Changed setting name since our splitters don't match Core's
		# TODO: Each release, see if we need to bump setting name (and figure out back compat?)
	# Needs purpose: 21815 prayank23:max-out-full-relay
	# FIXME: text below QR Code doesn't fit bech32 with Console font!
# Non-upstreamed functionality:
	TODO: Revert #21992 (removed -feefilter option, useful for manually prioritised transactions)
	TODO: Determine whether #22260 (wallet Bech32m default) is good or should be reverted
	-     gui_payreq_textedit-0.21				4a9c6fc46e5
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				011b11763f6
	-     walletnotify_w_win-0.21+knots			0fafbd4a598	last=a291491d2fd walletnotify_w_win
	14137 win_taskbar_progress					35568cf34dd	last=18eb4dbb8a
	-     restore_blockmaxsize					7cf11b880fc
	7107 qtnetworkport							dd2ad9343f6	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							1c4e51255a4
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								9eefbf8c5fb
	7510  rwconf_gui							31da64c50bc
	 559 accept_nonstdtxn						854677f3a98
	 929 tbc									b92159120bd
	 553 bugfix_qt_uri_amount_parser			2bef446009c
	-    mining_priority						c1b36c3197d  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					8fa52dc8120
	5891  qt_console_history_persist-0.21+knots	7ed83221a81	last=ea852deea35 qt_console_history_persist
	7219  rbf_opts-0.21+knots					ec4af75863b	last=5df41eadb59 fullrbf # missing 91786d16ccc + revert34ae6640174
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					c84af5db7d7
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			71cc4a727ef	# Latest code now
	-     gui_request_payment_label-0.19		bd9ec2f9431
	-     gui_peers_sort_network-0.21+knots		a3e6f0ec5e2
# Non-upstreamed Knots compatibility:
	-    preserve_unsupported_keyflags			8c461dcdced
	-    mempool_knots014_compat-0.21+knots		4d6b8b17d26	last=1befffc0b48 mempool_dat_extensible
		# NOTE: Load-only
	11413 rpc_feemode_explicit_compat-0.21+knots	ca8dbc1e33d
	-     netperms_implicit_addr				14687738e62
	12674 rpc_onetry_nonpriv-0.21+knots			b235a94b1ba
	# TODO: add a bitcoinknots.conf ?
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				66fa127a85b
	-    bytespersigopstrict-0.21+knots			42fef5047e8
	9749  unique_spk_mempool-0.21+knots			6f7822ceed3
	-     bloom_default-0.21+knots				d714d612b62
	-     enforce_checkpoints					d41dcd18f7c
	n/a   checkpoint_update-0.21				79d59f9403e
	10282 timebomb_knots						c8b2793aff0
	-     rwconf_policy-0.21+knots				bae9992c73c
		# Include Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	NOTE TO SELF: Remove release-notes-prNNNNN.md files BEFORE the svg icon merge so it doesn't get added then removed in different patch files >_<
	7483  svg_icon-0.21+knots					469d40983b1
# BRANDING:
	n/a   knots_branding-0.21					1ee7ca43f35
#FIXME: check there's no univalue push_back(bool) - see #20424 and stash 8724e2fae4
#FIXME: Check there are no menu icons
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
TODO: Check calls to RPCConsole::clear(bool) get expected behaviour
	n/a  (cherrypick=e0968d0328b2877330)		c7a144c218c	# doc/{bips,files}
	n/a  (bump_version=Knots:20210722)			0a9a4537a5d
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=96316586c91)				f1cc3f1e0b1  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		TODO: #21063 API change if merged
	n/a  (cherrypick=33ee7963ad4)				6addc3eccab  # update manpages (build first)
	n/a  (cherrypick=936fd13cd23)				a886811721c  # translation update
# NOTE: use git diff --minimal for patches!

@22.x-knots-android
