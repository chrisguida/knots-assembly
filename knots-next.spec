timestamp 2017-01-20 18:22:35
lastapply no-merge

#.. checked up to PR #9671

checkout master
@0.14.x-syslibs
	5872 subdir_incl_compat						1ac82ae
	2241 sys_leveldb							4e19700
	5416 sys_libsecp256k1						411cb7d
	7485 sys_univalue_def						3432902
	7522 bugfix_gitdir							5960300
	5618 separate_utils							4a38db7
	7339 opt_libevent							a4b3d8a
	# FIXME: can 7339 be done for 0.14?
@0.14.x-knots
# TESTS:
	-    travis_qt4_nolibevent					dc5d245
	9359	# Add test for CWalletTx::GetImmatureCredit() returning stale values.
# FIXES:
	9481 jonas/2017/01/fee_warning
	9495 #JeremyRubin:checkqueue-control-lock
	9497 #JeremyRubin:checkqueue-tests
	9522 achow101/fix-decoderawtx
	9524 marco/Mf1701-qaPruning
	9549 #practicalswift:avoid-potential-null-pointer-dereference-in-markblockasinflight
	9578 matt/2017-01-fix-missing-wallet-mempool-lock
	9619 bugfix_gbt_presw
	9622 #kallewoof:listsinceblock-include-lost-txs
# FUNCTIONALITY:
	 559 accept_nonstdtxn-0.13.x				ef78424
	 929 tbc									71afd77
	 553 bugfix_qt_uri_amount_parser			9372089
	5861 gui_restore_addresses					beb0845
	5891 qt_console_history_persist				4c61f10	last=d8a8f1b jonas/2015/03/qt_console_update
	5916 keyorigin-0.13							96b7b0c
	7061 jonas_rpc_rescan						7d87b7b last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							92af35b	last=1f37c87 origin-pull/7107/head
	7159 rpc_rbf-0.13.x							0cafb83	last=b64ebaf
	7219 txrepl_fullrbf							c63acf8
m	7533 sendraw_force-0.13.x					b6519dd last=9eee2df
	7510 rwconf-0.13.x-knots					b3bcfbc
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 pr8384-0.13							9f0194a	last=464c826
	-    trivial_blockmaxsize_mainnet_0.13		4079db4 # FIXME: remove?
	8775 multiwallet_prefactor_rpc-0.13			436abe5	last=7de5573
	8694 multiwallet+hd_gui-0.13				9c10f29	last=d8da183
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 getblock-extraverbose-0.13				27fe8d3	last=82a491f
	8751 pr8751-sort-multisigs-0.13				4554fe2	last=7439562
	8992 validatep2pkh-0.13						3e0497d	last=981af93  # FIXME: replace with 9017?
	8952 listunspent_query-0.13					291f4f5	last=98d0a6f
	9152 sweepprivkeys-0.13-knots				55f1168	last=ed60474
	9245 ionice									30fefc9
	8501 stats_rpc-0.13							81634f7	last=b7c021d
	8550 stats_qt-0.13							d060966	last=251ee28
	9108 #ryanofsky:watchtime
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	# useless? 9402  # Allow per network configuration file
	9422 mempool_dat_extensible
	9500 achow101/help-rpc-autocomplete
	9503 #JeremyRubin:listreceivedbyaddress-filtered
	9504 achow101/dumpmasterprivkey
	9571  # RPC: getblockchaininfo returns BIP signaling statistics
	9592 #ryanofsky:pr/grbf
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	n/a  checkpoint_update						219ac9b
# POLICY:
	# maybe? 9527 ryanofsky:pr/walletrbf
	7149 bugfix_priority-0.13.x					9883962	last=ae93a95  # TODO: check updates in morcos/dynamicPriority
m	-	 bytespersigopstrict-0.13.x-knots		b11e706	#last=6ae2e2d
	-    spamfilter+sendraw_force				c5d3284
fx,a	-    rwconf_policy							8e2cfb0
		# FIXME: add walletrbf & maybe others?
# BRANDING:
m	7483 svg_icon								ac19e0b
	n/a  knots_branding							c30e154
	n/a  (bump_version=Knots:20170120)			5ad6763
	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=4666564cb0)				ef9c66d  # release notes: write/update, including change log and credits
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=c912455f3f)				dd33592  # translation update (move after relnotes for 0.14?)
