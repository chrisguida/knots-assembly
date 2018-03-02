timestamp 2018-02-24 20:14:58
lastapply no-merge

#.. checked up to PR #12558

checkout v0.16.0
@0.16.x-syslibs
	5872 subdir_incl_compat						fc9f50d046
	2241 sys_leveldb							e3ab3ceb16
	5416 sys_libsecp256k1						1d38d78d4f
	7485 sys_univalue_def						027bc28176
	5618 separate_utils_only					9d3b7993ba
	12246 separate_utils
	7339 opt_libevent-0.16						e7e2488213
	11622 bip70_disable-0.16					5dbcd1a73d	last=7ecca66062
@0.16.x-knots
# TESTS:
	-    travis_nolibevent						2f096f65f4
# FIXES:
	9524 marco/Mf1701-qaPruning					8d37c7a0bb
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						b62c04406f
	10731 log_more_uacomment					9104b40f1d
	11596 chainactive_locking-0.16				c949b13d71	last=f122e02eaf
	11634 walletlocks-0.16						7914050bdb	last=fca14f6c8d
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
	12432 clear_all_coinctl-0.16							last=f506c0a7f8
	12479 rawmempool_spentby-0.16							last=1dfb4e7d75  # RPC: Add child transactions to getrawmempool verbose output
	12491 fadvise-0.16										last=5259c72a76  # Try to use posix_fadvise with CBufferedFile
	12495 leveldb_max_open_files-0.16						last=f4659ab250  # Increase LevelDB max_open_files on 64-bit POSIX systems
	12501 text_customfee-0.16								last=0bc095efd8  # [qt] Improved "custom fee" explanation in tooltip
# FUNCTIONALITY:
	-     restore_blockmaxsize					64a04dbf61
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.16					df6cffed47	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# FIXME REGRESSION: 11089 p2shp2wpkhstuff						f36a9fcfab  # replacing 8992, 9017; removed sign/verify message stuff
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys-0.15						435a063f0e	last=a397deb247
	12196 sweepprivkeys+scantxoutset						last=2c006f558b jonas/2017/12/utxo_sweep
	9245 ionice									63041adffd
	-    ionice_win								9df27e8828
	8501 old_stats_rpc							828af4e879	last=7af0ea43b2
		# Held back on old version due to lack of GUI updates
	8550 old_stats_qt							47ef592135	last=251ee28
		# NOTE: partial rebase at https://github.com/jonasschnelli/bitcoin/pull/9
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					140852f1a6
	9991 listreceivedbyaddress-filtered			f8598965c4	last=c262be5  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey-0.15					0b370e9ac7	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							239afe1d1e
	10615 multiwallet_rpc+opt_libevent			f0e200c20f	last=370d3361e8
	11383 multiwallet_gui-0.15+knots			cbaf625196	last=6445a935e6 multiwallet_gui
		# holding back from 7790bcdbf2..6445a935e6: callback refactor (stash 2116665f95), wallet selector comment
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10554 zmq_wtx								5316e0003c	last=ed4fd266f7	# ZMQ: add publishers for wallet transactions.
	10593 relax_invblk_punishment-0.15			ee052bf276	last=c36864368a relax_invblk_punishment
	10594 whitelist_outgoing-0.15				ede93391aa	last=416f9b9541 whitelist_outgoing
	10350 filtered_witblock-0.15				ee55b7d144	last=3f388ddcd3 codeshark/MFWB_no_bump_2
	10729 scriptex								7ece29590e
	10730 scriptflag_strings-mini				b828bc08be	last=97cae3915f
	n/a   script_debugger-mini					b13b502e4e	last=1d3ed0c48a script_debugger
	11200 achow101/gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				a2c58f6cb9
	11256 rpc_mempoolentry_weight-0.15+knots	0ae7920df4	last=d4b0d81b58
	11413 kallewoof/explicit-fee							# [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.10				7c64ef38db	last=a0102314df
	11491 -													# [gui] Add proxy icon in statusbar
	11653 rpc_getsignaturehash-0.15+knots		6bc34f035c	last=0a688c4f61
	11658 ibd_prune_extra						f7eb8d892c
		# Consider replacing with 12404...
	11666 NicolasDorier/signinput
	11708?
	11742 MarcoFalke/Mf1711-rpcMempoolAcceptOne
	11750 - # Multiselect in coincontrol treewidget and display selected count
	11765 - # [REST] added blockhash api, tests and documentation
	11770 - # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath
	# 11872? MarcoFalke:Mf1712-rpcCreateRawSortedOuts (what's the use case?)
	11937? - # Qt: Setting for deciding address type (legacy, p2sh or bech32)
	12080 promag/2018-01-searchaddressbook
	12096 kallewoof/better-bumpfee
	12136 achow101/psbt
	12208 gui_legacy_bech32
	12240 - # [rpc] Introduced a new `fees` structure that aggregates all sub-field fee types denominated in BTC
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters
	12257 avoidpartialspends-0.16						last=cf9df64071 kallewoof/feature-addrgrouped-coinselect
	12321 - # p2wsh and p2sh-p2wsh address in decodescript
	12421 Sjors/2018/02/qt-goto-transactions-after-send
	12568 zero_dustrelayfee_opt
	12580 -
# Non-upstreamed functionality:
	7107 qtnetworkport							c94d8a6dd7	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					12cfec6d9d	last=89e516ffcb sendraw_force
	11082 rwconf-0.15							e91bf830e6	last=59d78f9fc1 rwconf
	7510 rwconf_gui-0.15+qtnetworkport			2f5d4369d0	last=87f7d1f455 rwconf_gui-0.15
	5916 keyorigin								c5f583dfdc
	 559 accept_nonstdtxn						1243d2838c
	 929 tbc									d84d257f1c
	 553 bugfix_qt_uri_amount_parser			d7f460d856
	-    mining_priority-0.15					5db805e1ee	last=9837927654 mining_priority
	5861 gui_restore_addresses					f63829b67c
	5891 qt_console_history_persist-0.15		c5df60c17f	last=d5046701e0 qt_console_history_persist
	7219 txrepl_fullrbf							333528ea38
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots-0.15					647f952869	last=21f123db98
	12146 opt_wallet_segwit2
	n/a  checkpoint_update						106849c664
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget
	-	 bytespersigopstrict+sendraw_force		0b671f305d
	9749 unique_spk_mempool+sendraw_force		c2cabb6288	last=9b75ab5b39
	-    rwconf_policy							c45bdb9b2a
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								d4266f2cc2
# BRANDING:
	n/a  knots_branding							b31017ae44
	n/a  (cherrypick=af9c353c0dd6012e91)		3921a4b3cc	# doc/{bips,files}
	n/a  (bump_version=Knots:20180224)			3e23b17b68
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=38ee93d976)				b0dc9e2e3e  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=e82aca5f8c)				89aa6c3923  # translation update
	n/a  (cherrypick=8d8e7db1ab)				4c3f4e6fed	# update manpages
# NOTE: use git diff --minimal for patches!
