timestamp 2021-06-29 06:26:51
#lastapply no-merge

#.. checked up to PR #22369 / gui #375

merge in xenial patching if Qt5.5 supported still

checkout v0.21.1
@0.21.x-syslibs
# BUILD BUGS:
	21882 fuzz32_llvm_workaround-0.21+knots		d994684b569	last=bd55f62549e hebasto/210507-fuzz32
	20938 configure_latomic_checks-0.14^		ee5e40704b0
	21920 configure_latomic_checks-0.14			4f3c88f543a
# SYSLIBS: (and old build bugs)
	5872 subdir_incl_compat						f2e1e41e817
	2241 sys_leveldb							5e9497a8ed7
	5416 sys_libsecp256k1-0.21					c2e8d067f0b	last=258c28e99b3 sys_libsecp256k1
	7485 sys_univalue_def						663a72e6a12
	13789 bugfix_asm_pragmas					82ab60f2428
	-     bugfix_asm_leveldb_check				741060d31b8
	15155 test_external_bcli					251dcff7eee
	20202 opt_bdb-0.21							1b369a2bfd7
		# +#20458+#20267
		# Omitted default-tests-to-descriptors-when-bdb-not-compiled: a2282b44a4d 373158bc44c
		# Omitted "Don't make any wallets unless wallet is required": 45b4366f8ff 104a3a22564 6e06ca05880
		# Diff-minimised
	-     opt_bdb_extracare-0.21				3d26b04ad0f
	20121 secp256k1_allow_bignum				ed298e34b3d
	20358 -										980c71c1f50	last=330cb33985d  # src/randomenv.cpp: fix build on uclibc
	20594 conf_getauxval-0.21					cfc912ffcdc	last=836a3dc02c7 jonas/2020/12/getauxval
	# 22.0 TODO: g216  optional_font
	#Maybe restore: 7339  opt_libevent
@0.21.x-knots
# TESTS:
	22279 fix_fuzz_baseencdec_pr22279-0.21		3d80a04b144
	22002 fix_fuzz_system_pr22002-0.21			867a7fc53df
	22137 fix_fuzz_system_pr22137-0.21			a7912915185
	-     lint_relaxer							9afa5d8517a
	17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
	21785 fix_intrmttnt_qa_p2p_addr_relay-0.20	6430702d120
# FIXES:
	18818 fix_gitian_src_202004					e7ae473f644
	18902 fix_gitdir_again						48e2ecb874f
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					51d41a3ea10	last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case				b9b3f3bd5c0
	17828 p2p_log_categories					bab13c46b9b	last=04960621582 practicalswift/log-categories
	19832 hebasto/200829-log					1ed3a60bb05	last=1816327e533
	20845 net_logcategory_localdisconnect-0.21	fb5ba0afa13	last=fa55159b9ed marco/2101-netLogDisconnect
	# Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
	14968 laanwj/2018_12_http_bind_error		e75ff7b9323	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					81ed4fe33fa
	9524 marco/Mf1701-qaPruning					ae3444d7950	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					3cee4ceb1b1
	14485 fadvise								e87f5a4c952
		# Was #12491
	14501 fsync_dir								e4a9992dd5e
		# Was #12696
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	13608 -										bdb644e5423	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	-     deprecated_param_names				7a602d396d9
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
	18335 -										10c0773e7fd	last=8dd5946c0b7  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	18466 -										cf0e22b6d2f	last=a5cfb40e27b  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	18729 intro_dont_change_user_prune			25f70064ec8
	18766 blocksonly_no_feeest-0.21				e46a9d86ca1	last=4e28753f606
		# diff-minimised
		# HELD BACK 33ca3590243...4aaad74c4c8 due to refactor complication
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19362 rpc_scantxoutset_reset_progress-0.17	13e1e8980d8	last=8c4129b4540 prusnak/rpc-scantxoutset-reset-progress
m	19419 listwalletdir_skip_data-0.21+knots	a0f6d94c0b9	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: g18   hebasto-g/200701-peer
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19884 fixedseeds-0.21						5ff339ffa5d
		# +partial #21254 (bugfix only)
	19888 getblockstats_utxo_actual-0.21+knots	37dd20ac3a1
	# Needs review: 20196 vasild/fix_GetListenPort
	g87   hebasto-g/200910-mono					13002cb08f2	last=2e386cd3dd3
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: g121 promag-g/2020-10-missing-transaction-notifications
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	20448 unloadwallet_namematch				02b171f7ec5
	# Needs consideration.. why would we re-announce to the same peer?? 20561 sdaftuar:2020-12-moar-addrz
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					e7a792e44b6
	-     bugfix_gui_drop_abc_confusing_hack	c0f258de92f
	20805 copyright_2021-0.21					f9379afcd0c
		# NOTE: Diff-minimised
	# Needs careful review: 20966 banlist.json (TorV3 bans fix)
	# Needs more PRs - for Dark Mode support: g154 -  # qt: Colorize icons on macOS for Dark mode support
	# Too messy? g164 hebasto-g/201224-signal
		# +gui#375 fix
TM	g171  qt_createwallet_layoutmgr-0.21		1ab94ce61ef	last=d4feb6812a2 hebasto-g/210101-wallet
	# Meh? Diff too big? g176 hebasto-g/210103-delegate (fix in #20983)
TM	g177  workaround_qt_macos11_fusion-0.21		9ab4bdc6608	last=4e1154dfd12 hebasto-g/210107-style
	TODO: Revert g177 now that we have dark mode???
	20952 bdb_sanity_check-0.21					85ec10ee85e
TM	g188  bugfix_psbt_binmode-0.21				d46c3cb9d45	last=cc3971c9ff5 achow101-g/bin-mode-psbts
	21028 bips_44-49-84-0.21+knots				915ffbb4cea
	21029 cli_doc_geNnewaddr					b7634d92c59
	# Needs review: g201  jonatack-g/inbound-block-relay
	g202  bugfix_gui_peerdetail_hide-0.18		c27915c33d9
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	21111 openrc_no_rpcpassword-0.12			0c26ecef607	last=95f97111dd2 parazyd/openrc-init-improve
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	21192 bugfix_netinfo_tooverbose-0.21		b068b1f1c54	last=882ce25132e laanwj/2021-02-netinfo-verbosity
	g204  bugfix_gui_rm_old_fixer-0.18			94b0d8bf06d	last=3913d1e8c1f
		# Diff-minimised
	g217  gui_clickable_warning-0.11			0311cc01d15	last=67c59ae4793 jarolrod-g/warning-look-like-button
	# Needs careful review: g219 hebasto-g/210223-toolbar
	g236  gui_init_walleterror_cont				37fc886f39f
	# Complex: 21007 hebasto:210316-fork
		# +21447 TODO
	# Needs #21007, complex: 21418 laanwj/2021-03-systemd-daemonwait
	# TODO: Last commit? Diff-minimised somehow? 21560 laanwj/2021-03-torv3-hardcoded-seeds
	21644 bugfix_addlocal_downloadbind-0.21		2f5bc37b025
	21822 bugfix_cli_pr21822-0.21				791f7e23c3b
	21907 listwalletdir_iterate_inf-0.19		985e103723c
	21944 fix_listwalletdir_rootdir-0.21+knots	32993f653d7
	22013 ignoreblockrelayfordnsskip-0.21		219665bf068
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	19315 rpc_addconnection-0.21				1e691e1fff6
		# PARTIAL: Only the actual addconnection RPC method
		# NOTE: Modified to allow use on non-regtest networks
	22096 fix_p2p_addrfetch_ignoreselfadv-0.21+knots	e4674e393ba
		# Includes part of #21236 (to avoid an extra GetTime on top of the 4 existing)
	# TODO: Determine if any of #22154 (bech32m fixup) is needed
	g243  gui_createwallet_opts_conflict-0.21	4f217b9503c
	g251  fix_bip70_errormsg-0.20				5d45a4f9de0
	g271  fix_gui_rpcconsole_fontsz_prompt-0.21	492bb4b683a
	g276  gui_peers_elide-0.18					ba0720634c9
	g280  gui_urihandler_nophishing-0.20		b7026991708
	g325  gui_peers_rightalign_id-0.21			2d229bb6dd9
	g329  rpcconsole_toolbuttons-0.21+knots		a40ba0d5ba2
	# Needs review: 22261 jnewbery/2021-06-broadcast-fixes
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22308 bugfix_pr22308-0.17					c009ccfeb2f
	22311 bugfix_pr22311-0.21					995e84e1904
	# Needs review: g365  hebasto-g/210614-tx
	18842 fix_wallet_pr18842-0.21				42b45600d37
	22359 fix_wallet_pr22359-0.21				3244e0d002f	last=fa9ef0e8c6f
	# Needs review: 22362 marco/2106-addrdb  # Drop (only) invalid entries when reading banlist
	22417 bpchild_closefds-0.21								last=b611384f901 bpchild_closefds
		TODO: ad6b334232f util/system: Close non-std fds before execing slave processes
# SOFTFORK:
	21934 rpc_getblockchaininfo_lockedin_statistics-0.21.1	fe4dfbf3f33	last=2b19f3443ef rpc_getblockchaininfo_lockedin_statistics
	22016 rpc_gbci_period_start-0.21.1+knots	4910107f0d1	last=04ce309840f Sjors/2021/05/versionbits_period_start
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	g275  gui_darkmode-0.21						8939a4a109b
		# NOTE: Fixed bug in gui#330 a simpler way b942216a1a7
	g366  gui_palettechange-0.21				55b04f94483
	-     restore_win32-0.21+knots				d37803a84cc	last=3e30ae0514e restore_win32
	-     restore_linux32						efa9ee85ed6
		# NOTE: gitian only
	20963 gitian_power64-0.21+knots				d7151c1b629	last=543bf745d38 gitian_power64
		# NOTE: Originally #14066
		# Held back 31dbf0b677d..543bf745d38 - probably only applicable to master
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
	15423 tor_socks_port						67bfe9cad94
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
m	17463 gui_custom_sendyes					998dd492930
	15987 wallet_no_reuse-0.21+knots			7515d038c84
		# TODO: Rewrite based on bugfix_gui_bumpyes (g#148) + non-superconstructor #17463
	-     rpc_gai_txids-0.21+knots				01bfbd88472
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	18772 -										bcfd0b89ee7 last=66d012ad7f9  # rpc: calculate fees in getblock using BlockUndo data
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
	g319  gui_openuri_pastebtn-0.21				3cb5fcd37dd	last=84f23e8ec5b
		# NOTE: Used to be #17955
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	996d632f395	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	18689 rpc_dumptxoutset_hr					86a235cbd1f	last=65d0697fe34
	18722 O_addrman_unordered_map-0.21+knots	a8f034ffd43	last=a92485b2c25
		# NOTE: Restored C++11 compatibility from d6e782174ec
	g125  intro_prune_size-0.21					6d1b1a258f5
		# NOTE: Originally #18728
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19136 achow101/export-descriptor			3e817fee3cb	last=de6b389d5db
	19137 wallettool_dump-0.21+knots			71d5c75689e	last=23cac24dd3f achow101/dumpwalletrecords
		# NOTE: Disabled for BDB wallets since it doesn't dump/restore wallet id yet
		# NOTE: Changed to print warnings to stderr instead of stdout
		# NOTE: Diff-minimised
		# If bdb is reenabled, need #20267 49797c3ccfb
	19242 uaappend								0501a4912b2
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
	19463 prune_locks-0.21						7688250cdac	last=1ad45edbfeb prune_locks
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review: 19521 # Coinstats Index (without UTXO set hash)
		# +22047
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	19762 ryanofsky/pr/named					06d0b03981c	last=894c414dafb
	19776 -										6b92af07758	last=343dc4760fd  # net, rpc: expose high bandwidth mode state via getpeerinfo
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							d629ab65bcc
	# Needs work: 20154 kallewoof/202010-bip322
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	# Needs review (and diff minimisation?): 20197 jonatack:AttemptToEvictConnection-identify-onions-with-m_inbound_onion
	20226 rpc_listdescriptors-0.21				16086f5a271	last=647b81b7093
	21277 listdescriptors_normalized-0.21+knots	a45c8b5634a
		# TODO: Drop 0.21.0 compatibility "desc" when return format is updated or 21329 is ready
	# Needs review + upstream (changes wallet format): 21329 achow101:norm-desc-xpub-cache
	g291  gui_trafficgraph_vert-0.21			088733fcf9a	last=1f373f93a60  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
	21594 rpc_getnodeaddrs_network-0.21			d11f3acf005
		# Diff-minimised / doc changes left out
		# Includes part of #20965 (GetNetworkNames)
	21843 rpc_getnodeaddrs_by_network-0.21		cc3724d3400
	20254 i2p_static-0.21						b1aec3e913f	last=8b4a3714b91 vasild/i2p_static
		# + a4693f44cfe from #20685
		# TODO: +21825 ? (needs 21560?)
		#TODO: +21914
		#TODO: +21407+21631
		# TODO??? 21514 vasild:ignore_port_in_i2p
	# TODO: 20685 vasild/i2p_sam
	22211 i2p_IsRelayable-0.21+knots			03d28fdf8dd	last=7593b06bd12
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
m	20275 list_unsupported_wallets-0.21+knots	4db68baa351	last=f3d870fc227 ryanofsky/pr/exist
		# Mostly rewritten?
	20295 getblockfrompeer-0.21					947c37b0b52	last=d0b537458d9 Sjors/2020/11/getblockfrompeer
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-0.21					ed17a7d8d62	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20403 upgradewallet_pr20403-0.21+knots		69a6f1d0a06	last=3eb6f8b2e61 jonatack/upgradewallet-improvements
	20407 rpcauthfile-0.21+knots				0726f132d9d	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bug, added multi-line support, and added tests
	# Needs review and diff-minimisation: 20421 fanquake/miniupnpc_220
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						8979d48f938
	# Needs a reason to move code chunks: 20599 jnewbery/2020-12-tolerate-early-send-messages
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20664 rpc_scanblocks-0.21					ad927cbdb4c	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
		# Held back insignificant API changes ab315e5294b...71b7cdb460e
	20702 rpc_getblocklocations-0.21			8db5bda17bd	last=9b03c654eb3
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							1dcbfaca3b6
	# Needs review? 20867 darosior:descriptor_multi_wsh
	g163  gui_peer_conntype-0.21				1157253e0af  # jonatack-g/display-peer-conn-types
		# NOTE: Stripped unrelated string changes
	g180  gui_peer_relay_detail-0.21+knots		f76dd90768b	last=79a2576af1e jonatack-g/peer-details-connection-type-followups
		# +g203  Display plain "Inbound" in peer details
		# NOTE: Carries commit from g163 since it messes with the string anyway
		# NOTE: Left off final doxygen commit
m	g179  gui_peers_conntype-0.21+knots			91c9dee9995	last=be4cf4832f1 jonatack-g/add-peers-dir-and-type-columns
		# NOTE: Held back 9f76ba6597c...be4cf4832f1 (no real change once we add gui#363 on top)
	g363  qt_peers_directionarrow-0.21+knots	4c6de52a7fc	last=41c881c8a78 qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
	20916 rpc_testmempoolaccept_wtxid-0.21		c20cc1b1caa	last=fa0aa87071e marco/2101-wtxidTestmempool
		# Diff-minimised
m	g162  gui_peers_detail_network-0.21+knots	ce1628bb816
		# NOTE: Left out Peers table column & misc formatting changes
	20944 rpc_getmempoolinfo_total_fee-0.21		b864ecaf5ae	last=fa362064e38 marco/2101-rpcMempoolTotalFee
		# NOTE: Minor code rearranging to avoid conflicts
	# Needs review: 21006 -  # rpc: reduce LOCK(cs_min) scope in rest_block: ~5 times as many requests per second
	g186  gui_bumpfee_privacywarn-0.21+knots	9ca3cf1b24b
	15129 rpc_removeaddress-0.21				423fd4425f4	last=fdbd01b50e0 benthecarman/remove_watch_only_address
	# TODO: 18077 hebasto/20200130-natpmp
		# FIXME: Needs #21320
		# NOTE: Diff-minimised rebase of 2d5d98ce0aa is at c6ff5633b56
		# TODO: Switch to rwconf?
	# ---- BEGIN HWI SUPPORT, TODO ----
	# TODO: 16546 Sjors/2019/08/hww-box2
		# NOTE: Bumps boost version!
		# TODO: add #21292 + #21339
		# NOTE: Likely needed for HW wallet support: #21127
		#+#21417+#21467+#21576+#21666
		#+#21935?
		#+#22173?
		#+#22348 ?
	# TODO: 21928 Sjors/2021/05/hww-toggle
		# TODO: Avoid wallet format changes
	# TODO: g4    Sjors-g/2019/08/hww-qt
		# NOTE: was #16549
	# 22334 ?
	# ---- END HWI SUPPORT ----
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise						b79a8d71419
		# Context: 17529 rpc: Faster getblock using PureBlock
	# TODO: 15946 jonas/2019/05/prune_blockfilter
		#NOTE: When merging, update GUI neutrino stuff to allow pruning+filters!
		#NOTE: Integrate prune locks
	19763 p2p_no_relay_to_origin-0.21+knots		083e7e509a0
	20365 wallettool_create_descriptors-0.21+k	49afa106a33
	21056 rpcwaittimeout-0.21					937b82478b1
		# +#22327
	21141 walletnotify_blockhash-0.21			7ea94a73ffe
	# Needs API finalisation: 21158 -  # lib: Add Taproot support to libconsensus
		#TODO: minimise
	21173 optimise_hexstr-0.21					b4ac741d755
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 rpcwallet_tx_in_mempool-0.21			28ec9283de6	last=46bf0b7b5d8
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	g213  gui_payrequest_copyaddr-0.18			d165eeec1fc
	g214  gui_payrequest_disablena-0.18+knots	4853dd20a7e
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	21327 p2p_ignore_tx_in_ibd-0.21				093927be571	last=648c5c73aef
	21359 rpc_fundraw_includeunsafe-0.21+knots	52b632873e7
	g205  gui_save_txview_reqview_columns-0.19	6facbfb184d
		# +gui#368
		# NOTE: Diff minimised
		# NOTE: gui#229 not applicable to backport
	g206  gui_peers_relayinfo-0.21+knots		60e29d15120
	g226  gui_peers_lastblocktx-0.21+knots		1c333eb7c65
	g230  gui_backup_formats-0.21+knots			557904a49bb	last=e91a3f39d01 gui_backup_formats
		# NOTE: To avoid conflict with wallettool_dump-0.21+knots, added 5ab50bc98db GUI: Omit DbDump option for backup of BDB wallets
	# Needs review & wallet format impact eval: 21365 sipa/202102_taproot_sign
		# +22275+22342
	# Needs review (+ minimisation?): 20833 -  # rpc/validation: enable packages through testmempoolaccept
		# +22084
	# Depends on #20833: 21413 glozow/2021-03-bypass-timelocks
	# Needs Concept ACK: 21500 S3RK:listdescriptors_private
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
	# Needs review: 21528 amitiuttarwar:2021-03-addr-defer2
	21595 cli_addrinfo-0.21+knots				409d1d8be73
		# NOTE: Adapted error message for Knots
	21602 rpc_listbanned_deltas-0.21			7774e201444
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rpc_maxmempool-0.21					0bc176fa910	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Too many conflicts: 21832 cli_color_getinfo-0.21							last=14cb2e0fe13
	# Needs reivew: 21841 rebroad/SteadierFeefilter
	# Needs completion: 21851 fanquake/m1_support_depends
		# +22070
	# Needs review/optionality: 22009 achow101:cs-waste-2
	# Duplicate (of #14641): 22049 -  # rpc: allow specifying min chain depth for inputs in fund calls
	22072 autoreindex-0.21						66d83231979	last=602f4da9178
	22147 p2p_protect_last_outHB-0.21			8f7863d9729
	# AFTER CORE RELEASES: (PR unknown) taproot descriptors +22156? +22166?
	22159 conf_append_cxxflags-0.10				deede4f8965	last=faac8383364 marco/2106-buildPattern
	# TODO, Ugly Hack w/ conflicts: g256  hebasto-g/210323-peers
	# Not useful: g358  jarolrod-g/themedlabel-forms
	# Preferred simpler fix in gui#275: g330  jarolrod-g/prompt-icon-colorized
	g281  gui_console_fontsize_shortcuts-0.21+k	9b125b71d81
		# NOTE: Diff-minimised and moved AddButtonShortcut to avoid conflict with #553 later
	g293  gui_peers_services_wordwrap-0.18		d8b9433aeef
	g298  gui_peers_altrowcolor-0.21+knots_pt1	840c66b724f
	g307  gui_peers_altrowcolor-0.21+knots		7d9f56d4c76	last=fdf80937d1c hebasto-g/210501-stripes
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	g309  gui_neticon_peerstab-0.18				f3e47ff2e91
		# Diff-minimised
	g318  gui_peers_copyaddr-0.14				172639c9e05	last=65d1d351786 jarolrod-g/copy-addr-peer
		# NOTE: Added keyboard shortcut
	# Needs review: g342 hebasto-g/210521-wallet
	g343  gui_instaprogress-0.19				c62ac024c54
	g362  kbshortcuts_context-0.21+knots		60fbd5be8e7	last=e4c916a0ea0 kbshortcuts_context
	# TODO? 22253 glozow/2021-06-same-txid-diff-wtxid
	# Needs review: jonatack/ProtectEvictionCandidatesByRatio-perf-enhancements
	22288 torcontrol_dnslookup-0.21				d8f8412dcc4	last=cdd51e8ee15
		# Diff-minimised
	# Needs review: 22340 -  # Use legacy relaying to download blocks in blocks-only mode
		# NOTE: Rebased in 0e3b643ba55
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
	# Needs work: 22350 -  # Log rotation
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
m	10593 relax_invblk_punishment-0.21+knots	040052148d5	last=a06d916c75a relax_invblk_punishment
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
		FIXME: 42228f7aab1 Bugfix: GUI: Pairing: Don't try to add layout to the wrong parent even temporarily
		FIXME: 380bed9e0d0 Bugfix: GUI: Pairing: Only attach to non-null client model signals
		FIXME: QR code kinda messed up
	15421 tor_subprocess-0.21+knots				3de8ab01bf5	last=58c6cafd3a1 tor_subprocess
		FIXME: if tor survives bitcoin-qt exiting, it keeps the listening port bound??
			Fixing this is problematic. It needs a newer boost version that doesn't exist yet (see https://github.com/boostorg/process/issues/200)
	# TODO: tor gitian bundle!
	15633 nohbcbfornonwit-0.21+knots			c48ce12aa19	last=ac897f0bd3a nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# TODO: 16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					ca0940d77b6
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
m	15861 restore_vbits_warning-0.21+knots		43dad5a3906	last=f016cd420df restore_vbits_warning
	20832 rpc_validateaddress_error-0.21.1		46b02eee06b
	16807 bech32_error_detection-0.21.1+knots	47e52930e8f	last=3bc568d6753 meshcollider/201909_bech32_error_detection
	n/a   rpc_compat_error_index-0.21+knots		c0b669d2000
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	-     gui_bech32_errpos-0.21.1+knots		63858cb48e1  # Latest code
NM	16807 bech32_error_detection-0.21+knots		80ccc5ad7c5	last=54e107add41 meshcollider/201909_bech32_error_detection
NM	-     gui_bech32_errpos-0.21+knots			c0b3d61d95e
	17636 guisettings-0.21						d4da7377cb0	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
m	17958 rpc_getgeneralinfo-0.21+knots			95572de08a2	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0-0.19					fbe06449a10	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
m	19089 cli_getinfo_mwbalances-0.21+knots		19e9d705f4c	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
m	19092 cli_getinfo_mw_total_balance-0.21+knots	aedba84cdb0	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
m	18570 wallet_rpc_lastprocessedblock-0.21+k	a03387247fb	last=1e868bbbb1b
	# TODO: 18789 achow101/create-unsigned-sendconfdialog
		#TODO: Resolve conflict with wallet_no_reuse
		#OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	19117 rpc_getrpcwhitelist					4e5e20bd9ec
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.21+knots	bfaf26b19f1
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-0.21+knots	d6b39ef5628	last=f794108f9e9 whitelist_outgoing
		#TODO: Split this up?
		# NOTE: d756d0a01a6 needs legacyWhitelisted in minified version!
		# NOTE: Originally #10594
	# TODO: 20764 jonatack/netinfo-updates-dec-2020
		# FIXME: Check if all applicable to 0.21
	g165  gui_peers_splitter_ss-0.21+knots		8ea7e7fbc3f
		# +g194 Save/restore RPCConsole geometry only for window
		# NOTE: Changed setting name since our splitters don't match Core's
		# TODO: Each release, see if we need to bump setting name (and figure out back compat?)
	# Needs purpose: 21815 prayank23:max-out-full-relay
	# FIXME: text below QR Code doesn't fit bech32 with Console font!
# Non-upstreamed functionality:
	# 22.0 TODO: Revert #21992 (removed -feefilter option, useful for manually prioritised transactions)
	# 22.0 TODO: Determine whether #22260 (wallet Bech32m default) is good or should be reverted
	-     gui_payreq_textedit-0.21				4a9c6fc46e5
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				011b11763f6
m	-     walletnotify_w_win-0.21+knots			0fafbd4a598	last=a291491d2fd walletnotify_w_win
	14137 win_taskbar_progress					35568cf34dd	last=18eb4dbb8a
	-     restore_blockmaxsize					7cf11b880fc
	7107 qtnetworkport							dd2ad9343f6	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							1c4e51255a4
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								9eefbf8c5fb
m	7510  rwconf_gui							31da64c50bc
	 559 accept_nonstdtxn						854677f3a98
	g153 const_max_digits						2db6298f46c
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
NM	9422  mempool_dat_extensible_mod-0.21+knots	7ed6f1a62c7
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
m	-     rwconf_policy-0.21+knots				bae9992c73c
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
# 22.0 TODO: Check calls to RPCConsole::clear(bool) get expected behaviour
	n/a  (cherrypick=e0968d0328b2877330)		c7a144c218c	# doc/{bips,files}
	n/a  (bump_version=Knots:20210629)			0a9a4537a5d
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
		# 22.0 TODO: #21063 API change if merged
	n/a  (cherrypick=33ee7963ad4)				6addc3eccab  # update manpages (build first)
	n/a  (cherrypick=936fd13cd23)				a886811721c  # translation update
# NOTE: use git diff --minimal for patches!

@0.21.x-knots-android
