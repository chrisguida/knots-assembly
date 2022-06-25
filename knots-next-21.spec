timestamp 2022-06-18 10:52:32
#lastapply no-merge

#.. checked up to PR #22369 / gui #375 for features
#.. checked up to PR #25412 / gui #618 for fixes

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
	# Not worth it: 24295 -  # Remove std::move from fs wrapper to work around -D_LIBCPP_DEBUG=1 bug
	24633 bugfix_suppresswarnings_regex
# SYSLIBS: (and old build bugs)
	5872  subdir_incl_compat-0.10				9815be994a1	last=1490995c122 subdir_incl_compat
	2241  sys_leveldb-21+knots					60cd0a8e2fb	last=bd02e19eaf5 sys_leveldb-22+knots
	5416  sys_libsecp256k1-0.21+knots			813a5353e1d	last=da31940ec9e sys_libsecp256k1
	n/a   sys_univalue_doc-21								last=77c4f3e3af9 sys_univalue-23+knots
m	7485  sys_univalue_def-21					c393c7a7f51	last=cf9e588e22f sys_univalue_def-23+knots
	13789 bugfix_asm_pragmas					e33b0f86575
	-     bugfix_asm_leveldb_check-0.20			15cb5704a2a	last=3ca799db25f bugfix_asm_leveldb_check
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
	20594 conf_getauxval-0.21					563aacf22be	last=836a3dc02c7 jonas/2020/12/getauxval
	#Maybe restore: 7339  opt_libevent
	23716 qa_own_ripemd160-21					a93adb92909
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
	n/a   knots_ci_tweaks-21					a30b2c8bb0f
	#TODO: Can we get a minimum-dep-versions CI going??
# FIXES:
	# Only needed for focial gitian?? 22318 hebasto/210623-random								last=35aab4f0c0b aka depends_no_getrandom
	18818 fix_gitian_src_202004-21				01cd0f44b87	last=690985474a5 guix_reltar_autogen_distclean
	18902 fix_gitdir_again-21					9e6238975fe	last=dc420103874 fix_gitdir_again
		# NOTE: based directly on #18818
	24048 fix_pkgconf_missing-21
	18427 2020mingwthrd-mini-21					f4f276a44ae	last=df5ece3e064 2020mingwthrd
	(CHECK-LAST)	last=d9fd23bb08d 2020mingwthrd-mini
	18490 bugfix_symcheck_pe_case-21			dae51d82243	last=24a69574ece bugfix_symcheck_pe_case
	17828 p2p_log_categories-21					6ed22dedbde	last=04960621582 practicalswift/log-categories
	(CHECK-LAST)	last=137964d82dc p2p_log_categories
	19832 hebasto/200829-log					d64d3aaa576	last=1816327e533
	20845 net_logcategory_localdisconnect-0.21	11e46eb9473	last=fa55159b9ed marco/2101-netLogDisconnect
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 laanwj/2018_12_http_bind_error		8ff26264445	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	(CHECK-LAST)	last=8520c437a0d http_bind_error
	-     http_bind_error+extra-21				1d09d2dc41d	last=fd5353ed826 http_bind_error+extra
		# NOTE: Held back annotation in gdd 785429c2c7a fd5353ed826
	9524 marco/Mf1701-qaPruning					e8a96411986	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment-21					fb6f182d5c4	last=fa16d94b095 log_more_uacomment
	14485 fadvise-0.20							ebbe8fe4097	last=3f2c08b8202 fadvise
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
	-     bugfix_rpc_getbalance_hacky-0.21		1413e85f702	last=e8a9f9c83eb bugfix_rpc_getbalance_hacky
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
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	g404  bugfix_qvalidlineedit					05f54638d31
		# Was #18133
	18194 bugfix_gui_edit_sendaddr-mini			2747e096a1e	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	18335 -										dc0f3b960be	last=8dd5946c0b7  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	18466 -										7963fb63fea	last=a5cfb40e27b  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	18729 intro_dont_change_user_prune			0af71102295
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
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# TODO: g18   hebasto-g/200701-peer
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	19884 fixedseeds-0.21						35264ce4152
		# +partial #21254 (bugfix only)
	22798 doc_fix_pr22798-21.1					4ab4007c290
	19888 getblockstats_utxo_actual-21.1+knots	2a7f36a8d4a	last=884e7e1f95b
	(CHECK-LAST)	last=6fb4286f0eb getblockstats_utxo_actual-22+knots
	(CHECK-LAST)	last=937d948b76f getblockstats_utxo_actual-23+knots
		# Held back additional tests
	# Needs review: 20196 vasild/fix_GetListenPort
	g87   hebasto-g/200910-mono					df127c75a99	last=2e386cd3dd3
	20234 fix_bind_any_pr20234-21  # net: don't bind on 0.0.0.0 if binds are restricted to Tor
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	g121  fix_qt_early_sub_signals-21			ea2340e5824
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	20448 unloadwallet_namematch				34dfe668f49
	# Needs consideration.. why would we re-announce to the same peer?? 20561 sdaftuar:2020-12-moar-addrz
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					dbff865256f
	-     bugfix_gui_drop_abc_confusing_hack	6e1b3b65525
	20805 copyright_2021-0.21					c69ba0b3e58
		# NOTE: Diff-minimised
		#21.xTODO: Bump in 2022+
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
	g217  gui_clickable_warning-0.11			21f8d05d194	last=67c59ae4793 jarolrod-g/warning-look-like-button
	# Needs careful review: g219 hebasto-g/210223-toolbar
	g236  gui_init_walleterror_cont-21			11342604e1e	last=cc85951352a gui_init_walleterror_cont
		# NOTE: Held back refactoring 0b00fd650e1...fb3ea0ad3a8
	# Complex: 21007 hebasto:210316-fork
		# +21447 TODO
	# Needs #21007, complex: 21418 laanwj/2021-03-systemd-daemonwait
	# TODO: Last commit? Diff-minimised somehow? 21560 laanwj/2021-03-torv3-hardcoded-seeds
TM	21644 bugfix_addlocal_downloadbind-0.21		1ec9cfb310f
	21752 fix_feerates_kvB_pr21752-21
	21822 bugfix_cli_pr21822-0.21				a212e7c0446
TM	21907 listwalletdir_iterate_inf-0.19		1483674ad69
	21944 fix_listwalletdir_rootdir-0.21+knots	0cb9e8948d1
	22013 ignoreblockrelayfordnsskip-0.21		8216936b4d9
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	19315 rpc_addconnection-0.21				0ec207c9478	last=7d85d477730 rpc_addconnection_mainnet
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
	# Needs review: 22362 marco/2106-addrdb  # Drop (only) invalid entries when reading banlist
	22417 bpchild_closefds-21+knots				ae04745f860	last=4c19cea484b bpchild_closefds
	(CHECK-LAST)	last=9b9cdc9ae6f bpchild_closefds-0.21
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
	22879 fix_addrman_err_format-21				2340bf42de5	last=fab0b55cf06 marco/2109-testPeersDat
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
		# NOTE: Left off trivial string change
	g439 gui_hide_unused_icons-0.20				823c85e38d4
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs review: 23197 jonatack/fix-netaddress-UB-and-banman-fuzz-crash
	# Needs review: 23227 marco/2110-ToIntegral
	# Needs review of backport-rewrite in qt_catch_rpc_index_overflow-0.18 [alt to g446  marco/2110-qtRpcCons]
	# TODO: 23268 prayank23/dns-seed-fqdn
	# TODO: 23253 marco/2110-utilTxSeqId
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
	# Needs work/diff-minimisation: 23418 marco/2111-txPoolPrioOverflow
	# Needs review/diff-minimisation: 23486 marco/2111-rpcScript
	# Needs work: 23502 achow101/tr-low-fee-est
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	# Needs review: 23628 -  # Check descriptors returned by external signers
	# Needs review: 23631 -  # p2p: Don't use timestamps from inbound peers for Adjusted Time
	23634 rpc_scantxoutset_examples-21			f8148f4d430	last=1ed5681407a theStack/202111-rpc-add_scantxoutset_examples
	20556 doc_fix_pr20556-21					0e40564787e
	# Embedded font not in 21.x! g477  gui477_fix_mac_console_font-0.13  # Monospaced output in Console on macOS
	23644 wtx_timercvd_noadjust-21				f254b23b7d0
		# Diff-miniised
	# Needs correctness verification (especially startingheight which changed in 22.x): Diff-minimised 23652 marco/2112-docOptPeer
	# Needs review: 23673 hebasto/211204-native
	23750 docfix_importdesc_range_no_label-21	397093e7779	last=65efbba45d8 darosior/no_label_range_descriptors
	g506  qt_qrcode_sizefixes					4724488fe3d
	# idk? 23781 hebasto/211215-bptest
	23858 fix_qa_scantxoutset_pr23858-21
	23937 fix_rpcdoc_dumptxoutset_pr23937-21
	# Needs work: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs work: 24038 marco/2201-lockstuff #21.xTODO
	g508  fix_qt_progressrate_pr_g508-0.16
	g516  qt_recvreq_show_eyeicon-0.14
		# Diff-minimised
	# Needs review: 24066 whitslack/openrc-daemonwait
	24067 wallet_no_final_checks-21
	# Needs work: 24072 -  # doc: fix wording of alertnotify to match behaviour
	#21.xTODO# Needs review: 24090 RandyMcMillan/1642450390-issue-24049
	24095 fix_settings_jsonfmt-21
	24117 fix_index_dontcommitduringinit-21					last=bfcd60f5d50  # index: make indices robust against init aborts
		# NOTE: partial: coinstatsindex and feature_init test aren't in 21.x
	24145 fix_mempool_clear_txhashes-21						last=9d65ad365c5  # Clear vTxHashes when mapTx is cleared
	24168 fix_dumpbanlist_races-21
	# TODO? 22762+24201 -  # p2p: Avoid InitError when downgrading peers.dat
	#21.xTODO#Diff-minimise: 24231 -  # streams: Fix read-past-the-end and integer overflows
		#TODO: Substitute for 24253 (removes broken unused methods)
	24287 fix_genmanpages_tagver-0.19
	# Needs work: 24313 Sjors/2022/02/displayaddress						last=803387f054d
		# TODO: make sure this doesn't break compatibility (and fix review bugs)
	# Needs work/correctness: 24318 -  # doc: ZMQ documentation fix regarding topics
	22087 validate_port_opts-21								last=1dae86bfd22  # Validate port-options
	(CHECK-LAST)	last=d7f85a72354 validate_port_opts-23+knots
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
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
	# Wait for #24409? Or at least until merged in Core...? 24428 fanquake/improve_bitcoin_wallet_return
		# NOTE: rebase w/o 24409 in f41a608a397
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
	# Very annoying, needs care not to prematurely doc things; do draft on 21.2.1 tip #21.xTODO#: Triage: 24718 -  # rpc: getblock/getrawtransaction/decode*/gettxout fixups
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
	#21.xTODO# Anything fixed here? 24871 -  # refactor: Simplify GetTime
	# Needs review: 24912 mruddy/nchaintx_type
	25051 fix_configure_def_enable_arm_asms-21				last=7fd0860d12d fix_configure_def_enable_arm_asms
		# NOTE: Only half is applicable to 21.x
	25282 fix_configure_def_use_libevent-21					last=f0f5cd79b5d fix_configure_def_use_libevent
	24933 strerror_threadsafe-21							last=3c651702c68 strerror_threadsafe-23
	24957 fix_prune_during_loadblock-0.20					last=da8e95c0140 mruddy/issue_23852_import_prune
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
	g595  qt_handle_autostart_errors-0.15					last=d932157eb79 mruddy-g/issue_24953
	g599  ts_20220515-partial-21							last=5e23dabf265 ts_20220515
	(CHECK-LAST)	last=3d7b977bbf0 ts_20220515-partial-23
		# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
		# NOTE: ts_20220515-21 is full* backport ddfc86cf878=5e23dabf265 (* see two gui#599 notes later in spec)
		#21.xTODO# Update with other commits that are beneficial
	-     rpcdoc_sendmany_dummy_opt-0.20
	(CHECK-LAST)	last=32cca184b79 rpcdoc_sendmany_dummy_opt-23
		# Just the bugfix from #25093 rpc: Check for omitted, but required parameters
	# Needs review/triage: 25096 -  # [net] Minor improvements to addr caching
		# NOTE: Fixes in #25312 & #25333
	25106 rpc_dumptxoutset_fopen_check-0.20					last=805443ff3f9 rpc_dumptxoutset_fopen_check-23
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
	g260  qt_handle_exceptions_pr260-21						last=6a794f4737e qt_handle_exceptions_pr260-21-corepr
	25239 wallet_committx_catch_db_write_err-21
	# Needs review/work? 25272 wallet_sync_catch_db_write_err-21
	25256 log_threadname_unknown-0.19
	# Not clear this fixes anything: 25273 achow101/use-preset-tx-things
	25276 fix_rpcdoc_importdesc_pr25276-21
	# Meh? 25288 -  # test: Reliably don't start itself (lint-all.py runs all tests twice)
	# Simpler alternative to? 25294 -  # test: Fix wait_for_debug_log UnicodeDecodeError
	25320 impl_win_mlock_limit-0.17
	25333 -  # test: Fix out-of-range port collisions
	Needs review: 25351 fjahr/202204-import-scan
		# NOTE: Was #18964
	Needs review: 25380 darosior/fee_estimator_disable_cpfp
	Needs review: 25404 -  # p2p, doc: Use MAX_BLOCKS_TO_ANNOUNCE consistently
	Ensure it isn't needed in 21.x: g613 laanwj/2022-06-qtconsole-includes
	Triage: g615 -  # If -prune=0 is set, Uncheck Prune on Intro page
	25463 fix_leveldb_no_cloexec-0.20						last=a956806de2f fix_leveldb_no_cloexec
	n/a   (delete_release_notes_fragments)
	TODO: Check depends for fix-only updates
@21.x-knots
# PERFORMANCE:
	# Needs work: 25383 -  # wallet: don't read db every time that a new 'WalletBatch' is created
# SOFTFORK:
	21934 rpc_getblockchaininfo_lockedin_statistics-0.21.1	394e59e2f86	last=2b19f3443ef rpc_getblockchaininfo_lockedin_statistics
	22016 rpc_gbci_period_start-0.21.1+knots	b19116ccf14	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	(CHECK-LAST)	last=5e04731447b rpc_gbci_period_start
	(CHECK-LAST)	last=d6d1a1b47eb rpc_gbci_period_start-22+knots
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
	g275  gui_darkmode-0.21.2_pt1				9cd8d7e8a79
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
	(CHECK-LAST)	last=9652e0a2faa rpc_fundtx_minmaxconf
	(CHECK-LAST)	last=972a1feefa8 fundraw_min_conf_deprecated-23+knots
		# Includes param rename (min_conf->minconf) and tests from #22049 (but not new maxconf param)
		TODO: See if #22049 fixes anything for this
	12677 listunspent_ancestorinfo-21.1+knots	b0bd7118765	last=6cb60f3e6d6 listunspent_ancestorinfo
	18479 rpc_sign_show_fees-21					9f357b09916	last=47b2ba29df2 !kallewoof/sign-show-fees
		# NOTE: Originally #12911
	(CHECK-LAST)	last=1eef939edf1 rpc_sign_show_fees
	g119  rm_send2self-mini-21					8a6ed938070	last=2bb4e307634 rm_send2self
	(CHECK-LAST)	last=251189a4d4a rm_send2self-mini
		# NOTE: Originally #15115
	15423 tor_socks_port-0.21					109cf1f0e3b	last=b2774fc0bed tor_socks_port
		# Held back 962f168a014..398df42f449, da20c1e6d20 (not a bugfix)
	15836 fee_histogram-21						69874bd7a2f	last=b94292a7cb jonas/2019/04/feeinfo
	(CHECK-LAST)	last=8cdfa4e2bea fee_histogram+pr15836_api
	(CHECK-LAST)	last=f34072a4d4f origin-pull/21422/head
		# Held back approach changes (that ignore CPFP) f2ca3d35ee9..47b5c3e03a7 - current approach is arguably buggy (see sipa's review on PR)
		# NOTE: removed extraneous Bitcoin-Qt.* files
		# NOTE: Backported some features/test from #21422 (but not API incompatibilities)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 ? See also git diff b1f9af22425..9d16921553b -w
	17463 gui_custom_sendyes					087d3e642af
	g562  wallet_no_reuse-0.21+knots			952bb1fb9bc	last=776947e6cac wallet_warn_reuse_gui
		# NOTE: Was #15987
		# NOTE: Uses older bloom filter implementation
	22693 rpc_gai_txids-0.21+knots				69259a6ade8	last=8719b084754 getaddressinfo_txids
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
m	16795 rpc_inferred_output_descriptors-21+k	5d1bc19f6ca
		# NOTE: Includes custom refactoring to combine ScriptToUniv and ScriptPubKeyToUniv similar (but not identical) to master, to avoid possibly-incomplete backports
		# +#24636
	18972 neutrino_whitelist-mini-21			dabdcf3f324	last=339fe189eb9
	(CHECK-LAST)	last=3f0d4ecbc58 neutrino_whitelist-mini
		# NOTE: Diff-minimised
	17034 psbt_ver_proprietary_xpub-0.21		0cbd65dd17d	last=81521173ba8 achow101/bip174-extensions
		# +#23975
	(CHECK-LAST)	last=634c311b833 psbt_ver_proprietary_xpub-22-mini
		# NOTE: Held back `gdd 078abaac27e dc93052363d` comment correction
		# NOTE: Didn't bother removing duplicate test
		# NOTE: Diff-minimised
		# NOTE: Now includes 16463 bip174_xpub-0.21+knots				8e6f8d3cc9c	last=9926a387eab achow101/bip174-xpub
	17631 rest_blockfilter-0.21					36a9777315b	last=2b64fa3251a matt/2019-11-filter-rest
		# +#23213 + #23836 (partial)
	(CHECK-LAST)	last=91feea1216a rest_blockfilter-22
		# NOTE: Dropped unrelated extra commits
	g319  gui_openuri_pastebtn-0.21				24178d81b5f	last=dbde0558ce7
	(CHECK-LAST)	last=33258aef4cb qt_openuri_pastebtn_shortcut-23
		# NOTE: Used to be #17955
	18014 siphash_optimise_pr18014-0.21+knots	0c346e55ba0	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
m	18689 rpc_dumptxoutset_hr-21+knots			b79a47abcb6	last=65d0697fe34
	(CHECK-LAST)	last=e4004c28d7e rpc_dumptxoutset_hr-23+knots
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
		# NOTE: Disabled for BDB wallets since it doesn't dump/restore wallet id yet
		# NOTE: Changed to print warnings to stderr instead of stdout
		# NOTE: Diff-minimised
		# If bdb is reenabled, need #20267 49797c3ccfb
		# +#23834 achow101/dump-checksum-size
	19242 uaappend-21							c9099f45c3c	last=9552978b318 uaappend
	19463 prune_locks-0.21						ce3e7443523	last=276a5f9010c prune_locks
		# TODO: change default to temporary=true to match latest prune_locks branch?
		#		* 2554dc0ba3d Refactor PruneLockInfo.temporary to default to true
		# NOTE: Held back extra prune lock buffer & rebasing on #21726
	19762 ryanofsky/pr/named					3505e6dedbb	last=894c414dafb
	19776 -										2d98f923dec	last=343dc4760fd  # net, rpc: expose high bandwidth mode state via getpeerinfo
	19873 mempressure-21						368b6daca5d last=691e1d1dddd mempressure
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
	(CHECK-LAST)	last=06d1947a68e origin-pull/23813/head
	(CHECK-LAST)	last=4b3098817a6 origin-pull/24226/head
	(CHECK-LAST)	last=f5e008774b5 getblockfrompeer_param_names
	(CHECK-LAST)	last=3fa0053aabf rpc_getblockfrompeer_wo_header-22
	(CHECK-LAST)	last=7f2c0d576d2 rpc_getblockfrompeer_wo_header
	(CHECK-LAST)	last=6d074a3f87c rpc_getblockfrompeer_nodeid_compat-23
	(CHECK-LAST)	last=a926025ca82 jonatack/getblockfrompeer-param-inputs
	(CHECK-LAST)	last=4fe12e61847 rpc_getblockfrompeer_typecheck-23
		TODO: +#25259 ?
		# +#23702 +(doc from #23813) +#24226
		# +#24944
		# NOTE: Forward-compatible with peer_id param rename in #23706
		#21.xTODO# TODO? Forward-compatibility with block_hash param rename in #23706 (bad idea, these changes conflict with other/standard param names)
		#21.xTODO# TODO??? API change * 60243cac728 rpc: turn already downloaded into error in getblockfrompeer
		#                           + * 34d5399211e rpc: more detailed errors for getblockfrompeer
		# TODO: Find a way to get `476f63a081e test: Add test for getblockfrompeer on pruned nodes` w/o fastprune mode?
	20391 rpc_setfeerate-0.21					aef134635d5	last=1002e2d0d7f jonatack/setfeerate
	(CHECK-LAST)	last=4c0bc142de7 rpc_setfeerate-22
	(CHECK-LAST)	last=116199a46f4 rpc_setfeerate-23
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
m	20403 upgradewallet_pr20403-0.21+knots		5a4416104d5	last=3eb6f8b2e61 jonatack/upgradewallet-improvements
	20407 rpcauthfile-0.21+knots				389dda3a1a1	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
	(CHECK-LAST)	last=53383d94200 rpcauthfile-22
	(CHECK-LAST)	last=9ea91885d34 rpcauthfile
		# NOTE: fixed bug, added multi-line support, and added tests
	g149  intro_assumevalid-21					a434a92b063	last=75aff9e0ff7 intro_assumevalid
	(CHECK-LAST)	last=de495ad2f11 intro_assumevalid-23
	25339 rpcdoc_scantxoutset_20220611a-21					last=7862c4ac4e7 rpcdoc_scantxoutset_20220611a
	23549 rpc_scanblocks-21+knots				5eaa6ce2ea6	last=e1c89184cd3 jamesob/2021-11-scanblocks
	(CHECK-LAST)	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
	(CHECK-LAST)	last=d28e8e4e277 rpc_scanblocks
		# NOTE: Was #20664
		# NOTE: Includes lots of additional fixes/doc improvements
		# NOTE: Now includes #21426 (scantxoutset no longer experimental) too
		# Held back insignificant comment/errormsg changes ab315e5294b...71b7cdb460e
		# Added return value documentation (needed for QA to pass)
		# NOTE: Was #20664
	20702 rpc_getblocklocations-0.21			bc93fb1825b	last=9b03c654eb3
	(CHECK-LAST)	last=b60fdcbc2dc rpc_getblocklocations-22
	(CHECK-LAST)	last=18389bc711a rpc_getblocklocations
	20827 ibd_prune_max-21						894af588353	last=e426bb1ab50 ibd_prune_max
	(CHECK-LAST)	last=24f3936337d ibd_prune_max-22
	g163  gui_peer_conntype-0.21				a39642a4ef4  # jonatack-g/display-peer-conn-types
		# NOTE: Stripped unrelated string changes
	g180  gui_peer_relay_detail-0.21+knots		18243adb3a3	last=79a2576af1e jonatack-g/peer-details-connection-type-followups
		# +g203  Display plain "Inbound" in peer details
		# NOTE: Carries commit from g163 since it messes with the string anyway
		# NOTE: Left off final doxygen commit
	g179  gui_peers_conntype-0.21+knots			5a9d8b41bf9	last=be4cf4832f1 jonatack-g/add-peers-dir-and-type-columns
		# NOTE: Held back 9f76ba6597c...be4cf4832f1 (no real change once we add gui#363 on top)
	g363  qt_peers_directionarrow-0.21+knots	c76a8d4f215	last=4e2fe6b9878 qt_peers_directionarrow
	(CHECK-LAST)	last=4d70dc134c2 qt_peers_directionarrow-22+knots
	(CHECK-LAST)	last=6d169ee0c55 qt_peers_directionarrow-23+knots
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
	20916 rpc_testmempoolaccept_wtxid-0.21		c5b8eb0a8b4	last=fa0aa87071e marco/2101-wtxidTestmempool
		# Diff-minimised
	g162  gui_peers_detail_network-0.21+knots	9e73df68dc7
		# NOTE: Left out Peers table column & misc formatting changes
		# if merging full gui#599: * f0dbac928f1 GUI: Support translating peer network names
	20944 rpc_getmempoolinfo_total_fee-0.21		e0125b1b0d9	last=fa362064e38 marco/2101-rpcMempoolTotalFee
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
	g213  gui_payrequest_copyaddr-0.18			3fbc3512e3c
	g214  gui_payrequest_disablena-0.18+knots	88cfbc9641b
	21327 p2p_ignore_tx_in_ibd-0.21				cb54eca2c0b	last=6aed8b7e9b2
	(CHECK-LAST)	last=704a7b03d53 p2p_ignore_tx_in_ibd-22
m	21359 rpc_fundraw_includeunsafe-0.21+knots	78c5639bd85
	g205  gui_save_txview_reqview_columns-0.19	f5fcee6e0a3
		# +gui#368
		# NOTE: Diff minimised
		# NOTE: gui#229 not applicable to backport
	g206  gui_peers_relayinfo-0.21+knots		d5d383b9daa
	g226  gui_peers_lastblocktx-0.21+knots		8482728d1e2
	g230  gui_backup_formats-0.21+knots			6115edf25d3	last=835d49b30bc gui_backup_formats
	(CHECK-LAST)	last=4490d994755 gui_backup_formats-22
		# NOTE: To avoid conflict with wallettool_dump-0.21+knots, added 5ab50bc98db GUI: Omit DbDump option for backup of BDB wallets
	21595 cli_addrinfo-0.21+knots				7c408353347
		# NOTE: Adapted error message for Knots
	21602 rpc_listbanned_deltas-0.21			3462d5598d1
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rpc_maxmempool-0.21					9a2751a9347	last=040b280c661 rebroad/MaxMempoolRPC
	(CHECK-LAST)	last=a05a4fe9fcd rpc_maxmempool
	(CHECK-LAST)	last=43eb542612e rpc_maxmempool-22
		# + bugfix and applying limit immediately
	22072 autoreindex-0.21						7fb696c631e	last=602f4da9178
	22147 p2p_protect_last_outHB-0.21			995947de083
	# AFTER CORE RELEASES: (PR unknown) taproot descriptors +22156? +22166?
	22159 conf_append_cxxflags-0.10				b9c4f0c218e	last=fa14c6818f4 marco/2106-buildPattern
	# TODO, Ugly Hack w/ conflicts: g256  hebasto-g/210323-peers
	# Preferred simpler fix in gui#275: g330  jarolrod-g/prompt-icon-colorized
	g281  gui_console_fontsize_shortcuts-0.21+k	a9ed8095ab9
		# NOTE: Diff-minimised and moved AddButtonShortcut to avoid conflict with #553 later
	g293  gui_peers_services_wordwrap-0.18		a9065accdaa
	g298  gui_peers_altrowcolor-0.21+knots_pt1	281357e21fe
	g307  gui_peers_altrowcolor-0.21+knots		81f3be93772	last=fdf80937d1c hebasto-g/210501-stripes
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
	22372 multinotify-21						b002df55c73	last=041b1ed8b79 multinotify
	g469  qt_psbt_b64-21+knots					65f1d080b90	last=2c3ee4c3478 achow101-g/b64-psbt-gui
	(CHECK-LAST)	last=5f7a4882e39 qt_loadpsbt_b64-23
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	# Needs review & MUCH softer deprecation: 24098 -  # rest: Use query parameters to control resource loading
	# After merged+released a while? 24171 sdaftuar/2022-01-download-from-inbound
	# Check if fixes anything: 24178 sdaftuar/2022-01-headers-response-requires-minchainwork
	24198 rpc_wtx_wtxid-0.20								last=7abd8b21ba3  # wallet, rpc: add wtxid in WalletTxToJSON
	(CHECK-LAST)	last=954bc3e5e73 rpc_wtx_wtxid-23+knots
	g526  qt_peers_addrprocessed-21+knots
	# Maybe? 25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
	#21.xTODO# Decide if above minor features need to wait for 21.3, or can go in 21.2.1
	# SENDING ONLY? Needs work: 24897 w0xlt/silent_payment_021
# Non-progress functionality:
	8751  sort-multisigs-0.21					0cd85c73c6f	last=e11cb50a09  # multisig sorting
	(CHECK-LAST)	last=db2b618ec07 sort-multisigs-22
	(CHECK-LAST)	last=8db63499737 sort-multisigs-23
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152  sweepprivkeys-0.21					2aeaeeb1ba1	last=ba17ce68d20 sweepprivkeys
	(CHECK-LAST)	last=6fcb1e43426 sweepprivkeys-22
	9245  ionice-21								d935e6fc4ab	last=26996baceb1 ionice
	(CHECK-LAST)	last=6de915d6dc0 ionice-22
		# NOTE: Left off deprioritisation of LoadExternalBlockFile, ReplayBlocks, RollforwardBlock(22.x?)
	-     ionice_win-0.21						1c6f29b3e4f	last=65dcf0dc11c ionice_win
	(CHECK-LAST)	last=b59bc253116 ionice_win-22
	8501  old_stats_rpc-0.21					3eee2d40dbe	last=7af0ea43b2
	(CHECK-LAST)	last=8cfab679cb2 old_stats_rpc-22
	(CHECK-LAST)	last=040565d1047 old_stats_rpc-23
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-0.21						65892ef0064	last=63fb11652f
	(CHECK-LAST)	last=9b99d9c327b old_stats_qt-22
	(CHECK-LAST)	last=aa3f38ecd79 old_stats_qt-23
		# Held back on old version due to conflict with RPC updates...
	9504 dumpmasterprivkey-0.21					5e32058f65a	last=07fc81109a
	(CHECK-LAST)	last=d6299945048 dumpmasterprivkey-22
	(CHECK-LAST)	last=5e01bd283b8 dumpmasterprivkey-23
	g444  gui_netwatch-0.21+knots				842149fff05	last=524665c116a gui_netwatch
	(CHECK-LAST)	last=7f59a6deb52 gui_netwatch-22+knots
	(CHECK-LAST)	last=9482300fab7 gui_netwatch-23+knots
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-0.21+knots			bae1509a9d1	last=1a2bc175ffc multiwallet_rpc-23+knots
	(CHECK-LAST)	last=d927c064439 multiwallet_rpc-22+knots
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-0.21+knots					a6b0a8894fb	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	(CHECK-LAST)	last=39cf88db90b zmq_wtx-22+knots
	(CHECK-LAST)	last=71689c52c52 zmq_wtx-23+knots
	20551 rpc_onetry_conntype-21				d7fcef7c236	last=1c63b3ff236 rpc_onetry_conntype
	(CHECK-LAST)	last=7661ce6ddaf rpc_onetry_conntype-22
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment-0.21+knots	d4765cc92bd	last=0971192425f relax_invblk_punishment
	(CHECK-LAST)	last=57903e3f34d relax_invblk_punishment-22
		# Held back 0971192425f QA: Use addconnection rather than addnode onetry
	10350 filtered_witblock-0.21				4e1122ece17	last=3f388ddcd3 codeshark/MFWB_no_bump_2
	(CHECK-LAST)	last=6bf4092cb7b filtered_witblock-22
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				c4c8ec10f47	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-21+knots						1009e765049	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	(CHECK-LAST)	last=5d5b2fb8442 rest_fee-0.21
	(CHECK-LAST)	last=cec2e1bb857 rest_fee-22
	(CHECK-LAST)	last=2c51873b614 rest_fee
		# Fixed a minor bug in conf_target range check
		# Added functional tests: 5d5b2fb8442 QA: Exercise REST interface in feature_fee_estimation
	11803 bugfix_dumpwallet_hdkeypath-0.20		280b1276bfb
	(CHECK-LAST)	last=a6d25571113 bugfix_dumpwallet_hdkeypath
	12965 scriptthreads-0.20					095986b847a	last=dfab6c6866 jonas/2018/04/svt
	(CHECK-LAST)	last=f6052208ab0 scriptthreads-22
	(CHECK-LAST)	last=12e673a8c23 scriptthreads
		# Held back RPCResult NONE cuz undocumented is actually better
	13203 dsha256_power8-0.20					357397180c7	last=3b402e0738 matt/2018-05-asm
	(CHECK-LAST)	last=a72483b8e14 dsha256_power8-23
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		60c82d4c598	last=99986de8b02 dsha256_power8_asm_pragmas-23
	15218 postibd_flush-21+knots				8858f44e523	last=d2ecb70d64  # validation: Flush stateafter initial sync
	(CHECK-LAST)	last=8faeb93d48d postibd_flush-22+knots
	(CHECK-LAST)	last=6bd37fe1133 postibd_flush-23
	15428 tor_gui_pairing-0.21+knots			9b710f4ddfb	last=38f5608ece9 tor_gui_pairing-23+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 16cb2ae1fe0)
	(CHECK-LAST)	last=4a881554991 tor_gui_pairing-22+knots
m	15421 tor_subprocess-0.21+knots				ccf77ea4de5	last=58c6cafd3a1 tor_subprocess
	(CHECK-LAST)	last=1fae7eff568 tor_subprocess-22+knots
	15633 nohbcbfornonwit-0.21+knots			f81d53ce8c5	last=f5e4f1650fe nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# TODO: 16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					975064084f4
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning-0.21+knots		d001554bb8d	last=abb8c8c2d6c restore_vbits_warning
	(CHECK-LAST)	last=896eea449ad restore_vbits_warning-22
	20832 rpc_validateaddress_error-0.21.1+k	0859c222db0
	16807 bech32_error_detection-0.21.1+knots	c08a0bcebf7	last=88cc4810926 meshcollider/201909_bech32_error_detection
	(CHECK-LAST)	last=3bc568d6753 old_bech32_error_detection
		# Held back rewrite 3bc568d6753..974227bb457 for now; when updating, add in #23577
		# Held back comment drop 974227bb457..88cc4810926
	n/a   rpc_compat_error_index-0.21+knots		e8b159d62b3	last=57e05a6f13c rpc_compat_error_index-23+knots
	(CHECK-LAST)	last=e480af6868c rpc_compat_error_index-22+knots
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos-0.21.1+knots		a4921198f16	last=539beeaae85 gui_bech32_errpos
	(CHECK-LAST)	last=7532115c6d8 gui_bech32_errpos-22+knots
	(CHECK-LAST)	last=954bb8ca738 gui_bech32_errpos-23+knots
NM	16807 bech32_error_detection-0.21+knots		c0339fe9c28	last=54e107add41 meshcollider/201909_bech32_error_detection
NM	-     gui_bech32_errpos-0.21+knots			ae0986b142d
	17636 guisettings-0.21						aec700dd5c2	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo-0.21+knots			31332337e68	last=cdbd38df131  # getgeneralinfo RPC
	(CHECK-LAST)	last=65f6caeebbd rpc_getgeneralinfo-22
	(CHECK-LAST)	last=3b7c5bc7e2c rpc_getgeneralinfo
	18223 blockfilter_v0-0.19					a1d7fc7821f	last=5561e7a0c79
	(CHECK-LAST)	last=7f0131feac7 blockfilter_v0
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances-0.21+knots		98e3ae63888	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	(CHECK-LAST)	last=cd48a6982ca cli_getinfo_mwbalances-22
	(CHECK-LAST)	last=2b2d4c06e10 cli_getinfo_mwbalances
	19092 cli_getinfo_mw_total_balance-0.21+knots	5672474d49e	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=e8bab0a4077 cli_getinfo_mw_total_balance-22
	(CHECK-LAST)	last=a65c48636bc cli_getinfo_mw_total_balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
m	18570 wallet_rpc_lastprocessedblock-0.21+k	75d59808743	last=1e868bbbb1b
	(CHECK-LAST)	last=363c4e02d3d wallet_rpc_lastprocessedblock-22+k
	(CHECK-LAST)	last=dc58f8f46e6 wallet_rpc_lastprocessedblock-23+k
	19117 rpc_getrpcwhitelist-21				f005cd98854	last=3fd323ca11f rpc_getrpcwhitelist
	(CHECK-LAST)	last=3a5869713b4 rpc_getrpcwhitelist-22
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.21+knots	e2bae466a89	last=fad1716d500 getrpcwhitelist_wallets-23+knots
	(CHECK-LAST)	last=1e1d1e2e62c getrpcwhitelist_wallets-22+knots
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-0.21+knots	d50c4c7d4af	last=36cc299baee whitelist_outgoing
	(CHECK-LAST)	last=9cf184186c9 whitelist_outgoing-mini-22+knots
	(CHECK-LAST)	last=27ad690c9d2 whitelist_outgoing-mini-23+knots
		# NOTE: d756d0a01a6 needs legacyWhitelisted in minified version!
		# NOTE: Originally #10594
	g165  gui_peers_splitter_ss-0.21+knots		b71e008e2cf
		# +g194 Save/restore RPCConsole geometry only for window
		# NOTE: Changed setting name since our peer table width doesn't match Core's
		# TODO: Each release, see if we need to bump setting name (and figure out back compat?)
	# Needs review: (MAYBE JUST PART OF) g539  RandyMcMillan/1643263956-network-graph-issue-532
# Non-upstreamed functionality:
	-     gui_payreq_textedit-0.21				bfe154411de last=9cb216e6ff8 gui_payreq_textedit
	-     rpc_mempoolentry_txhash-0.20			0b5a0196787	last=b011a9bf2c6 rpc_mempoolentry_txhash
	-     walletnotify_w_win-0.21+knots			103ea74ed61	last=7b3c78aa40e walletnotify_w_win-23+knots
	(CHECK-LAST)	last=4c481517859 walletnotify_w_win-22+knots
	14137 win_taskbar_progress-0.21+knots		cf8835a0b82	last=18eb4dbb8a
	(CHECK-LAST)	last=f30b740b4ff win_taskbar_progress-22
	(CHECK-LAST)	last=de45972a3f2 win_taskbar_progress
	-     restore_blockmaxsize-21				244ddb8587d	last=d66d020e9d2 restore_blockmaxsize
	(CHECK-LAST)		last=0df4a820dd6 restore_blockmaxsize-22
	7107  qtnetworkport-21						1c31de03b71	last=1f37c87 origin-pull/7107/head
	(CHECK-LAST)	last=061cd3f46cf qtnetworkport-23+knots
m	7533  sendraw_force-21+knots				84c7abed1ab	last=8b4a4f9b2b4 sendraw_force
	(CHECK-LAST)	last=074e22628db sendraw_force-22
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf-0.21							901121d0ce9	last=3e6f24bf30b rwconf-23+knots
	(CHECK-LAST)	last=ad7812c9eb7 rwconf-22
	7510  rwconf_gui-0.21						2df27d4a04e	last=11539fbed54 rwconf_gui-23+knots
	(CHECK-LAST)	last=5465696bf16 rwconf_gui-22
		# NOTE: Missing cac3d7873a3 due to not having #15946 in 21.x
m	559   accept_nonstdtxn-21+knots				0d7a5178261	last=70b0f3bf1ed accept_nonstdtxn
	(CHECK-LAST)	last=d2a16fe9618 accept_nonstdtxn-0.21
	(CHECK-LAST)	last=75b02a00617 accept_nonstdtxn-22
	g153 const_max_digits						32e16e210f2
	 929  tbc-21+knots							8aa517b2bd1	last=ec29a85b5f6 tbc
		# NOTE: Held back 6a4900bc4e6..ec29a85b5f6 (UCSUR output is a feature?; "fix" ec29a85b5f6 doesn't seem to affect anything)
		# if merging full gui#599: deal with possibly silent conflicts
	 553  bugfix_qt_uri_amount_parser-0.17		ce9be680833	last=e3ad5956dda bugfix_qt_uri_amount_parser
m	-     mining_priority-0.21+knots			1e33269a0ae	last=a284d6253ff mining_priority
	(CHECK-LAST)	last=58e2cab4b18 mining_priority-22
		# Didn't backport next_block_height passing (maybe consider when/if someday cs_main can be released)
		# Didn't backport platform-independent double serialisation
	5861 gui_restore_addresses					a81fd2b77ff
	5891  qt_console_history_persist-0.21+knots	831cc0d61d1	last=0cd5fc301d6 qt_console_history_persist
m	7219  rbf_opts-0.21+knots					6b8135375e9	last=c6decd62837 fullrbf # missing 91786d16ccc + revert34ae6640174
	(CHECK-LAST)	last=8db545872f6 fullrbf-22+knots
	(CHECK-LAST)	last=149b286b44e fullrbf-23+knots
		# NOTE: Held back "clean mempool" from b81235ee156 (not needed in 21.x?)
		# NOTE: Re-PR'd as #25373
		TODO: Compatibility with #25353 ?
	12146 opt_wallet_segwit2-0.1				ffc242d52be	last=6a939ab54c6 opt_wallet_segwit2
		TODO: Make sure descriptor wallets default to non-segwit addresses
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
	-     netperms_implicit_addr-0.21+knots		7d39ba69a9e	last=075c281b273 netperms_implicit_addr
	(CHECK-LAST)	last=d1ce634b708 netperms_implicit_addr-22+knots
	12674 rpc_onetry_nonpriv-0.21+knots			7607b0cb005	last=896995cd251 rpc_onetry_nonpriv-23+knots
	(CHECK-LAST)	last=054c2214369 rpc_onetry_nonpriv-22+knots
	Maybe? 24963 rpc_walletprocesspsbt_options
	# TODO: add a bitcoinknots.conf ?
# POLICY:
	-    1day_default_conftarget				3f1c8d8ab40
	-     bytespersigopstrict-0.21+knots		c021176f67a	last=43d7d3889cf bytespersigopstrict-22+knots
	(CHECK-LAST)	last=712c7abc3a1 bytespersigopstrict-22+knots
	9749  unique_spk_mempool-0.21+knots			52cb2331dee	last=7882096ddef unique_spk_mempool-23+knots
	(CHECK-LAST)	last=36bb6460136 unique_spk_mempool-22+knots
	-     bloom_default-0.21+knots				ab9afbc6fee
	-     enforce_checkpoints-0.21				09feeecfdfe	last=1de4af3f6c7 enforce_checkpoints
	n/a   checkpoint_update-0.21				67bc16f3c2a	last=1923722495d checkpoint_update-23
	10282 timebomb_knots-21						4d798a3f50b	last=8a98c44f042 timebomb_knots
	-     rwconf_policy-0.21+knots				1d0a8a7bf36	last=ade5197bc55 rwconf_policy-23+knots
	(CHECK-LAST)	last=f89126d2136 rwconf_policy-22+knots
		# Include Knots policy changes for simplification of final rebase process
		# Held back git diff 19fd29ce45d..af4614fbd26 which is likely a noop
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		e0a236336e2
	7483  svg_icon-21.2+knots					10090268130	last=64ed5a651d7 svg_icon-23+knots
	(CHECK-LAST)	last=afaab080b87 svg_icon-22+knots
# BRANDING:
	n/a   knots_branding-21						9db64a56d30	last=16035761f8b knots_branding-23
	(CHECK-LAST)	last=282420dea44 knots_branding-22
		TODO: Review security policy & report(s)
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
TODO: Make sure there's no optional .has_value() (Boost 1.68 dep)
#TODO: Make sure there's no 'build_bitcoin_util\b|natpmp'
TODO: Run #25243 to pick up on missing bash completion updates
	n/a  (cherrypick=e0968d0328b2877330)		fbd68408390	# doc/{bips,files}
	n/a  knots_bips-21							95f1a0c7adb
	n/a  (bump_version=Knots:20210629)			27c16a89cc5  # DO NOT CHANGE for just fixes
#	n/a  knots_historical_relnotes				61100a2
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
	n/a  (cherrypick=a76c71bf46b)				42a7a1b3d52  # update manpages (build first)
	n/a  (cherrypick=3b34e884d32)				2d4f6166a4b  # translation update
# EXTRA TESTS:
	24797 -  # test: compare /chaininfo response with getblockchaininfo RPC
# NOTE: use git diff --minimal for patches!
