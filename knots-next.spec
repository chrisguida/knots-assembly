timestamp 2021-01-30 05:16:37
lastapply no-merge

#.. checked up to PR #21038 / gui #199

checkout v0.21.0
@0.21.x-syslibs
	5872 subdir_incl_compat						1cbdb2ff17a
	2241 sys_leveldb							9cb10b093fb
	5416 sys_libsecp256k1-0.21					0c3cda80472	last=258c28e99b3 sys_libsecp256k1
	7485 sys_univalue_def						7e29fdf0d03
	13789 bugfix_asm_pragmas					a5fc4e7be85
	-     bugfix_asm_leveldb_check				b37c1f867cd
	15155 test_external_bcli					b1ca07dc0f0
	# TODO: 20202 achow101/opt-sqlite-bdb
		#FIXME: Make sure tests skip properly per review concerns
		# Needs #20458 #20267 #20478
	20121 secp256k1_allow_bignum				6137b192b01
	20358 -										20c750b874c													last=330cb33985d  # src/randomenv.cpp: fix build on uclibc
	20594 conf_getauxval-0.21					0489bf7a484								last=836a3dc02c7 jonas/2020/12/getauxval
@0.21.x-knots
# TESTS:
	-     lint_relaxer							6b3ec23b7ed
	17402 travis_ppc64							12dfd387f7c	last=1d684f05341 elichai/2019-11-powerpc64
# FIXES:
	18818 fix_gitian_src_202004					6fc637d9972
	18902 fix_gitdir_again						f7355def795
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					6d99a88337e	last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case				ada6068f813
	17828 p2p_log_categories					f8284c15abb	last=04960621582 practicalswift/log-categories
	19832 hebasto/200829-log					9edcf4da007								last=1816327e533
	20845 net_logcategory_localdisconnect-0.21	52a728a1cba				last=fae5c7c92b0 marco/2101-netLogDisconnect
	# Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
	14968 laanwj/2018_12_http_bind_error		935169d3c0d	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					8005696f9f3
	9524 marco/Mf1701-qaPruning					63652de0988	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					57045135e86
	14485 fadvise								70f7188dcaf
		# Was #12491
	14501 fsync_dir								a68c3372204
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
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
	# Needs concept ACK: 18466 -  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	18729 intro_dont_change_user_prune			c80f7d5e9a5
	18766 blocksonly_no_feeest-0.21				4249edfa001	last=4e28753f606
		# diff-minimised
		# HELD BACK 33ca3590243...4aaad74c4c8 due to refactor complication
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19362 rpc_scantxoutset_reset_progress-0.17	57179188510	last=8c4129b4540 prusnak/rpc-scantxoutset-reset-progress
	19419 listwalletdir_skip_data				eaa839d579c	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: g18    hebasto:200701-peer
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs review: g59 hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	# Needs concept ACK: 19884 -  # p2p: No delay in adding fixed seeds if -dnsseed=0 and peers.dat is empty
	# Needs work: 19888 fjahr/genesisblockstats
	# Needs review: 20196 vasild/fix_GetListenPort
	g87   hebasto-g/200910-mono					cecabfc6440								last=2e386cd3dd3
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: g121 promag/2020-10-missing-transaction-notifications
	# Needs work: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	20448 unloadwallet_namematch				23c02df92c0
	# Needs consideration.. why would we re-announce to the same peer?? 20561 sdaftuar:2020-12-moar-addrz
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					f5193e74b49
	-     bugfix_gui_drop_abc_confusing_hack	a22512d2d9d
	20805 copyright_2021-0.21					11239d013ad
		# NOTE: Diff-minimised
	# Needs careful review: 20966 banlist.json (TorV3 bans fix)
	# Needs more PRs - for Dark Mode support: g154 -  # qt: Colorize icons on macOS for Dark mode support
	# Too messy? g164 hebasto:201224-signal
	# Confirm bug even exists: g167 RandyMcMillan:help-message-raise
	g171  qt_createwallet_layoutmgr-0.21		b3652905431					last=d4feb6812a2 hebasto-g/210101-wallet
	# Meh? Diff too big? g176 hebasto:210103-delegate (fix in #20983)
	g177  workaround_qt_macos11_fusion-0.21		1d7792c06df					last=4e1154dfd12 hebasto-g/210107-style
	20952 bdb_sanity_check-0.21					ee58bbed140
	g188  bugfix_psbt_binmode-0.21				4024211b958							last=cc3971c9ff5 achow101-g/bin-mode-psbts
	21028 bips_44-49-84							84554a991f3
	21029 cli_doc_geNnewaddr					733dcdcccfb
	# Needs review: g201  jonatack/inbound-block-relay
	# Needs review: g202  RandyMcMillan/peers-tab-sidepanel
# FUNCTIONALITY:
	-     restore_win32-0.21+knots				ead2c865bd9	last=3e30ae0514e restore_win32
	-     restore_linux32						264fb4a463a
		# NOTE: gitian only
	20963 gitian_power64-0.21+knots				4f3da061154	last=543bf745d38 gitian_power64
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
	14641 fundraw_minconf-0.21					53168e0677a	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	12677 listunspent_ancestorinfo				ddc422a8bca
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					40a9e7ebcf2	last=47b2ba29df2 !kallewoof/sign-show-fees
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
	g119  rm_send2self-mini						7e3a29cbc3e	last=77a74aac443 rm_send2self
		# NOTE: Originally #15115
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						2112864282e
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs work: 18077 hebasto/20200130-natpmp
		# NOTE: Diff-minimised rebase of 2d5d98ce0aa is at c6ff5633b56
		# TODO: Switch to rwconf?
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram							849a2065ba5	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: removed extraneous Bitcoin-Qt.* files
	# Totally broken: g108 jonas/2020/03/mempool_graph									last=42b451ebf1e
	# Needs QA/review: 15946 jonas/2019/05/prune_blockfilter
		# NOTE: When merging, update GUI neutrino stuff to allow pruning+filters!
	17463 gui_custom_sendyes					3fa98c71293
	15987 wallet_no_reuse-0.21+knots			7af5b97435f
		# TODO: Rewrite based on bugfix_gui_bumpyes (g#148) + non-superconstructor #17463
	-     rpc_gai_txids-0.21+knots				09dda80206a
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	18772 -										8c865bd7993 last=66d012ad7f9  # rpc: calculate fees in getblock using BlockUndo data
	16083 rpc_getblock_prevouts_fees-0.21		e5d7ec500f5	last=dd83c4c925
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# Needs mucho review: 16546 Sjors:2019/08/hww-box2 # -signer
		# NOTE: Bumps boost version!
	# Depends-on-16546: g4 Sjors:2019/08/hww-qt
		# NOTE: was #16549
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	16795 rpc_inferred_output_descriptors		9ec8f64e1d8	last=3038f944a6d instagibbs/decode_descriptor
		# Fixes: 478a4da04e77ca4438929909fafdbb0e57614577
	# Needs review: 16981 LarryRuane:reindex-speedup
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs review: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options? (watch out for send RPC)
		# TODO: Diff-minimise
	# Needs fix: 17355 za-kk:oct-19-17174
	18972 neutrino_whitelist-mini				cb9291c7bad	last=339fe189eb9
		# NOTE: Diff-minimised
	17034 psbt_ver_proprietary_xpub-0.21		840783b508a	last=93d232e57e5 achow101/bip174-extensions
		# NOTE: Diff-minimised
		# NOTE: Now includes 16463 bip174_xpub-0.21+knots				8e6f8d3cc9c	last=9926a387eab achow101/bip174-xpub
	# Needs review: 17529 rpc: Faster getblock using PureBlock
	17631 rest_blockfilter-0.21					3d8a59fb9b3	last=16d8d2da598 matt/2019-11-filter-rest
		# NOTE: Dropped unrelated extra commits
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	17955 emilengler/2020-01-paste-bitcoin-uri-button	7fe8642bcf3	last=0139b428923
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	3ac87315cb0	last=9ed348ddea3 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonas/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	18689 rpc_dumptxoutset_hr					e453aea92c5	last=82046cf7fa3
	18722 O_addrman_unordered_map-0.21+knots	26e8d08bead	last=d517c9d376f
		# NOTE: Restored C++11 compatibility from d6e782174ec
	g125  intro_prune_size						4aa0b4e2086
		# NOTE: Originally #18728
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19136 achow101/export-descriptor			10a78003307						last=de6b389d5db
	19137 wallettool_dump-0.21+knots			6e4c01eef9b						last=23cac24dd3f achow101/dumpwalletrecords
		# NOTE: Disabled for BDB wallets since it doesn't dump/restore wallet id yet
		# NOTE: Changed to print warnings to stderr instead of stdout
		# NOTE: Diff-minimised
	19242 uaappend								b8318bfba10
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
	19463 prune_locks							5a0483add3c
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review: 19521 # Coinstats Index (without UTXO set hash)
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	19762 ryanofsky/pr/named					bea9f7551da								last=894c414dafb
	# Needs review and triage (fix or feature?): 19763 vasild:only_relay_to_unaware
	19776 -										a72e7a2d9a6													last=343dc4760fd  # net, rpc: expose high bandwidth mode state via getpeerinfo
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							6bfac736370
	# Needs serious work: 20139 -  # "Removed unused warning and formatted RPC result" supposedly
	# Needs work: 20154 kallewoof/202010-bip322
	# Needs work: g86 hebasto/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	# Needs review (and diff minimisation?): 20197 jonatack:AttemptToEvictConnection-identify-onions-with-m_inbound_onion
	20226 rpc_listdescriptors-0.21				51597dbf206							last=647b81b7093
	g90   gui_trafficgraph_vert-0.21			89de795cf02						last=8b79225642a  # Enlarge Network Traffic Graph
		# Removed dialog size change
	20254 i2p_static-0.21						dc52d5be97b									last=8b4a3714b91 vasild/i2p_static
	# Needs review: 20685 vasild/i2p_sam
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonas/2020/10/client_rpc_nested
	20275 no_sqlite_but_list-mini				0af641fbf7d							last=f3d870fc227 ryanofsky/pr/exist
		# Mostly rewritten?
	20295 getblockfrompeer-0.21					e52bf0d34da								last=c0030dd69cb Sjors/2020/11/getblockfrompeer
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	# Needs review: 20365 -  # wallettool: add parameter to create descriptors wallet
	20391 rpc_setfeerate-0.21					1d40dd103b6								last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20403 upgradewallet_pr20403-0.21+knots		05bb76078f5					last=3eb6f8b2e61 jonatack/upgradewallet-improvements
	20407 rpcauthfile-0.21+knots				0891951feea							last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bug, added multi-line support, and added tests
	# Needs review and diff-minimisation: 20421 fanquake/miniupnpc_220
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						d07758b6754
	# Needs a reason to move code chunks: 20599 jnewbery/2020-12-tolerate-early-send-messages
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20664 rpc_scanblocks-0.21					39acb06952b								last=ab315e5294b jonas/2020/12/filterblocks_rpc
	20702 rpc_getblocklocations-0.21			7c9162cd981						last=9b03c654eb3
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							e11ac4ec12a
	# Needs BIP review: 20861 sipa:202101_bech32m
	# Needs review? 20867 darosior:descriptor_multi_wsh
	g163  gui_peer_conntype-0.21				518b754c560  # jonatack-g/display-peer-conn-types
		# NOTE: Stripped unrelated string changes
	g180  gui_peer_relay_detail-0.21+knots		65c7c363c67					last=79a2576af1e jonatack-g/peer-details-connection-type-followups
		# NOTE: Carries commit from g163 since it messes with the string anyway
		# NOTE: Left off final doxygen commit
	g179  gui_peers_conntype-0.21+knots			733bbb77cd2	last=9f76ba6597c jonatack-g/add-peers-dir-and-type-columns
	-     qt_peers_directionarrow-0.21+knots	745d420e1ea				last=52279e4b24a tmp_gui_peers_dir_arrows
	20916 rpc_testmempoolaccept_wtxid-0.21		06963a9d2c4					last=fa0aa87071e marco/2101-wtxidTestmempool
		# Diff-minimised
	g162  gui_peers_detail_network-0.21+knots	83d04e66f00
		# NOTE: Left out Peers table column & misc formatting changes
	20944 rpc_getmempoolinfo_total_fee-0.21		5b4ff46424b					last=fa362064e38 marco/2101-rpcMempoolTotalFee
		# NOTE: Minor code rearranging to avoid conflicts
	# Needs review: 21006 -  # rpc: reduce LOCK(cs_min) scope in rest_block: ~5 times as many requests per second
	g186  gui_bumpfee_privacywarn-0.21+knots	d487b8229e4
# Non-progress functionality:
	8751  sort-multisigs-0.21					c20ff62345d	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152 sweepprivkeys							c308f0b0fea
	9245 ionice									a1ae98f9c12
	-    ionice_win								92e74a9729a
	8501  old_stats_rpc-0.21					b80b0bf4cac	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-0.21						c4344a9ab76	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-0.21					7231de18898	last=07fc81109a
	9849 gui_netwatch-0.21+knots				2d5db48866b	last=c4599591e97 gui_netwatch
	10615 multiwallet_rpc-0.21+knots			cf7ad9bdb9f	last=ee12dd02601 multiwallet_rpc
	10554 zmq_wtx-0.21+knots					f37654b052a	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					80e01e8bde9
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment				142a8ef12eb
	10350 filtered_witblock-0.21				37e112c7a0e	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				0d392c98b96	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.21							af587f6ecba	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			17bb4451381
	12965 scriptthreads-0.20					12d12975755	last=dfab6c6866 jonas/2018/04/svt
	13203 dsha256_power8-0.20					d63443ce22b	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		53f3949b223
	15218 postibd_flush							349d3c6b1fd	last=d2ecb70d64  # validation: Flush state after initial sync
		# TODO: Rewrite after #17487 is ready/safe to merge
	15428 tor_gui_pairing-0.21+knots			b3f4bfb80d6	# latest code now
	15421 tor_subprocess-0.21+knots				1a7f9b47910	last=58c6cafd3a1 tor_subprocess
	# TODO: tor gitian bundle!
	15633 nohbcbfornonwit-0.21+knots			38eaf636c85	last=ac897f0bd3a nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	#16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					a0b64ba7443
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					71bd7e16acd
	16807 bech32_error_detection-0.21+knots		47d326bd017	last=54e107add41 meshcollider/201909_bech32_error_detection
		# NOTE: Minor diff-minimisation, dropped relnotes, added autodetect hack, +x test
	# Redundant/conflicts with 16807: 20832 -  # rpc: Better error messages for invalid addresses
	-     gui_bech32_errpos-0.21+knots			2b47c826d7a  # Latest code
	17636 guisettings-0.21						a918c816c1a	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo-0.21+knots			be7e52d5bcd	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0-0.19					61b2dc8a957	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances-0.21+knots		2b340e15e1c	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-0.21+knots	259b3c38ccf	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock			5ca1b442fb7	last=1e868bbbb1b
	#18789 achow101:create-unsigned-sendconfdialog
		#TODO: Resolve conflict with wallet_no_reuse
		#OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	19117 rpc_getrpcwhitelist					b35eb528620
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.21+knots	03b60a7d3fa
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-0.21+knots	ec161759498	last=200e09f00b0 whitelist_outgoing
		#TODO: Split this up?
		# NOTE: d756d0a01a6 needs legacyWhitelisted in minified version!
		# NOTE: Originally #10594
	# TODO: 20764 jonatack/netinfo-updates-dec-2020
		#FIXME: Check if all applicable to 0.21
	# Needs review (+ minimisation?): 20833 -  # rpc/validation: enable packages through testmempoolaccept
	g165  gui_peers_splitter_ss-0.21+knots		2b06dd788b0
		# +g194 Save/restore RPCConsole geometry only for window
		# NOTE: Changed setting name since our splitters don't match Core's
		# TODO: Each release, see if we need to bump setting name (and figure out back compat?)
# Non-upstreamed functionality:
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				6994c339f7d
	-     walletnotify_w_win					0dd83c59689
	14137 win_taskbar_progress					2a0680772ea	last=18eb4dbb8a
	-     restore_blockmaxsize					0ba6ae5ab8c
	7107 qtnetworkport							3100bc6cd35	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							365cda0f395
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								5d1c28546f2
	7510 rwconf_gui								fd9be6559b0
	 559 accept_nonstdtxn						cb0777a2233
	g153 const_max_digits						de9511ddfa1
	 929 tbc									90a9c3f69c1
	 553 bugfix_qt_uri_amount_parser			43ae1ebc7af
	-    mining_priority						3d07a7b32c5  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					3cab2a8afb9
	5891  qt_console_history_persist-0.21+knots	e349623240f	last=ea852deea35 qt_console_history_persist
	7219 rbf_opts-0.21+knots					3bc2012527e
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					ee563750f0a
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			858d7c971c9	# Latest code now
	-     gui_request_payment_label-0.19		55a7a562eb3
	-     gui_peers_sort_network-0.21+knots		f6013321d23
# Non-upstreamed Knots compatibility:
	-    preserve_unsupported_keyflags			739687c6e2e
	9422  mempool_dat_extensible_mod-0.21+knots	223ad7b95fa last=1befffc0b48 mempool_dat_extensible
		# 0.22 TODO: Load-only (kept read/write for 0.21 only so 0.14-0.20 don't lose prioirities on downgrade)
	11413 rpc_feemode_explicit_compat-0.21+knots	dd46bba4788
	-     netperms_implicit_addr				c1fb0f81348
	12674 rpc_onetry_nonpriv-0.21+knots			6b108de8e8e
	# TODO: add a bitcoinknots.conf ?
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				8f46c758d12
	-    bytespersigopstrict-0.21+knots			b03f0671dff
	9749  unique_spk_mempool-0.21+knots			60cd34e4e80
	-     bloom_default-0.21+knots				fc7f4e56166
	n/a   checkpoint_update-0.21				57725767b26
	10282 timebomb_knots						7e51e3d45c3
	-     rwconf_policy-0.21+knots				c5025467ab3
		# Include Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	7483  svg_icon-0.21+knots					1347651a4d6
# BRANDING:
	n/a   knots_branding-0.21					bd3ed79be1d
#FIXME: check there's no univalue push_back(bool) - see #20424 and stash 8724e2fae4
#FIXME: Check there are no menu icons
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
	n/a  (cherrypick=e0968d0328b2877330)		78d9761b2de	# doc/{bips,files}
	n/a  (bump_version=Knots:20210130)			2e25b726cd1
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=55df7a04800)				b9a285e7cb5  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=f85265ea4d8)				420a6e6a991  # update manpages (build first)
	n/a  (cherrypick=63fcf9deced)				b9245d3d8cf  # translation update
# NOTE: use git diff --minimal for patches!

@0.21.x-knots-android
