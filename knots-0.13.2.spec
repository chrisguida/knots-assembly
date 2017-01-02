timestamp 2017-01-02 11:34:42

checkout v0.13.2
@0.13.x-syslibs
	5872 subdir_incl_compat						f0c1de4
	2241 sys_leveldb							496990c
	5416 sys_libsecp256k1						133b086
TM	8293 sys_univalue_opt						a7b532e
	7485 sys_univalue_def						aabc2c8
	7522 bugfix_gitdir							0074a4d
TM	8492 conf_only_bench						453630d
	5618 separate_utils							f903865
	7339 opt_libevent							f1a8ca8
@0.13.x-knots
TM	8784 license_build-0.13.x					d1e737f
TM	8357 origin-pull/8357/head					07f2180  # Fix relaypriority calculation error
TM	8845 pr8845-0.13							8bb0fe0  # Don't return the address of a P2SH of a P2SH
# TESTS:
	-    travis_qt4_nolibevent					54172df
	7728 jtimon/0.12.99-feerate-precision-test	23a5222
# FUNCTIONALITY:
	 559 accept_nonstdtxn-0.13.x				f809a4d
	 929 tbc									271c105
	 553 bugfix_qt_uri_amount_parser			2f73e59
NM	1918 mempool_req							3a08a55
	5861 gui_restore_addresses					35cde1a
	8877 qt_console_history_filter-0.13knots	fa0bf1e	last=8562792
	5891 qt_console_history_persist				a2b2278	last=d8a8f1b jonas/2015/03/qt_console_update
	5916 keyorigin-0.13							35b635a
	6996 preciousblock							6038b90	last=5805ac8
	#+9097a
	7061 jonas_rpc_rescan						2cc569b last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							8045526	last=1f37c87 origin-pull/7107/head
	7159 rpc_rbf-0.13.x							eabea64	last=b64ebaf
	8601 walletrbf-knots-0.13.x					52f96e7
	7219 txrepl_fullrbf							ba9acd8
m	7533 sendraw_force-0.13.x					f4c521f last=9eee2df
NM	7551 importmulti-old-0.13.x-knots			ccd9553	# holding back PR updates because upstream has been entirely redesigned
	7551 importmulti-0.13-knots					2d97bf2 last=215caba
	#+8980 Avoid using boost::variant::operator!=
		# not currently including 9108, but perhaps consider...
	7510 rwconf-0.13.x-knots					c7027be
	8583 recog_node_xthin+txrepl_fullrbf		fb8c93d
			# grab merged one by rebroad
	8456 bumpfee-0.13-knots						af3d812	last=2443193  # [RPC] Simplified bumpfee command. SEE ALSO bumpfee-0.13
	#+9168
	7948 bip9_softforks_since-0.13				1c2fb91  # RPC: augment getblockchaininfo bip9_softforks data
	8371 UI-out-of-sync-0.13					9c177ab
	#+8805
	#+8821 marco/Mf1609-qtSyncReindex
	#+8985
	#+8906
	# TODO: +9218 (but needs networkactive first..)
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 pr8384-0.13							f9c4385	last=464c826
	8517 hd_gui-0.13							80bdbb3
	8610 sharemem-0.13							c461df2	last=ba3cecf
	8672 gui_tx_details_size-0.13				03f7673	last=c015634  # Qt: Show transaction size in transaction details window
	-    trivial_blockmaxsize_mainnet_0.13		81ad58d
	8918 gui_req_copy_uri						c371b42
	8774 multiwallet_prefactor_qt				687899f
	8775 multiwallet_prefactor_rpc-0.13			3ea02b5	last=7de5573
	8776 multiwallet_prefactor_wallet-0.13		1a05c5b	last=5394b39
	8694 multiwallet+hd_gui-0.13				1df9a5f	last=d8da183
	8996 networkactive-0.13						0913a2b
	#+9130+9131+9145
	7785 qt_console_nested-0.13-knots
	#+9329
	# not ready? 7871 origin-pull/7871/head		         # Manual block file pruning.
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 getblock-extraverbose-0.13						last=82a491f
	8450 rpctest_wallet_accts-0.13
	8751 pr8751-sort-multisigs-0.13						last=7439562
	8813 daemonize-0.13									last=a92bf4a
	8874 peer-multiselect-0.13							last=1077577  # Multiple Selection for peer and ban tables
	#+ part of 8085 531214f
	#+9255
	8448 dumpmempool-0.13								last=582068a
		#+9133?
	8925 dbg_minping-0.13	# JUST adding min ping
	8936 misbehaving_nodeid-0.13
	8992 validatep2pkh-0.13 (C:930f3888a82)				last=981af93
	8952 listunspent_query-0.13							last=98d0a6f
	9025 getrawtx_bool-0.13											# getrawtransaction should take a bool for verbose
	9152 sweepprivkeys-0.13-knots						last=ed60474
	9222 fundrawtx_subfeefromamt-0.13					last=453bda6
	9245 ionice
	8501 stats_rpc-0.13									last=b7c021d
	8550 stats_qt-0.13									last=251ee28
	n/a  checkpoint_update						8f2e624
# POLICY:
	7149 bugfix_priority-0.13.x					e040cc5	last=ae93a95  # TODO: check updates in morcos/dynamicPriority
m	-	 bytespersigopstrict-0.13.x-knots		b6613a0	#last=6ae2e2d
	-    spamfilter+sendraw_force				438aee1
a	-    rwconf_policy							d7ea73c
# BRANDING:
m	7483 svg_icon								236fca5
	n/a  knots_branding							5909fb6
	n/a  (bump_version=Knots:20170102)			21e12b2
	n/a  knots_historical_relnotes				42bb8ed
	n/a  (cherrypick=c912455f3f)				f4772d6  # translation update (move after relnotes for 0.14?)
NM	8459 0.13_relnotes_remove_bad_advice		10f5f57
TM	8490 relnotes_013_misc						ce34853
	n/a  (cherrypick=4666564cb0)				45f61ea  # release notes: write/update, including change log and credits
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
