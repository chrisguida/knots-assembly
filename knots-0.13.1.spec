timestamp 2016-10-27 08:26:07

checkout v0.13.1
@0.13.x-syslibs
	5872 subdir_incl_compat						dbbf960
	2241 sys_leveldb							1af238f
	5416 sys_libsecp256k1						6c8932f
TM	8293 sys_univalue_opt						b96f99f
	7485 sys_univalue_def						0caaddb
	7522 bugfix_gitdir							e27eec3
TM	8492 conf_only_bench						f532bf1
	5618 separate_utils							a438aaf
	7339 opt_libevent							ac98ecd
@0.13.x-knots
	8784 license_build-0.13.x
	8357 origin-pull/8357/head							# Fix relaypriority calculation error
	8845 pr8845-0.13  # Don't return the address of a P2SH of a P2SH
# TESTS:
	-    travis_qt4_nolibevent					23f4b5c
	7728 jtimon/0.12.99-feerate-precision-test
# FUNCTIONALITY:
	 559 accept_nonstdtxn-0.13.x				8350bf0
	 929 tbc									e76cdfc
	 553 bugfix_qt_uri_amount_parser			daf7ea0
NM	1918 mempool_req							ef56cf7
	5861 gui_restore_addresses					af1e94d
	8877 qt_console_history_filter
m	5891 qt_console_history_persist				48813e2	last=d8a8f1b jonasschnelli/2015/03/qt_console_update
	5916 keyorigin-0.13							81857a0
	6996 preciousblock							c22f014	last=5805ac8
	7061 jonas_rpc_rescan						67870be last=d1aa8a9 jonasschnelli/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							1585f8a	last=1f37c87 origin-pull/7107/head
	7159 rpc_rbf-0.13.x							d0163a6	last=b64ebaf
	8601 walletrbf-knots-0.13.x					7fdb4e6
	7219 txrepl_fullrbf							2540acc
m	7533 sendraw_force-0.13.x					d654b65
NM	7551 importmulti-old-0.13.x-knots			e74933f	# holding back PR updates because upstream has been entirely redesigned
	7551 importmulti-0.13-knots
	#+8980 Avoid using boost::variant::operator!=
	7510 rwconf-0.13.x-knots					a087e2e
	8583 recog_node_xthin+txrepl_fullrbf		0747907
			# grab merged one by rebroad
	# breaks history filter: 7783 qt_console_nested-0.13
	8456 bumpfee-0.13									last=8e969e3  # [RPC] Simplified bumpfee command.
	# needs string cleanup: 8182 jonasschnelli/2016/04/qt_rbf_set_new
	7948 bip9_softforks_since-0.13						# RPC: augment getblockchaininfo bip9_softforks data
	8371 UI-out-of-sync-0.13
	#+8805
	#+8821 MarcoFalke/Mf1609-qtSyncReindex
	# not ready: 8889 overlay_theme
	# needs de-blobbing: 8550 jonasschnelli/2016/08/stats_qt
	8384 pr8384-0.13
	# not ready? 7871 origin-pull/7871/head							# Manual block file pruning.
	# needs UI improvements!? 7949 jonasschnelli/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	# untested: 8501 jonasschnelli/2016/08/stats_rpc
	8517 hd_gui-0.13
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8610 sharemem-0.13									last=27562ef
	8672 gui_tx_details_size-0.13						last=c015634  # Qt: Show transaction size in transaction details window
	# poisoned and could use work: 8704 achow101/getblock-extraverbose
	# poisoned: 8751 afk11/sort-multisigs
	-    trivial_blockmaxsize_mainnet_0.13		9bf79a8
	# poisoned: 8813 laanwj/2016_09_daemonize
	# poisoned: 8817 # update bitcoin-tx to output witness data
	#BROKEN: 8874 peer-multiselect-0.13							last=db74962  # Multiple Selection for peer and ban tables
		#+ part of 8085 531214f
	# needs work... no automatic interval flush: 8448 sipa/dumpmempool  # FIXME
	8918 gui_req_copy_uri
	8774 multiwallet_prefactor_qt
	8775 multiwallet_prefactor_rpc-0.13 #(or 8788)
	8776 multiwallet_prefactor_wallet-0.13
	8694 multiwallet+hd_gui-0.13
	8996 networkactive-0.13
	n/a  checkpoint_update						78bb209
# POLICY:
	7149 bugfix_priority-0.13.x					c1d358a	# TODO: check updates in morcos/dynamicPriority
m	-	 bytespersigopstrict-0.13.x-knots		fa08c39
	-    spamfilter+sendraw_force				9088e2e
	-    rwconf_policy							5c66cc1
# BRANDING:
	7483 svg_icon								f8bf558
	n/a  knots_branding							2cbf3a7
	n/a  (bump_version=Knots:20161027)			2056654
	n/a  knots_historical_relnotes				7bfd301
	n/a  (cherrypick=f206cd3bc8)				548c39d  # translation update
NM	8459 0.13_relnotes_remove_bad_advice		ac229eb
TM	8490 relnotes_013_misc						033988b
	n/a  (cherrypick=c081e487c6)				c372395  # release notes: write/update, including change log and credits
		# remove asterisk in changelog for what's been merged last-minute
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
