timestamp 2018-07-30 03:49:09
#lastapply no-merge

#.. checked up to PR #14101

checkout v0.16.2
@0.16.x-syslibs
	5872 subdir_incl_compat						c134703e62
	2241 sys_leveldb-0.17						3510c4e6eb
	5416 sys_libsecp256k1						f79618bee8
	7485 sys_univalue_def						79f1d9208d
	5618 separate_utils_only					0c45680e8e
	12246 separate_utils						c09d510d89
	7339 opt_libevent-0.16						07da87df90
	11622 bip70_disable-0.16					af740adc4f	last=7ecca66062
TM	12859 incl_memory							f7346c5426
	12854 desktop_categories					dad0af3d2f
	-     ppa_updates-0.16						c29eb66382
	13788 bugfix_asm_opt-0.16					4324338adf	last=4207c1b35c bugfix_asm_opt
	13789 bugfix_asm_pragmas-0.16				b8d31df2f8	last=8bca9cd7ba bugfix_asm_pragmas
	-     bugfix_asm_leveldb_check-0.16			54a0d3a45b
@0.16.x-knots
# TESTS:
	14065 symbol_check-0.17									last=8b03a40e6c symbol_check
	13105 test_failfast-0.16					d98301f6e3
	-    travis_nolibevent						bcd1f77c04
	14036 -	# travis: Run unit tests --with-sanitizers=undefined
	14080 MarcoFalke/Mf1808-travisSanThread
# FIXES:
	9524 marco/Mf1701-qaPruning					891509bbdf
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						938ce42c1a
	10731 log_more_uacomment					71ccec6290
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	# ^ 11634 walletlocks-0.16						7914050bdb	last=491ec75b9f
		# held back annotations, and minimised patch
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
TM	12432 clear_all_coinctl-0.16				3732182a3b
	12479 rawmempool_spentby-0.16				6e52c0d544	last=1dfb4e7d75  # RPC: Add child transactions to getrawmempool verbose output
	12491 fadvise-0.16							1c929547a4	last=5259c72a76  # Try to use posix_fadvise with CBufferedFile
	12501 text_customfee-0.16					6aa2f93d86	last=0bc095efd8  # [qt] Improved "custom fee" explanation in tooltip
TM	12573 bugfix_no_clz-0.16					83a4ba110a
TM	12617 2018_03_gui_textbox-0.16				4cc88de920
	12696 eklitzke_fsync-0.16					b22514b73f	last=4894e368fa  # Fix possible data race when committing block files
	# For 0.17: Revert #12723?
TM	12743 201803_waitblockchange-0.16			7a03359c52
		# NOTE: held back variable renaming
TM	12793 fix_resetgui0-0.16					7a6cc930bb
	13084 fix_1neg-0.16							80751fee66	last=5af7625079 sipa/201804_keepnegone
	# Requires 11739, which touches too much consensus logic: minimized 13120 MarcoFalke:Mf1805-segwitGenesisPolicy
	13149 check_fseek-0.16						5d73d9e9df
	13159 handle-reopen-failed-0.16				56be2f61a6	last=37efe5b7ea practicalswift/handle-reopen-failed
		# minimised diff
TM	13452 actuallyverifytxoutproof-0.16			b4eabf3e5c
NM	-     optimise_wallet_inv-0.16				9a5db540e8
TM	13437 walletPrunedFundsSegfault-0.16		bbbf62d227
TM	13545 bugfix_streams_test-0.16				911e57c0c9
TM	13300 bugfix_qa_lockstack-0.16				43d11b057c
TM	12887 bugfix_log_newlines-0.16				82fb7c056b
TM	13304 bugfix_wallet_listreceivedby_test-0.16	0af7dfc16f
TM	13192 bugfix_p2p_sendheaders-0.16			269c19f3fc
	13547 bugfix_signraw_amountcheck-0.16		a7a8f4cecb
	13608 bugfix_b-tx_amountcheck-0.15			6fc500c51d	last=876f49c6cd
	13655 bugfix_libcon_verify_invflags-0.16	d927793ede
	# Needs review: 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	13910 domob1812/progress
# FUNCTIONALITY:
	14066 gitian_power64-0.17								last=05cd16bf29 gitian_power64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.16					1d3cc741e6	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sort_multisigs			ed43377924	last=127ec180bd sweepprivkeys
NM	12196 sweepprivkeys+scantxoutset			47140cb7a7
	12196 sweepprivkeys+scantxoutset			52dfb4735e	last=be98b2d9a8 jonas/2017/12/utxo_sweep
		# modified to remove scan-by-address garbage
		# held back feature removals
	9245 ionice									3400eeb80d
	-    ionice_win								3303deb376
m	8501 old_stats_rpc-0.16						e8fc393fa6	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 stats_qt-0.16							74347db52f	last=63fb11652f
		# NOTE: partial rebase at https://github.com/jonasschnelli/bitcoin/pull/9 ??? OLDER THAN CURRENT NOW
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					d787eb624d
	9991 listreceivedbyaddress-filtered+knots	c9f486bc59	last=f087613719  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey-0.16					4c84494958	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							ded9e72741
	11383 multiwallet_gui-0.16+knots			d101176535	last=f5aa574c37 multiwallet_gui
	10615 multiwallet_rpc						e646c77988
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10554 zmq_wtx-0.16							5f5cc19ac3	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					dd2a168c2a
	10593 relax_invblk_punishment				e7398a9b8d
	10594 whitelist_outgoing					20d5c10ce0
	10350 filtered_witblock-0.16				e3c0fcef0a	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								a6d4274f12
m	10730 scriptflag_strings-mini-0.16			98813105ab	last=e2e183bc1f
	n/a   script_debugger-mini					019bcb76b8	last=1d3ed0c48a script_debugger
	# Needs work: 11200 achow101/gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				e79db541a0
m	11256 rpc_mempoolentry_weight-0.16+knots	3e005b804a	last=d4b0d81b58
	11413 explicit_fee-0.16						472b79c25e	last=628f6e971a kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.16				4bfb75be0c	last=c23bd2892b
	11491 proxy_icon-0.16+knots					038b222878	last=73cd5b25b9  # [gui] Add proxy icon in statusbar
		# NOTE: uses manual merge to avoid crazy conflict in svg_icon later
		# NOTE: held back meaningless changes to pixmap/icon init
	11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	11658 ibd_prune_extra						4aa1453899
		# Consider replacing with 12404...
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	# Not ready: 11742 testmempoolaccept-0.16							last=faa03a6dad
		# test fails, RPC includes int instead of bool, etc
	11750 -										3b3fbcbb3e # Multiselect in coincontrol treewidget and display selected count
	11765 rest-blockhash-endpoint-0.16			7fca723689	last=1323df9ff1 # [REST] added blockhash api, tests and documentation
	11770 rest_fee-0.16							7ba67d2910	last=935b364978  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath-0.16		51d373acca	last=393511cb22 bugfix_dumpwallet_hdkeypath
	# 11872? MarcoFalke:Mf1712-rpcCreateRawSortedOuts (what's the use case?)
	12080 promag/2018-01-searchaddressbook		71e6e7a83a
	12096 bumpfee_reduce_output-0.16			5d92f4453b	last=51826d4de0 kallewoof/better-bumpfee
NM	12136 psbt-0.16								1bf1bcfd03	#last=950746725a achow101/psbt
TM	13251 gui_legacy_bech32-0.16				f56a687e43
m	12240 rpc_mempool_fees-0.16					65e2eabc85	last=7de1de7da4  # [rpc] Introduced a new `fees` structure that aggregates all sub-field fee types denominated in BTC
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters
	12257 avoidpartialspends-0.16				d9919d8447	last=452485e1b7 kallewoof/feature-addrgrouped-coinselect
		# NOTE: held back af586af9f0..452485e1b7
	12321 decodescript-p2wsh-0.16				8835a9c0b2	last=41ff9675a9  # p2wsh and p2sh-p2wsh address in decodescript
	12421 send_to_txhistory-0.16				5d48df825e
	12568 zero_dustrelayfee_opt					358af6cf21
	12580 gui_vsize-0.16						d53b7c886f
	12677 listunspent_ancestorinfo-0.16			2642343fb6	last=daeb431011 listunspent_ancestorinfo
	# Not sure if safe with 0.16: 12559 promag/2018-02-avoid-cs_main-lock
	# Too dangerous. PART OF 12560 achow101:sethdseed
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	12616 modaloverlay-hide-default-0.16		92e3c302a0
	12621 gui_txfilter_optimise-0.16			407b301d71
	12653 blocksdir-0.16						1418b1d840
	12676 rawmempool_bip125-0.16+knots			d0871f6a99	last=870bd4c73d
		# NOTE: rewritten
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.16						3a58144b6c	last=8c45d93b0e
	# 12769 ???
	12778 rpc_loguser-0.16+knots				988f12cd37
	12783 disable_appnap-0.16					389dc7a96f	last=33a25f1e02
		# Retained older inhibitor too
	12791 rpc_tx_weight-0.16					f8f75e79f7
	# TODO ? 12792 w/ renamed param
	12818 gui_feebump_select-0.16				a1c7d44271	last=90c614cb8b
	12911 signrawtx_showfees-0.16				613381e9c4	last=b7159aa585 kallewoof/sign-show-fees
	12965 scriptthreads-0.16+knots				ec38b2650d	last=dfab6c6866 jonas/2018/04/svt
	# TODO ADD ONLY 13008 # rpc: Rename size to vsize in mempool related calls
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Needs fixes: 13072 ajtowns/signmultisig
		#FIXME: rename legacy to bip16
	13134 optional_bip61-0.16					b3cecd612b
	13151 direct_from_disk-0.16+knots			4aec0b6f0e
	# Test fails: 13152 rpc_getnodeaddress-0.16							last=f10e380630
	13158 gui_send_readability-0.16				12d70ffbda
m	13191 dsha256_64-0.16+knots					feda959492
		# Includes 13611
	13393 dsha256_i386-0.16						389b4be12d
	13471 avxossupport-0.16						3e56e69282
	13408 dsha256_cleanup-0.16+knots			0b48acc326
	13438 dsha256_selftest-0.16					0967e3cd5e
m	13386 dsha256_shani-0.16+knots				6d1c2bccbc	last=66b2cf1ccf sipa/201806_shani
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
m	13203 dsha256_power8-0.16+knots				6a93a81e3e	last=3b402e0738 matt/2018-05-asm
	-     bugfix_asm_opt_and_pragmas-0.16+knots	7d916e293f
	# TODO: Possible performance concern 13310 promag/2018-05-replayblocks-progress
	13339 walletnotify_w-0.16					10c0ad0430	last=cef0327afd promag/2018-05-walletnotify
	# broken? 13399 rpc_submitheader-0.16								last=fa7d7dd34c marco/Mf1806-rpcBlockHeader
		# held back removal of duplicate-header submission check
	13537 gui_peertable_inout-0.10				53249d4842
	# Needs work: 13541 wallet/rpc: sendrawtransaction maxfeerate
	13570 rpc_getzmqnotifications-0.16+knots	01c650d509
	# Needs review: 13666 Always create signatures with Low R values
	# Needs work: 13697 Support output descriptors in scantxoutset
	# Needs work: 13756 wallet: -avoidreuse feature for improved privacy
	# Needs review: 13791 gui: Reject EditAddressDialog on ESC key
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# TBD (part of) 13926 [WIP] [Tools] bitcoin-wallet-tool
	13932 achow101/psbt-util-rpcs
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	13987 ajtowns/201808-peerinfo-minfee
	# Needs review: 13989 add avx512 instrinsic
	# Needs work: 13990 WIP: allow fee estimation to work with lower fees
	# Needs rationale: 14019 Import pubkeys when importing p2sh with importmulti
	# Changes wallet? 14021 Import key origin data through importmulti
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	PARTIAL 14060 mruddy:zmqhwm
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs work: 14090 [windows] progress bar in task bar
# Non-upstreamed functionality:
m	-     restore_blockmaxsize					7b4ef75162
	7107 qtnetworkport							86a22ede93	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					821e79eca8  # Latest code now
	11082 rwconf-0.16							7ac8e5584d	last=aac0501148 rwconf
	7510 rwconf_gui-0.16+knots					f5d2f52fba	# Latest code now
	# Seems buggy: 13043 -													# [qt] OptionsDialog: add prune setting
	5916 keyorigin								6e769279fa
	 559 accept_nonstdtxn						f07335d45f
	 929 tbc									065b18ab4a
	 553 bugfix_qt_uri_amount_parser			99f0b1f4ca
	-    mining_priority-0.16					9a90dc34e7  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					525633a9d5
	5891 qt_console_history_persist				90c6f0a538
	7219 txrepl_fullrbf							a9fd5b6577
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						db079c9033
m	12146 opt_wallet_segwit2-0.16+knots			d855625b12	last=f5f5a922ba opt_wallet_segwit2
	n/a  checkpoint_update						a9c8a9ef4c
	# 0.17: Revert 12795
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				82becc9391
	-	 bytespersigopstrict+knots				fa99fdb901
	9749 unique_spk_mempool+knots				df8e9047db
m	-    rwconf_policy-0.16+knots				2786f6f8d6
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	-    txrepl_fullrbf_default+knots			f5c7ca2cd9	last=61fae13df1 txrepl_fullrbf_default
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.16+knots					2a4168de17
# BRANDING:
	n/a  knots_branding-0.16					ef04113ea1
#FIXME: Check Univalue 1.0.3 is sufficient to build
#	TODO: Check if any pushKV do booleans
#FIXME: Check includes use <>
#FIXME: allow building without libmemenv if the necessary code is in libleveldb
#FIXME: check libleveldb .20 ABI issues; runtime check we're linked to same version?
	n/a  (cherrypick=1a7c7b4b97ee6bd79c)		17c327ad76	# doc/{bips,files}
	n/a  (bump_version=Knots:20180730)			2f197b2b7b
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=08de50437e)				0a1f46883d  # release notes: write/update, including change log and credits
#ADD:  origin-pull/13043/head
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=6c11f79434)				11d53f8eb1  # translation update
	n/a  (cherrypick=fa03d8db65)				427450894c	# update manpages (build first)
# NOTE: use git diff --minimal for patches!
