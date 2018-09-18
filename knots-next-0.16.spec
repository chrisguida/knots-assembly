timestamp 2018-09-18 02:14:17
#lastapply no-merge

#.. checked up to PR #13797
# NOTE: bugfix-only from 0.16.2

checkout v0.16.3
@0.16.x-syslibs
	5872 subdir_incl_compat						a632ff0b96
	2241 sys_leveldb-0.16						a381bb2d09
	5416 sys_libsecp256k1-0.16					4fe6450b57	last=c0abf31e2a sys_libsecp256k1
	7485 sys_univalue_def						e3e0daac59
	5618 separate_utils_only-0.16				88d4d7f6ef	last=68ec15e746 separate_utils_only
	12246 separate_utils-0.16					d83a7fa7f0	last=a2a04a5abb separate_utils
	7339 opt_libevent-0.16						80f0930bc6
	11622 bip70_disable-0.16					0f1f65821b	last=7ecca66062
TM	12859 incl_memory							3c90b5dbaf
	12854 desktop_categories					e794a0a754
	-     ppa_updates-0.16						d965837974
	13788 bugfix_asm_opt-0.16					9e0c520aae	last=4207c1b35c bugfix_asm_opt
	13789 bugfix_asm_pragmas-0.16				e9d7b36791	last=8bca9cd7ba bugfix_asm_pragmas
	-     bugfix_asm_leveldb_check-0.16			4a993bc52a
@0.16.x-knots
# TESTS:
	13105 test_failfast-0.16					7a1a8700c8
	-    travis_nolibevent						73a7bc4cc0
# FIXES:
	9524 marco/Mf1701-qaPruning					d8ef87a021
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						42c3220cfd
	10731 log_more_uacomment					bdb8873601
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	# ^ 11634 walletlocks-0.16						7914050bdb	last=491ec75b9f
		# held back annotations, and minimised patch
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
TM	12432 clear_all_coinctl-0.16				8efb063db0
	12479 rawmempool_spentby-0.16				f6af570302	last=1dfb4e7d75  # RPC: Add child transactions to getrawmempool verbose output
	12491 fadvise-0.16							2da7843a27	last=5259c72a76  # Try to use posix_fadvise with CBufferedFile
	12495 leveldb_max_open_files-0.16			c7528a92b8	last=ccedbafd73  # Increase LevelDB max_open_files on 64-bit POSIX systems
		# held back changes to developer doc file
	12501 text_customfee-0.16					3f7b41daaf	last=0bc095efd8  # [qt] Improved "custom fee" explanation in tooltip
TM	12573 bugfix_no_clz-0.16					a7a735a27d
TM	12617 2018_03_gui_textbox-0.16				ec6df1a484
	12696 eklitzke_fsync-0.16					a8509a39d5	last=4894e368fa  # Fix possible data race when committing block files
	# For 0.17: Revert #12723?
TM	12743 201803_waitblockchange-0.16			28074b7766
		# NOTE: held back variable renaming
TM	12793 fix_resetgui0-0.16					344910444a
	13084 fix_1neg-0.16							444674a0ce	last=5af7625079 sipa/201804_keepnegone
	# Requires 11739, which touches too much consensus logic: minimized 13120 MarcoFalke:Mf1805-segwitGenesisPolicy
	13149 check_fseek-0.16						bab8e1a529
	13159 handle-reopen-failed-0.16				769adc000c	last=37efe5b7ea practicalswift/handle-reopen-failed
		# minimised diff
TM	13452 actuallyverifytxoutproof-0.16			cb8a9549e4
NM	-     optimise_wallet_inv-0.16				f144cd9459
TM	13437 walletPrunedFundsSegfault-0.16		26fb5eb12f
TM	13545 bugfix_streams_test-0.16				b592dd7fe9
TM	13300 bugfix_qa_lockstack-0.16				ecc988b35b
TM	12887 bugfix_log_newlines-0.16				68656abffd
TM	13304 bugfix_wallet_listreceivedby_test-0.16	12622d9975
TM	13192 bugfix_p2p_sendheaders-0.16			d5576b230f
TM	13547 bugfix_signraw_amountcheck-0.16		ec64c8641f
	13608 bugfix_b-tx_amountcheck-0.15			14e161d278	last=876f49c6cd
TM	13655 bugfix_libcon_verify_invflags-0.16	205d789a9a
	# Needs review: 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
# FUNCTIONALITY:
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.16					77bdcebc53	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sort_multisigs			cdd8d1c9c9	last=127ec180bd sweepprivkeys
NM	12196 sweepprivkeys+scantxoutset			cb13b833ce
	12196 sweepprivkeys+scantxoutset			8bebb7aeb2	last=be98b2d9a8 jonas/2017/12/utxo_sweep
		# modified to remove scan-by-address garbage
		# held back feature removals
	9245 ionice									bc72040af9
	-    ionice_win								93823871a9
m	8501 old_stats_rpc-0.16						27aaf825c6	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 stats_qt-0.16							d3aaf0269d	last=63fb11652f
		# NOTE: partial rebase at https://github.com/jonasschnelli/bitcoin/pull/9 ??? OLDER THAN CURRENT NOW
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					b1d1c6a3e1
	9991 listreceivedbyaddress-filtered+knots	f59b48b1f2	last=f087613719  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey-0.16					4c94361b46	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							54c4a8f548
	11383 multiwallet_gui-0.16+knots			0835dd4b12	last=f5aa574c37 multiwallet_gui
	10615 multiwallet_rpc						c8fc973305
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10554 zmq_wtx-0.16							fd748f076c	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					e0725d981e
	10593 relax_invblk_punishment				f0dce18f42
	10594 whitelist_outgoing					62cbb14e71
	10350 filtered_witblock-0.16				9acbe3cf0d	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								20629bd839
m	10730 scriptflag_strings-mini-0.16			33586b67cd	last=e2e183bc1f
	n/a   script_debugger-mini					3abe2c81b6	last=1d3ed0c48a script_debugger
	# Needs work: 11200 achow101/gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				15eebb667c
m	11256 rpc_mempoolentry_weight-0.16+knots	d4ce3f9962	last=d4b0d81b58
	11413 explicit_fee-0.16						9751deecd5	last=628f6e971a kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.16				e46cdbf830	last=c23bd2892b
	11491 proxy_icon-0.16+knots					d0fbcd605f	last=73cd5b25b9  # [gui] Add proxy icon in statusbar
		# NOTE: uses manual merge to avoid crazy conflict in svg_icon later
		# NOTE: held back meaningless changes to pixmap/icon init
	11653 rpc_getsignaturehash+knots			51d790fac6	last=0a688c4f61 NicolasDorier/getsignaturehash
	11658 ibd_prune_extra						e966a1639a
		# Consider replacing with 12404...
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	# Not ready: 11742 testmempoolaccept-0.16							last=faa03a6dad
		# test fails, RPC includes int instead of bool, etc
	11750 -										600d8c7566 # Multiselect in coincontrol treewidget and display selected count
	11765 rest-blockhash-endpoint-0.16			fcdb84a37b	last=1323df9ff1 # [REST] added blockhash api, tests and documentation
	11770 rest_fee-0.16							46d0f306b8	last=935b364978  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath-0.16		3296f5b095	last=393511cb22 bugfix_dumpwallet_hdkeypath
	# 11872? MarcoFalke:Mf1712-rpcCreateRawSortedOuts (what's the use case?)
	12080 promag/2018-01-searchaddressbook		cf2ab47420
	12096 bumpfee_reduce_output-0.16			23fff1e3d8	last=51826d4de0 kallewoof/better-bumpfee
NM	12136 psbt-0.16								dcf16aad0c	#last=950746725a achow101/psbt
TM	13251 gui_legacy_bech32-0.16				f95dc3a45a
m	12240 rpc_mempool_fees-0.16					925fe05236	last=7de1de7da4  # [rpc] Introduced a new `fees` structure that aggregates all sub-field fee types denominated in BTC
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters
	12257 avoidpartialspends-0.16				36617b1a8d	last=452485e1b7 kallewoof/feature-addrgrouped-coinselect
		# NOTE: held back af586af9f0..452485e1b7
	12321 decodescript-p2wsh-0.16				9a8a56d5f0	last=41ff9675a9  # p2wsh and p2sh-p2wsh address in decodescript
	12421 send_to_txhistory-0.16				7fe01ac816
	12568 zero_dustrelayfee_opt					702d205844
	12580 gui_vsize-0.16						3cd82a65fe
	12677 listunspent_ancestorinfo-0.16			541e34ad19	last=daeb431011 listunspent_ancestorinfo
	# Not sure if safe with 0.16: 12559 promag/2018-02-avoid-cs_main-lock
	# Too dangerous. PART OF 12560 achow101:sethdseed
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	12616 modaloverlay-hide-default-0.16		a1714a416d
	12621 gui_txfilter_optimise-0.16			5d3f3573d1
	12653 blocksdir-0.16						28d322382c
	12676 rawmempool_bip125-0.16+knots			cf1cb9d8d5	last=870bd4c73d
		# NOTE: rewritten
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.16						7c13747cb9	last=8c45d93b0e
	# 12769 ???
	12778 rpc_loguser-0.16+knots				c875f38cf8
	12783 disable_appnap-0.16					2803ff3458	#HACK last=33a25f1e02
		# Retained older inhibitor too
	12791 rpc_tx_weight-0.16					e61504cc4a
	# TODO ? 12792 w/ renamed param
	12818 gui_feebump_select-0.16				0cb03752d4	last=d795c610d3
	12911 signrawtx_showfees-0.16				4c86763e21	last=b7159aa585 kallewoof/sign-show-fees
	12965 scriptthreads-0.16+knots				d9f3ff4fa7	last=dfab6c6866 jonas/2018/04/svt
	# TODO ADD ONLY 13008 # rpc: Rename size to vsize in mempool related calls
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Needs fixes: 13072 ajtowns/signmultisig
		#FIXME: rename legacy to bip16
	13134 optional_bip61-0.16					8b7df6609c
	13151 direct_from_disk-0.16+knots			c8bec86df6
	# Test fails: 13152 rpc_getnodeaddress-0.16							last=f10e380630
	13158 gui_send_readability-0.16				6601b96eb6
m	13191 dsha256_64-0.16+knots					59e1ab2a07
		# Includes 13611
	13393 dsha256_i386-0.16						f7b705d4da
	13471 avxossupport-0.16						a2f83bbe18
	13408 dsha256_cleanup-0.16+knots			47ab9430a8
	13438 dsha256_selftest-0.16					7ce61c43b6
m	13386 dsha256_shani-0.16+knots				30279bf9a1	last=66b2cf1ccf sipa/201806_shani
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
m	13203 dsha256_power8-0.16+knots				761d937bef	last=3b402e0738 matt/2018-05-asm
	-     bugfix_asm_opt_and_pragmas-0.16+knots	478a47682e
	# TODO: Possible performance concern 13310 promag/2018-05-replayblocks-progress
	13339 walletnotify_w-0.16					a2b75f149f	last=cef0327afd promag/2018-05-walletnotify
	# broken? 13399 rpc_submitheader-0.16								last=fa7d7dd34c marco/Mf1806-rpcBlockHeader
		# held back removal of duplicate-header submission check
	13537 gui_peertable_inout-0.10				81b106f0fd
	# Needs work: 13541 wallet/rpc: sendrawtransaction maxfeerate
	13570 rpc_getzmqnotifications-0.16+knots	cb20c70031
	# Needs review: 13666 Always create signatures with Low R values
	# Needs work: 13697 Support output descriptors in scantxoutset
	# Needs work: 13756 wallet: -avoidreuse feature for improved privacy
	# Needs review: 13791 gui: Reject EditAddressDialog on ESC key
# Non-upstreamed functionality:
m	-     restore_blockmaxsize					3c93f4dc89
	7107 qtnetworkport							2a436e1b83	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					ff30462276  # Latest code now
	11082 rwconf-0.16							07cb02f711	last=aac0501148 rwconf
	7510 rwconf_gui-0.16+knots					5781d01d4f	# Latest code now
	# Seems buggy: 13043 -													# [qt] OptionsDialog: add prune setting
	5916 keyorigin								2932f8de6b
	 559 accept_nonstdtxn						ffdbf839f2
	 929 tbc									b2699c1cf1
	 553 bugfix_qt_uri_amount_parser			4baa3a41d2
	-    mining_priority-0.16					98b6d17cb3  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					1fa57eb4a8
	5891 qt_console_history_persist				0575a03a4a
	7219 txrepl_fullrbf							d8de6817f8
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						c8edb8b928
m	12146 opt_wallet_segwit2-0.16+knots			037a6cb3f5	last=f5f5a922ba opt_wallet_segwit2
	n/a  checkpoint_update						083cae59dc
	# 0.17: Revert 12795
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				f4e1c56d1e
	-	 bytespersigopstrict+knots				0eb6904961
	9749 unique_spk_mempool+knots				390cd30daa
m	-    rwconf_policy-0.16+knots				87955aa11b
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	-    txrepl_fullrbf_default+knots			e84dbaf595	last=61fae13df1 txrepl_fullrbf_default
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.16+knots					9dec041ff5
# BRANDING:
	n/a  knots_branding-0.16					7ee14a32bc
#FIXME: Check Univalue 1.0.3 is sufficient to build
#	TODO: Check if any pushKV do booleans
#FIXME: Check includes use <>
#FIXME: allow building without libmemenv if the necessary code is in libleveldb
#FIXME: check libleveldb .20 ABI issues; runtime check we're linked to same version?
	n/a  (cherrypick=1a7c7b4b97ee6bd79c)		4afbdab073	# doc/{bips,files}
	n/a  (bump_version=Knots:20180730)			a9750c353a
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=e1a7851f53)				d396c33814  # release notes: write/update, including change log and credits
#ADD:  origin-pull/13043/head
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=7c52ff6a4e)				94a29dbe8a  # translation update
	n/a  (cherrypick=5d87f5b380)				65e076f0e1	# update manpages (build first)
# NOTE: use git diff --minimal for patches!
