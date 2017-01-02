timestamp 2017-01-02 11:34:42

checkout v0.13.2
@0.13.x-syslibs
	5872 subdir_incl_compat						1ac82ae
	2241 sys_leveldb							4e19700
	5416 sys_libsecp256k1						411cb7d
TM	8293 sys_univalue_opt						46effe2
	7485 sys_univalue_def						3432902
	7522 bugfix_gitdir							5960300
TM	8492 conf_only_bench						d456ee1
	5618 separate_utils							4a38db7
	7339 opt_libevent							a4b3d8a
@0.13.x-knots
TM	8784 license_build-0.13.x					7197b89
TM	8357 origin-pull/8357/head					b3e113b  # Fix relaypriority calculation error
TM	8845 pr8845-0.13							26543e2  # Don't return the address of a P2SH of a P2SH
# TESTS:
	-    travis_qt4_nolibevent					dc5d245
	7728 jtimon/0.12.99-feerate-precision-test	12f5496
# FUNCTIONALITY:
	 559 accept_nonstdtxn-0.13.x				ef78424
	 929 tbc									71afd77
	 553 bugfix_qt_uri_amount_parser			9372089
NM	1918 mempool_req							7b97686
	5861 gui_restore_addresses					beb0845
	8877 qt_console_history_filter-0.13knots	270bfd6	last=8562792
	5891 qt_console_history_persist				4c61f10	last=d8a8f1b jonas/2015/03/qt_console_update
	5916 keyorigin-0.13							96b7b0c
	6996 preciousblock							5902fe2	last=5805ac8
	#+9097a
	7061 jonas_rpc_rescan						7d87b7b last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							92af35b	last=1f37c87 origin-pull/7107/head
	7159 rpc_rbf-0.13.x							0cafb83	last=b64ebaf
	8601 walletrbf-knots-0.13.x					6b13c65
	7219 txrepl_fullrbf							c63acf8
m	7533 sendraw_force-0.13.x					b6519dd last=9eee2df
NM	7551 importmulti-old-0.13.x-knots			12d38d9	# holding back PR updates because upstream has been entirely redesigned
	7551 importmulti-0.13-knots					8557f0d last=215caba
	#+8980 Avoid using boost::variant::operator!=
		# not currently including 9108, but perhaps consider...
	7510 rwconf-0.13.x-knots					b3bcfbc
	8583 recog_node_xthin+txrepl_fullrbf		3d4710a
			# grab merged one by rebroad
	8456 bumpfee-0.13-knots						13daa89	last=2443193  # [RPC] Simplified bumpfee command. SEE ALSO bumpfee-0.13
	#+9168
	7948 bip9_softforks_since-0.13				4b0cc31  # RPC: augment getblockchaininfo bip9_softforks data
	8371 UI-out-of-sync-0.13					2cab2b2
	#+8805
	#+8821 marco/Mf1609-qtSyncReindex
	#+8985
	#+8906
	# TODO: +9218 (but needs networkactive first..)
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 pr8384-0.13							9f0194a	last=464c826
	8517 hd_gui-0.13							44062a8
	8610 sharemem-0.13							3928e18	last=ba3cecf
	8672 gui_tx_details_size-0.13				39c0dae	last=c015634  # Qt: Show transaction size in transaction details window
	-    trivial_blockmaxsize_mainnet_0.13		4079db4
	8918 gui_req_copy_uri						3b148fa
	8774 multiwallet_prefactor_qt				0059c3f
	8775 multiwallet_prefactor_rpc-0.13			436abe5	last=7de5573
	8776 multiwallet_prefactor_wallet-0.13		18f8d01	last=5394b39
	8694 multiwallet+hd_gui-0.13				9c10f29	last=d8da183
	8996 networkactive-0.13						bb936d1
	#+9130+9131+9145
	7785 qt_console_nested-0.13-knots			e944140
	#+9329
	# not ready? 7871 origin-pull/7871/head		         # Manual block file pruning.
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 getblock-extraverbose-0.13				27fe8d3						last=82a491f
	8450 rpctest_wallet_accts-0.13				9203c96
	8751 pr8751-sort-multisigs-0.13				4554fe2						last=7439562
	8813 daemonize-0.13							4a27b9d									last=a92bf4a
	8874 peer-multiselect-0.13					f465233							last=1077577  # Multiple Selection for peer and ban tables
	#+ part of 8085 531214f
	#+9255
	8448 dumpmempool-0.13						b91b5e1								last=582068a
		#+9133?
	8925 dbg_minping-0.13						698e5e0	# JUST adding min ping
	8936 misbehaving_nodeid-0.13				b1ed013
	8992 validatep2pkh-0.13 (C:930f3888a82)		3e0497d				last=981af93
	8952 listunspent_query-0.13					291f4f5							last=98d0a6f
	9025 getrawtx_bool-0.13						aa87308											# getrawtransaction should take a bool for verbose
	9152 sweepprivkeys-0.13-knots				55f1168						last=ed60474
	9222 fundrawtx_subfeefromamt-0.13			5b8e4c0					last=453bda6
	9245 ionice									30fefc9
	8501 stats_rpc-0.13							81634f7									last=b7c021d
	8550 stats_qt-0.13							d060966									last=251ee28
	n/a  checkpoint_update						219ac9b
# POLICY:
	7149 bugfix_priority-0.13.x					9883962	last=ae93a95  # TODO: check updates in morcos/dynamicPriority
m	-	 bytespersigopstrict-0.13.x-knots		b11e706	#last=6ae2e2d
	-    spamfilter+sendraw_force				c5d3284
a	-    rwconf_policy							8e2cfb0
# BRANDING:
m	7483 svg_icon								ac19e0b
	n/a  knots_branding							c30e154
	n/a  (bump_version=Knots:20170102)			5ad6763
	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=c912455f3f)				dd33592  # translation update (move after relnotes for 0.14?)
NM	8459 0.13_relnotes_remove_bad_advice		c2e2f38
TM	8490 relnotes_013_misc						f867fb5
	n/a  (cherrypick=4666564cb0)				ef9c66d  # release notes: write/update, including change log and credits
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
