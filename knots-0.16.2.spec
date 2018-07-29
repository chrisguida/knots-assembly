timestamp 2018-07-21 02:05:23
#lastapply no-merge

#.. checked up to PR #13797

checkout v0.16.2
@0.16.x-syslibs
	5872 subdir_incl_compat						0dc6410709
	2241 sys_leveldb-0.16						303e7fb17b
	5416 sys_libsecp256k1						0c71b8509b
	7485 sys_univalue_def						7058f9681d
	5618 separate_utils_only					d5c91a0d29
	12246 separate_utils						3101ffbc0d
	7339 opt_libevent-0.16						e748672088
	11622 bip70_disable-0.16					2df1371ff1	last=7ecca66062
TM	12859 incl_memory							7a8558fdd5
	12854 desktop_categories					08f6cceb4f
	-     ppa_updates-0.16						7810c2d1d3
	13788 bugfix_asm_opt-0.16								last=4207c1b35c bugfix_asm_opt
	13789 bugfix_asm_pragmas-0.16							last=8bca9cd7ba bugfix_asm_pragmas
	-     bugfix_asm_leveldb_pragma-0.16
@0.16.x-knots
# TESTS:
	13105 test_failfast-0.16					14caa2b18f
	-    travis_nolibevent						c40fd4e5b0
# FIXES:
	9524 marco/Mf1701-qaPruning					8b4de6cfe6
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						5ce08dd859
	10731 log_more_uacomment					22401d478b
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	# ^ 11634 walletlocks-0.16						7914050bdb	last=491ec75b9f
		# held back annotations, and minimised patch
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
TM	12432 clear_all_coinctl-0.16				42f0d7e7da
	12479 rawmempool_spentby-0.16				ff31f0fed3	last=1dfb4e7d75  # RPC: Add child transactions to getrawmempool verbose output
	12491 fadvise-0.16							cec7997900	last=5259c72a76  # Try to use posix_fadvise with CBufferedFile
	12495 leveldb_max_open_files-0.16			fb33260e1e	last=ccedbafd73  # Increase LevelDB max_open_files on 64-bit POSIX systems
		# held back changes to developer doc file
	12501 text_customfee-0.16					04bfba481a	last=0bc095efd8  # [qt] Improved "custom fee" explanation in tooltip
TM	12573 bugfix_no_clz-0.16					d71bd11d76
TM	12617 2018_03_gui_textbox-0.16				41fd6d14c1
	12696 eklitzke_fsync-0.16					1cfc3aeddc	last=4894e368fa  # Fix possible data race when committing block files
	# For 0.17: Revert #12723?
TM	12743 201803_waitblockchange-0.16			e59a996089
		# NOTE: held back variable renaming
TM	12793 fix_resetgui0-0.16					9d49645994
	13084 fix_1neg-0.16							7ffec1c189	last=5af7625079 sipa/201804_keepnegone
	# Requires 11739, which touches too much consensus logic: minimized 13120 MarcoFalke:Mf1805-segwitGenesisPolicy
	13149 check_fseek-0.16						4d62acbe06
	13159 handle-reopen-failed-0.16				ade70fc69a	last=37efe5b7ea practicalswift/handle-reopen-failed
		# minimised diff
TM	13452 actuallyverifytxoutproof-0.16			f4a7b09cd5
NM	-     optimise_wallet_inv-0.16				74c9c1b11f
TM	13437 walletPrunedFundsSegfault-0.16		d7e2a677a2
TM	13545 bugfix_streams_test-0.16				b5b94d985a
TM	13300 bugfix_qa_lockstack-0.16				9a30600318
TM	12887 bugfix_log_newlines-0.16				fd469899df
TM	13304 bugfix_wallet_listreceivedby_test-0.16	ca63969f98
TM	13192 bugfix_p2p_sendheaders-0.16			fa7f49cca1
	13547 bugfix_signraw_amountcheck-0.16
	13608 bugfix_b-tx_amountcheck-0.15						last=876f49c6cd
	13655 bugfix_libcon_verify_invflags-0.16
	# Needs review: 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
# FUNCTIONALITY:
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.16					ffcb4cd05d	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sort_multisigs			b2ce8aae14	last=127ec180bd sweepprivkeys
NM	12196 sweepprivkeys+scantxoutset			1ff7bfeb7e
	12196 sweepprivkeys+scantxoutset			c048354fef						last=be98b2d9a8 jonas/2017/12/utxo_sweep
		# modified to remove scan-by-address garbage
		# held back feature removals
	9245 ionice									250ed07696
	-    ionice_win								e8296c54f5
m	8501 old_stats_rpc-0.16						e0cf24c0f8	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 stats_qt-0.16							4b69cc74fa	last=63fb11652f
		# NOTE: partial rebase at https://github.com/jonasschnelli/bitcoin/pull/9 ??? OLDER THAN CURRENT NOW
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					5cd24e181e
	9991 listreceivedbyaddress-filtered+knots	e32928c277	last=f087613719  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey-0.16					2b9f7fa563	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							08ae3461d4
	11383 multiwallet_gui-0.16+knots			3b46a27eaf	last=f5aa574c37 multiwallet_gui
	10615 multiwallet_rpc						feb4cc9eec
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10554 zmq_wtx-0.16							200a2d3420	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					a2b002f2cb
	10593 relax_invblk_punishment				2c47a86875
	10594 whitelist_outgoing					3d69144480
	10350 filtered_witblock-0.16				330e646dc0	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								4556dd6628
m	10730 scriptflag_strings-mini-0.16			5d75779e76	last=e2e183bc1f
	n/a   script_debugger-mini					f1f3bbaafa	last=1d3ed0c48a script_debugger
	# Needs work: 11200 achow101/gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				228d67d4cc
m	11256 rpc_mempoolentry_weight-0.16+knots	72f59f3ca2	last=d4b0d81b58
	11413 explicit_fee-0.16						d8e0792da3	last=628f6e971a kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.16				1a8a499257	last=c23bd2892b
	11491 proxy_icon-0.16+knots					5cc3186847	last=73cd5b25b9  # [gui] Add proxy icon in statusbar
		# NOTE: uses manual merge to avoid crazy conflict in svg_icon later
		# NOTE: held back meaningless changes to pixmap/icon init
	11653 rpc_getsignaturehash+knots			9b7aeee493	last=0a688c4f61 NicolasDorier/getsignaturehash
	11658 ibd_prune_extra						4794fd8469
		# Consider replacing with 12404...
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	# Not ready: 11742 testmempoolaccept-0.16							last=faa03a6dad
		# test fails, RPC includes int instead of bool, etc
	11750 -										304ac95bfb # Multiselect in coincontrol treewidget and display selected count
	11765 rest-blockhash-endpoint-0.16			2be7452240 last=1323df9ff1 # [REST] added blockhash api, tests and documentation
	11770 rest_fee-0.16							ff1076da70	last=935b364978  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath-0.16		49455f4947	last=393511cb22 bugfix_dumpwallet_hdkeypath
	# 11872? MarcoFalke:Mf1712-rpcCreateRawSortedOuts (what's the use case?)
	12080 promag/2018-01-searchaddressbook		84978e32c9
	12096 bumpfee_reduce_output-0.16			ce3cf13ba6	last=51826d4de0 kallewoof/better-bumpfee
NM	12136 psbt-0.16								8d1d894bba	#last=950746725a achow101/psbt
TM	13251 gui_legacy_bech32-0.16				f787751d39
m	12240 rpc_mempool_fees-0.16					20e64d6b07	last=7de1de7da4  # [rpc] Introduced a new `fees` structure that aggregates all sub-field fee types denominated in BTC
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters
	12257 avoidpartialspends-0.16				ed6cfe05c4	last=452485e1b7 kallewoof/feature-addrgrouped-coinselect
		# NOTE: held back af586af9f0..452485e1b7
	12321 decodescript-p2wsh-0.16				1066b6e3ae	last=41ff9675a9  # p2wsh and p2sh-p2wsh address in decodescript
	12421 send_to_txhistory-0.16				cf8c3ea86f
	12568 zero_dustrelayfee_opt					8cf6a02216
	12580 gui_vsize-0.16						3d6f3a0816
	12677 listunspent_ancestorinfo-0.16			4e8d9b8149	last=daeb431011 listunspent_ancestorinfo
	# Not sure if safe with 0.16: 12559 promag/2018-02-avoid-cs_main-lock
	# Too dangerous. PART OF 12560 achow101:sethdseed
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	12616 modaloverlay-hide-default-0.16		3b6c1f15a7
	12621 gui_txfilter_optimise-0.16			0963d6a9af
	12653 blocksdir-0.16						be136cf8df
	12676 rawmempool_bip125-0.16+knots			09d5c52f39	last=870bd4c73d
		# NOTE: rewritten
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.16						7d793131db	last=8c45d93b0e
	# 12769 ???
	12778 rpc_loguser-0.16+knots				bc9ef3a4ab
	12783 disable_appnap-0.16					04125efb41	last=33a25f1e02
		# Retained older inhibitor too
	12791 rpc_tx_weight-0.16					ef02484afe
	# TODO ? 12792 w/ renamed param
	12818 gui_feebump_select-0.16				63745c7be5	last=90c614cb8b
	12911 signrawtx_showfees-0.16				1bf2a1ee4f	last=b7159aa585 kallewoof/sign-show-fees
	12965 scriptthreads-0.16+knots				00c2ae90f5	last=dfab6c6866 jonas/2018/04/svt
	# TODO ADD ONLY 13008 # rpc: Rename size to vsize in mempool related calls
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Needs fixes: 13072 ajtowns/signmultisig
		#FIXME: rename legacy to bip16
	13134 optional_bip61-0.16					29323f7666
	13151 direct_from_disk-0.16+knots			2829679e32
	# Test fails: 13152 rpc_getnodeaddress-0.16							last=f10e380630
	13158 gui_send_readability-0.16				055bb837f8
m	13191 dsha256_64-0.16+knots					816e2f1228
		# Includes 13611
	13393 dsha256_i386-0.16						93be77a787
	13471 avxossupport-0.16						ca8dca3a9f
	13408 dsha256_cleanup-0.16+knots			e9c541e8a5
	13438 dsha256_selftest-0.16					b5fe11969b
m	13386 dsha256_shani-0.16+knots				0f5ea68849	last=66b2cf1ccf sipa/201806_shani
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
m	13203 dsha256_power8-0.16+knots				eef4629013	last=3b402e0738 matt/2018-05-asm
	-     bugfix_asm_opt_and_pragmas-0.16+knots
	# TODO: Possible performance concern 13310 promag/2018-05-replayblocks-progress
	13339 walletnotify_w-0.16					de556050f8	last=cef0327afd promag/2018-05-walletnotify
	# broken? 13399 rpc_submitheader-0.16								last=fa7d7dd34c marco/Mf1806-rpcBlockHeader
		# held back removal of duplicate-header submission check
	13537 gui_peertable_inout-0.10
	# Needs work: 13541 wallet/rpc: sendrawtransaction maxfeerate
	13570 rpc_getzmqnotifications-0.16
	# Needs review: 13666 Always create signatures with Low R values
	# Needs work: 13697 Support output descriptors in scantxoutset
	# Needs work: 13756 wallet: -avoidreuse feature for improved privacy
	# Needs review: 13791 gui: Reject EditAddressDialog on ESC key
# Non-upstreamed functionality:
m	-     restore_blockmaxsize					a7ec6a7fe8
	7107 qtnetworkport							49b1a942eb	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					986bd0c118  # Latest code now
	11082 rwconf-0.16							fced2b6fed	last=aac0501148 rwconf
	7510 rwconf_gui-0.16+knots					66ff172ba3	# Latest code now
	# Seems buggy: 13043 -													# [qt] OptionsDialog: add prune setting
	5916 keyorigin								e48967173c
	 559 accept_nonstdtxn						2c399bd488
	 929 tbc									a0b8c8f986
	 553 bugfix_qt_uri_amount_parser			6462ebe9db
	-    mining_priority-0.16					11831eb085  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					e38287a81f
	5891 qt_console_history_persist				0a0284e160
	7219 txrepl_fullrbf							aeb68906a1
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						0b776ade30
m	12146 opt_wallet_segwit2-0.16+knots			796e874c5f	last=f5f5a922ba opt_wallet_segwit2
	n/a  checkpoint_update						e96f70a59a
	# 0.17: Revert 12795
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				560179102c
	-	 bytespersigopstrict+knots				7513011981
	9749 unique_spk_mempool+knots				99aae2551f
m	-    rwconf_policy-0.16+knots				e4d1059638
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	-    txrepl_fullrbf_default+knots			557b0885b2	last=61fae13df1 txrepl_fullrbf_default
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.16+knots					42d99c01ec
# BRANDING:
	n/a  knots_branding-0.16					969b9f92ed
#FIXME: Check Univalue 1.0.3 is sufficient to build
#	TODO: Check if any pushKV do booleans
#FIXME: Check includes use <>
#FIXME: allow building without libmemenv if the necessary code is in libleveldb
#FIXME: check libleveldb .20 ABI issues; runtime check we're linked to same version?
	n/a  (cherrypick=1a7c7b4b97ee6bd79c)		c1ca0105eb	# doc/{bips,files}
	n/a  (bump_version=Knots:20180721)			ce9c0d36f4
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=b4fac14a1f)				e003de4b07  # release notes: write/update, including change log and credits
#ADD: https://github.com/bitcoin/bitcoin/pull/13570/files
#ADD:  origin-pull/13043/head
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=1b6733d786)				d3b82c426a  # translation update
	n/a  (cherrypick=a3224a3ee9)				2c2cce54e3	# update manpages (build first)
# NOTE: use git diff --minimal for patches!
