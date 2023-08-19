timestamp 2023-08-19 08:27:30
#lastapply no-merge

#.. checked up to PR #22369 / gui #375 for features
#.. checked up to PR #28296 / gui #749 for fixes
TODO: Still need to look at PRs merged from #26649/gui#684 until #27489/gui#723 for fixes: is:pr is:merged created:<2023-04-19

TODO: Make sure latest branches are checked in here

checkout v0.21.2
@21.x-syslibs
# BUILD BUGS:
	21882 fuzz32_llvm_workaround-0.21+knots		d83d545d869	last=e4c8bb62e4a hebasto/210507-fuzz32
	20938 configure_latomic_checks-0.14^		5ad9c951c3c
	21920 configure_latomic_checks-0.14			b155f1d63f9
	# Not needed (depends only): 22380 fanquake/set_std_c_version_depends
	22390 netbsd_dont_set_locale-0.20			a6bf704ecb8
	# Needs review: 23030 -  # src/randomenv.cpp: fix uclibc build
	# OR: 23082 fanquake/remove_weak_auxval
	23045 fix_crc32c_arm64_detect-0.20			874c19af6f6	last=f2747d1602e laanwj/2021-09-arm64-crc32
	23182 py3_9t11-0.21							9a47c189d43	last=e11c21c8454 py3_10o11-22
		# +#23317
	23314 disable_s2561k_openssl_test-0.21		1c1ec16b46a	last=8031de63b5a disable_s2561k_openssl_test-22
	23345 wallettool_drop_extra_deps-0.21+knots	2d9930b2a36	last=4fe7cf16779 hebasto/211024-bw-deps
		# Dropped MSVC changes
		# BUILD_LEVELDB becomes EMBEDDED_LEVELDB for v21.x+v22.x
		# Held back 347774b86c8...4fe7cf16779 removal of embedded leveldb conditional (might have worked better with sys_leveldb, but oh well)
		# Fixed silent conflicts (bitcoin-util & natpmp not supported by 21.x)
	24051 config_utils_drop_extra_deps-21+knots				last=98868633d1d config_utils_drop_extra_deps
	22348 workaround_boost_issue96-21			db54924736a	last=67669ab425b hebasto/210627-boost
	24523 boost1.78_workaround_narrowing-21
		# NOTE: Was #24415 (never in Knots)
	23607 evhttp_connection_get_peer_compat-21	a5d963d4635	last=c62d763fc31  # evhttp_connection_get_peer compatibility with possible-future libevent
	# Needs review: 23609 hebasto/211126-reduce
	21421 skip_stack_clash_windows-21
	23335 origin-pull/25318/head^							last=efb9f00f07c origin-pull/25318/head  # include a missing <limits> header in fs.cpp
	23947 config_summary_host_os-21
	24104 boost1.78_fs_compat-21
	24240 fix_capnp_fetch-21
	# Not really needed: 24277 hebasto/220206-deploy
	# Not needed: 2af9be1f1a4 build: Remove hexdump and libboost-test-dev dependencies when --enable-fuzz
		# NOTE: Inspired by first revision of #24291
	24633 bugfix_suppresswarnings_regex
	# NOTE: WRONG FOR C++11: 25436 fanquake/libxkbcommon_gcc_12
	25605 dmg_tools_new_paths_pr25605-0.17					last=718d29af233 fanquake/dmg_tools_new_paths
	# Needs review: 25612 fanquake/lto_improvements
	25852 fix_intrinsic_check_userflags-0.20+k
	Check if needed and useful: 26086 fanquake/bitcoin_tx_prune_boost_cpp
	# Triage: If needed (MSVC only?): 27892 MarcoFalke/2306-translate-copy-
# SYSLIBS: (and old build bugs)
	5872  subdir_incl_compat-0.10				9815be994a1	last=1490995c122 subdir_incl_compat
	2241  sys_leveldb-21+knots					60cd0a8e2fb	last=1c6ae96f0a3 sys_leveldb
	(CHECK-LAST)	last=bd02e19eaf5 sys_leveldb-22+knots
	(CHECK-LAST)	last=e02626bf8e0 sys_leveldb-23+knots
	5416  sys_libsecp256k1-0.21+knots			813a5353e1d	last=6d7f62dca81 sys_libsecp256k1
	(CHECK-LAST)	last=da31940ec9e sys_libsecp256k1-23+knots
	n/a   sys_univalue_doc-21								last=77c4f3e3af9 sys_univalue-23+knots
m	7485  sys_univalue_def-21					c393c7a7f51	last=cf9e588e22f sys_univalue_def-23+knots
	13789 bugfix_asm_pragmas-21+knots			e33b0f86575 last=4edfd1e0d6c bugfix_asm_pragmas
TM	-     bugfix_asm_leveldb_check-0.20			15cb5704a2a	last=3ca799db25f bugfix_asm_leveldb_check
	15155 test_external_bcli-21					3385d2476a3	last=06ec7f56dfb test_external_bcli
	20202 opt_bdb-0.21							4c0c81adb3a
		# +#20458+#20267
		# Omitted default-tests-to-descriptors-when-bdb-not-compiled: a2282b44a4d 373158bc44c
		# Omitted "Don't make any wallets unless wallet is required": 45b4366f8ff 104a3a22564 6e06ca05880
		# Diff-minimised
	-     opt_bdb_extracare-0.21				65ea0f5ab4e	last=aa6a707d7ca opt_bdb_extracare
		#21.xTODO# should this get promoted to non-experimental now that it's considered stable in 23.x?
	20121 secp256k1_allow_bignum-21+knots		b2befc7fef1
	20358 -										3e3443170a8	last=330cb33985d  # src/randomenv.cpp: fix build on uclibc
	20594 conf_getauxval-0.21					563aacf22be	last=836a3dc02c7 jonasschnelli/2020/12/getauxval
	#Maybe restore: 7339  opt_libevent
	23716 qa_own_ripemd160-21					a93adb92909
		# NOTE: Identical backport in #25538 now
	# TODO?? Qt6 support
	# OpenBSD-only: 25332 fanquake/test_for_timingsafe_bcmp
	n/a   (delete_release_notes_fragments)
@21.x-knotsfixes
# TESTS:
TM	22279 fix_fuzz_baseencdec_pr22279-0.21		0c8d22592f5
TM	22002 fix_fuzz_system_pr22002-0.21			4fd9b177451
TM	22137 fix_fuzz_system_pr22137-0.21			b774212bc52
	-     lint_relaxer-0.21						8bfe42fe606	last=be7776a0ed6 lint_relaxer
		# Held back unnecessary d4d8eb13cbb...be7776a0ed6
	17402 travis_ppc64							3f88efab27c	last=1d684f05341 elichai/2019-11-powerpc64
	21785 fix_intrmttnt_qa_p2p_addr_relay-0.20	4a97d761fcc
	# TODO? 25123 fjahr/202205-index-prune-fix
	# TODO? 25124 -  # test: Fix intermittent race in p2p_unrequested_blocks.py
	Triage: Needs review? 27529 theStack/test-fix_feature_addrman_on_big_endian_systems
	Needs review: 28027 achow101/2023-07-test-wallet-back-compat-updates
	Needs review: 28028 MarcoFalke/2307-test-stderr-
	n/a   knots_ci_tweaks-21					a30b2c8bb0f
	#TODO: Can we get a minimum-dep-versions CI going??
# FIXES:
	# Only needed for focial gitian?? 22318 hebasto/210623-random								last=35aab4f0c0b aka depends_no_getrandom
	18818 fix_gitian_src_202004-21				01cd0f44b87	last=345f0b2283e guix_reltar_autogen_distclean
	18902 fix_gitdir_again-21					9e6238975fe	last=dc420103874 fix_gitdir_again
		# NOTE: based directly on #18818
	24048 fix_pkgconf_missing-21
	18427 2020mingwthrd-mini-21					f4f276a44ae	last=df5ece3e064 2020mingwthrd
	(CHECK-LAST)	last=d9fd23bb08d 2020mingwthrd-mini
	18490 bugfix_symcheck_pe_case-21			dae51d82243	last=24a69574ece bugfix_symcheck_pe_case
	17828 p2p_log_categories-21					6ed22dedbde	last=04960621582 practicalswift/log-categories
	(CHECK-LAST)	last=137964d82dc p2p_log_categories
	19832 hebasto/200829-log					d64d3aaa576	last=1816327e533
	20845 net_logcategory_localdisconnect-0.21	11e46eb9473	last=fa55159b9ed MarcoFalke/2101-netLogDisconnect
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 laanwj/2018_12_http_bind_error		8ff26264445	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	(CHECK-LAST)	last=8520c437a0d http_bind_error
	-     http_bind_error+extra-21				1d09d2dc41d	last=78ccf6a12ce http_bind_error+extra
	(CHECK-LAST)	last=fd5353ed826 http_bind_error+extra-22
		# NOTE: Held back annotation in gdd 785429c2c7a fd5353ed826
	 9524 MarcoFalke/Mf1701-qaPruning					e8a96411986	last=88883ae13d
	(CHECK-LAST)	last=b0c8dfaca2c rpc_pruneblkchain0
	10731 log_more_uacomment-21					fb6f182d5c4	last=5b3b93c9eaf log_more_uacomment
	(CHECK-LAST)	last=f89cd1133c3 log_more_uacomment-24
	(CHECK-LAST)	last=fa16d94b095 log_more_uacomment-22
	14485 fadvise-0.20							ebbe8fe4097	last=a81aaba24db fadvise
	(CHECK-LAST)	last=3f2c08b8202 fadvise-23
		# Was #12491
	14501 fsync_dir								06128cecd60
		# Was #12696
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	13608 -										bccc1011cdb	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
		# Didn't bother rebasing to #23784 (merged in 23.x):
		#	1) Useless string change (inferior IMO)
		#	2) Added tests which are annoying to merge
	-     deprecated_param_names				1e916ec2f4b
	-     bugfix_rpc_getbalance_hacky-0.21		1413e85f702	last=e6408204500 bugfix_rpc_getbalance_hacky
	(CHECK-LAST)	last=5b7d4c9a9af bugfix_rpc_getbalance_hacky-24
	(CHECK-LAST)	last=e8a9f9c83eb bugfix_rpc_getbalance_hacky-23
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			f969f7720ba	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
		# NOTE: 19420 requires #24681 ?
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted -OR- 27539 Empact/2023-04-minimum-file-descriptor-18911
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	g404  bugfix_qvalidlineedit					05f54638d31
		# Was #18133
	18194 bugfix_gui_edit_sendaddr-mini			2747e096a1e	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	18335 -										dc0f3b960be	last=8dd5946c0b7  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	18466 -										7963fb63fea	last=a5cfb40e27b  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	g658  intro_dont_change_user_prune-0.20		0af71102295	last=??? intro_dont_change_user_prune
	(CHECK-LAST)	last=ae90e08d4f2 intro_dont_change_user_prune-24
		# Was #18729
	18766 blocksonly_no_feeest-0.21				13b50d43699	last=4e28753f606
		# diff-minimised
		# HELD BACK 33ca3590243...4aaad74c4c8 due to refactor complication
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
TM	19362 rpc_scantxoutset_reset_progress-0.17	ad8d887d3af	last=8c4129b4540 prusnak/rpc-scantxoutset-reset-progress
	19419 listwalletdir_skip_data-0.21+knots	ce14eff5578	last=3f9cc0cd736 Saibato/wallet_351
	(CHECK-LAST)	last=27be41dbc4e listwalletdir_skip_data
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect OR 27245 fjahr/202303-pr19434 OR 27909
	# TODO: g18   hebasto-g/200701-peer
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19884 fixedseeds-0.21						35264ce4152
		# +partial #21254 (bugfix only)
	22798 doc_fix_pr22798-21.1					4ab4007c290
	19888 getblockstats_utxo_actual-21.1+knots	2a7f36a8d4a	last=d885bb2f6ea
	(CHECK-LAST)	last=6fb4286f0eb getblockstats_utxo_actual-22+knots
	(CHECK-LAST)	last=937d948b76f getblockstats_utxo_actual-23+knots
	(CHECK-LAST)	last=a339d3dec51 getblockstats_utxo_actual-24+knots
		# Held back additional tests
	# Needs review: 20196 vasild/fix_GetListenPort
	g87   hebasto-g/200910-mono					df127c75a99	last=2e386cd3dd3
	20234 fix_bind_any_pr20234-21  # net: don't bind on 0.0.0.0 if binds are restricted to Tor
		# NOTE: Includes partial #25333
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	g121  fix_qt_early_sub_signals-21			ea2340e5824
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	20448 unloadwallet_namematch				34dfe668f49
	# Needs consideration.. why would we re-announce to the same peer?? 20561 sdaftuar:2020-12-moar-addrz
	# Needs concept review: 20583 MarcoFalke/2012-walletSync
	g152  gui_notify_setup_bg-0.10				dbff865256f	last=4436094508e gui_notify_setup_bg
	-     bugfix_gui_drop_abc_confusing_hack	6e1b3b65525
	20805 copyright_2022-0.21					c69ba0b3e58
		# NOTE: Diff-minimised
		#21.xTODO: Bump in 2023+
	# Needs careful review: 20966 banlist.json (TorV3 bans fix)
	# Too messy? g164 hebasto-g/201224-signal
		# +gui#375 fix
TM	g171  qt_createwallet_layoutmgr-0.21		7396b4f4443	last=d4feb6812a2 hebasto-g/210101-wallet
	# Meh? Diff too big? g176 hebasto-g/210103-delegate (fix in #20983)
TM	g177  workaround_qt_macos11_fusion-0.21		b39cebc3da8	last=4e1154dfd12 hebasto-g/210107-style
	20952 bdb_sanity_check-0.21					d4d734d9101
TM	g188  bugfix_psbt_binmode-0.21				79e220794d8	last=cc3971c9ff5 achow101-g/bin-mode-psbts
	21028 bips_44-49-84-0.21+knots				cb73d176001
	21029 cli_doc_geNnewaddr					4266a037c44
	# Needs review: g201  jonatack-g/inbound-block-relay
	g202  bugfix_gui_peerdetail_hide-0.18		dad5dd04e51
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	21111 openrc_no_rpcpassword-0.12			c6097eca413	last=95f97111dd2 parazyd/openrc-init-improve
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	21192 bugfix_netinfo_tooverbose-0.21		23d1eb26651	last=882ce25132e laanwj/2021-02-netinfo-verbosity
	g204  bugfix_gui_rm_old_fixer-0.18			b787e27bb7e	last=3913d1e8c1f
		# Diff-minimised
		TODO: Check if gui#662 is needed
	g217  gui_clickable_warning-0.11			21f8d05d194	last=67c59ae4793 jarolrod-g/warning-look-like-button
	# Needs careful review: g219 hebasto-g/210223-toolbar
	g236  gui_init_walleterror_cont-21			11342604e1e	last=6cbea59a35c gui_init_walleterror_cont
		# NOTE: Held back refactoring 0b00fd650e1...fb3ea0ad3a8
	# Complex: 21007 hebasto:210316-fork
		# +21447 TODO
	# Needs #21007, complex: 21418 laanwj/2021-03-systemd-daemonwait
	# TODO: Last commit? Diff-minimised somehow? 21560 laanwj/2021-03-torv3-hardcoded-seeds
	#21.xTODO# As soon as ready (possibly disabled by default?): 21603 -  # log: Mitigate disk filling attacks by rate limiting LogPrintf
TM	21644 bugfix_addlocal_downloadbind-0.21		1ec9cfb310f
	21752 fix_feerates_kvB_pr21752-21
	21822 bugfix_cli_pr21822-0.21				a212e7c0446
TM	21907 listwalletdir_iterate_inf-0.19		1483674ad69
	21944 fix_listwalletdir_rootdir-0.21+knots	0cb9e8948d1
	22013 ignoreblockrelayfordnsskip-0.21		8216936b4d9
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	19315 rpc_addconnection-0.21				0ec207c9478	last=87511fc2357 rpc_addconnection_mainnet
	(CHECK-LAST)	last=7d85d477730 rpc_addconnection_mainnet-22
		# PARTIAL: Only the actual addconnection RPC method
		# NOTE: Modified to allow use on non-regtest networks
	22096 fix_p2p_addrfetch_ignoreselfadv-0.21+knots	54c07ed4488
		# Includes part of #21236 (to avoid an extra GetTime on top of the 4 existing)
	# TODO: Determine if any of #22154 (bech32m fixup) is needed
	g243  gui_createwallet_opts_conflict-0.21	4004893c858
	g251  fix_bip70_errormsg-0.20				334b0e5b54a
	g271  fix_gui_rpcconsole_fontsz_prompt-0.21	c4525101c61
	g276  gui_peers_elide-0.18					3cb159c42f5
TM	g280  gui_urihandler_nophishing-0.20		0db675f8e90
	g325  gui_peers_rightalign_id-0.21			d9896709284
	g329  rpcconsole_toolbuttons-0.21+knots		6b6a1faf2f1
	# Needs review: 22261 jnewbery/2021-06-broadcast-fixes
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22308 bugfix_pr22308-0.17					f2ecce228b6
	22311 bugfix_pr22311-0.21					ff82f47b840
	18842 fix_wallet_pr18842-0.21				e1092e2e61e
	22359 fix_wallet_pr22359-0.21				6e658b9f2fd	last=fa6fd3dd6a4
	(CHECK-LAST)	last=171ac54ea47 fix_wallet_pr22359-22
		# Semi-diff-minimised
	# Needs review: 22362 MarcoFalke/2106-addrdb  # Drop (only) invalid entries when reading banlist
	22417 bpchild_closefds-21+knots				ae04745f860	last=bc8a2010501 bpchild_closefds
	(CHECK-LAST)	last=9b9cdc9ae6f bpchild_closefds-0.21
	(CHECK-LAST)	last=4c19cea484b bpchild_closefds-22
	(CHECK-LAST)	last=2255d3bc827 bpchild_closefds-24
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
		# NOTE: Workaround for boost bug included; see also #24523
	g379  qt_reset_bad_settingsjson-0.21		0952d0c615e
	# FIXME: When upgrading any guix/gitian to GCC 9: Ensure #20005 "memcmp with constants that contain zero bytes are broken in GCC" gets addressed
	22577 fix_race_pr22577-0.21.1				40a6192ef6c	last=05e84aa550c fix_race_pr22577-22
	22591 missing_settings_err-0.21				b2631c36f28
	22834 bugfix_onlynet-21						ffe8ea31150	last=0eea83a85ec vasild/onlynet
		# Refactored to be less optimised in favour of being more obviously correct
		# NOTE: Rebase of final PR in dea312e08a6 net: respect -onlynet= when making outbound connections
			# If updating, include #24991 too (included in Knots v23.0)
	(CHECK-LAST)	last=61c0c0f7bad bugfix_onlynet-22
	# Needs review: 22665 darosior:rbf_optin_nomempool
	22722 fix_estsfee_minrelay-21+knots			65397b3d6f1	last=ea31caf6b4c  # rpc: update estimatesmartfee to return max of CBlockPolicyEstimator::estimateSmartFee, mempoollMinFee and minRelayTxFee
		# +#23547
	(CHECK-LAST)	last=73a5d927f34 fix_estsfee_minrelay-22
	23027 bugfix_util_test_config-0.20			c1acc532685	last=41ff6c343e9 bugfix_util_test_config
	22781 fix_ishdenabled-0.21					bd8c4aa3b30
	# Needs review (& diff minimisation?): 22817 MarcoFalke:2108-testRaceConnect
	# n/a without #21565: 22820 fix_config_qtinputsupport-22
	# Needs review: 22834 vasild:onlynet
	# TODO? 22836 sipa:202108_bipvec5
	# Not worth added build overhead? 22840 fanquake:fix_depends_lib_optimisation
	19851 abstract_parseopcode-21				9cf7454f577  # needed for 22875
	22875 parseopcode_threadsafe-21				ad627dc37a2	last=7b481f015a0
	(CHECK-LAST)	last=34fd8e3992c parseopcode_threadsafe-22
	22879 fix_addrman_err_format-21				2340bf42de5	last=fab0b55cf06 MarcoFalke/2109-testPeersDat
	(CHECK-LAST)	last=0a3ec03ea33 fix_addrman_err_format-22
	22895 fix_RBFD_lock_pr22895-0.16			c36be3256af	last=94c04681edb fix_RBFD_lock_pr22895-22
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review: 22929 S3RK/fix_19856
	# Needs review and diff minimisation: 22932 jonatack:require-GetBlockPos-to-hold-cs_main
	g399  fix_load_psbt_wo_wallet-21			117869a3d40	last=27f8c7c425d fix_load_psbt_wo_wallet-22
	g409  fix_gui_walletop_titlebar-0.20		f667025d807	last=01bff8f0494
		# Held back trivial comment change f86fe193329..01bff8f0494
	(CHECK-LAST)	last=e817b217145 fix_gui_walletop_titlebar-22
	g418  mac_platform_metadata-0.20			ffc15f5eee7	last=3765c486ef5 jarolrod-g/applesilicon-categorization
	23050 bugfix_pr23050-0.15					84ffaf55e8c  # log: change an incorrect fee to fee rate, and vice-versa
	23061 fix_argparse_persistmempool-21		f5b384e1cd6	last=60ef97c3e80 fix_argparse_persistmempool-22
	# Needs review & concept check: 23074 Package-aware fee estimation
	23106 fix_unlock_before_psbtsign-21			a1272dad525	last=aebd7bceaf3 fix_unlock_before_psbtsign-22
	# ---- BEGIN IN SEQUENCE ----
	23136 fix_qa_assert_feeamt_pr23136-21
	22949 fix_fee_roundup_pr22949-21
	24239 ceildiv_int_check-21
	# ---- END IN SEQUENCE ----
	23139 doc_fix_pr23139_txdesc-21.1			37349b7f46e
	# Needs review: 23140 sipa/202109_addrmanbias
	# Not sure about this: 23142 meshcollider:202109_no_assert_corruption
	g430 gui_txlinks_g430-0.19					4241a5a7ac2	last=a3b35507ce7 gui_txlinks_g430-22
	g439 gui_hide_unused_icons-0.20				823c85e38d4
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs review: 23197 jonatack/fix-netaddress-UB-and-banman-fuzz-crash
	# Needs review: 23227 MarcoFalke/2110-ToIntegral
	# Needs review of backport-rewrite in qt_catch_rpc_index_overflow-0.18 [alt to g446  MarcoFalke/2110-qtRpcCons]
	# TODO: 23268 prayank23/dns-seed-fqdn
	# TODO: 23253 MarcoFalke/2110-utilTxSeqId
	23304 wallet_derive_inactive_pr23304-21
	# n/a without #20764? 23324 netinfo_peer_count_all_reachable-22
	# n/a without #19651: 23333 theStack/202110-wallet-fix_getwalletinfo_segfault_after_importing_descriptor
	# Maybe just the docs from #23341 ?
	23348 wallet_descr_hide_keypoololdest-0.21	bf69f3d1a37	last=ee03c782ba6 hebasto/211024-rpc-gwi
		# Held back std::optional refactoring 303ee60f817...ee03c782ba6
	# Needs review: 23365 -  # index: Fix backwards search for bestblock
		# Followups in #23777
	# Needs review + diff minimisation: 23380 jnewbery:2021-10-addrman-add-logging
	# Moved to Knots bips.md update in branding: 21925 + 23410 hebasto/211101-bips
	# Needs work/diff-minimisation: 23418 MarcoFalke/2111-txPoolPrioOverflow
	# Needs review/diff-minimisation: 23486 MarcoFalke/2111-rpcScript
	# Needs work: 23502 achow101/tr-low-fee-est
		# See also #28573
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	# Needs review: 23628 -  # Check descriptors returned by external signers
	# Needs review: 23631 -  # p2p: Don't use timestamps from inbound peers for Adjusted Time
	23634 rpc_scantxoutset_examples-21			f8148f4d430	last=1ed5681407a theStack/202111-rpc-add_scantxoutset_examples
	20556 doc_fix_pr20556-21					0e40564787e
	# Embedded font not in 21.x! g477  gui477_fix_mac_console_font-0.13  # Monospaced output in Console on macOS
	23644 wtx_timercvd_noadjust-21				f254b23b7d0
		# Diff-miniised
	# Needs correctness verification (especially startingheight which changed in 22.x): Diff-minimised 23652 MarcoFalke/2112-docOptPeer
	# Needs review: 23673 hebasto/211204-native
	23750 docfix_importdesc_range_no_label-21	397093e7779	last=65efbba45d8 darosior/no_label_range_descriptors
	# Buggy? UI change too... g447  -  # Never disable HD status icon
	g506  qt_qrcode_sizefixes					4724488fe3d
	# idk? 23781 hebasto/211215-bptest
	23858 fix_qa_scantxoutset_pr23858-21
	23937 fix_rpcdoc_dumptxoutset_pr23937-21
	# Needs work: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	g508  fix_qt_progressrate_pr_g508-0.16
	g516  qt_recvreq_show_eyeicon-0.14
		# Diff-minimised
	# Needs review: 24066 whitslack/openrc-daemonwait
	24067 wallet_no_final_checks-21
	# Needs work: 24072 -  # doc: fix wording of alertnotify to match behaviour
	#21.xTODO# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	24095 fix_settings_jsonfmt-21
	24117 fix_index_dontcommitduringinit-21					last=bfcd60f5d50  # index: make indices robust against init aborts
		# NOTE: partial: coinstatsindex and feature_init test aren't in 21.x
	24145 fix_mempool_clear_txhashes-21						last=9d65ad365c5  # Clear vTxHashes when mapTx is cleared
	24168 fix_dumpbanlist_races-21
	# TODO? 22762+24201 -  # p2p: Avoid InitError when downgrading peers.dat
	24231 fix_datastream_overflows-21
	24253 rm_broken_datastream_inserterase-0.17
	24287 fix_genmanpages_tagver-0.19
	# Needs work: 24313 Sjors/2022/02/displayaddress						last=803387f054d
		# TODO: make sure this doesn't break compatibility (and fix review bugs)
	# Needs work/correctness: 24318 -  # doc: ZMQ documentation fix regarding topics
	22087 validate_port_opts-21								last=1dae86bfd22  # Validate port-options
	(CHECK-LAST)	last=e006505695c validate_port_opts-23+knots
	(CHECK-LAST)	last=361d247b3bc validate_port_opts-24+knots
	22461 fix_descwallet_upgrade_noop-21
	24365 fix_watchwallet_upgrade_noop-21
	24371 fix_torcontrol_overread-0.15
	# Not worth it? 24381 -  # test: Run symlink regression tests on Windows
	# Needs work: 24392 hebasto/220219-cmake
	# Meh: 24406 -  # test: Fix Wambiguous-reversed-operator compiler warnings
	-     compat_llvm_divmoddi4-0.17
		# Part of #24448 in Knots 23.0+
	# Not worth the effort? 24409 fanquake/24263_followups  # Always output license/copyright info with -version
		# NOTE: Care needed to ensure manpage generation doesn't break
		# NOTE: Might need #20468
	24434 fix_english_addrmanerr_pr24434-21
	24453 fix_rpcdoc_changeaddr_STR-21						last=e8272024ab6 fix_rpcdoc_changeaddr_STR
	# Not worth it? 24469 ryanofsky/pr/testu
	24479 bugfix_settings_numberval-0.20					last=33722279495 bugfix_settings_numberval
	24538 fix_miner_policy_modfee_pr24538-0.20
	24629 bugfix_rpc_prunebc_retval-21						last=e593ae07c4f bugfix_rpc_prunebc_retval
	24640 fix_rpcdoc_gbci_pruneheight_desc-21+k				last=06822f86545 fix_rpcdoc_gbci_pruneheight_desc
	22684 qa_invalid_prune-21
	24626 err_reidxCS_pruned-21
	24630 reindexCS_resetindexes-21							last=cf531ba531c
	(CHECK-LAST)	last=c37ab289c4b reindexCS_resetindexes-23
	20769 fix_listenonion_wo_listen-21^
	g568  fix_listenonion_wo_listen-21
	# TODO: Triage along w/ KDE patches: 24668 prusnak/qt5-5.15.3
		# NOTE: WIP list of KDE patches in 202204-KDEQtPatchesForBitcoin
	24716 fix_doc_rpc_rawtx_pr24716-21+knots
	# If needed: 24722 -  # build: patch around qt duplicate symbol issue (duplicate symbol 'lcQpaFonts()')
	# Not needed unless Windows builds use GCC 10+ (21.x uses GCC 7): Force inlining of functions with __m256i params in rc/crypto/sha256_avx2.cpp to fix #24727 (only when building with GCC - not MSVC or Clang!)
	24804 check_GetAncestor_rv-21
		# NOTE: Diff-minimised, including keeping `int` type for nTimeDiff since we depend on 32-bit int anyway (and MTP can't be >31-bit right now)
	-     doc_rest_chaininfo_update-21
		# Inspired by #24776
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	24837 fix_noproxy_hack-21^	# init: Prevent -noproxy and -proxy=0 from interacting with other settings
	-     fix_noproxy_hack-21
		# Simpler alternative to 24830 -  # init: Allow -proxy="" setting values
		# NOTE: Depends on #24837 to work right!
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Simpler version of? 24845 -  # wallet: createTransaction, return proper error description for "too-long-mempool-chain" + introduce generic Result classes
	# Needs work: 24851 -  # init: ignore BIP-30 verification in DisconnectBlock for problematic blocks
	24855 fix_doc_rpc_setwalletflag_warnings-0.20
	# Needs review: 24858 mruddy/issue_21379  # reindex, log, test: incorrect blk file size calculation during reindex results in undesirable blk file malformedness
	24859 fix_wallet_badcreate_pr24859-21					last=e80b64b382f fix_wallet_badcreate_pr24859-23  # wallet: Change wallet validation order (to avoid creating invalid wallet dbs)
		# +#25011 achow101/fix-legacy-createwallet-test
	# Anything fixed here? Not AFAICT... 24871 -  # refactor: Simplify GetTime
	# Needs review: 24912 mruddy/nchaintx_type
	25051 fix_configure_def_enable_arm_asms-21				last=7fd0860d12d fix_configure_def_enable_arm_asms
		# NOTE: Only half is applicable to 21.x
	25282 fix_configure_def_use_libevent-21					last=f0f5cd79b5d fix_configure_def_use_libevent
	24933 strerror_threadsafe-21							last=3c651702c68 strerror_threadsafe-23
	24957 fix_prune_during_loadblock-0.20					last=347664ec718
	(CHECK-LAST)	last=c86f129fd1d fix_prune_during_loadblock-22
	24984 fix_wallet_race_attachingbb-21^
	25088 fix_wallet_race_attachingbb-21					last=ba10b90915d fix_wallet_race_attachingbb
	(CHECK-LAST)	last=8fc36e243a7 fix_wallet_race_attachingbb-22
	# Needs review: 24994 hebasto/220426-consensus
	# Needs review: 25036 w0xlt/save_scan_progress
	25074 fix_idx_sync_consistency_pr25074-0.19				last=7171ebc7cbd
	# TODO: 25077 fix_dataraces_pr25077-21							last=fa35585c74c
	#		(CHECK-LAST)	last=d300cd95c0a fix_dataraces_pr25077-23
	# NOTE: Too convoluted to backport safely - partially done in fb7e7781d90
	g595  qt_handle_autostart_errors-0.15					last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	g599  ts_20220515-partial-21							last=d9411324066 ts_20220515
	(CHECK-LAST)	last=3d7b977bbf0 ts_20220515-partial-23
	(CHECK-LAST)	last=eda73090c7f ts_20220515-partial-24
	(CHECK-LAST)	last=f4fe307b84b ts_20220515-partial-25
		# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
		# NOTE: ts_20220515-21 is full* backport ddfc86cf878=5e23dabf265 (* see two gui#599 notes later in spec)
		#21.xTODO# Update with other commits that are beneficial
	25093 rpcdoc_sendmany_dummy_opt-0.20
	(CHECK-LAST)	last=32cca184b79 rpcdoc_sendmany_dummy_opt-23
	# Needs review/triage: 25096 -  # [net] Minor improvements to addr caching
		# NOTE: Fixes in #25312 & #25333
	25106 rpc_dumptxoutset_fopen_check-0.20					last=805443ff3f9 rpc_dumptxoutset_fopen_check-23
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
	# Needs triage/review: Maybe part of (see reference to #17167) 25156 -  # refactor: Introduce PeerManagerImpl::RejectIncomingTxs
	25157 fix_bcli_negtime_pr25157-21						last=fdc6e7cf753 fix_bcli_negtime_pr25157-23
		# NOTE: Other half included in #21056 below
		# Diff-minimised
	# Needs concept ACK/review: 25158 -  # rpc, wallet: add abandoned field for all categories of transaction in ListTransaction
	# Needs review: 25193 -  # indexes: Read the locator's top block during init, allow interaction with reindex-chainstate
	25216 docfix_zmq_hwm_ex_pr25216-21  # Doc: Fix parameter in hwm example block
	# Needs review: 25220 brunoerg/2022-05-fix-incorrect-warning-createmultisig
	# Needs review: 25227 -  # Return empty vector on invalid hex encoding
	# Needs concept review: 25235 -  # GetExternalSigner(): fail if multiple signers are found
	g260  qt_handle_exceptions_pr260-21						last=3609f2d1b0d qt_handle_exceptions_pr260-21-corepr
	25239 wallet_committx_catch_db_write_err-21
	# Needs review/work? 25272 wallet_sync_catch_db_write_err-21
	25256 log_threadname_unknown-0.19
	# Not clear this fixes anything: 25273 achow101/use-preset-tx-things
	25276 fix_rpcdoc_importdesc_pr25276-21
	# Meh? 25288 -  # test: Reliably don't start itself (lint-all.py runs all tests twice)
	# Simpler alternative to? 25294 -  # test: Fix wait_for_debug_log UnicodeDecodeError
	25320 impl_win_mlock_limit-0.17
	25333 qa_fix_port_collisions_pr25333-21
		# NOTE: 1 out of 3 test changes here; others included with relevant PR(s)
	25351 wallet_import_scanmempool-21						last=1be79641893 fjahr/202204-import-scan
		# NOTE: Was #18964
	# Needs review: 25380 darosior/fee_estimator_disable_cpfp
		# NOTE: Tests need parts of #22539+#24817
	25404 fix_p2p_maxblkann_pr25404-0.17					last=e357c895388
	# Bug doesn't affect Knots: g615 -  # If -prune=0 is set, Uncheck Prune on Intro page
	25463 fix_leveldb_no_cloexec-0.20						last=a956806de2f fix_leveldb_no_cloexec
		# TODO: Remove if bumping to a fixed LevelDB?
	25425 fix_wsystem_check-0.19
	# Triage: 25454 sdaftuar/2022-06-single-getheaders
	25456 getrpcinfo_steadyclock-21
	# Not worth it? 25476 fjahr/2022-06-importdesctest
	25495 fix_bnb_bestwaste0-0.20
	25497 wallet_manyinput_fees_pr25497-0.20
	25548 readlink_overflow_check
	# Not worth it? 25506 1440000bytes/peertimeout-error-msg
	# Either n/a or very difficult to backport: 25507 S3RK/correct_target_with_sffo
	#21.xTODO# Check on #25561
	# Needs concept review: 25574 -  # validation: Skip VerifyDB checks of level >=3 if dbcache is too small
	# Not applicable? Unsure... 25590 achow101/sign-psbt-tr-wo-utxos
	# Needs work: 25595 instagibbs/verify_psbt_input
	# Needs review: 25599 achow101/specifc-atomics-check
	-     fix_rpcdoc_addresses_part20286-21+k
	25615 fix_rpcdoc_gettxout_pr25615-21+k					last=743a84a5f6f
		# NOTE: Part moved to #22918
	# Bug in fuzzer, not worth it? 25624 -  # fuzz: Fix assert bug in txorphan target +#25641
	g631 watchonly_no_encrypt-0.5							last=4c495413e13 achow101-g/watchonly-disable-encryption
	# Needs review: 25642 darosior/ext_key_derive_wrap_around
	# When translations exist, or correct mistaken old translations: 25666 -  # refactor: wallet, do not translate init options names
	Merged: 25678 -  # p2p: skip querying dns seeds if -onlynet disables IPv4 and IPv6
	25687 depends_no_export_pkgconf-21
	Triage: 25634 fix_wallet_blank_unset_pr25634-25
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	25691 docfix_getblock&asmhex-21+k						last=56d92447d0e docfix_getblock&asmhex
		# NOTE: Parts moved to #22918 and #16795
	# Needs review: 25698 -  # crypto: avoid potential buffer overread in ChaCha20::SetKey
	# Likely not applicable, and in any case only needed for LTO additions in 24.x? 25708 fanquake/win_qt_always_correct_ar
	g633  qt_opts_ambig_shortcuts_pr633-0.19+k				last=5fde8fbe085
	# Needs review: 25717 sdaftuar/2022-02-headers-dos-prevention + #25960 + #25968? + #25978
		# Maybe too complex and unnecessary for LTS branch
		# Fixed in #26172
	# TODO, Not trivial backport: 25720 sdaftuar/2022-07-reduce-headers-sync-bandwidth
	25727 reject_conf_in_conf-21+knots						last=deba6fe3158
	(CHECK-LAST)	last=01cbf92c7e7 reject_conf_in_conf-23
	# Needs review: 25729 -  # wallet: Check max transaction weight in CoinSelection
	Merged in master: 25768 achow101/unify-resend-reaccept
		Fixed by #26132 and #26205
	25829 dist_rpcauth-21
		# NOTE: Partial: does not include installing example bitcoin.conf
			# Rationale: 1) not originally included, 2) no bug in excluding, 3) static/trivial in 21.x anyway
	# Too complex/risky, and depends-only fix doesn't affect gitian builds: 25838 hebasto/220813-mkspec
	# Meh: 25854 -  # tracing.md trivial English fixes
	#21.xTODO# Either 25856 or 25858 to fix PSBTs with empty tap_tree
	# Needs work/concept: 25867 -  # lint: enable E722 do not use bare except
		# NOTE: Fixes Ctrl-C being caught/ignored
	# Needs work/concept: g653 achow101/show-bal-send
	#21.xTODO# 25880 -  # p2p: Increase BLOCK_STALLING_TIMEOUT timeout during IBD
	25922 wallet_resend_check_ea_min-21+knots
	25924 docfix_rescanwallet_typo_pr25924-21+k
	# TODO Partial: 25925 theStack/202208-doc-add_new_descriptor_calls_to_docs
		# But whole doc needs revising for Knots? :/
	25964 fanquake/fixup_mingw_cflags
		TODO: Ensure it actually works with this & 21.x-knots-lts-deps miniupnpc versions; and that _WIN32_WINNT is the version we want for 21.x
	Needs review: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	25983 hebasto/220902-httpmutex
		See #26034 for backport as far as 22.x
	If fixes 21.x: 25990 -  # test: apply fixed feerate to avoid variable dynamic fees in wallet_groups.py
	If applicable: 26005 fix_wallet_copyfail_nullresult
	If applicable: 26009 fanquake/remove_boost_libtest
	FIXME: Taproot wallets CRASH - see #26015; possible fix in #26021
	Needs review: 26032 Sjors/2022/09/external-signer-feerate
	Needs work & minimising: 26039 -  # rpc: Return RPC_TYPE_ERROR, not RPC_MISC_ERROR on type mismatch (1/2) OR #25737
		Fix in #26213 (but maybe too much fixed/strict?)
	Needs review: 26053 furszy/2022_rpc_wallet_fix_help_add_inputs
	g664 hebasto-g/220907-gb
	g665 w0xlt-g/load_wallet_signal
	# Wait for #24409? Or at least until released by Core...? In Knots now... Diff-minimise? 26067 -  # util: improve bitcoin-wallet exit codes
		# NOTE: Was #24428
		# NOTE: rebase w/o 24409 in f41a608a397
	Check for fixes in: 26069 furszy/2022_rpc_unify_error_type
	# If BSD depends support matters: 26073 fanquake/_BSD_bdb_compilation
	Careful: 26089 fanquake/prune_unneeded_upnp_natpmp
	Check if needed: 26091 -  # test: Fix syncwithvalidationinterfacequeue calls
	Needs review? Are all fixes? 26109 jonatack/2022-09-getpeerinfo-netinfo-updates
       # NOTE: Included in backport PR #26457
       #21.xTODO# Check if these fixes are correct; see https://github.com/bitcoin/bitcoin/pull/26457#pullrequestreview-1181641835
	26116 -  # rpc: Allow importmulti watchonly imports with locked wallet
	26119 -  # doc: Move -permitbaremultisig to the relay help category
	26130 fix_descrwallet_signmsg_deadlck
	Is needed? Needs review: 26138 -  # test: Avoid race in disconnect_nodes helper
	Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	If applicable: Needs work: 26142 hebasto/220920-package
	If applicable: 26143 brunoerg/2022-10-fix-rest-test
	# Needs review: 26152 -  # Bump unconfirmed ancestor transactions to target feerate
	Partial: Needs review: 26186 -  # rpc: Sanitize label name in various RPCs with tests
	Needs review & backport checking: 26188 vasild/fix_coinstatsindex_initial_sync
	Needs review: 26203 -  # wallet: Use correct effective value when checking target
		Backport to 24.x in #26242
	If applicable: 26212 -  # contrib: Fix capture_output in getcoins.py
	As needed: 26213 -  # univalue: Remove confusing getBool/isTrue/isFalse
	If applicable: 26248 -  # net: Set relay in version msg to peers with relay permission in -blocksonly mode
	Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	26275 -  # Fix crash on deriveaddresses when index is 2147483647 (2^31-1)
	Needs minimisation of just a fix? 26289 stickies-v/mempool-use-result
	Needs review: 26316 andrewtoth/block-read-shared-mutex
	If applicable: Needs work? 26328 jonatack/update-netinfo-relaytxes-help
	Needs review: 26331 -  # Implement CCoinsViewErrorCatcher::HaveCoin and check disk space periodically
	Needs review: 26343 mzumsande/202210_addrfetch_servicebits
	Needs review: 26347 -  # wallet: ensure the wallet is unlocked when needed for rescanning
	Needs review: 26349 w0xlt/issue_26338
	If relevant: 26355 -  # p2p: Handle IsContinuationOfLowWorkHeadersSync return value correctly when new headers sync is started
		Followups in #26387 (not included in 24.x)
	If needed: 26380 -  # Revert "test: check importing wallets when blocks are pruned throw an error"
	Needs work/review: 26399 -  # Fix #24049: signed integer overflow in SeenLocal
	Needs review: g673 jonatack/2022-09-display-fallback-for-gui-peers-version-and-user-agent
	If applicable: g677 fix_qt_peers_na-24+knots							last=cfe5bbe6ccd fix_qt_peers_na
	# Relevant? 26404 mzumsande/202210_testfix_blockfrompeer
	If applicable: 26418 achow101/fix-psbt-multia
	Meh? 26424 -  # doc: correct deriveaddresses RPC name
	# Needs work/review: 26426 fjahr/202210-coinstatsindex-overflow
	# Relevant? 26448 mzumsande/202211_fix_sendtxrcncl
	Needs work: 26462 theStack/202211-wallet_fix_crash_on_descriptor_wallet_load
	# Needs conceptual/review: 26471 -  # Don't share mempool with dbcache in -blocksonly mode
		# TODO: Ensure defaults to same behaviour for 21.x
	If applicable: Needs review: 26477 jamesob/2022-11-fix-maxtipage
	Needs work: 26512 -  # init: Evaluate sysperms before config file
	If applicable: Needs review: 26515 mzumsande/202211_getpeerinfo_allornothing and/or 26516?
	Fix only? Needs review: 26532 furszy/2022_wallet_fix_ckeys_checksum
	Needs review & concept for backport: 26533 andrewtoth/scan-and-unlink-pruned-files
	Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	If applicable: Needs review: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	If applicable: g680 -  # Fixes MacOS 13 segfault by preventing certain notifications after main window is destroyed
	If applicable: Important? Needs review: 26559 furszy/2022_v24_wallet_sad
		See also: #26560
	If applicable: 26584 -  # cli: include local ("unroutable") peers in -netinfo table
	If applicable: Needs review: g682 -  # Don't directly delete abandoned txes from GUI
	# Not worth it? 26611 achow101/coin-sel-dont-assert
	26618 -  # rpc: Prevent unloading a wallet when rescanning
	Needs review: 26628 ryanofsky/pr/nmult
	If applicable: Needs review: 26643 achow101/move-fee-underpay-check
	If applicable: Needs review: 26646 glozow/package-single-tx-result
	Needs review: g684  -  # Improve 'Requested Payments History' Multiselect
	Needs review? 26728 achow101/wallet-knows-master-key
	Needs review? 26762 hebasto/221228-queue  # Make CCheckQueue RAII-styled
	26828 andrewtoth/assumeutxo-remove-fix
	Just fixes from? 26836 furszy/2022_wallet_finish_addressbook_encapsulation
	Needs review: 26903 pstratem/2023-01-17-baseindex-commit-error
	Needs review: 26950 fanquake:check_for_SecureZeroMemory
	SECURITY Needs review: 26964 willcl-ark/2023-01-cookie-bind
	If needed for below: 27850 pinheadmz/blockstore-tests
	Triage: 27039 pinheadmz/reindex-read-only
	Triage: Needs review: 27071 vasild/lookup_subnet_cjdns
	Triage if we Need a fix for #26176 (Opening macOS DMG does not open Finder window)
	Triage 27231 jonatack/2023-03-logging-fixes-and-test-coverage
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	Triage: Only f73782a from #27279 (see #27474 for 24.x backport)
	# Triage/Needs review 27295 brunoerg/2023-03-improv-deserialize-v2
	Triage 27303 pinheadmz/cache-conf-file OR 27302 (used in Knots 25)
	# Needs review: 27307 -  # wallet: track mempool conflicts with wallet transactions
	Needs review: 27411 mzumsande/202303_advertise_nets
	Alternative to: 27434 pinheadmz/chaintips-invalid
	Triage: 27468 (see #27474 for 24.x backport; #27468 for regression test)
	Triage: 27473 (see #27474 for 24.x backport)
	27501 -  # mempool / rpc: add getprioritisedtransactions, delete a mapDeltas entry when delta==0
		At least the bugfix!
	27554 -  # test: Treat bitcoin-wallet binary in the same way as others
	Needs review: g696 -  # Switch RPCConsole wallet selection to the one most recently opened/restored/created
	Triage & Needs work? g719 theStack-g/gui-nuke_cc_dust_label
	Triage & Needs work? g722 -  # Wallet : Allow user to navigate options while encrypting at creation
	Triage & Needs review? g739 achow101-g/gui-dont-blank-noprivkeys
	Triage: 27556 -  # wallet: fix deadlock in bdb read write operation
	Triage & Needs review: 27557 pinheadmz/async-getaddrinfo
	Triage: 27577 mzumsande/202304_seednode_fixedseed_interaction
		Check #28016
	Triage: 27591 glozow/2023-05-mempool-vsize
	Triage & # Needs review: 27601 furszy/2023_wallet_double_change_output
	Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	Triage & Needs review: 27602 -  # net processing: avoid serving non-announced txs as a result of a MEMPOOL message
	Triage: 27608 (see #27624 for 23.x backport)
	Triage: 27610 (see #27624 for 23.x backport)
	Triage: Allow toggling on mainnet (and by default off?): 27622 -  # Fee estimation: avoid serving stale fee estimate
	Test well: 27626 instagibbs/2023-05-parallel-block-downloads
		+27743
		NOTE: BACKPORTS IN #27752
	Triage: n/a   fix_div0_connecttip_loadblocks_log-25
		# Affected code removed in #27673
	Triage: Needs review: 27684 hebasto/230516-punish OR ???
	Triage: 27708 -  # Return EXIT_FAILURE on post-init fatal errors
	27717 test_util_env-0.16
	Triage: If needed? 27720 furszy/2023_index_init_race_bugfix
	Triage: 27724 -  # build: disable boost multi index safe mode in debug mode
	Triage: 27727 MarcoFalke/2305-rpc-bech32-; backports in #27756 (23.x), #27755 (24.x), and #27750 (25.x)
		+27747
	Triage: Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	Triage: Needs review: 27804 -  # init: deduplicate added connections
	Triage: 27814 -  # Blocking arguments -nohelp, -noh, and -no?
	Triage/reduce?: 27815 -  # CLI: Only one Request Handler can be specified.
		NOTE: Requires adapting in -addrinfo merged below (#21595)
	Triage & Needs review: 27820 -  # Sanitizing ports of -rpcconnect and -rpcport.
	# Triage & Needs review: 27823 mzumsande/202306_feature_init_fix
	Triage & Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	Triage: 27846 -  # [coinselection] Increase SRD target by change_fee
	Triage: 27853 brunoerg/2023-06-bugfix-rest-deploymentinfo (25.x backport in #27887)
	Triage: 27862 ryanofsky/pr/assumeabort
	Triage: 27863 brunoerg/2023-06-net-netgroup-continue
	Triage: 27905 mzumsande/202306_dirty_blockindex
	Triage & Needs review: 27912 -  # net: run disconnect in I2P thread
	Some good fix for 27915 (#27920?)
	Triage: 27930 -  # util: Don't derive secure_allocator from std::allocator
	Triage: Needs review: 27969 -  # bumpfee: ignore WALLET_INCREMENTAL_RELAY_FEE when user specifies fee_rate
	Triage: Needs review: 27981 sipa/202306_pushback
	Triage: Needs work: 27991 fanquake/instrument_libsecp
	Triage: Needs review (& extra care for wallet?): 27997 darosior/miniscript_non_satisfiable
	Triage: Needs work? 28020 -  # exclude ipc scheme from port check
	Triage: # If needed: 28026 furszy/2023_fix_index_timeout
	Triage: Needs review: g742 john-moffett-g/2023_06_ExitOnLooseArgument
	Triage: 28029 fix_zmq_errhandling_202307-25+k					last=07086589b27 fix_zmq_errhandling_202307
	28056 rpcdoc_gbt_lpid_data-22							last=f6a26196cfb
	Triage: Needs review? 28067 furszy/2023_wallet_infer_watchonly_sh_script
	# Not a fix: 28076 MarcoFalke/2307-fs-lint-
		# "I don't think anything here is a bug fix" -MarcoFalke, https://github.com/bitcoin/bitcoin/pull/28076#issuecomment-1682450942
	Triage: 28123 fix_nonstring_onelinedesc
	Triage: Needs review: 28125 furszy/2023_wallet_bugfix_migration_invalid_scripts
	Triage: Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	Triage: Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Windows-only functional test fix: 28204 hebasto/230802-sqlite
	Triage: Needs concept: 28205 theStack/202308-netprocessing-reallow_fetching_of_genesis_block
	28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	Triage: #28248
	Triage: FIXME: curl RPCdoc examples use wrong content type!
	g749 furszy/2023_gui_start_minimized
	
	#21.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
@21.x-knots-lts-deps
	25763 bdb_no_werror-21
	-     boost_1.71fixes-21
	21991 libevent_2.1.12-21
	-     miniupnpc_2.0.20180503-21
	-     qt_5.9.9-21
	-     sqlite_3.32.3+-21+knots
	23956 zeromq_4.3.4-21
		# +#24134 fixes
		# NOTE: Dropped 72718ab1ace & f74c5c9241a; we don't support NetBSD, and the autotools in the gitian VM is too old to rebuild a working configure
	#21.xTODO# Check depends for fix-only updates
		# boost 1.70: not maintained :| (maybe bump to 1.71 for Ubuntu focal until 2030? or just manually backport fixes in bionic's 1.65 and focal's 1.71?)
			# manually backported fixes between 1.70 and 1.71
			# updated to Ubuntu bionic 1.65.1.0ubuntu1 (no patches)
			# updated to Ubuntu focal 1.71.0.0ubuntu2 (no patches)
		# libevent 2.1: upstream or Ubuntu jammy until 2032
			# updated to Ubuntu jammy 2.1.12-stable-1build3
		# miniupnpc 2.0: RHEL 7 until 2024
			# updated to RHEL 7 2.0-3.el7
		# qrencode 3.4: Debian stretch until 2027 or Ubuntu jammy [universe] until 2032
			# updated to Debian stretch 3.4.4-1
			# updated to Ubuntu jammy 3.4.4-1build1
		# qt 5.9: copy patches from Ubuntu bionic 5.9.5 until 2028
			# updated to Ubuntu bionic 5.9.5+dfsg-0ubuntu2.6
				# TODO: Triage dead_key_symbols.diff
				# TODO: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=884956 not-really-fixed in Ubuntu with hidpi_scale_at_192.diff
		# sqlite 3.32: Debian bullseye or RHEL 9 until 2031
			# NOTE: Manually patched in fixes from 3.34.1 (which is what Debian/RHEL support)
			# TODO Complex: * 86f477eda Catch fts5 index corruption caused by issuing 'delete' commands with incorrect data earlier in some cases. Also fix a couple of test script problems.
			# updated to Debian bullseye 3.34.1-3 (no patches)
		# zeromq 4.3: upstream or Ubuntu jammy until 2032
			# updated to Ubuntu jammy 4.3.4-2
	#21.xTODO# Check bundled for fix-only updates
		# leveldb: nothing necessary for bump in bitcoin-core fork
			# NOTE: Revert #25463 if bumping to an updated version
		# crc32c: nothing necessary for bump in bitcoin-core fork or upstream
		# libsecp256k1: NOT UPDATING (users should use system libsecp256k1)
			# at least check for no known critical issues?
				# skimmed up to 694ce8f
		# ctaes: nothing important as of 2022-08-24 / 8012b06
		# univalue: nothing important as of 2022-08-24 / bitcoin-fork de4f73d / stable-1.0.x 76b474e / master d6715ee
@21.x-knots
# PERFORMANCE:
	# Needs work: 25383 -  # wallet: don't read db every time that a new 'WalletBatch' is created
	# Consider: 25985 fanquake/revert_slow_macos_sqlite
# SOFTFORK:
	21934 rpc_getblockchaininfo_lockedin_statistics-0.21.1	394e59e2f86	last=2b19f3443ef rpc_getblockchaininfo_lockedin_statistics
	22016 rpc_gbci_period_start-0.21.1+knots	b19116ccf14	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	(CHECK-LAST)	last=5e04731447b rpc_gbci_period_start
	(CHECK-LAST)	last=d6d1a1b47eb rpc_gbci_period_start-22+knots
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
m	g275  gui_darkmode-0.21.2_pt1				9cd8d7e8a79
		# NOTE: Fixed bug in gui#330 a simpler way b942216a1a7
	g154  gui_darkmode-0.21						55019938d93
	g366  gui_palettechange-0.21				ee70e2584ff
	-     restore_win32-0.21+knots				849948efaa5	last=3e30ae0514e restore_win32-0.21
	(CHECK-LAST)	last=42e0d32b391 restore_win32-22  # (currently broken)
	-     restore_linux32-0.21					8b1830211aa	last=eeea5b787d4 gitian_linux32
		# NOTE: gitian only
	20963 gitian_power64-0.21+knots				7d207bda20d	last=543bf745d38 gitian_power64
		# NOTE: Originally #14066
		# Held back 31dbf0b677d..543bf745d38 - probably only applicable to master
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
m	14641 fundraw_minconf-21+knots				b097763986a	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	(CHECK-LAST)	last=cd52287b586 fundraw_minconf-0.21
	(CHECK-LAST)	last=9834825c4b7 rpc_fundtx_minmaxconf-23+knots
	(CHECK-LAST)	last=7f4c9039f71 origin-pull/22049/head
	(CHECK-LAST)	last=4485a0bbbb7 rpc_fundtx_minmaxconf-24
	(CHECK-LAST)	last=972a1feefa8 fundraw_min_conf_deprecated-23+knots
	(CHECK-LAST)	last=b5c60e131d3 fundraw_min_conf_deprecated-24+knots
	(CHECK-LAST)	last=f38eb81191e origin-pull/25375/head
		# Includes param rename (min_conf->minconf) and tests from #22049 (but not new maxconf param)
		# TODO: Once #25375 is merged, include its strings/tests
		# NOTE: Backported #25375 (minus sendall RPC, not in Knots 21.x) in b289e97b8f0
	12677 listunspent_ancestorinfo-21.1+knots	b0bd7118765	last=6cb60f3e6d6 listunspent_ancestorinfo
	18479 rpc_sign_show_fees-21					9f357b09916	last=47b2ba29df2 !origin-pull/12911/head
		# NOTE: Originally #12911
	(CHECK-LAST)	last=ac2d457500e rpc_sign_show_fees
	g119  rm_send2self-mini-21					8a6ed938070	last=099dbe4224e rm_send2self
	(CHECK-LAST)	last=39fa4ba47e6 rm_send2self-mini
		# NOTE: Originally #15115
	15423 tor_socks_port-0.21					109cf1f0e3b	last=b2774fc0bed tor_socks_port
		# Held back 962f168a014..398df42f449, da20c1e6d20 (not a bugfix)
	15836 fee_histogram-21						69874bd7a2f	last=b94292a7cb jonasschnelli/2019/04/feeinfo
	(CHECK-LAST)	last=8cdfa4e2bea fee_histogram+pr15836_api
	(CHECK-LAST)	last=f2fb1f17444 origin-pull/21422/head
		# Held back approach changes (that ignore CPFP) f2ca3d35ee9..47b5c3e03a7 - current approach is arguably buggy (see sipa's review on PR)
		# NOTE: removed extraneous Bitcoin-Qt.* files
		# NOTE: Backported some features/test from #21422 (but not API incompatibilities)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 ? See also git diff b1f9af22425..9d16921553b -w
	17463 gui_custom_sendyes					087d3e642af
	g562  wallet_no_reuse-0.21+knots			952bb1fb9bc	last=627aa679d26 wallet_warn_reuse_gui
		# NOTE: Was #15987
		# NOTE: Uses older bloom filter implementation
	22693 rpc_gai_txids-0.21+knots				69259a6ade8	last=b510d2c3e32 getaddressinfo_txids
		TODO: backport bccbdc0a7e771aeb370a839118c4181932597d31 + 94931090134 ?
	18772 -										72084e6f2d7 last=66d012ad7f9  # rpc: calculate fees in getblock using BlockUndo data
	22918 rpc_getblock_prevouts_fees-0.21		ce365cd8a1c	last=5c34507ecbb
	(CHECK-LAST)	last=80612d8aded rpc_getblock_prevouts_fees-22
		# Was originally #16083, then #21245
		# Held back change of verbosity to class enum, and generally kept #16083 base
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
		# + docs from #23320 (left off refactor commit)
		# + doc fixes from #25615 & #25691
m	16795 rpc_inferred_output_descriptors-21+k	5d1bc19f6ca
		# NOTE: Includes custom refactoring to combine ScriptToUniv and ScriptPubKeyToUniv similar (but not identical) to master, to avoid possibly-incomplete backports
		# +#24636
		# + part of #25691 (implied in #22918 by this)
	18972 neutrino_whitelist-mini-21			dabdcf3f324	last=339fe189eb9
	(CHECK-LAST)	last=513465c7d6a neutrino_whitelist-mini
		# NOTE: Diff-minimised
	17034 psbt_ver_proprietary_xpub-0.21		0cbd65dd17d	last=81521173ba8 achow101/bip174-extensions
		# +#23975
	(CHECK-LAST)	last=634c311b833 psbt_ver_proprietary_xpub-22-mini
		# NOTE: Held back `gdd 078abaac27e dc93052363d` comment correction
		# NOTE: Didn't bother removing duplicate test
		# NOTE: Diff-minimised
		# NOTE: Now includes 16463 bip174_xpub-0.21+knots				8e6f8d3cc9c	last=9926a387eab achow101/bip174-xpub
	17631 rest_blockfilter-0.21					36a9777315b	last=2b64fa3251a TheBlueMatt/2019-11-filter-rest
		# +#23213 + #23836 (partial)
	(CHECK-LAST)	last=91feea1216a rest_blockfilter-22
		# NOTE: Dropped unrelated extra commits
	g319  gui_openuri_pastebtn-0.21				24178d81b5f	last=dbde0558ce7
	(CHECK-LAST)	last=33258aef4cb qt_openuri_pastebtn_shortcut-23
		# NOTE: Used to be #17955
	18014 siphash_optimise_pr18014-0.21+knots	0c346e55ba0	last=409c2e34522 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
m	18689 rpc_dumptxoutset_hr-21+knots			b79a47abcb6	last=65d0697fe34
	(CHECK-LAST)	last=e4004c28d7e rpc_dumptxoutset_hr-23+knots
	(CHECK-LAST)	last=a0acbce5122 rpc_dumptxoutset_hr
		# Held back refactoring & test improvements 9427b409195...5d0c86d494a (in rpc_dumptxoutset_hr)
		# TODO: Compat with(?) #24202
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202/files#r801191486
	18722 O_addrman_unordered_map-0.21+knots	008067709d9	last=a92485b2c25
		# NOTE: Restored C++11 compatibility from d6e782174ec
	g125  intro_prune_size-0.21					9d324c49f67
		# NOTE: Originally #18728
	19136 achow101/export-descriptor			6dacc070a6a	last=de6b389d5db
	19137 wallettool_dump-0.21+knots			a03a2b07990	last=23cac24dd3f achow101/dumpwalletrecords
	(CHECK-LAST)	last=858f74a8dd5 wallettool_dump_warning-22+knots
	(CHECK-LAST)	last=5009c359275 wallettool_dump_warning-23+knots
	(CHECK-LAST)	last=d4227721f64 wallettool_dump_warning-25+knots
		# NOTE: Disabled for BDB wallets since it doesn't dump/restore wallet id yet
		# NOTE: Changed to print warnings to stderr instead of stdout
		# NOTE: Diff-minimised
		# If bdb is reenabled, need #20267 49797c3ccfb
		# +#23834 achow101/dump-checksum-size
	19242 uaappend-21							c9099f45c3c	last=9552978b318 uaappend
	19463 prune_locks-0.21						ce3e7443523	last=b3a10bca9dd prune_locks
		# TODO: change default to temporary=true to match latest prune_locks branch?
		#		* 2554dc0ba3d Refactor PruneLockInfo.temporary to default to true
		# NOTE: Held back extra prune lock buffer & rebasing on #21726
		TODO: Check if any fix from #26215 is needed
	19762 ryanofsky/pr/named					3505e6dedbb	last=fa15c9b843b
	19776 -										2d98f923dec	last=343dc4760fd  # net, rpc: expose high bandwidth mode state via getpeerinfo
	19873 mempressure-21						368b6daca5d last=27d43142a0d mempressure
	20226 rpc_listdescriptors-0.21				e6939a88d7c	last=647b81b7093
	(CHECK-LAST)	last=90b7bb0121c rpcdoc_listdescs_active_internal-22
		# +#24977 [diff-minimised inline]
	21277 listdescriptors_normalized-0.21+knots	21a08339968
		# TODO: Drop 0.21.0 compatibility "desc" when return format is updated or 21329 is ready
	g291  gui_trafficgraph_vert-0.21			7d40296136d	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	21594 rpc_getnodeaddrs_network-0.21			6ae25fd6c1f
		# Diff-minimised / doc changes left out
		# Includes part of #20965 (GetNetworkNames)
	21843 rpc_getnodeaddrs_by_network-0.21		5e0ead94982
m	20254 i2p_static-21+knots					24dc32b1e18	last=8b4a3714b91 vasild/i2p_static
		# + a4693f44cfe from #20685
		# TODO: +21825 ? (needs 21560?)
		#TODO: +21914
		#TODO: +21407+21631
		# TODO??? 21514 vasild:ignore_port_in_i2p
	22211 i2p_IsRelayable-0.21+knots			8f8a6ed673d	last=7593b06bd12
	20275 list_unsupported_wallets-0.21+knots	45986c05cec	last=f3d870fc227 ryanofsky/pr/exist
		# Mostly rewritten?
	20295 rpc_getblockfrompeer_wo_header-21		8f143502034	last=dce8c4c3811 Sjors/2020/11/getblockfrompeer
	(CHECK-LAST)	last=da1bd8e31dc origin-pull/23813/head
	(CHECK-LAST)	last=22df64564bf origin-pull/24226/head
	(CHECK-LAST)	last=f5e008774b5 getblockfrompeer_param_names
	(CHECK-LAST)	last=3fa0053aabf rpc_getblockfrompeer_wo_header-22
	(CHECK-LAST)	last=6ecde0711d5 rpc_getblockfrompeer_wo_header
	(CHECK-LAST)	last=44516225c2d rpc_getblockfrompeer_wo_header-24+k
	(CHECK-LAST)	last=6d074a3f87c rpc_getblockfrompeer_nodeid_compat-23
	(CHECK-LAST)	last=ef1c43e51df rpc_getblockfrompeer_nodeid_compat
	(CHECK-LAST)	last=2ef5294a5bb jonatack/getblockfrompeer-param-inputs
	(CHECK-LAST)	last=4fe12e61847 rpc_getblockfrompeer_typecheck-23
		# +#23702 +(doc from #23813) +#24226
		FIXME: Consider reverting/removing 61a204efbe1: fetching enough old blocks may make a block file that gets pruned before the current height https://github.com/bitcoin/bitcoin/pull/23813#discussion_r1022184258
		# +#24944
		# +#25259
		# NOTE: Forward-compatible with peer_id param rename in #23706
		#21.xTODO# TODO??? API change * 60243cac728 rpc: turn already downloaded into error in getblockfrompeer
		#                           + * 34d5399211e rpc: more detailed errors for getblockfrompeer
		# TODO: Find a way to get `da1bd8e31dc test: Add test for getblockfrompeer on pruned nodes` w/o fastprune mode?
		TODO: +#28055 fix_getblockfrompeer_rereq_err
	20391 rpc_setfeerate-0.21					aef134635d5	last=1002e2d0d7f jonatack/setfeerate
	(CHECK-LAST)	last=4c0bc142de7 rpc_setfeerate-22
	(CHECK-LAST)	last=116199a46f4 rpc_setfeerate-23
	(CHECK-LAST)	last=41fc5b4002a rpc_setfeerate-24
	(CHECK-LAST)	last=86e4d4e1b79 rpc_setfeerate-25
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
m	20403 upgradewallet_pr20403-0.21+knots		5a4416104d5	last=3eb6f8b2e61 jonatack/upgradewallet-improvements
	20407 rpcauthfile-0.21+knots				389dda3a1a1	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
	(CHECK-LAST)	last=53383d94200 rpcauthfile-22
	(CHECK-LAST)	last=84513428151 rpcauthfile-24
	(CHECK-LAST)	last=004e3f8cee4 rpcauthfile
		# NOTE: fixed bug, added multi-line support, and added tests
	g149  intro_assumevalid-21					a434a92b063	last=cf940f0e5f5 intro_assumevalid
	(CHECK-LAST)	last=de495ad2f11 intro_assumevalid-23
	25339 rpcdoc_scantxoutset_20220611a-21					last=7862c4ac4e7 rpcdoc_scantxoutset_20220611a
	23549 rpc_scanblocks-21+knots				5eaa6ce2ea6	last=bb553d4478b jamesob/2021-11-scanblocks
	(CHECK-LAST)	last=71b7cdb460e jonasschnelli/2020/12/filterblocks_rpc
	(CHECK-LAST)	last=d28e8e4e277 rpc_scanblocks
	(CHECK-LAST)	last=d28e8e4e277 rpc_scanblocks-24+knots
		# NOTE: Was #20664
		# NOTE: Includes lots of additional fixes/doc improvements
		# NOTE: Now includes #21426 (scantxoutset no longer experimental) too
		# Held back insignificant comment/errormsg changes ab315e5294b...71b7cdb460e
		# Added return value documentation (needed for QA to pass)
		# NOTE: Was #20664
		TODO: Consider #26325 & #26508
	20702 rpc_getblocklocations-0.21			bc93fb1825b	last=9b03c654eb3
	(CHECK-LAST)	last=b60fdcbc2dc rpc_getblocklocations-22
	(CHECK-LAST)	last=05b618ead44 rpc_getblocklocations
		FIXME: Check range of nblocks (implicit int->size_t conversion)
		FIXME: gcp 1693dc78e9a
	20827 ibd_prune_max-21						894af588353	last=1d23d9515e9 ibd_prune_max
	(CHECK-LAST)	last=24f3936337d ibd_prune_max-22
	g163  gui_peer_conntype-0.21				a39642a4ef4  # jonatack-g/display-peer-conn-types
		# NOTE: Stripped unrelated string changes
	g180  gui_peer_relay_detail-0.21+knots		18243adb3a3	last=79a2576af1e jonatack-g/peer-details-connection-type-followups
		# +g203  Display plain "Inbound" in peer details
		# NOTE: Carries commit from g163 since it messes with the string anyway
		# NOTE: Left off final doxygen commit
	g179  gui_peers_conntype-0.21+knots			5a9d8b41bf9	last=be4cf4832f1 jonatack-g/add-peers-dir-and-type-columns
		# NOTE: Held back 9f76ba6597c...be4cf4832f1 (no real change once we add gui#363 on top)
	g363  qt_peers_directionarrow-0.21+knots	c76a8d4f215	last=727a2f83cca qt_peers_directionarrow
	(CHECK-LAST)	last=4d70dc134c2 qt_peers_directionarrow-22+knots
	(CHECK-LAST)	last=6d169ee0c55 qt_peers_directionarrow-23+knots
	(CHECK-LAST)	last=6d169ee0c55 qt_peers_directionarrow-25+knots
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
	20916 rpc_testmempoolaccept_wtxid-0.21		c5b8eb0a8b4	last=fa0aa87071e MarcoFalke/2101-wtxidTestmempool
		# Diff-minimised
	g162  gui_peers_detail_network-0.21+knots	9e73df68dc7
		# NOTE: Left out Peers table column & misc formatting changes
		# if merging full gui#599: * f0dbac928f1 GUI: Support translating peer network names
	20944 rpc_getmempoolinfo_total_fee-0.21		e0125b1b0d9	last=fa362064e38 MarcoFalke/2101-rpcMempoolTotalFee
		# NOTE: Minor code rearranging to avoid conflicts
		# +#23980 minor typo fix
	g186  gui_bumpfee_privacywarn-0.21+knots	725973ae6f9
	15129 rpc_removeaddress-0.21				013625c373f	#21.2TODO#last=fdbd01b50e0 benthecarman/remove_watch_only_address #21.2TODO
		# NOTE: Temporarily disabled! TODO: restore fixed
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	#21.2TODO#(CHECK-LAST)	last=??? remove_watch_only_address-22
	21319 getblock_optimise-21					def4cce130b	last=43882cf5240 getblock_optimise
		# Context: 17529 rpc: Faster getblock using PureBlock
	19763 p2p_no_relay_to_origin-0.21+knots		d2b73d2d218
	20365 wallettool_create_descriptors-0.21+k	24eb0deabc3
	21056 rpcwaittimeout-0.21					b26b2768222
	(CHECK-LAST)	last=fdc6e7cf753 fix_bcli_negtime_pr25157-23
		# +#22327
		# + second commit from #25157 fix_bcli_negtime_pr25157-23
	21141 walletnotify_blockhash-0.21			6ab2dc1a35a
	# Needs API finalisation: 21158 -  # lib: Add Taproot support to libconsensus
		#TODO: minimise
	21173 optimise_hexstr-0.21					211f7cf954e
	21260 rpcwallet_tx_in_mempool-21.1+knots	5e9dcde9997	last=46bf0b7b5d8
	(CHECK-LAST)	last=ee0a735e6c1 rpcwallet_tx_in_mempool-23+knots
	(CHECK-LAST)	last=faba549c582 rpcwallet_tx_in_mempool-24+knots
	g213  gui_payrequest_copyaddr-0.18			3fbc3512e3c
	g214  gui_payrequest_disablena-0.18+knots	88cfbc9641b
	21327 p2p_ignore_tx_in_ibd-0.21				cb54eca2c0b	last=6aed8b7e9b2
	(CHECK-LAST)	last=704a7b03d53 p2p_ignore_tx_in_ibd-22
m	21359 rpc_fundraw_includeunsafe-0.21+knots	78c5639bd85
	g205  gui_save_txview_reqview_columns-0.19	f5fcee6e0a3
		# +gui#368
		# NOTE: Diff minimised
		# NOTE: gui#229 not applicable to backport
		TODO: Check if gui#662 is needed
	g206  gui_peers_relayinfo-0.21+knots		d5d383b9daa
		TODO: +g676 jonatack/update-peers-transaction-relay-label-and-tooltip
		TODO: +g681 jonatack/relaytxes-tooltip-fix
	g226  gui_peers_lastblocktx-0.21+knots		8482728d1e2
	g230  gui_backup_formats-0.21+knots			6115edf25d3	last=7a2e4fb8d1a gui_backup_formats
	(CHECK-LAST)	last=4490d994755 gui_backup_formats-22
	(CHECK-LAST)	last=835d49b30bc gui_backup_formats-23
		# NOTE: To avoid conflict with wallettool_dump-0.21+knots, added 5ab50bc98db GUI: Omit DbDump option for backup of BDB wallets
	21595 cli_addrinfo-0.21+knots				7c408353347
		# NOTE: Adapted error message for Knots
	21602 rpc_listbanned_deltas-0.21			3462d5598d1
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rpc_maxmempool-0.21					9a2751a9347	last=040b280c661 rebroad/MaxMempoolRPC
	(CHECK-LAST)	last=6d95d708bf3 rpc_maxmempool
	(CHECK-LAST)	last=43eb542612e rpc_maxmempool-22
	(CHECK-LAST)	last=a05a4fe9fcd rpc_maxmempool-23
		# + bugfix and applying limit immediately
	22072 autoreindex-0.21						7fb696c631e	last=602f4da9178
	(CHECK-LAST)	last=069ccfcbc4e autoreindex
	22147 p2p_protect_last_outHB-0.21			995947de083
	# AFTER CORE RELEASES: (PR unknown) taproot descriptors +22156? +22166?
	22159 conf_append_cxxflags-0.10				b9c4f0c218e	last=fa14c6818f4
	# TODO, Ugly Hack w/ conflicts: g256  hebasto-g/210323-peers
	# Preferred simpler fix in gui#275: g330  jarolrod-g/prompt-icon-colorized
	g281  gui_console_fontsize_shortcuts-0.21+k	a9ed8095ab9
		# NOTE: Diff-minimised and moved AddButtonShortcut to avoid conflict with #553 later
	g293  gui_peers_services_wordwrap-0.18		a9065accdaa
	g298  gui_peers_altrowcolor-0.21+knots_pt1	281357e21fe
	g307  gui_peers_altrowcolor-0.21+knots		81f3be93772	last=fdf80937d1c hebasto-g/210501-stripes
	(CHECK-LAST)	last=dc89007d2c3 gui_peers_rowcolouropt
	(CHECK-LAST)	last=84206370984 gui_peers_rowcolouropt-22
	g309  gui_neticon_peerstab-0.18				f19b2295109
		# NOTE: Fixed Qt5.5 compatibility
		# Diff-minimised
	g318  gui_peers_copyaddr-0.14				ac1d7e09490	last=3ec061d9da0 jarolrod-g/copy-addr-peer
	(CHECK-LAST)	last=676b32e3717 gui_peers_copyaddr-22
		# NOTE: Added keyboard shortcut
		# NOTE: Fixed Qt5.5 compatibility
	g343  gui_instaprogress-0.19				a376b4cd1d9
	g362  kbshortcuts_context-0.21+knots		979ab82059f	last=e4c916a0ea0 kbshortcuts_context
	22288 torcontrol_dnslookup-0.21				192658456c6	last=cdd51e8ee15
		# Diff-minimised
	22372 multinotify-21						b002df55c73	last=2c4cbac9334 multinotify
	g469  qt_psbt_b64-21+knots					65f1d080b90	last=2c3ee4c3478 achow101-g/b64-psbt-gui
	(CHECK-LAST)	last=5f7a4882e39 qt_loadpsbt_b64-23
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	# Needs review & MUCH softer deprecation: 24098 -  # rest: Use query parameters to control resource loading
	# After merged+released a while? 24171 sdaftuar/2022-01-download-from-inbound
	# Check if fixes anything: 24178 sdaftuar/2022-01-headers-response-requires-minchainwork
	24198 rpc_wtx_wtxid-0.20								last=7abd8b21ba3  # wallet, rpc: add wtxid in WalletTxToJSON
	(CHECK-LAST)	last=954bc3e5e73 rpc_wtx_wtxid-23+knots
	# SENDING ONLY? Needs work: 24897 w0xlt/silent_payment_021
	g526  qt_peers_addrprocessed-21+knots
	# Maybe? 25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
	25439 rpc_gmpi_incrementalrelayfee-21+knots
	# Maybe? Tho pretty big conceptually... Review: 25504 darosior/rpc_track_coins_by_descriptor
		# +#26037
	# Needs work & applicability check: 25680 -  # rpc, docs: Add note for commands that supports only legacy wallets
	# Needs review: g655 -  # Persist "mask values" in gui
	-     guix_shell_compat-24
		# More compatible alternative to #26077 fanquake/guix_shell_over_environment
	Needs review: 26088 -  # init: Add option for rpccookie permissions
	Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
		Only if too few current fixed seeds are valid?
	Needs work: 26131 jamesob/jamesob-22-09-log-rpc-port
	Minimised as applicable: 26162 Sjors/2022/09/taproot
	IF IN KNOTS: Needs review: 26174 w0xlt/list_address_book
	Compatibility with: MERGED 26194 w0xlt/next_index_listdescriptors
	26280 -  # rpc: Return coinbase flag in scantxoutset
	26645 -  # util: Include full version id in bug reports
	Triage: Needs work: 27409 ryanofsky/pr/1data
	Ensure Ctrl-L clears debug console (see g#702 for inspiration)
	Triage: Needs review? g740 -  # Show own outputs on PSBT signing window
	27278 jamesob/2023-03-log-new-headers
	Partial: Needs review? 27826 Sjors/2023/05/saw-header
	Triage: Needs review: 27827 josibake/silent-payments-base-pr-slim-down
	If a clear win: 28101 -  # init: changing -torcontrol help to specify that a default port is used

	#21.xTODO# Decide if above minor features need to wait for 21.3, or can go in 21.2.1
# Non-progress functionality:
	8751  sort-multisigs-0.21					0cd85c73c6f	last=e11cb50a09  # multisig sorting
	(CHECK-LAST)	last=db2b618ec07 sort-multisigs-22
	(CHECK-LAST)	last=8db63499737 sort-multisigs-23
	(CHECK-LAST)	last=d353a124a49 sort-multisigs-25
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152  sweepprivkeys-0.21					2aeaeeb1ba1	last=724b597973c sweepprivkeys
	(CHECK-LAST)	last=6fcb1e43426 sweepprivkeys-22
	(CHECK-LAST)	last=ba17ce68d20 sweepprivkeys-23
	9245  ionice-21								d935e6fc4ab	last=abb0e433efa ionice
	(CHECK-LAST)	last=6de915d6dc0 ionice-22
	(CHECK-LAST)	last=b4647b23813 ionice-24
		# NOTE: Left off deprioritisation of LoadExternalBlockFile, ReplayBlocks, RollforwardBlock(22.x?)
	-     ionice_win-0.21						1c6f29b3e4f	last=b19d30dc8c5 ionice_win
	(CHECK-LAST)	last=b59bc253116 ionice_win-22
	(CHECK-LAST)	last=65dcf0dc11c ionice_win-23
	8501  old_stats_rpc-0.21					3eee2d40dbe	last=7af0ea43b2
	(CHECK-LAST)	last=8cfab679cb2 old_stats_rpc-22
	(CHECK-LAST)	last=040565d1047 old_stats_rpc-23
	(CHECK-LAST)	last=6d5ac5aea11 old_stats_rpc-25
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-0.21						65892ef0064	last=63fb11652f
	(CHECK-LAST)	last=9b99d9c327b old_stats_qt-22
	(CHECK-LAST)	last=aa3f38ecd79 old_stats_qt-23
	(CHECK-LAST)	last=07558897347 old_stats_qt-25
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-0.21					5e32058f65a	last=07fc81109a
	(CHECK-LAST)	last=d6299945048 dumpmasterprivkey-22
	(CHECK-LAST)	last=5e01bd283b8 dumpmasterprivkey-23
	(CHECK-LAST)	last=5ba765db629 dumpmasterprivkey-25
	g444  gui_netwatch-0.21+knots				842149fff05	last=f225d264255 gui_netwatch-25+knots
	(CHECK-LAST)	last=7f59a6deb52 gui_netwatch-22+knots
	(CHECK-LAST)	last=9482300fab7 gui_netwatch-23+knots
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-0.21+knots			bae1509a9d1	last=8ea217e7251 multiwallet_rpc-25+knots
	(CHECK-LAST)	last=d927c064439 multiwallet_rpc-22+knots
	(CHECK-LAST)	last=1a2bc175ffc multiwallet_rpc-23+knots
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-0.21+knots					a6b0a8894fb	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	(CHECK-LAST)	last=39cf88db90b zmq_wtx-22+knots
	(CHECK-LAST)	last=71689c52c52 zmq_wtx-23+knots
	(CHECK-LAST)	last=bc3dd51021b zmq_wtx-25+knots
	20551 rpc_onetry_conntype-21				d7fcef7c236	last=f3e6badeeb4 rpc_onetry_conntype
	(CHECK-LAST)	last=7661ce6ddaf rpc_onetry_conntype-22
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment-0.21+knots	d4765cc92bd	last=0971192425f relax_invblk_punishment
	(CHECK-LAST)	last=57903e3f34d relax_invblk_punishment-22
	(CHECK-LAST)	last=0971192425f relax_invblk_punishment-23
		# Held back 0971192425f QA: Use addconnection rather than addnode onetry
	10350 filtered_witblock-0.21				4e1122ece17	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
	(CHECK-LAST)	last=6bf4092cb7b filtered_witblock-22
	(CHECK-LAST)	last=478e92981cc filtered_witblock-25
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				c4c8ec10f47	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-21+knots						1009e765049	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	(CHECK-LAST)	last=5d5b2fb8442 rest_fee-0.21
	(CHECK-LAST)	last=cec2e1bb857 rest_fee-22
	(CHECK-LAST)	last=2c51873b614 rest_fee-23
	(CHECK-LAST)	last=8f4b72a2951 rest_fee
		# Fixed a minor bug in conf_target range check
		# Added functional tests: 5d5b2fb8442 QA: Exercise REST interface in feature_fee_estimation
	11803 bugfix_dumpwallet_hdkeypath-0.20		280b1276bfb
	(CHECK-LAST)	last=a6d25571113 bugfix_dumpwallet_hdkeypath
	12965 scriptthreads-0.20					095986b847a	last=dfab6c6866 jonasschnelli/2018/04/svt
	(CHECK-LAST)	last=f6052208ab0 scriptthreads-22
	(CHECK-LAST)	last=12e673a8c23 scriptthreads
		# Held back RPCResult NONE cuz undocumented is actually better
		FIXME: Check if there's an off-by-one in nScriptThreads vs script_threads (and that it all actually works)
	13203 dsha256_power8-0.20					357397180c7	last=3b402e0738 TheBlueMatt/2018-05-asm
	(CHECK-LAST)	last=a72483b8e14 dsha256_power8-23
	(CHECK-LAST)	last=3a1ad464f2e dsha256_power8-25
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		60c82d4c598	last=140e4307add dsha256_power8_asm_pragmas-25
	15218 postibd_flush-21+knots				8858f44e523	last=d2ecb70d64  # validation: Flush stateafter initial sync
	(CHECK-LAST)	last=8faeb93d48d postibd_flush-22+knots
	(CHECK-LAST)	last=6bd37fe1133 postibd_flush-23
	(CHECK-LAST)	last=940eb7c7e81 postibd_flush-25
	15428 tor_gui_pairing-0.21+knots			9b710f4ddfb	last=443570660ef tor_gui_pairing-25+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 16cb2ae1fe0)
	(CHECK-LAST)	last=4a881554991 tor_gui_pairing-22+knots
m	15421 tor_subprocess-0.21+knots				ccf77ea4de5	last=58c6cafd3a1 tor_subprocess
	(CHECK-LAST)	last=1fae7eff568 tor_subprocess-22+knots
		TODO: Add boost_171_177_workarounds
			# NOTE: Originally part of #25111 hww_windows replaced by #25696 (merged)
	15633 nohbcbfornonwit-0.21+knots			f81d53ce8c5	last=f5e4f1650fe nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# TODO: 16490 MarcoFalke/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					975064084f4
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning-0.21+knots		d001554bb8d	last=c6d1e2e1b99 restore_vbits_warning
	(CHECK-LAST)	last=896eea449ad restore_vbits_warning-22
	20832 rpc_validateaddress_error-0.21.1+k	0859c222db0
	16807 bech32_error_detection-0.21.1+knots	c08a0bcebf7	last=88cc4810926 meshcollider/201909_bech32_error_detection
	(CHECK-LAST)	last=3bc568d6753 old_bech32_error_detection
		# Held back rewrite 3bc568d6753..974227bb457 for now; when updating, add in #23577
		# Held back comment drop 974227bb457..88cc4810926
	n/a   rpc_compat_error_index-0.21+knots		e8b159d62b3	last=1f7f17db21d rpc_compat_error_index-25+knots
	(CHECK-LAST)	last=e480af6868c rpc_compat_error_index-22+knots
	(CHECK-LAST)	last=57e05a6f13c rpc_compat_error_index-23+knots
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos-0.21.1+knots		a4921198f16	last=539beeaae85 gui_bech32_errpos
	(CHECK-LAST)	last=7532115c6d8 gui_bech32_errpos-22+knots
	(CHECK-LAST)	last=954bb8ca738 gui_bech32_errpos-23+knots
	(CHECK-LAST)	last=a949fb06d73 gui_bech32_errpos-25+knots
NM	16807 bech32_error_detection-0.21+knots		c0339fe9c28	last=54e107add41 meshcollider/201909_bech32_error_detection
NM	-     gui_bech32_errpos-0.21+knots			ae0986b142d
	17636 guisettings-0.21						aec700dd5c2	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo-0.21+knots			31332337e68	last=cdbd38df131  # getgeneralinfo RPC
	(CHECK-LAST)	last=65f6caeebbd rpc_getgeneralinfo-22
	(CHECK-LAST)	last=a1874220367 rpc_getgeneralinfo
	18223 blockfilter_v0-0.19					a1d7fc7821f	last=5561e7a0c79
	(CHECK-LAST)	last=27827c9b892 blockfilter_v0
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances-0.21+knots		98e3ae63888	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	(CHECK-LAST)	last=cd48a6982ca cli_getinfo_mwbalances-22
	(CHECK-LAST)	last=66dddec6601 cli_getinfo_mwbalances
	19092 cli_getinfo_mw_total_balance-0.21+knots	5672474d49e	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=e8bab0a4077 cli_getinfo_mw_total_balance-22
	(CHECK-LAST)	last=abc086174b3 cli_getinfo_mw_total_balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
m	18570 wallet_rpc_lastprocessedblock-0.21+k	75d59808743	last=1e868bbbb1b
	(CHECK-LAST)	last=363c4e02d3d wallet_rpc_lastprocessedblock-22+k
	(CHECK-LAST)	last=dc58f8f46e6 wallet_rpc_lastprocessedblock-23+k
	(CHECK-LAST)	last= wallet_rpc_lastprocessedblock-25+k (based on #26094)
		TODO: Bump to #26094 (at least check for fixes)
	19117 rpc_getrpcwhitelist-21				f005cd98854	last=d87cd4f47ed rpc_getrpcwhitelist
	(CHECK-LAST)	last=3a5869713b4 rpc_getrpcwhitelist-22
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.21+knots	e2bae466a89	last=e58e7666948 getrpcwhitelist_wallets-25+knots
	(CHECK-LAST)	last=1e1d1e2e62c getrpcwhitelist_wallets-22+knots
	(CHECK-LAST)	last=fad1716d500 getrpcwhitelist_wallets-23+knots
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-0.21+knots	d50c4c7d4af	last=36cc299baee whitelist_outgoing
	(CHECK-LAST)	last=9cf184186c9 whitelist_outgoing-mini-22+knots
	(CHECK-LAST)	last=27ad690c9d2 whitelist_outgoing-mini-23+knots
	(CHECK-LAST)	last= whitelist_outgoing-mini-25+knots
		# NOTE: d756d0a01a6 needs legacyWhitelisted in minified version!
		# NOTE: Originally #10594
		Being replaced with #27114
	g165  gui_peers_splitter_ss-0.21+knots		b71e008e2cf
		# +g194 Save/restore RPCConsole geometry only for window
		# NOTE: Changed setting name since our peer table width doesn't match Core's
		# TODO: Each release, see if we need to bump setting name (and figure out back compat?)
	# Needs review: (MAYBE JUST PART OF) g539  RandyMcMillan/1643263956-network-graph-issue-532
# Non-upstreamed functionality:
	-     gui_payreq_textedit-0.21				bfe154411de last=79b7acbf7ec gui_payreq_textedit
	-     rpc_mempoolentry_txhash-0.20			0b5a0196787	last=f72fb60b048 rpc_mempoolentry_txhash
	-     walletnotify_w_win-0.21+knots			103ea74ed61	last=a03bca904fa walletnotify_w_win-25+knots
	(CHECK-LAST)	last=4c481517859 walletnotify_w_win-22+knots
	14137 win_taskbar_progress-0.21+knots		cf8835a0b82	last=18eb4dbb8a
	(CHECK-LAST)	last=f30b740b4ff win_taskbar_progress-22
	(CHECK-LAST)	last=de45972a3f2 win_taskbar_progress
	-     restore_blockmaxsize-21				244ddb8587d	last=d9191ae38dd restore_blockmaxsize
	(CHECK-LAST)		last=0df4a820dd6 restore_blockmaxsize-22
	(CHECK-LAST)		last=d66d020e9d2 restore_blockmaxsize-23
	7107  qtnetworkport-21						1c31de03b71	last=1f37c87 origin-pull/7107/head
	(CHECK-LAST)	last=061cd3f46cf qtnetworkport-23+knots
	(CHECK-LAST)	last=1f5f7db944c qtnetworkport-25+knots
m	7533  sendraw_force-21+knots				84c7abed1ab	last=8b4a4f9b2b4 sendraw_force
	(CHECK-LAST)	last=074e22628db sendraw_force-22
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf-0.21							901121d0ce9	last=3e6f24bf30b rwconf-25+knots
	(CHECK-LAST)	last=ad7812c9eb7 rwconf-22
	(CHECK-LAST)	last=3e6f24bf30b rwconf-23+knots
	7510  rwconf_gui-0.21						2df27d4a04e	last=11539fbed54 rwconf_gui-25+knots
	(CHECK-LAST)	last=5465696bf16 rwconf_gui-22
	(CHECK-LAST)	last=11539fbed54 rwconf_gui-23+knots
		# NOTE: Missing cac3d7873a3 due to not having #15946 in 21.x
m	559   accept_nonstdtxn-21+knots				0d7a5178261	last=2e2ecd0eeab accept_nonstdtxn
	(CHECK-LAST)	last=d2a16fe9618 accept_nonstdtxn-0.21
	(CHECK-LAST)	last=75b02a00617 accept_nonstdtxn-22
	(CHECK-LAST)	last=f9cf9320e2d accept_nonstdtxn-25+knots
	g153 const_max_digits						32e16e210f2
	 929  tbc-21+knots							8aa517b2bd1	last=ec29a85b5f6 tbc
		# NOTE: Held back 6a4900bc4e6..ec29a85b5f6 (UCSUR output is a feature?; "fix" ec29a85b5f6 doesn't seem to affect anything)
		# if merging full gui#599: deal with possibly silent conflicts
	 553  bugfix_qt_uri_amount_parser-0.17		ce9be680833	last=4d1d8e41188 bugfix_qt_uri_amount_parser
m	-     mining_priority-0.21+knots			1e33269a0ae	last=a284d6253ff mining_priority
	(CHECK-LAST)	last=58e2cab4b18 mining_priority-22
		# Didn't backport next_block_height passing (maybe consider when/if someday cs_main can be released)
		# Didn't backport platform-independent double serialisation
	5861 gui_restore_addresses-0.16				a81fd2b77ff	last=3ad197c5c69 gui_restore_addresses
	5891  qt_console_history_persist-0.21+knots	831cc0d61d1	last=0cd5fc301d6 qt_console_history_persist
m	7219  rbf_opts-0.21+knots					6b8135375e9	last=eb6bb1e3528 fullrbf # missing 91786d16ccc + revert34ae6640174
	(CHECK-LAST)	last=8db545872f6 fullrbf-22+knots
	(CHECK-LAST)	last=149b286b44e fullrbf-23+knots
	(CHECK-LAST)	last=475d87b5342 mempoolreplacement_2022
		# NOTE: Held back "clean mempool" from b81235ee156 (not needed in 21.x?)
		# NOTE: Re-PR'd as #25373
		# NOTE: Compatibility with #25353 -mempoolfullrbf option is in rwconf_policy
		#21.xTODO# When/if adding minor features:
			# aae66ab43d7 (#25353) Add 'fullrbf' return field to getmempoolinfo RPC
			# f4f83f73a7f (#25626) Add 'replacement_policy' return field to getmempoolinfo RPC
		FIXME: Adapt to 24.x changes - make advertising optional??
	12146 opt_wallet_segwit2-0.21				ffc242d52be	last=67725950be9 opt_wallet_segwit2
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			fbd5c1d14f4	# Latest code now
	-     gui_request_payment_label-0.19		803f33b7c43
	-     gui_peers_sort_network-0.21+knots		0ea3b567d9c
	(CHECK-LAST)	last=3ae2746dcf7 gui_peers_sort_network-22
	(CHECK-LAST)	last=c22bbba9689 gui_peers_sort_network-23
# Non-upstreamed Knots compatibility:
	-    preserve_unsupported_keyflags			bde74230139
	-    mempool_knots014_compat-0.21+knots		ffc4f556b8a	last=1befffc0b48 mempool_dat_extensible
		# NOTE: Load-only
NM	9422  mempool_dat_extensible_mod-0.21+knots	dc44eb1b7ae
	11413 rpc_feemode_explicit_compat-0.21+knots	194343ec101 last=56553e0d43c rpc_feemode_explicit_compat-22
	-     netperms_implicit_addr-0.21+knots		7d39ba69a9e	last=e4402815c4d netperms_implicit_addr
	(CHECK-LAST)	last=d1ce634b708 netperms_implicit_addr-22+knots
	12674 rpc_onetry_nonpriv-0.21+knots			7607b0cb005	last=87f22fc9661 rpc_onetry_nonpriv-25+knots
	(CHECK-LAST)	last=054c2214369 rpc_onetry_nonpriv-22+knots
	# Maybe? 24963 rpc_walletprocesspsbt_options
	TODO: gui_peers_bump_setting_keys equivalent?
	# TODO: add a bitcoinknots.conf ?
# POLICY:
	-    1day_default_conftarget				3f1c8d8ab40
	-     bytespersigopstrict-0.21+knots		c021176f67a	last=0cfa0880376 bytespersigopstrict-25+knots
	(CHECK-LAST)	last=712c7abc3a1 bytespersigopstrict-22+knots
	(CHECK-LAST)	last=43d7d3889cf bytespersigopstrict-23+knots
	9749  unique_spk_mempool-0.21+knots			52cb2331dee	last=2e3a780f5a7 unique_spk_mempool-25+knots
	(CHECK-LAST)	last=36bb6460136 unique_spk_mempool-22+knots
	(CHECK-LAST)	last=7882096ddef unique_spk_mempool-23+knots
	-     bloom_default-0.21+knots				ab9afbc6fee
	TODO: Adapt existing limits to apply to Taproot?
	-     enforce_checkpoints-0.21				09feeecfdfe	last=86dfb334158 enforce_checkpoints
	n/a   checkpoint_update-0.21				67bc16f3c2a	last=a382b8620eb checkpoint_update-25
	(CHECK-LAST)	last=37271214dfe checkpoint_update-23
		#21.xTODO# Add new checkpoint
	10282 timebomb_knots-21						4d798a3f50b	last=7612a464d3a timebomb_knots
	-     rwconf_policy-0.21+knots				1d0a8a7bf36	last=6a06b3f2b3b rwconf_policy-25+knots
	(CHECK-LAST)	last=f89126d2136 rwconf_policy-22+knots
	(CHECK-LAST)	last=6a06b3f2b3b rwconf_policy-23+knots
		# Include Knots policy changes for simplification of final rebase process
		# Held back git diff 19fd29ce45d..af4614fbd26 which is likely a noop
		# Added -mempoolfullrbf compatibility (see #25353)
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		e0a236336e2
	7483  svg_icon-21.2+knots					10090268130	last=75796f01b75 svg_icon-25+knots
	(CHECK-LAST)	last=afaab080b87 svg_icon-22+knots
	(CHECK-LAST)	last=75796f01b75 svg_icon-23+knots
		# NOTE: Held back guix support 64ed5a651d7...75796f01b75
# BRANDING:
	n/a   update_security_policy-21
		# Includes (part of #23450) remove Jonas, #23466 keyserver, #25850 remove laanwj, #25910 add achow101
	n/a   knots_branding-21						9db64a56d30	last=16035761f8b knots_branding-25
	(CHECK-LAST)	last=282420dea44 knots_branding-22
	n/a   ver_dropzero-21.2+knots				0d04104e95d
		# this should be 21.1.1 I guess? keeping 21.2.0 for now to match Core...
		# TODO: bump ver properly when Core abandons it
#FIXME: check there's no univalue push_back(bool) - see #20424 and stash 8724e2fae4
#FIXME: Check there are no menu icons
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --no-merges --pretty='%s' v0.21.2..|sort|uniq -c |sort -n
#       EXPECTED:
#           2 Add Bech32 error location function
#           2 GUI: Initialise DBus notifications in another thread
#           2 GUI: Point out position of invalid characters in Bech32 addresses
#           2 GUI: Support returning positions from BitcoinAddress{Entry,Check}Validator::validate
#           2 build: improve macro for testing -latomic requirement
#       lol  # look for ^\|/ branch points later than the tag
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
#TODO: Make sure there's no f' f" in python code: git grep '\bf['\''"]' $(git ls-files | grep '\.py$')
#TODO: Make sure there's no \d'\d or 0b\d+ in C++ code: git grep '[0-9]'\''[0-9]\|\b0b[01]\+[^2-9][^0-9a-z]'
#TODO: Make sure there's no Qt5.5 incompatibilities: git grep 'addAction(.*\[.*\]\s*{'
#TODO: Make sure there's no -Wc++14-extensions triggered
#21.xTODO# Make sure there's no optional .has_value() (Boost 1.68 dep) or std::optional (should be Optional typedef) - git grep 'std::nullopt\|std::optional\|<optional>' - tolerated inside src/test/fuzz
#TODO: Make sure there's no 'build_bitcoin_util\b|natpmp'
#21.xTODO# Run #25243 to pick up on missing bash completion updates
#21.xTODO# Check there are only [[noreturn]]s in: git grep '\[\[[a-z_]\+\]\]' src (nodiscard, maybe_unused, etc are C++17)
#21.xTODO# Check on #21508
Triage: TODO: Ensure std::filesystem isn't introduced (see #28076)
	n/a  (cherrypick=e0968d0328b2877330)		fbd68408390	# doc/{bips,files}
		TODO: If applicable, #26443
	n/a  knots_bips-21							95f1a0c7adb
	n/a  (bump_version=Knots:20210629)			27c16a89cc5  # DO NOT CHANGE for just fixes
#	n/a  knots_historical_relnotes				61100a2
	TODO: Ensure NSIS doesn't bundle _Core_ relnotes either! See #25809; also see #26139
	n/a  (cherrypick=1c6a7f409ff)				f1e6ee7f195  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		540190c138f for #24198
		TODO: Merge in 202208-KnotsDepsPlan
	n/a  (cherrypick=a76c71bf46b)				42a7a1b3d52  # update manpages (build first)
		BELOW TODO: ensure 26117 is fixed
	n/a  (cherrypick=3b34e884d32)				2d4f6166a4b  # translation update
@21.x-knots-extratests
# EXTRA TESTS:
	24797 -  # test: compare /chaininfo response with getblockchaininfo RPC
	25733 fanquake/tidy_enable_bugprone_use_after_move
	26519 -  # test: Add getpeerinfo test for missing version message
# NOTE: use git diff --minimal for patches!
