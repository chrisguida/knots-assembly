timestamp 2021-06-12 09:06:11
#lastapply no-merge

#.. checked up to PR #22230 / gui #363

checkout v0.21.1
@0.21.x-syslibs
# BUILD BUGS:
	21882 fuzz32_llvm_workaround-0.21+knots					last=bd55f62549e hebasto/210507-fuzz32
	20938 configure_latomic_checks-0.14^
	21920 configure_latomic_checks-0.14
# SYSLIBS: (and old build bugs)
	5872 subdir_incl_compat						1cbdb2ff17a
	2241 sys_leveldb							9cb10b093fb
	5416 sys_libsecp256k1-0.21					0c3cda80472	last=258c28e99b3 sys_libsecp256k1
	7485 sys_univalue_def						7e29fdf0d03
	13789 bugfix_asm_pragmas					a5fc4e7be85
	-     bugfix_asm_leveldb_check				b37c1f867cd
	15155 test_external_bcli					b1ca07dc0f0
	20202 opt_bdb-0.21
		# +#20458+#20267
		# Omitted default-tests-to-descriptors-when-bdb-not-compiled: a2282b44a4d 373158bc44c
		# Omitted "Don't make any wallets unless wallet is required": 45b4366f8ff 104a3a22564 6e06ca05880
		# Diff-minimised
	-     opt_bdb_extracare-0.21
	20121 secp256k1_allow_bignum				6137b192b01
	20358 -										20c750b874c	last=330cb33985d  # src/randomenv.cpp: fix build on uclibc
	20594 conf_getauxval-0.21					0489bf7a484	last=836a3dc02c7 jonas/2020/12/getauxval
	# 22.0 TODO: g216  optional_font
	#Maybe restore: 7339  opt_libevent
@0.21.x-knots
# TESTS:
	-     lint_relaxer							6b3ec23b7ed
	17402 travis_ppc64							12dfd387f7c	last=1d684f05341 elichai/2019-11-powerpc64
	21785 fix_intrmttnt_qa_p2p_addr_relay-0.20
# FIXES:
	18818 fix_gitian_src_202004					6fc637d9972
	18902 fix_gitdir_again						f7355def795
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					6d99a88337e	last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case				ada6068f813
	17828 p2p_log_categories					f8284c15abb	last=04960621582 practicalswift/log-categories
	19832 hebasto/200829-log					9edcf4da007	last=1816327e533
	20845 net_logcategory_localdisconnect-0.21	52a728a1cba	last=fa55159b9ed marco/2101-netLogDisconnect
	# Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
	14968 laanwj/2018_12_http_bind_error		935169d3c0d	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					8005696f9f3
	9524 marco/Mf1701-qaPruning					63652de0988	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					57045135e86
	14485 fadvise								70f7188dcaf
		# Was #12491
	14501 fsync_dir								a68c3372204
		# Was #12696
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	13608 -										22b031869b0	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	-     deprecated_param_names				1d990681394
	-     bugfix_rpc_getbalance_hacky			d191e08bada
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			ec86b20d014	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	18133 bugfix_qvalidlineedit					99cf2ccfb58
	18194 bugfix_gui_edit_sendaddr-mini			9ee5d6ad7ff	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18335 -										038acf93243	last=8dd5946c0b7  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	18466 -													last=a5cfb40e27b  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	18729 intro_dont_change_user_prune			c80f7d5e9a5
	18766 blocksonly_no_feeest-0.21				4249edfa001	last=4e28753f606
		# diff-minimised
		# HELD BACK 33ca3590243...4aaad74c4c8 due to refactor complication
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19362 rpc_scantxoutset_reset_progress-0.17	57179188510	last=8c4129b4540 prusnak/rpc-scantxoutset-reset-progress
m	19419 listwalletdir_skip_data-0.21+knots	eaa839d579c	last=3f9cc0cd736 Saibato/wallet_351
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
	19884 fixedseeds-0.21
		# +partial #21254 (bugfix only)
	19888 getblockstats_utxo_actual-0.21+knots
	# Needs review: 20196 vasild/fix_GetListenPort
	g87   hebasto-g/200910-mono					cecabfc6440	last=2e386cd3dd3
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: g121 promag-g/2020-10-missing-transaction-notifications
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	20448 unloadwallet_namematch				23c02df92c0
	# Needs consideration.. why would we re-announce to the same peer?? 20561 sdaftuar:2020-12-moar-addrz
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					f5193e74b49
	-     bugfix_gui_drop_abc_confusing_hack	a22512d2d9d
	20805 copyright_2021-0.21					11239d013ad
		# NOTE: Diff-minimised
	# Needs careful review: 20966 banlist.json (TorV3 bans fix)
	# Needs more PRs - for Dark Mode support: g154 -  # qt: Colorize icons on macOS for Dark mode support
	# Too messy? g164 hebasto-g/201224-signal
TM	g171  qt_createwallet_layoutmgr-0.21		b3652905431	last=d4feb6812a2 hebasto-g/210101-wallet
	# Meh? Diff too big? g176 hebasto-g/210103-delegate (fix in #20983)
TM	g177  workaround_qt_macos11_fusion-0.21		1d7792c06df	last=4e1154dfd12 hebasto-g/210107-style
	20952 bdb_sanity_check-0.21					ee58bbed140
TM	g188  bugfix_psbt_binmode-0.21				4024211b958	last=cc3971c9ff5 achow101-g/bin-mode-psbts
	21028 bips_44-49-84-0.21+knots				84554a991f3
	21029 cli_doc_geNnewaddr					733dcdcccfb
	# Needs review: g201  jonatack-g/inbound-block-relay
	g202  bugfix_gui_peerdetail_hide-0.18
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	21111 openrc_no_rpcpassword-0.12						last=95f97111dd2 parazyd/openrc-init-improve
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	21192 bugfix_netinfo_tooverbose-0.21					last=882ce25132e laanwj/2021-02-netinfo-verbosity
	g204  bugfix_gui_rm_old_fixer-0.18						last=3913d1e8c1f
		# Diff-minimised
	g217  gui_clickable_warning-0.11						last=67c59ae4793 jarolrod-g/warning-look-like-button
	# Needs careful review: g219 hebasto-g/210223-toolbar
	g236  gui_init_walleterror_cont
	# Complex: 21007 hebasto:210316-fork
		# +21447 TODO
	# Needs #21007, complex: 21418 laanwj/2021-03-systemd-daemonwait
	# TODO: Last commit? Diff-minimised somehow? 21560 laanwj/2021-03-torv3-hardcoded-seeds
	21644 bugfix_addlocal_downloadbind-0.21
	21907 listwalletdir_iterate_inf-0.19
	21944 fix_listwalletdir_rootdir-0.21+knots
	22013 ignoreblockrelayfordnsskip-0.21
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	19315 rpc_addconnection-0.21
		# PARTIAL: Only the actual addconnection RPC method
	22096 fix_p2p_addrfetch_ignoreselfadv-0.21+knots
		# Includes part of #21236 (to avoid an extra GetTime on top of the 4 existing)
	# TODO: Determine if any of #22154 (bech32m fixup) is needed
	g243  gui_createwallet_opts_conflict-0.21
	g251  fix_bip70_errormsg-0.20
	g271  fix_gui_rpcconsole_fontsz_prompt-0.21
	g276  gui_peers_elide-0.18
	g280  gui_urihandler_nophishing-0.20
	g325  gui_peers_rightalign_id-0.21
	g329  rpcconsole_toolbuttons-0.21+knots
# SOFTFORK:
	21934 rpc_getblockchaininfo_lockedin_statistics-0.21.1	last=2b19f3443ef rpc_getblockchaininfo_lockedin_statistics
	22016 rpc_gbci_period_start-0.21.1+knots				last=04ce309840f Sjors/2021/05/versionbits_period_start
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	g275  gui_darkmode-0.21
	-     restore_win32-0.21+knots				ead2c865bd9	last=3e30ae0514e restore_win32
	-     restore_linux32						7a156d40653
		# NOTE: gitian only
	20963 gitian_power64-0.21+knots				d664727f04e	last=543bf745d38 gitian_power64
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
	14641 fundraw_minconf-0.21					ca8582814f4	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	12677 listunspent_ancestorinfo				5756632159d
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					9cb53f8df4d	last=47b2ba29df2 !kallewoof/sign-show-fees
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
	g119  rm_send2self-mini						2fac1e80cc9	last=77a74aac443 rm_send2self
		# NOTE: Originally #15115
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						4cc96b0edc2
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram							d5711407461	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: removed extraneous Bitcoin-Qt.* files
		# NOTE: Backported some features/test from #21422 (but not API incompatibilities)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 ? See also git diff b1f9af22425..9d16921553b -w
	(CHECK-LAST)	last=36f5e224f5f origin-pull/21422/head
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
m	17463 gui_custom_sendyes					f97f61983f6
	15987 wallet_no_reuse-0.21+knots			d2a92674d94
		# TODO: Rewrite based on bugfix_gui_bumpyes (g#148) + non-superconstructor #17463
	-     rpc_gai_txids-0.21+knots				0b19fadfdaa
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	18772 -										6b8d1024b6c last=66d012ad7f9  # rpc: calculate fees in getblock using BlockUndo data
	21245 rpc_getblock_prevouts_fees-0.21		194833f5285	last=7fc316e2c9f
		# Was originally #16083
		# Held back change of verbosity to class enum, and generally kept #16083 base
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	16795 rpc_inferred_output_descriptors		7ff89fc575a	last=3038f944a6d instagibbs/decode_descriptor
		# Fixes: 478a4da04e77ca4438929909fafdbb0e57614577
	# Needs review: 16981 LarryRuane:reindex-speedup
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs review: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options? (watch out for send RPC)
		# TODO: Diff-minimise
	18972 neutrino_whitelist-mini				738e702e9a1	last=339fe189eb9
		# NOTE: Diff-minimised
	17034 psbt_ver_proprietary_xpub-0.21		bae5cc5fc29	last=cc2644ffc6e achow101/bip174-extensions
		# NOTE: Held back `gdd 078abaac27e dc93052363d` comment correction
		# NOTE: Diff-minimised
		# NOTE: Now includes 16463 bip174_xpub-0.21+knots				8e6f8d3cc9c	last=9926a387eab achow101/bip174-xpub
	17631 rest_blockfilter-0.21					f1d75e5e5ed	last=16d8d2da598 matt/2019-11-filter-rest
		# NOTE: Dropped unrelated extra commits
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	g319  gui_openuri_pastebtn-0.21				f645ed82537	last=84f23e8ec5b
		# NOTE: Used to be #17955
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	95cd39cbb6e	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	18689 rpc_dumptxoutset_hr					c056cd7b249	last=65d0697fe34
	18722 O_addrman_unordered_map-0.21+knots	402247de36d	last=a92485b2c25
		# NOTE: Restored C++11 compatibility from d6e782174ec
	g125  intro_prune_size-0.21					f1f840d7e24
		# NOTE: Originally #18728
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19136 achow101/export-descriptor			c920850bd18	last=de6b389d5db
	19137 wallettool_dump-0.21+knots			c2cf1b59bd9	last=23cac24dd3f achow101/dumpwalletrecords
		# NOTE: Disabled for BDB wallets since it doesn't dump/restore wallet id yet
		# NOTE: Changed to print warnings to stderr instead of stdout
		# NOTE: Diff-minimised
		# If bdb is reenabled, need #20267 49797c3ccfb
	19242 uaappend								a2676744f50
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
	19463 prune_locks							00eb76ff486
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review: 19521 # Coinstats Index (without UTXO set hash)
		# +22047
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	19762 ryanofsky/pr/named					8e03dc582e5	last=894c414dafb
	19776 -										c0f75c5e52a	last=343dc4760fd  # net, rpc: expose high bandwidth mode state via getpeerinfo
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							433e6af60db
	# Needs work: 20154 kallewoof/202010-bip322
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	# Needs review (and diff minimisation?): 20197 jonatack:AttemptToEvictConnection-identify-onions-with-m_inbound_onion
	20226 rpc_listdescriptors-0.21				35574ef5955	last=647b81b7093
	21277 listdescriptors_normalized-0.21+knots
		# TODO: Drop 0.21.0 compatibility "desc" when return format is updated or 21329 is ready
	# Needs review + upstream (changes wallet format): 21329 achow101:norm-desc-xpub-cache
	g90   gui_trafficgraph_vert-0.21			823073c11b8	last=8b79225642a  # Enlarge Network Traffic Graph
		# Removed dialog size change
	21594 rpc_getnodeaddrs_network-0.21
		# Diff-minimised / doc changes left out
		# Includes part of #20965 (GetNetworkNames)
	21843 rpc_getnodeaddrs_by_network-0.21
	20254 i2p_static-0.21						5e7a2e67827	last=8b4a3714b91 vasild/i2p_static
		# + a4693f44cfe from #20685
		# TODO: +21825 ? (needs 21560?)
		#TODO: +21914
		#TODO: +21407+21631
		# TODO??? 21514 vasild:ignore_port_in_i2p
	# TODO: 20685 vasild/i2p_sam
	22211 i2p_IsRelayable-0.21+knots						last=7593b06bd12
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
m	20275 list_unsupported_wallets-0.21+knots	48a3b95a506	last=f3d870fc227 ryanofsky/pr/exist
		# Mostly rewritten?
	20295 getblockfrompeer-0.21					36a451cb339	last=d0b537458d9 Sjors/2020/11/getblockfrompeer
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-0.21					9c613464efe	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20403 upgradewallet_pr20403-0.21+knots		b6cabe60262	last=3eb6f8b2e61 jonatack/upgradewallet-improvements
	20407 rpcauthfile-0.21+knots				e44b9f53561	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bug, added multi-line support, and added tests
	# Needs review and diff-minimisation: 20421 fanquake/miniupnpc_220
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						ce7b5633bf5
	# Needs a reason to move code chunks: 20599 jnewbery/2020-12-tolerate-early-send-messages
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20664 rpc_scanblocks-0.21					6f48a710889	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
		# Held back insignificant API changes ab315e5294b...71b7cdb460e
	20702 rpc_getblocklocations-0.21			2b8c96aa433	last=9b03c654eb3
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							cc7902a09d0
	# Needs review? 20867 darosior:descriptor_multi_wsh
	g163  gui_peer_conntype-0.21				fcc7d7afd82  # jonatack-g/display-peer-conn-types
		# NOTE: Stripped unrelated string changes
	g180  gui_peer_relay_detail-0.21+knots		79575c9d88a	last=79a2576af1e jonatack-g/peer-details-connection-type-followups
		# +g203  Display plain "Inbound" in peer details
		# NOTE: Carries commit from g163 since it messes with the string anyway
		# NOTE: Left off final doxygen commit
	g179  gui_peers_conntype-0.21+knots			db1d8415614	last=be4cf4832f1 jonatack-g/add-peers-dir-and-type-columns
		# NOTE: Held back 9f76ba6597c...be4cf4832f1 (no real change once we add gui#363 on top)
	g363  qt_peers_directionarrow-0.21+knots	fa00cf3cbca	last=14b35df0293 qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		TODO: * ee3fa45933c GUI: Make Peers table aware of runtime palette change
	20916 rpc_testmempoolaccept_wtxid-0.21		a78ab94ec0f	last=fa0aa87071e marco/2101-wtxidTestmempool
		# Diff-minimised
	g162  gui_peers_detail_network-0.21+knots	2e85fc5aa76
		# NOTE: Left out Peers table column & misc formatting changes
	20944 rpc_getmempoolinfo_total_fee-0.21		4ca6b64935f	last=fa362064e38 marco/2101-rpcMempoolTotalFee
		# NOTE: Minor code rearranging to avoid conflicts
	# Needs review: 21006 -  # rpc: reduce LOCK(cs_min) scope in rest_block: ~5 times as many requests per second
	g186  gui_bumpfee_privacywarn-0.21+knots	7a0256e272a
	15129 benthecarman/remove_watch_only_address
	18077 hebasto/20200130-natpmp
		FIXME: Needs #21320
		# NOTE: Diff-minimised rebase of 2d5d98ce0aa is at c6ff5633b56
		TODO: Switch to rwconf?
	16546 Sjors/2019/08/hww-box2
		NOTE: Bumps boost version!
		TODO: add #21292 + #21339
		NOTE: Likely needed for HW wallet support: #21127
		+#21417+#21467+#21576+#21666
		+#21935?
		+#22173?
	21928 Sjors/2021/05/hww-toggle
		TODO: Avoid wallet format changes
	g4    Sjors-g/2019/08/hww-qt
		# NOTE: was #16549
	17355 -  # gui: grey out used address in address book
		TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	21283 achow101/psbt2
		TODO: diff-minimise??
	21319 getblock_optimise
		# Context: 17529 rpc: Faster getblock using PureBlock
	15946 jonas/2019/05/prune_blockfilter
		NOTE: When merging, update GUI neutrino stuff to allow pruning+filters!
		NOTE: Integrate prune locks
	19763 vasild/only_relay_to_unaware
	20365 -  # wallettool: add parameter to create descriptors wallet
	21056 cdecker/rpcwait-timeout
	21141 -  # wallet: Add new format string placeholders for walletnotify
	21158 -  # lib: Add Taproot support to libconsensus
		TODO: minimise
	21173 -  # util: faster HexStr => 13% faster blockToJSON
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 -  # wallet: indicate whether a transaction is in the mempool
		TODO: Check if my review comments have been addressed
	21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		TODO: Check if my review comments have been addressed
	g213  jarolrod-g/add-copyaddress-requestedpayments
	g214  jarolrod-g/disable-contextactions-novalue
	g236  gui_init_walleterror_cont
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	21327 -  # net_processing: ignore transactions while in IBD
	21359 -  # rpc: include_unsafe option for fundrawtransaction
		TODO: Make API changes inside CCoinControl instead
	g205  hebasto-g/210131-header
		TODO: +gui#229
	g206  jonatack-g/add-fields-to-peer-details
	g226  jonatack-g/add-last-block-and-last-transaction-to-peer-details
	g230  gui_backup_formats
	# Needs review & wallet format impact eval: 21365 sipa/202102_taproot_sign
	Depends on another PR? 21413 glozow/2021-03-bypass-timelocks
	21426 jonatack/rm-scantxoutset-warning
	Needs Concept ACK: 21500 S3RK:listdescriptors_private
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
	# Needs review: 21528 amitiuttarwar:2021-03-addr-defer2
	21595 jonatack/addressinfo
	21602 jarolrod/ban-time-info
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rebroad/MaxMempoolRPC
		# TODO: Apply limit immediately (look at rwconf_gui and LimitMempoolSize)
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	21832 -  # cli: Improve -getinfo return format
	# Needs reivew: 21841 rebroad/SteadierFeefilter
	# Needs completion: 21851 fanquake/m1_support_depends
		# +22070
	# Needs review/optionality: 22009 achow101:cs-waste-2
	Review: 22049 -  # rpc: allow specifying min chain depth for inputs in fund calls
	22072 -  # Add reindex=auto flag to automatically reindex corrupt data
	22147 sdaftuar/2021-06-reserve-outbound-hb
	# AFTER CORE RELEASES: (PR unknown) taproot descriptors +22156? +22166?
	22159 marco/2106-buildPattern
	g256  hebasto-g/210323-peers
	g330  jarolrod-g/prompt-icon-colorized
	g281  jarolrod-g/mul-shortcuts-resize
	g291  -  # Network Graph layout - debug window improvement
	g293  RandyMcMillan-g/enable-wordwrap-services
	g298  RandyMcMillan-g/alt-row-colors
	g307  hebasto-g/210501-stripes
	Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	g309  hebasto-g/210501-network
	g318  jarolrod-g/copy-addr-peer
		TODO: Add keyboard shortcut
	Needs review: g342 hebasto-g/210521-wallet
	Diff-minimise: g343 hebasto-g/210522-ppd
	g362  kbshortcuts_context
# Non-progress functionality:
	8751  sort-multisigs-0.21					a1b1f408a1a	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152 sweepprivkeys							8e776230ab9
	9245 ionice									35bf68eddce
	-    ionice_win								02a1efe6391
	8501  old_stats_rpc-0.21					b05e4480fdf	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-0.21						5b6c263cd1f	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-0.21					82506cdd9e8	last=07fc81109a
	9849 gui_netwatch-0.21+knots				d8b7e2d12e0	last=c4599591e97 gui_netwatch
	10615 multiwallet_rpc-0.21+knots			9ebcde7606c	last=ee12dd02601 multiwallet_rpc
		FIXME: Restrict backupwallet/dumpwallet somehow???
	10554 zmq_wtx-0.21+knots					d933d13de8c	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					ba634e68076
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment				b3602f5b7b5
	10350 filtered_witblock-0.21				69ebcc245a9	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				ba7596dc7df	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.21							701406be432	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			7575e9d686c
	12965 scriptthreads-0.20					756abfdf8b4	last=dfab6c6866 jonas/2018/04/svt
	13203 dsha256_power8-0.20					d3b4b876a5d	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		209c76842a6
	15218 postibd_flush							3ec41fd7756	last=d2ecb70d64  # validation: Flush state after initial sync
		# TODO: Rewrite after #17487 is ready/safe to merge
	15428 tor_gui_pairing-0.21+knots			a5eac11425e	# latest code now
	15421 tor_subprocess-0.21+knots				34f6a4170ba	last=58c6cafd3a1 tor_subprocess
	# TODO: tor gitian bundle!
	15633 nohbcbfornonwit-0.21+knots			a2a5e87357d	last=ac897f0bd3a nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					2ba0d7680f2
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					bd72d5147d2
	16807 bech32_error_detection-0.21+knots		14b2c049b33	last=54e107add41 meshcollider/201909_bech32_error_detection
		# NOTE: Minor diff-minimisation, dropped relnotes, added autodetect hack, +x test
	# Redundant/conflicts with 16807: 20832 -  # rpc: Better error messages for invalid addresses
	-     gui_bech32_errpos-0.21+knots			065bf445e2f  # Latest code
	17636 guisettings-0.21						d1a9bd6dcc2	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo-0.21+knots			a2866ddc27a	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0-0.19					0350277f3df	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances-0.21+knots		9f091b577ae	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-0.21+knots	559324faf71	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock			d8be75679d9	last=1e868bbbb1b
	18789 achow101/create-unsigned-sendconfdialog
		#TODO: Resolve conflict with wallet_no_reuse
		#OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	19117 rpc_getrpcwhitelist					eb3d760b63a
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.21+knots	c7725d21554
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-0.21+knots	a1fdd41267d	last=200e09f00b0 whitelist_outgoing
		#TODO: Split this up?
		# NOTE: d756d0a01a6 needs legacyWhitelisted in minified version!
		# NOTE: Originally #10594
	20764 jonatack/netinfo-updates-dec-2020
		FIXME: Check if all applicable to 0.21
	# Needs review (+ minimisation?): 20833 -  # rpc/validation: enable packages through testmempoolaccept
		# +22084
	g165  gui_peers_splitter_ss-0.21+knots		e6d89996c67
		# +g194 Save/restore RPCConsole geometry only for window
		# NOTE: Changed setting name since our splitters don't match Core's
		# TODO: Each release, see if we need to bump setting name (and figure out back compat?)
	# Needs purpose: 21815 prayank23:max-out-full-relay
# Non-upstreamed functionality:
	# 22.0 TODO: Revert #21992 (removed -feefilter option, useful for manually prioritised transactions)
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				7282a392f4f
	-     walletnotify_w_win					ee2308c6163
	14137 win_taskbar_progress					731d80d2fa5	last=18eb4dbb8a
	-     restore_blockmaxsize					762f1ed78d1
	7107 qtnetworkport							37d1a79eda3	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							ce8afbd4b4c
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								d23b5dd2c4c
	7510 rwconf_gui								7cf7822ab2f
	 559 accept_nonstdtxn						d50ed506672
	g153 const_max_digits						582bdd2599f
	 929 tbc									d0f0c094f51
	 553 bugfix_qt_uri_amount_parser			c4e43cc2e84
	-    mining_priority						c5322455df2  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					c91a2e74ed1
	5891  qt_console_history_persist-0.21+knots	0c6fb2613e8	last=ea852deea35 qt_console_history_persist
	7219  rbf_opts-0.21+knots					3dbe593a6e4	last=5df41eadb59 fullrbf # missing 91786d16ccc + revert34ae6640174
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					53432dc49d3
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			afe0f69061e	# Latest code now
	-     gui_request_payment_label-0.19		94abe57a960
	-     gui_peers_sort_network-0.21+knots		c4fbf4c6084
# Non-upstreamed Knots compatibility:
	-    preserve_unsupported_keyflags			189276115ab
	9422  mempool_dat_extensible_mod-0.21+knots	f4f5c7f69bf last=1befffc0b48 mempool_dat_extensible
		# 0.22 TODO: Load-only (kept read/write for 0.21 only so 0.14-0.20 don't lose prioirities on downgrade)
		FIXME: Address 32 MB limit bug (https://github.com/bitcoinknots/bitcoin/issues/30)
	11413 rpc_feemode_explicit_compat-0.21+knots	55502e4eeff
	-     netperms_implicit_addr				710fc292260
	12674 rpc_onetry_nonpriv-0.21+knots			b660a9f435d
	# TODO: add a bitcoinknots.conf ?
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				f6eb067a1a7
	-    bytespersigopstrict-0.21+knots			c6e7665a461
	9749  unique_spk_mempool-0.21+knots			81517600915
	-     bloom_default-0.21+knots				784558e4f7b
	-     enforce_checkpoints
	n/a   checkpoint_update-0.21				ef8f3826f52
	10282 timebomb_knots						486d4c9f50f
	-     rwconf_policy-0.21+knots				8d876234db0
		# Include Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	7483  svg_icon-0.21+knots					ac8d3e0bd57
# BRANDING:
	n/a   knots_branding-0.21					54fc558d21e
#FIXME: check there's no univalue push_back(bool) - see #20424 and stash 8724e2fae4
#FIXME: Check there are no menu icons
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
TODO: Check calls to RPCConsole::clear(bool) get expected behaviour
	n/a  (cherrypick=e0968d0328b2877330)		c91fc545126	# doc/{bips,files}
	n/a  (bump_version=Knots:20210309)			ea72e5a5e33
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=55df7a04800)				cc37fd7c8be  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# 22.0 TODO: #21063 API change if merged
		gs origin-pull/21594/head^^ doc/release-notes.md
		gs origin-pull/21843/head
	n/a  (cherrypick=f85265ea4d8)				878980c69c4  # update manpages (build first)
	n/a  (cherrypick=63fcf9deced)				d4a64f61c13  # translation update
# NOTE: use git diff --minimal for patches!

@0.21.x-knots-android
