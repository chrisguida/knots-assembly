timestamp 2018-06-12 14:47:03
#lastapply no-merge

#.. checked up to PR #13452

checkout v0.16.1rc2
@0.16.x-syslibs
	5872 subdir_incl_compat						9ded41c3f3
	2241 sys_leveldb							5d340f9cc8
	5416 sys_libsecp256k1						efe5ca7511
	7485 sys_univalue_def						1b98117196
	5618 separate_utils_only					e1c13fbc60
	12246 separate_utils						9435351ece
	7339 opt_libevent-0.16						1f6a4c1b16
	11622 bip70_disable-0.16					7cbbf97899	last=7ecca66062
	? 13355 practicalswift:openbsd-gmake-check
@0.16.x-knots
# TESTS:
	13105 jamesob/2018-04-testrunner-failfast
	-    travis_nolibevent						b1459695b2
# FIXES:
	9524 marco/Mf1701-qaPruning					98b97a8e8a
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						de542996ff
	10731 log_more_uacomment					3963e0f61a
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	# ^ 11634 walletlocks-0.16						7914050bdb	last=491ec75b9f
		# held back annotations, and minimised patch
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
	12432 clear_all_coinctl-0.16				0c022c9a50	last=f506c0a7f8
	12479 rawmempool_spentby-0.16				052cf41f16	last=1dfb4e7d75  # RPC: Add child transactions to getrawmempool verbose output
	12491 fadvise-0.16							81e6159537	last=5259c72a76  # Try to use posix_fadvise with CBufferedFile
	12495 leveldb_max_open_files-0.16			1bb2e4277e	last=21e2144a31  # Increase LevelDB max_open_files on 64-bit POSIX systems
		# held back changes to developer doc file
	12501 text_customfee-0.16					31dc91ef25	last=0bc095efd8  # [qt] Improved "custom fee" explanation in tooltip
	12573 bugfix_no_clz-0.16					f22512d576  # Fix compilation when compiler do not support __builtin_clz*
	12617 laanwj/2018_03_gui_textbox
	12622 laanwj/2018_03_addrman_log_fixup
	12696 -													# Fix possible data race when committing block files
	# For 0.17: Revert #12723?
	PARTIAL: 12743 sipa:201803_waitblockchange
	12784 practicalswift/calc-error
	12793 MarcoFalke/Mf1803-qtReset0
	12859 incl_memory
		FIXME: maybe include this one in syslibs?
	13084 sipa/201804_keepnegone
	minimized 13120 MarcoFalke:Mf1805-segwitGenesisPolicy
	13149 practicalswift/fseek
	min-diff 13159 practicalswift/handle-reopen-failed
	13452 instagibbs/actuallyverifytxoutproof
# FUNCTIONALITY:
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.16					d998108784	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sort_multisigs			b7cfb4f153	last=127ec180bd sweepprivkeys
	12196 sweepprivkeys+scantxoutset			0bb54a08ab	last=3835de0da4 jonas/2017/12/utxo_sweep
	9245 ionice									ee401959ec
	-    ionice_win								1773e4c91c
	8501 old_stats_rpc-0.16						f1433a2ba2	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 stats_qt-0.16							ca7ace5acb	last=63fb11652f
		# NOTE: partial rebase at https://github.com/jonasschnelli/bitcoin/pull/9 ??? OLDER THAN CURRENT NOW
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					e168be5f70
	9991 listreceivedbyaddress-filtered+knots	4e96467f03	last=f087613719  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey-0.16					6d173c5fb5	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							e2fa8ef331
	11383 multiwallet_gui-0.16+knots			b319d6ca3d	last=f5aa574c37 multiwallet_gui
	10615 multiwallet_rpc						0713f29045
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10554 zmq_wtx-0.16							20f25e2a42	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					fd8db57b0e
	10593 relax_invblk_punishment				11759c2d01
	10594 whitelist_outgoing					bf1b027d2d
	10350 filtered_witblock-0.16				0c6010bf23	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								cb3bbbad7f
	10730 scriptflag_strings-mini				0365f306bb	last=97cae3915f
	n/a   script_debugger-mini					571378c9f0	last=1d3ed0c48a script_debugger
	# Needs work: 11200 achow101/gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				103772d8b9
	11256 rpc_mempoolentry_weight-0.16+knots	5c160d5a58	last=d4b0d81b58
	11413 explicit_fee-0.16						2176d12bd2	last=ff9f32eeac kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.16				908d7e8dbe	last=c23bd2892b
	11491 proxy_icon-0.16+knots					536d878e03	last=d4b6d92f53  # [gui] Add proxy icon in statusbar
		# NOTE: uses manual merge to avoid crazy conflict in svg_icon later
	11653 rpc_getsignaturehash+knots			cb1f212066	last=0a688c4f61 NicolasDorier/getsignaturehash
	11658 ibd_prune_extra						b344103db7
		# Consider replacing with 12404...
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	# Not ready: 11742 testmempoolaccept-0.16							last=faa03a6dad
		# test fails, RPC includes int instead of bool, etc
	11750 -										b95268b9b5 # Multiselect in coincontrol treewidget and display selected count
	11765 -										ca0e508d5b # [REST] added blockhash api, tests and documentation
	11770 rest_fee-0.16							3aeca1daea	last=935b364978  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			2b60c654de
	# 11872? MarcoFalke:Mf1712-rpcCreateRawSortedOuts (what's the use case?)
	12080 promag/2018-01-searchaddressbook		0b5a3f21dc
	12096 bumpfee_reduce_output-0.16			1a34df91aa	last=8430032df2 kallewoof/better-bumpfee
	12136 psbt-0.16								3b0ff8c589	last=85fbed49e6 achow101/psbt
	12208 gui_legacy_bech32						c43ed38811
		# merged as 13251
	12240 rpc_mempool_fees-0.16					d33e09676c	last=450ec6eed9  # [rpc] Introduced a new `fees` structure that aggregates all sub-field fee types denominated in BTC
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters
	12257 avoidpartialspends-0.16				3dd27638f6	last=a011e8bfdb kallewoof/feature-addrgrouped-coinselect
	12321 decodescript-p2wsh-0.16				2a90a5c300	last=4f933b3d23  # p2wsh and p2sh-p2wsh address in decodescript
	12421 send_to_txhistory-0.16				2987bef6f3
	12568 zero_dustrelayfee_opt					4382e57d64
	12580 gui_vsize-0.16						2bec130bb0
	12677 listunspent_ancestorinfo-0.16			7b9bcb392a	last=daeb431011 listunspent_ancestorinfo
	12559 promag/2018-02-avoid-cs_main-lock
	PART OF 12560 achow101:sethdseed
	MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	12616 promag/2018-03-modaloverlay
	12621 promag/2018-03-transaction-filter-avoid-querying
	12653 jonasschnelli/2018/03/blocksdir
	12676 dexX7/rpc-raw-replaceable-flag
	12705 kallewoof/importmulti-wif-support
	12763 JeremyRubin/whitelistrpc
	12769 ???
	12778 -													# RPC: Add username and ip logging for RPC method requests
	? 12783
	12791 TheBlueMatt/2018-03-weight
	? 12792 w/ renamed param
	12818 Sjors/2018/03/bump-fee-focus
	12854 desktop_categories
	12911 kallewoof/sign-show-fees
	12965 jonasschnelli/2018/04/svt
	ADD ONLY 13008 # rpc: Rename size to vsize in mempool related calls
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	13072 ajtowns/signmultisig
		FIXME: rename legacy to bip16
	13134 laanwj/2018_05_optional_bip61
	13151 laanwj/2018_05_direct_from_disk
	13152 chris-belcher/2018-04-rpc-getaddress
	13158 -													# [Qt]: Improve sendcoinsdialog readability
	13191 sipa/201709_dsha256_64
	13203 TheBlueMatt/2018-05-asm
	FIXME 13386 sipa/201806_shani
	13393 sipa/201806_dsha256_i386
	13442 sipa/201806_sse4intrin
	13310 promag/2018-05-replayblocks-progress
	13339 promag/2018-05-walletnotify
	minimised 13399 MarcoFalke/Mf1806-rpcBlockHeader
# Non-upstreamed functionality:
	-     restore_blockmaxsize					5498f1f3ee
		FIXME: revert 12756
	7107 qtnetworkport							645688ac3d	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					fd19c84489  # Latest code now
	11082 rwconf-0.16							ca7aa3dd0e	last=148c4ec24e rwconf
	7510 rwconf_gui-0.16+knots					908a4ef45a	# Latest code now
	13043 -													# [qt] OptionsDialog: add prune setting
	5916 keyorigin								fda5d449a6
	 559 accept_nonstdtxn						9e19784420
	 929 tbc									5110d02ef0
	 553 bugfix_qt_uri_amount_parser			dee1453a98
	-    mining_priority-0.16					948feb3a3b  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					1edc3fbb0f
	5891 qt_console_history_persist				4dd1e13804
	7219 txrepl_fullrbf							09e3ba7b94
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						ab29a63d68
	12146 opt_wallet_segwit2					e8acde8cf8
	n/a  checkpoint_update						5e7956fbf6
	# 0.17: Revert 12795
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				a7ebee1c57
	-	 bytespersigopstrict+knots				9ff9717fcb
	9749 unique_spk_mempool+knots				9ebbadca57
	-    rwconf_policy-0.16+knots				f1d39ca5a2
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	-    txrepl_fullrbf_default+knots			e044d3c789	last=61fae13df1 txrepl_fullrbf_default
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.16+knots					c22208def9
# BRANDING:
	n/a  knots_branding-0.16					df804fb452
FIXME: ADD Icon=bitcoinknots to desktop file
FIXME: Check Univalue 1.0.3 is sufficient to build
#FIXME: Check includes use <>
#TODO: Check if any pushKV do booleans
	n/a  (cherrypick=ff00b54211c29afc99)		a652129367	# doc/{bips,files}
	n/a  (bump_version=Knots:20180321)			4600612295
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=b264b31c28)				77dd0be080  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=d5e5bdbe2a)				6eccb37255  # translation update
	n/a  (cherrypick=477382f413)				23b1f768a9	# update manpages
# NOTE: use git diff --minimal for patches!
