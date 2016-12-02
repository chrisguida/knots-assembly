timestamp 2016-10-27 08:26:07

checkout origin/0.13
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
	8877 qt_console_history_filter-0.13knots	fa0bf1e	last=5c7fc22
m	5891 qt_console_history_persist				a2b2278	last=d8a8f1b jonas/2015/03/qt_console_update
	5916 keyorigin-0.13							35b635a
	6996 preciousblock							6038b90	last=5805ac8
	7061 jonas_rpc_rescan						2cc569b last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							8045526	last=1f37c87 origin-pull/7107/head
	7159 rpc_rbf-0.13.x							eabea64	last=b64ebaf
	8601 walletrbf-knots-0.13.x					52f96e7
	7219 txrepl_fullrbf							ba9acd8
m	7533 sendraw_force-0.13.x					f4c521f last=4b32b8b
NM	7551 importmulti-old-0.13.x-knots			ccd9553	# holding back PR updates because upstream has been entirely redesigned
	7551 importmulti-0.13-knots					2d97bf2 last=215caba
	#+8980 Avoid using boost::variant::operator!=
	7510 rwconf-0.13.x-knots					c7027be
	8583 recog_node_xthin+txrepl_fullrbf		fb8c93d
			# grab merged one by rebroad
	8456 bumpfee-0.13							af3d812	last=a0b7e34  # [RPC] Simplified bumpfee command.
	7948 bip9_softforks_since-0.13				1c2fb91  # RPC: augment getblockchaininfo bip9_softforks data
	8371 UI-out-of-sync-0.13					9c177ab
	#+8805
	#+8821 marco/Mf1609-qtSyncReindex
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 pr8384-0.13							f9c4385	last=464c826
	8517 hd_gui-0.13							80bdbb3
	8610 sharemem-0.13							c461df2	last=27562ef
	8672 gui_tx_details_size-0.13				03f7673	last=c015634  # Qt: Show transaction size in transaction details window
	-    trivial_blockmaxsize_mainnet_0.13		81ad58d
	8918 gui_req_copy_uri						c371b42
	8774 multiwallet_prefactor_qt				687899f
	8775 multiwallet_prefactor_rpc-0.13			3ea02b5	last=d6bc295
	8776 multiwallet_prefactor_wallet-0.13		1a05c5b	last=5394b39
	8694 multiwallet+hd_gui-0.13				1df9a5f	last=e54fc75
FX	8996 networkactive-0.13						0913a2b  # upstream bugfixes
	7785 qt_console_nested-0.13
	# not ready? 7871 origin-pull/7871/head		         # Manual block file pruning.
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 getblock-extraverbose-0.13						last=ad8fc81
	8751 afk11/sort-multisigs
	8813 laanwj/2016_09_daemonize
	8817 # update bitcoin-tx to output witness data
	8874 peer-multiselect-0.13							last=db74962  # Multiple Selection for peer and ban tables
		#+ part of 8085 531214f
	8448 sipa/dumpmempool
	8501 stats_rpc-0.13									last=5722e27
	# needs de-blobbing: 8550 jonas/2016/08/stats_qt
FX	n/a  checkpoint_update						8f2e624
# POLICY:
	7149 bugfix_priority-0.13.x					e040cc5	last=887fc24  # TODO: check updates in morcos/dynamicPriority
m	-	 bytespersigopstrict-0.13.x-knots		b6613a0	#last=6ae2e2d
	-    spamfilter+sendraw_force				438aee1
	-    rwconf_policy							d7ea73c
# BRANDING:
	7483 svg_icon								236fca5
	n/a  knots_branding							5909fb6
	n/a  (bump_version=Knots:20161027)			21e12b2
	n/a  knots_historical_relnotes				42bb8ed
	n/a  (cherrypick=f206cd3bc8)				f4772d6  # translation update
NM	8459 0.13_relnotes_remove_bad_advice		10f5f57
TM	8490 relnotes_013_misc						ce34853
	n/a  (cherrypick=c081e487c6)				45f61ea  # release notes: write/update, including change log and credits
		# UPDATE doc/files.md versions!
		# remove asterisk in changelog for what's been merged last-minute
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
