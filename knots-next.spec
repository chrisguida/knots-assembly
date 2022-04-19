timestamp 2022-04-13 02:43:18
lastapply no-merge

#.. checked up to PR #24840 / gui #581

checkout origin/23.x
@23.x-syslibs
# BUILD BUGS:
	# Not needed (depends only): 22380 fanquake/set_std_c_version_depends
	# Needs review: 23609 hebasto/211126-reduce
	24051 config_utils_drop_extra_deps
	5872 subdir_incl_compat						a218f649f67
	24295 -													last=faf7a61483a  # Remove std::move from fs wrapper to work around -D_LIBCPP_DEBUG=1 bug
		# 24.xTODO: Can this go away?
	24633 bugfix_suppresswarnings_regex
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb							8cb438ae8ca
	5416  sys_libsecp256k1						6bb55432d3d
	-     sys_univalue-23+knots
	7485  sys_univalue_def-23+knots				1d03ddd0d67
	#24.xTODO: sys_libminisketch
	13789 bugfix_asm_pragmas					2fffe355376
	-     bugfix_asm_leveldb_check				74ba4e0ac1f
	15155 test_external_bcli					0c5868df17b
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	# ---- BEGIN qt6 SUPPORT, TODO ----
	# NOTE: Partial qt6 backport in WIP_qt6-23
	# Diff-minimise? Need to test: g577 -             # Qt 6 (1/n)
	# Only w/ rest of Qt6: g579 hebasto/220409-strut  # Qt 6 (2/n)
	# Needs work? & test: g580 hebasto/220409-event   # Qt 6 (3/n)
	# Needs review: 24813 hebasto/220409-appcheck     # Qt 6 (4/n)
	# Needs work/splitting-up: 24798 hebasto/220406-qt6
	# ---- END qt6 SUPPORT ----
	n/a   (delete_release_notes_fragments)
@23.x-knotsfixes
# TESTS:
	#23.xTODO: as needed only: -     lint_relaxer							f351877c154
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	24205 jonatack/network-reachability-assertion-and-testing	last=58a14795b89
	24687 qa_invalid_i2psam-23+knots
	#23.xTODO# Revert pedantic RPC checks for production ; see #24695
# FIXES:
	18818 guix_reltar_autogen_distclean			e8914fe7cab	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again						48e994efd24
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					55e20380c66	last=df5ece3e064 2020mingwthrd
	18490 bugfix_symcheck_pe_case				be8f2d388ea
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 http_bind_error						2d0253e07a7	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					e22b19f9462
		# NOTE: libevent-copied code up to date as of 2021-07-16 c29f1dbe116c88434e77721ca215b8d2082b247f
	9524 marco/Mf1701-qaPruning					5d299ba2a6b	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					93e8f48f027
	14485 fadvise								9c2d09f9515
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name-23+knots			d40fdba46d8
	-     bugfix_rpc_getbalance_hacky			b783debf686
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
		# NOTE: 19420 requires #24681 ?
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	18194 bugfix_gui_edit_sendaddr-mini			39f0ee79b01	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	18729 intro_dont_change_user_prune			39b2462ba7b
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				03d0ef69ca2	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19888 getblockstats_utxo_actual-23+knots	d0fceeac30a	last=ff1685124df
		# Diff-minimised incl test changes
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	g152  gui_notify_setup_bg					6d5fc327268
	-     bugfix_gui_drop_abc_confusing_hack	0ac70704c08
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				9859a56089a
	-     rpc_addconnection_mainnet				d7d29e53ba2
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22417 bpchild_closefds						95725111d52	last=3b6153ba336 bpchild_closefds
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				162911e79ab
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	g557  gui_numeric_GBs						b6869ae3ee7
	# Needs work/diff-minimisation: 23418 marco/2111-txPoolPrioOverflow
	# Needs work: 23502 achow101/tr-low-fee-est
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	g506  qt_qrcode_sizefixes
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs review: 24066 whitslack/openrc-daemonwait
	#23.xTODO# Needs review: 24090 RandyMcMillan/1642450390-issue-24049
	24145 -													last=9d65ad365c5  # Clear vTxHashes when mapTx is cleared
	24313 Sjors/2022/02/displayaddress						last=803387f054d
		#23.xTODO: make sure this doesn't break compatibility (and fix review bugs)
	22087 validate_port_opts-23+knots						last=1b6f8d3ea08  # Validate port-options
	24371 -													last=a84650ebd5a  # util: Fix ReadBinaryFile reading beyond maxsize
		#23.xTODO# Needs testing
	# Needs work: 24392 hebasto/220219-cmake
	#23.xTODO# Check if there's a real bug: 24523 promag/220222-boost
		# NOTE: Was #24415 (never in Knots)
	24428 fanquake/improve_bitcoin_wallet_return			last=dd532ee9c4d
	#23.xTODO# Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24453 fix_rpcdoc_changeaddr_STR
	#23.xTODO# Needs review: 24454 achow101/fix-input-weight-test
	24462 Empact/2022-03-descriptor-pubkey-context			last=9b526727000
	# Not worth it? 24469 ryanofsky/pr/testu
	24479 bugfix_settings_numberval-23						last=33722279495 bugfix_settings_numberval
	# Needs a real fix instead: 24502 glozow/2022-03-rejectlongchains
	# Needs review: 24538 glozow/2022-03-miner-prioritised
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24579 fix_docs_rpc_gbci_gdi_pr24579-23					last=facd5d92e18  # doc: Fix getblockchaininfo/getdeploymentinfo RPC docs
	24629 bugfix_rpc_prunebc_retval
		#23.xTODO# Check upstream concept-ACK-or-NACK
	24640 fix_rpcdoc_gbci_pruneheight_desc-23				last=06822f86545 fix_rpcdoc_gbci_pruneheight_desc
	#23.xTODO# FIXME: https://github.com/bitcoin-core/gui/issues/567
	24630 reindexCS_resetindexes-23							last=cf531ba531c
	24649 fix_wallet_utxos_not_external-23					last=3b83b8a3b03
	# TODO: Triage along w/ KDE patches: 24668 prusnak/qt5-5.15.3
		# NOTE: WIP list of KDE patches in 202204-KDEQtPatchesForBitcoin
	24716 fix_doc_rpc_rawtx_pr24716-23
	24718 fix_rpc_docs_pr24718-23+knots						last=68a041dd12b
	#23.xTODO# Triage: 24722 -  # build: patch around qt duplicate symbol issue
	#23.xTODO# Needs review & diff-minimising: 24804 -  # Sanity assert GetAncestor() != nullptr where appropriate
	24776 doc_update_rest_chaininfo-23						last=cff4fb37d7b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	Simpler alternative to 24830 -  # init: Allow -proxy="" setting values
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	24837 -  # init: Prevent -noproxy and -proxy=0 from interacting with other settings
	FIXME: Something to address gui#582
	n/a   (delete_release_notes_fragments)
@23.x-knots
# PERFORMANCE:
	23880 marco/2112-p2pAsync								last=fa61dd44f99
	# Needs reivew: 24158 JeremyRubin/epoch-mempool-reorg-updates
	n/a   rm_minisketch
		#24.xTODO# Probably need to drop this
	24558 disable_boost_multi_index_ser-23					last=49441752ea1 fanquake/no_boost_multi_index_serialization
	# Needs review: 24589 -  # sha512.cpp improvements
	# Needs review: 24699 achow101/faster-available-coins
	# Probably a bad idea: 24712 -  # wallet: reduce coin selection iterations
	# Knots doesn't support MSVC builds: 24773 Enable AVX2 implementation of SHA256 for MSVC builds
	# Needs review: 24814 -  # refactor: improve complexity of removing preselected coins
	# Needs review: 24832 -  # index: Verify the block filter hash when reading the filter from disk.
# SOFTFORK:
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	24448 guix_linux_i686_compat				d7cabad678b	last=c76ac9d57f2 guix_linux_i686
		#24.xTODO# Revert #24639
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
	22049 rpc_fundtx_minmaxconf-23+knots					last=7f4c9039f71  # rpc: allow specifying min chain depth for inputs in fund calls
	(CHECK-LAST)	last=9652e0a2faa rpc_fundtx_minmaxconf
		# Was #14641 (moved to Knots compat)
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
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	g119  rm_send2self-mini						12909b036b0	last=2bb4e307634 rm_send2self
		# NOTE: Originally #15115
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						07f2e143d73
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram+pr15836_api				855210e5045	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ?
	(CHECK-LAST)	last=4af229650fe origin-pull/21422/head
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
		# TODO: https://twitter.com/RandyMcMillan/status/1490107008443457538?t=Qc4LO63rRuWxErtRel06EQ&s=19
		# 			aka 4613c88c91f4f3846aa62c929ad73d1a3e6ac70e
	22693 getaddressinfo_txids					a2dd1687f06
	g562  wallet_warn_reuse_gui					3cd9339e389
		# NOTE: Was #15987
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs review: 16981 LarryRuane:reindex-speedup
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				90b945d9f21	last=a3300c6b200 neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	g319  qt_openuri_pastebtn_shortcut-23		ec5bceab101
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	65bdd6b4b43	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	18689 rpc_dumptxoutset_hr					63bd42e0546	last=65d0697fe34
		# Fixed bugs (eg, scoping of ascii_types)
		# NOTE: Rebased onto (but not compatible with) #24202
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202/files#r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								2b7b1f97f42
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	# Needs review: 21726 -  # Improve Indices on pruned nodes via prune blockers
	19463 prune_locks							05583647cd3
	(CHECK-LAST)	last=ce081ba2b1a origin-pull/21726/head  # based on
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	19762 ryanofsky/pr/named					387e706f17f	last=894c414dafb
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							ef44bb829e6
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			6af482d58f7	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
	-     rpc_getblockfrompeer_wo_header		42a76849c19
		# Prior Knots bundled this in with #20295
		See #24806
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-23						237cdcaf3ee	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20407 rpcauthfile							aea95ce8fe7	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid-23					aa633c92306	last=88863cf11c7 intro_assumevalid
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	23549 rpc_scanblocks						7c0065a63e4	last=e1c89184cd3 jamesob/2021-11-scanblocks
		# NOTE: Was #20664
		# NOTE: Includes lots of additional fixes/doc improvements
	(CHECK-LAST)	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
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
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						de6aa3acf24	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 -										98ae86d5a81	last=602f4da9178  # autoreindex-0.21
	22159 marco/2106-buildPattern				6c70dc6bc61	last=fa14c6818f4 marco/2106-buildPattern
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt-22				74d6f3d34c6	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							05053cd7598
	MERGED: 22513 rpcwallet_psbt_no_finalize-22+knots	51cac865a4d	last=a99ed898655 achow101/psbt-no-finalize
		# Modified to use a new options object instead of an additional bool positional param
	# Needs work: g471 -  # Add Wallet Restore in the GUI
	# Needs review: 22558 achow101/taproot-psbt
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	# Needs review: 22729 vasild/torbind
	22751 kallewoof/202108-analyzerawtransaction		364c0507238	last=b269f1bb0d6  # simulaterawtx
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Only if Core merges (alternative makes more sense): 22776 kallewoof:202108-getbalances-tx
	# TODO: 22778 jnewbery:2021-02-tx-relay-init
	# Needs BIP? 22838 achow101:multipath-descs
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs work: g410  benthecarman/uppercase-uri
	# Needs review: 23319 -  # rpc: Return fee and prevout (utxos) to getrawtransaction
		# Rebase of 2c56d72acac in a662191612c w/ failing test :/ (had to replace hard-coded fee assumption too)
	# Needs API review: 23330 JeremyRubin/header-fetch
	23362 importfromcoldcard-22					ba52f717337	last=8076f8d4c2a hebasto/211025-cc
		# Needed fs::Path{To,From}String rebasing
		# Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 greenaddress/dump_fee_estimates		ec0f6c01a85	last=d5b41e6b2ed  # savefeeestimates
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs concept review: 23395 -  # util: Add -shutdownnotify option
	23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs review/walletsafety checks: 23480 sipa/202110_untweakedtr
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs work: 23578 Sjors/2021/11/taproot_signer
	# Needs work: 23611 fanquake/lto_in_depends
	Review: 23624 -  # zmq: add rawmempooltx publisher
	g469  achow101-g/b64-psbt-gui
	g473  rebroad-g/NonLinearTraffic
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	# Needs concept (performance hit?): 23662 theStack:202112-rpc-improve_getreceivedby_performance
	g492  rebroad-g/NetworkGraphTooltip
	g497  qt_fontsel
	-     qt_fontsel_qrcodes
		TODO: Add tor_gui_pairing support
	TODO: qt_fontsel_console
	# Needs work? g505  -  # RPCConsole: add hidePeersDetail() button and functionality
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	# Needs review: 24043 sipa/202201_multi_a
		# +#24490 achow101/fix-wallet-tr-unique-descs
	# Needs review & BIP changes: 24058 kallewoof/202201-bip322
	# Needs review & softer deprecation: 24098 -  # rest: Use query parameters to control resource loading
	# Needs concept + review: 24118 -  # Add 'sweepwallet' RPC
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 kallewoof/202201-deriveaddr-nochecksum
		TODO: Change example/nit
	Review closer: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	24171 sdaftuar/2022-01-download-from-inbound
	# Needs review: 24178 sdaftuar/2022-01-headers-response-requires-minchainwork
	24198 -  # wallet, rpc: add wtxid in WalletTxToJSON
		#23.xTODO# fix RPC help description
	g533  -  # gui: add more detailed address error message
	g543  RandyMcMillan-g/1643853831-peers-tab-add-duration-column
	24408 -  # rpc: add rpc to get mempool txs spending specific prevouts
	# Needs review: 24494 glozow/2022-03-minchange
	# Needs concept ack: g553 w0xlt-5/change_error_background
		# CAUTION: requires theming changes for gui#537
	Needs work? g560 w0xlt-g/3_error_message_addr
	Needs optionality/review: 24539 -  # Add a "tx output spender" index
	Needs review: 24545 -  # BIP324: Enable v2 P2P encrypted transport
	Needs review? 24552 prusnak/guix-attest-override-gpg
	Needs work: 24615/24569/24556 guix on non-x86
	# Needs work: 24584 -  # wallet: avoid mixing different OutputTypes during coin selection
	24611 -  # Add fish completions
	# Needs review: 24824 -  # net: create IP to ASN database from file - makeseeds.py
	# Needs review + make part of sendrawtx: 24836 glozow/client-submitpackage
	TODO? BIP 179 (tho... Lightning)
# Non-progress functionality:
	8751  sort-multisigs-22						6923385f2e0	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					32dd1d34493	last=1898b9be12c Sjors/2021/05/versionbits_period_start
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
		TODO: adapt to #22541 being merged
		FIXME: ./wallet/rpcwallet.h:25:6: warning: redundant redeclaration of ‘bool GetWalletRestrictionFromJSONRPCRequest(const JSONRPCRequest&, std::string&)’ in same scope [-Wredundant-decls]
			./rpc/util.h:370:6: note: previous declaration of ‘bool GetWalletRestrictionFromJSONRPCRequest(const JSONRPCRequest&, std::string&)’
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-22+knots						27d1ffd6d18	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					898fc5bf686
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment				f582f6c385f
		TODO: gcp (& merge as fixups?) d2d3601cf80 QA: Use addconnection rather than addnode onetry
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
	# TODO: tor guix bundle!
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
		TODO: Check correctness of 24072 -  # doc: fix wording of alertnotify to match behaviour
	MERGED: 16807 old_bech32_error_detection			09c2d5f6fd5	last=88cc4810926 meshcollider/201909_bech32_error_detection
		# Held back rewrite 3bc568d6753..974227bb457 for now; when updating, add in #23577
		# Held back comment drop 974227bb457..88cc4810926
	n/a   rpc_compat_error_index-22+knots		733deba4309
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos-22+knots			b0efb7af93b  # Latest code
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
	#23.xTODO: Revert #24065 safely (ie, Ensure external signing on all systems)
		see also #24254, #24524(?)
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs review: g539  RandyMcMillan/1643263956-network-graph-issue-532
# Non-upstreamed functionality:
	n/a   restore_feefilter_opt					bf9a6597726
	TODO: Determine whether #22260 (wallet Bech32m default) is good or should be reverted
	-     gui_payreq_textedit					55bd287346d
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				d995448a23d
	-     walletnotify_w_win-22+knots			edd33a2d427	last=a291491d2fd walletnotify_w_win
	14137 win_taskbar_progress					e9dc3bcac3d	last=18eb4dbb8a
		FIXME: checking whether to build with QWinTaskbarProgress support... checking for Berkeley DB C++ headers... /usr/include/db4.8/
			(no result? on jun)
	-     restore_blockmaxsize					9db4529dde0
	7107 qtnetworkport							d73a95d8da0	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							960c792aa3c
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								107ed46704d
	7510  rwconf_gui							7271f785252
	 559 accept_nonstdtxn						4f7dc7b3613
	 929 tbc									3f84a3b048c
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
		TODO: Check if we're using UCSUR or not
	 553 bugfix_qt_uri_amount_parser			864d90dc093
	-    mining_priority						aeb54b4fc8f  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					8f11d2dcae3
	5891  qt_console_history_persist			189074c6a1a	last=0cd5fc301d6 qt_console_history_persist
	7219  fullrbf-22+knots						5c5190476b9	last=5d58ebcc60f fullrbf # missing 91786d16ccc + revert34ae6640174
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					901c180339a
		TODO: Revert(?) #23731 - but maybe n/a since it's for descriptor wallets which are explicit for all types?
		TODO: Make sure descriptor wallets default to non-segwit addresses (or Taproot??)
		TODO: Make sure change is non-segwit too
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			5b753d4e201	# Latest code now
	-     gui_request_payment_label-0.19		1bc559e14c5
	-     gui_peers_sort_network-22				6c709ff6846
	-     gui_peers_no_net_column				42faba73091
	22439 guix_in_gitian						6f8b29bd9f8	last=ebda0463748 achow101/guix-in-gitian
		FIXME: Add i686-pc-linux-gnu
		FIXME: assign_DISTNAME script is gone now
	TODO: revert #23927  rpc: Pruning nodes can not fetch blocks before syncing past their height
	TODO: revert #24031  build: don't compress macOS DMG
	TODO: revert #24142  Deprecate SubtractFeeFromOutputs
# Non-upstreamed Knots compatibility:
	TODO: revert? #24505  wallet: Add a deprecation warning for newly created legacy wallets
	14641 fundraw_min_conf_deprecated-23+knots				last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			d61bb3c22e9
	-     netperms_implicit_addr				3ab6318c892
	12674 rpc_onetry_nonpriv-22+knots			527c9a13cae
	23.xTODO: Ensure blockhash+nodeid param names are supported by rpc_getblockfrompeer_wo_header (see #24294 / getblockfrompeer_param_names)
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-22+k		94e73baadff
		#23.xTODO# Each release, see if we need to bump setting names for GUI states
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				b8136f8bc93
	-     bytespersigopstrict-22+knots			efeaa4d511c
	9749  unique_spk_mempool-22+knots			1e69a9eb689
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	-     bloom_default-0.21+knots				bfd460431a0
	-     enforce_checkpoints					9bd94bf5d54
	n/a   checkpoint_update-22					197ba14f3ca	last=531aaa286d3 checkpoint_update-0.21
	10282 timebomb_knots						4c57977383e
	-     rwconf_policy-22+knots				4c9a3ad0147
		FIXME: https://github.com/bitcoinknots/bitcoin/issues/48
		# Include Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
	TODO: Check #24776
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		dc7e4b0d473
	7483  svg_icon-22+knots						22cb29a7fa3
		TODO: partial revert #23909 & pull earlier #23778 out of reflog
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
	n/a  (bump_version=Knots:20220213)			bcc3f6e8502
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
		540190c138f for #24198
		git stash show -p 35856571b90472274169ddf84d5b2ef06fdcae6e for #24629
		need notes for #24636 ?
	n/a  (cherrypick=59fae184489)				06a4bf467f6  # update manpages (build first)
	n/a  (cherrypick=0b0a1a14592)				b2c9337cfd7  # translation update
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @23.x-knots-android
