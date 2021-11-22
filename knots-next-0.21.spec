timestamp 2021-11-08 17:44:18
#lastapply no-merge

#.. checked up to PR #22369 / gui #375 for features
#.. checked up to PR #23436 / gui #459 for fixes

checkout v0.21.2
@0.21.x-syslibs
# BUILD BUGS:
	21882 fuzz32_llvm_workaround-0.21+knots		d994684b569	last=e4c8bb62e4a hebasto/210507-fuzz32
	20938 configure_latomic_checks-0.14^		ee5e40704b0
	21920 configure_latomic_checks-0.14			4f3c88f543a
	# Not needed (depends only): 22380 fanquake/set_std_c_version_depends
	22390 netbsd_dont_set_locale-0.20
	# Needs review: 23030 -  # src/randomenv.cpp: fix uclibc build
	# OR: 23082 fanquake/remove_weak_auxval
	23045 fix_crc32c_arm64_detect-0.20						last=f2747d1602e laanwj/2021-09-arm64-crc32
	23182 py3_9t11-0.21										last=e11c21c8454 py3_10o11-22
		# +#23317
	23314 disable_s2561k_openssl_test-0.21					last=8031de63b5a disable_s2561k_openssl_test-22
	23345 wallettool_drop_extra_deps-0.21+knots				last=4fe7cf16779 hebasto/211024-bw-deps
		# Dropped MSVC changes
		# BUILD_LEVELDB becomes EMBEDDED_LEVELDB for v21.x+v22.x
		# Held back 347774b86c8...4fe7cf16779 removal of embedded leveldb conditional (might have worked better with sys_leveldb, but oh well)
# SYSLIBS: (and old build bugs)
	5872 subdir_incl_compat						f2e1e41e817
m	2241 sys_leveldb-21+knots					5e9497a8ed7	last=bd02e19eaf5 sys_leveldb-22+knots
m	5416 sys_libsecp256k1-0.21+knots			c2e8d067f0b	last=f749462f68c sys_libsecp256k1
	7485 sys_univalue_def						663a72e6a12
	13789 bugfix_asm_pragmas					82ab60f2428
	-     bugfix_asm_leveldb_check				741060d31b8
	15155 test_external_bcli-21					251dcff7eee	last=06ec7f56dfb test_external_bcli
	20202 opt_bdb-0.21							1b369a2bfd7
		# +#20458+#20267
		# Omitted default-tests-to-descriptors-when-bdb-not-compiled: a2282b44a4d 373158bc44c
		# Omitted "Don't make any wallets unless wallet is required": 45b4366f8ff 104a3a22564 6e06ca05880
		# Diff-minimised
	-     opt_bdb_extracare-0.21				3d26b04ad0f	last=aa6a707d7ca opt_bdb_extracare
m	20121 secp256k1_allow_bignum-21+knots		ed298e34b3d
	20358 -										980c71c1f50	last=330cb33985d  # src/randomenv.cpp: fix build on uclibc
	20594 conf_getauxval-0.21					cfc912ffcdc	last=836a3dc02c7 jonas/2020/12/getauxval
	#Maybe restore: 7339  opt_libevent
@0.21.x-knotsfixes
# TESTS:
TM	22279 fix_fuzz_baseencdec_pr22279-0.21		3d80a04b144
TM	22002 fix_fuzz_system_pr22002-0.21			867a7fc53df
TM	22137 fix_fuzz_system_pr22137-0.21			a7912915185
	-     lint_relaxer-0.21						9afa5d8517a	last=598cf8bfb7b lint_relaxer
		# Held back unnecessary d4d8eb13cbb...598cf8bfb7b
	17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
	21785 fix_intrmttnt_qa_p2p_addr_relay-0.20	6430702d120
# FIXES:
	# Only needed for focial gitian?? 22318 hebasto/210623-random								last=35aab4f0c0b
	18818 fix_gitian_src_202004-21				e7ae473f644	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again-21					48e2ecb874f	last=686cedcc9cd fix_gitdir_again
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					51d41a3ea10	last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case-21			b9b3f3bd5c0	last=24a69574ece bugfix_symcheck_pe_case
	17828 p2p_log_categories-21					bab13c46b9b	last=04960621582 practicalswift/log-categories
	(CHECK-LAST)	last=dbbb7c4265e p2p_log_categories
	19832 hebasto/200829-log					1ed3a60bb05	last=1816327e533
	20845 net_logcategory_localdisconnect-0.21	fb5ba0afa13	last=fa55159b9ed marco/2101-netLogDisconnect
	# Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
	14968 laanwj/2018_12_http_bind_error		e75ff7b9323	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	(CHECK-LAST)	last=8520c437a0d http_bind_error
	-     http_bind_error+extra-21				81ed4fe33fa	last=fd5353ed826 http_bind_error+extra
		# NOTE: Held back annotation in gdd 785429c2c7a fd5353ed826
	9524 marco/Mf1701-qaPruning					ae3444d7950	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment-21					3cee4ceb1b1	last=fa16d94b095 log_more_uacomment
	14485 fadvise								e87f5a4c952
		# Was #12491
	14501 fsync_dir								e4a9992dd5e
		# Was #12696
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	13608 -										bdb644e5423	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	-     deprecated_param_names				7a602d396d9
	-     bugfix_rpc_getbalance_hacky-0.21		2fc80cecb4c	last=bb3ba6bebe8 bugfix_rpc_getbalance_hacky
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			d61ba875650	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	g404  bugfix_qvalidlineedit					7933a2d752b
		# Was #18133
	18194 bugfix_gui_edit_sendaddr-mini			64ebfdfb0a1	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18335 -										10c0773e7fd	last=8dd5946c0b7  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	18466 -										cf0e22b6d2f	last=a5cfb40e27b  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	18729 intro_dont_change_user_prune			25f70064ec8
	18766 blocksonly_no_feeest-0.21				e46a9d86ca1	last=4e28753f606
		# diff-minimised
		# HELD BACK 33ca3590243...4aaad74c4c8 due to refactor complication
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
TM	19362 rpc_scantxoutset_reset_progress-0.17	13e1e8980d8	last=8c4129b4540 prusnak/rpc-scantxoutset-reset-progress
	19419 listwalletdir_skip_data-0.21+knots	a0f6d94c0b9	last=3f9cc0cd736 Saibato/wallet_351
	(CHECK-LAST)	last=17f214f4b7f listwalletdir_skip_data
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
	19884 fixedseeds-0.21						5ff339ffa5d
		# +partial #21254 (bugfix only)
	19888 getblockstats_utxo_actual-0.21+knots	37dd20ac3a1	last=6cd78060c8e
	(CHECK-LAST)	last=6fb4286f0eb getblockstats_utxo_actual-22+knots
		# Held back additional tests
	# Needs review: 20196 vasild/fix_GetListenPort
	g87   hebasto-g/200910-mono					13002cb08f2	last=2e386cd3dd3
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	g121  fix_qt_early_sub_signals-21
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	20448 unloadwallet_namematch				02b171f7ec5
	# Needs consideration.. why would we re-announce to the same peer?? 20561 sdaftuar:2020-12-moar-addrz
	# Needs concept review: 20583 marco/2012-walletSync
	g152  gui_notify_setup_bg					e7a792e44b6
	-     bugfix_gui_drop_abc_confusing_hack	c0f258de92f
	20805 copyright_2021-0.21					f9379afcd0c
		# NOTE: Diff-minimised
	# Needs careful review: 20966 banlist.json (TorV3 bans fix)
	# Too messy? g164 hebasto-g/201224-signal
		# +gui#375 fix
TM	g171  qt_createwallet_layoutmgr-0.21		1ab94ce61ef	last=d4feb6812a2 hebasto-g/210101-wallet
	# Meh? Diff too big? g176 hebasto-g/210103-delegate (fix in #20983)
TM	g177  workaround_qt_macos11_fusion-0.21		9ab4bdc6608	last=4e1154dfd12 hebasto-g/210107-style
	20952 bdb_sanity_check-0.21					85ec10ee85e
TM	g188  bugfix_psbt_binmode-0.21				d46c3cb9d45	last=cc3971c9ff5 achow101-g/bin-mode-psbts
	21028 bips_44-49-84-0.21+knots				915ffbb4cea
	21029 cli_doc_geNnewaddr					b7634d92c59
	# Needs review: g201  jonatack-g/inbound-block-relay
	g202  bugfix_gui_peerdetail_hide-0.18		c27915c33d9
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	21111 openrc_no_rpcpassword-0.12			0c26ecef607	last=95f97111dd2 parazyd/openrc-init-improve
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	21192 bugfix_netinfo_tooverbose-0.21		b068b1f1c54	last=882ce25132e laanwj/2021-02-netinfo-verbosity
	g204  bugfix_gui_rm_old_fixer-0.18			94b0d8bf06d	last=3913d1e8c1f
		# Diff-minimised
	g217  gui_clickable_warning-0.11			0311cc01d15	last=67c59ae4793 jarolrod-g/warning-look-like-button
	# Needs careful review: g219 hebasto-g/210223-toolbar
	g236  gui_init_walleterror_cont-21			37fc886f39f
	# Complex: 21007 hebasto:210316-fork
		# +21447 TODO
	# Needs #21007, complex: 21418 laanwj/2021-03-systemd-daemonwait
	# TODO: Last commit? Diff-minimised somehow? 21560 laanwj/2021-03-torv3-hardcoded-seeds
TM	21644 bugfix_addlocal_downloadbind-0.21		2f5bc37b025
	21822 bugfix_cli_pr21822-0.21				791f7e23c3b
TM	21907 listwalletdir_iterate_inf-0.19		985e103723c
	21944 fix_listwalletdir_rootdir-0.21+knots	32993f653d7
	22013 ignoreblockrelayfordnsskip-0.21		219665bf068
	# Needs work: 22079 -  # zmq: Add support to listen on IPv6 addresses
	19315 rpc_addconnection-0.21				1e691e1fff6
		# PARTIAL: Only the actual addconnection RPC method
		# NOTE: Modified to allow use on non-regtest networks
	22096 fix_p2p_addrfetch_ignoreselfadv-0.21+knots	e4674e393ba
		# Includes part of #21236 (to avoid an extra GetTime on top of the 4 existing)
	# TODO: Determine if any of #22154 (bech32m fixup) is needed
	g243  gui_createwallet_opts_conflict-0.21	4f217b9503c
	g251  fix_bip70_errormsg-0.20				5d45a4f9de0
	g271  fix_gui_rpcconsole_fontsz_prompt-0.21	492bb4b683a
	g276  gui_peers_elide-0.18					ba0720634c9
TM	g280  gui_urihandler_nophishing-0.20		b7026991708
	g325  gui_peers_rightalign_id-0.21			2d229bb6dd9
	g329  rpcconsole_toolbuttons-0.21+knots		a40ba0d5ba2
	# Needs review: 22261 jnewbery/2021-06-broadcast-fixes
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22308 bugfix_pr22308-0.17					c009ccfeb2f
	22311 bugfix_pr22311-0.21					995e84e1904
	18842 fix_wallet_pr18842-0.21				42b45600d37
	22359 fix_wallet_pr22359-0.21				3244e0d002f	last=fa6fd3dd6a4
	(CHECK-LAST)	last=171ac54ea47 fix_wallet_pr22359-22
		# Semi-diff-minimised
	# Needs review: 22362 marco/2106-addrdb  # Drop (only) invalid entries when reading banlist
	22417 bpchild_closefds-0.21								last=3b6153ba336 bpchild_closefds
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
	g379  qt_reset_bad_settingsjson-0.21
	# FIXME: When upgrading any guix/gitian to GCC 9: Ensure #20005 "memcmp with constants that contain zero bytes are broken in GCC" gets addressed
	22577 fix_race_pr22577-0.21.1							last=05e84aa550c fix_race_pr22577-22
	22591 missing_settings_err-0.21
	22834 bugfix_onlynet-21									last=051c2554ca1 vasild/onlynet
		# Refactored to be less optimised in favour of being more obviously correct
	(CHECK-LAST)	last=61c0c0f7bad bugfix_onlynet-22
	# Needs review: 22665 darosior:rbf_optin_nomempool
	22722 fix_estsfee_minrelay-21+knots						last=ea31caf6b4c  # rpc: update estimatesmartfee to return max of CBlockPolicyEstimator::estimateSmartFee, mempoollMinFee and minRelayTxFee
		# +#23547
	(CHECK-LAST)	last=73a5d927f34 fix_estsfee_minrelay-22
	23027 bugfix_util_test_config
	22781 fix_ishdenabled-0.21
	# Needs review: 22798 MarcoFalke:2108-docRpc
	# Needs review (& diff minimisation?): 22817 MarcoFalke:2108-testRaceConnect
	# n/a without #21565: 22820 fix_config_qtinputsupport-22
	# Needs review: 22834 vasild:onlynet
	# TODO? 22836 sipa:202108_bipvec5
	# Not worth added build overhead? 22840 fanquake:fix_depends_lib_optimisation
	19851 abstract_parseopcode-21  # needed for 22875
	22875 parseopcode_threadsafe-21							last=d5e006c84a1
	(CHECK-LAST)	last=34fd8e3992c parseopcode_threadsafe-22
	22879 fix_addrman_err_format-21							last=fab0b55cf06 marco/2109-testPeersDat
	(CHECK-LAST)	last=0a3ec03ea33 fix_addrman_err_format-22
	22895 fix_RBFD_lock_pr22895-0.16						last=94c04681edb fix_RBFD_lock_pr22895-22
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review: 22929 S3RK/fix_19856
	# Needs review and diff minimisation: 22932 jonatack:require-GetBlockPos-to-hold-cs_main
	g399  fix_load_psbt_wo_wallet-21						last=27f8c7c425d fix_load_psbt_wo_wallet-22
	g409  fix_gui_walletop_titlebar-0.20					last=01bff8f0494
		# Held back trivial comment change f86fe193329..01bff8f0494
	(CHECK-LAST)	last=e817b217145 fix_gui_walletop_titlebar-22
	g418  mac_platform_metadata-0.20						last=3765c486ef5 jarolrod-g/applesilicon-categorization
	23050 bugfix_pr23050-0.15  # log: change an incorrect fee to fee rate, and vice-versa
	23061 fix_argparse_persistmempool-21					last=60ef97c3e80 fix_argparse_persistmempool-22
	# Needs review & concept check: 23074 Package-aware fee estimation
	23106 fix_unlock_before_psbtsign-21						last=aebd7bceaf3 fix_unlock_before_psbtsign-22
	# TODO: 23139 jonatack/fix-rpc-trusted-field-help
	# Needs review: 23140 sipa/202109_addrmanbias
	# Not sure about this: 23142 meshcollider:202109_no_assert_corruption
	g430 gui_txlinks_g430-0.19								last=a3b35507ce7 gui_txlinks_g430-22
		# NOTE: Left off trivial string change
	g439 gui_hide_unused_icons-0.20
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs review: 23197 jonatack/fix-netaddress-UB-and-banman-fuzz-crash
	# Needs review: 23227 marco/2110-ToIntegral
	# Needs review of backport-rewrite in qt_catch_rpc_index_overflow-0.18 [alt to g446  marco/2110-qtRpcCons]
	# TODO: 23268 prayank23/dns-seed-fqdn
	# TODO: 23253 marco/2110-utilTxSeqId
	# Needs careful work: 23277 -  # wallet: Add size check on meta.key_origin.path
	# Needs care/review: 23304 achow101/inactivehd-derive-keypath-string
	# n/a without #20764? 23324 netinfo_peer_count_all_reachable-22
	# n/a without #19651: 23333 theStack/202110-wallet-fix_getwalletinfo_segfault_after_importing_descriptor
	# Maybe just the docs from #23341 ?
	23348 wallet_descr_hide_keypoololdest-0.21				last=ee03c782ba6 hebasto/211024-rpc-gwi
		# Held back std::optional refactoring 303ee60f817...ee03c782ba6
	# Needs review: 23365 -  # index: Fix backwards search for bestblock
	# Needs review + diff minimisation: 23380 jnewbery:2021-10-addrman-add-logging
		# + fix in #23434 ???
	# Moved to Knots bips.md update in branding: 21925 + 23410 hebasto/211101-bips
	# Needs work/diff-minimisation: 23418 marco/2111-txPoolPrioOverflow
@0.21.x-knots
# SOFTFORK:
	21934 rpc_getblockchaininfo_lockedin_statistics-0.21.1	fe4dfbf3f33	last=2b19f3443ef rpc_getblockchaininfo_lockedin_statistics
	22016 rpc_gbci_period_start-0.21.1+knots	4910107f0d1	last=70d7e0812a7 Sjors/2021/05/versionbits_period_start
	(CHECK-LAST)	last=d6d1a1b47eb rpc_gbci_period_start-22+knots
	# TODO: 21702 CheckTemplateVerify
# FUNCTIONALITY:
m	g275  gui_darkmode-0.21.2_pt1				8939a4a109b
		# NOTE: Fixed bug in gui#330 a simpler way b942216a1a7
	g154  gui_darkmode-0.21
	g366  gui_palettechange-0.21				55b04f94483
	-     restore_win32-0.21+knots				d37803a84cc	last=3e30ae0514e restore_win32-0.21
	(CHECK-LAST)	last=42e0d32b391 restore_win32-22  # (currently broken)
	-     restore_linux32-0.21					efa9ee85ed6	last=eeea5b787d4 gitian_linux32
		# NOTE: gitian only
	20963 gitian_power64-0.21+knots				d7151c1b629	last=543bf745d38 gitian_power64
		# NOTE: Originally #14066
		# Held back 31dbf0b677d..543bf745d38 - probably only applicable to master
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	14641 fundraw_minconf-0.21					fde6c8132bc	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	(CHECK-LAST)	last=4138cb304b8 fundraw_minconf
	12677 listunspent_ancestorinfo-21			28b3902be59	last=6cb60f3e6d6 listunspent_ancestorinfo
	18479 rpc_sign_show_fees-21					4d67400f273	last=47b2ba29df2 !kallewoof/sign-show-fees
		# NOTE: Originally #12911
	(CHECK-LAST)	last=8b77eb9d493 rpc_sign_show_fees
	g119  rm_send2self-mini-21					f97c6773966	last=aa744e4382e rm_send2self
		# NOTE: Originally #15115
	(CHECK-LAST)	last=6328248b214 rm_send2self-mini
	15423 tor_socks_port-0.21					67bfe9cad94	last=d37d95a9ea2 tor_socks_port
		# Held back 962f168a014..398df42f449
	15836 fee_histogram-21						82829beb890	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: removed extraneous Bitcoin-Qt.* files
		# NOTE: Backported some features/test from #21422 (but not API incompatibilities)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 ? See also git diff b1f9af22425..9d16921553b -w
	(CHECK-LAST)	last=ae9739d64cc fee_histogram+pr15836_api
	(CHECK-LAST)	last=f2ca3d35ee9 origin-pull/21422/head
	17463 gui_custom_sendyes					998dd492930
	15987 wallet_no_reuse-0.21+knots			7515d038c84	last=63d1070f734 wallet_warn_reuse_gui
		# NOTE: Uses older bloom filter implementation
	-     rpc_gai_txids-0.21+knots				01bfbd88472	last=f954a0d7a00 getaddressinfo_txids
	18772 -										bcfd0b89ee7 last=66d012ad7f9  # rpc: calculate fees in getblock using BlockUndo data
	22918 rpc_getblock_prevouts_fees-0.21		5b3f15dcda3	last=5c34507ecbb
	(CHECK-LAST)	last=80612d8aded rpc_getblock_prevouts_fees-22
		# Was originally #16083, then #21245
		# Held back change of verbosity to class enum, and generally kept #16083 base
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
		# + docs from #23320 (left off refactor commit)
	16795 rpc_inferred_output_descriptors-21	5de05c6c9f6	last=5e256883651 instagibbs/decode_descriptor
	(CHECK-LAST)	last=19a6902d148 rpc_inferred_output_descriptors
	18972 neutrino_whitelist-mini-21			892d210d2eb	last=339fe189eb9
	(CHECK-LAST)	last=3f0d4ecbc58 neutrino_whitelist-mini
		# NOTE: Diff-minimised
	17034 psbt_ver_proprietary_xpub-0.21		8cfa229a8e4	last=7f066240654 achow101/bip174-extensions
	(CHECK-LAST)	last=634c311b833 psbt_ver_proprietary_xpub-22-mini
		# NOTE: Held back `gdd 078abaac27e dc93052363d` comment correction
		# NOTE: Diff-minimised
		# NOTE: Now includes 16463 bip174_xpub-0.21+knots				8e6f8d3cc9c	last=9926a387eab achow101/bip174-xpub
m	17631 rest_blockfilter-0.21					31a7b2798a2	last=2b64fa3251a matt/2019-11-filter-rest
	(CHECK-LAST)	last=91feea1216a rest_blockfilter-22
		# NOTE: Dropped unrelated extra commits
	g319  gui_openuri_pastebtn-0.21				3cb5fcd37dd	last=dbde0558ce7
	(CHECK-LAST)	last=742a5de8f0b gui_openuri_pastebtn-22
		# NOTE: Used to be #17955
	18014 siphash_optimise_pr18014-0.21+knots	996d632f395	last=19e28a41168 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	18689 rpc_dumptxoutset_hr-21				86a235cbd1f	last=65d0697fe34
	(CHECK-LAST)	last=9427b409195 rpc_dumptxoutset_hr
	18722 O_addrman_unordered_map-0.21+knots	a8f034ffd43	last=a92485b2c25
		# NOTE: Restored C++11 compatibility from d6e782174ec
	g125  intro_prune_size-0.21					6d1b1a258f5
		# NOTE: Originally #18728
	19136 achow101/export-descriptor			3e817fee3cb	last=de6b389d5db
	19137 wallettool_dump-0.21+knots			71d5c75689e	last=23cac24dd3f achow101/dumpwalletrecords
		# NOTE: Disabled for BDB wallets since it doesn't dump/restore wallet id yet
		# NOTE: Changed to print warnings to stderr instead of stdout
		# NOTE: Diff-minimised
		# If bdb is reenabled, need #20267 49797c3ccfb
	19242 uaappend-21							0501a4912b2	last=9552978b318 uaappend
	19463 prune_locks-0.21						7688250cdac	last=1ad45edbfeb prune_locks
	19762 ryanofsky/pr/named					06d0b03981c	last=894c414dafb
	19776 -										6b92af07758	last=343dc4760fd  # net, rpc: expose high bandwidth mode state via getpeerinfo
	19873 mempressure-21						d629ab65bcc last=b9da34cec33 mempressure
	20226 rpc_listdescriptors-0.21				16086f5a271	last=647b81b7093
	21277 listdescriptors_normalized-0.21+knots	a45c8b5634a
		# TODO: Drop 0.21.0 compatibility "desc" when return format is updated or 21329 is ready
	g291  gui_trafficgraph_vert-0.21			088733fcf9a	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	21594 rpc_getnodeaddrs_network-0.21			d11f3acf005
		# Diff-minimised / doc changes left out
		# Includes part of #20965 (GetNetworkNames)
	21843 rpc_getnodeaddrs_by_network-0.21		cc3724d3400
m	20254 i2p_static-21+knots					b1aec3e913f	last=8b4a3714b91 vasild/i2p_static
		# + a4693f44cfe from #20685
		# TODO: +21825 ? (needs 21560?)
		#TODO: +21914
		#TODO: +21407+21631
		# TODO??? 21514 vasild:ignore_port_in_i2p
	# TODO: 20685 vasild/i2p_sam
	22211 i2p_IsRelayable-0.21+knots			03d28fdf8dd	last=7593b06bd12
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	20275 list_unsupported_wallets-0.21+knots	4db68baa351	last=f3d870fc227 ryanofsky/pr/exist
		# Mostly rewritten?
	20295 rpc_getblockfrompeer_wo_header-21		947c37b0b52	last=9181e2e2179 Sjors/2020/11/getblockfrompeer
	(CHECK-LAST)	last=3fa0053aabf rpc_getblockfrompeer_wo_header-22
	20391 rpc_setfeerate-0.21					ed17a7d8d62	last=1002e2d0d7f jonatack/setfeerate
	(CHECK-LAST)	last=4c0bc142de7 rpc_setfeerate-22
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20403 upgradewallet_pr20403-0.21+knots		69a6f1d0a06	last=3eb6f8b2e61 jonatack/upgradewallet-improvements
	20407 rpcauthfile-0.21+knots				0726f132d9d	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
	(CHECK-LAST)	last=53383d94200 rpcauthfile
		# NOTE: fixed bug, added multi-line support, and added tests
	g149  intro_assumevalid						8979d48f938
	20664 rpc_scanblocks-0.21					ad927cbdb4c	last=71b7cdb460e jonas/2020/12/filterblocks_rpc
	(CHECK-LAST)	last=fc381397e2b rpc_scanblocks
		# Held back insignificant API changes ab315e5294b...71b7cdb460e
	20702 rpc_getblocklocations-0.21			8db5bda17bd	last=9b03c654eb3
	(CHECK-LAST)	last=b60fdcbc2dc rpc_getblocklocations
	20827 ibd_prune_max							1dcbfaca3b6
	g163  gui_peer_conntype-0.21				1157253e0af  # jonatack-g/display-peer-conn-types
		# NOTE: Stripped unrelated string changes
	g180  gui_peer_relay_detail-0.21+knots		f76dd90768b	last=79a2576af1e jonatack-g/peer-details-connection-type-followups
		# +g203  Display plain "Inbound" in peer details
		# NOTE: Carries commit from g163 since it messes with the string anyway
		# NOTE: Left off final doxygen commit
	g179  gui_peers_conntype-0.21+knots			91c9dee9995	last=be4cf4832f1 jonatack-g/add-peers-dir-and-type-columns
		# NOTE: Held back 9f76ba6597c...be4cf4832f1 (no real change once we add gui#363 on top)
	g363  qt_peers_directionarrow-0.21+knots	4c6de52a7fc	last=41c881c8a78 qt_peers_directionarrow
	(CHECK-LAST)	last=??? qt_peers_directionarrow-22+knots
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
	20916 rpc_testmempoolaccept_wtxid-0.21		c20cc1b1caa	last=fa0aa87071e marco/2101-wtxidTestmempool
		# Diff-minimised
	g162  gui_peers_detail_network-0.21+knots	ce1628bb816
		# NOTE: Left out Peers table column & misc formatting changes
	20944 rpc_getmempoolinfo_total_fee-0.21		b864ecaf5ae	last=fa362064e38 marco/2101-rpcMempoolTotalFee
		# NOTE: Minor code rearranging to avoid conflicts
	g186  gui_bumpfee_privacywarn-0.21+knots	9ca3cf1b24b
	15129 rpc_removeaddress-0.21				423fd4425f4	last=fdbd01b50e0 benthecarman/remove_watch_only_address
		TODO: Temporarily neuter this or null-merge it?
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	(CHECK-LAST)	last=??? remove_watch_only_address-22
	# TODO: 18077 hebasto/20200130-natpmp
		# FIXME: Needs #21320
		# NOTE: Diff-minimised rebase of 2d5d98ce0aa is at c6ff5633b56
		# TODO: Switch to rwconf?
	21319 getblock_optimise						b79a8d71419
		# Context: 17529 rpc: Faster getblock using PureBlock
	19763 p2p_no_relay_to_origin-0.21+knots		083e7e509a0
	20365 wallettool_create_descriptors-0.21+k	49afa106a33
	21056 rpcwaittimeout-0.21					937b82478b1
		# +#22327
	21141 walletnotify_blockhash-0.21			7ea94a73ffe
	# Needs API finalisation: 21158 -  # lib: Add Taproot support to libconsensus
		#TODO: minimise
	21173 optimise_hexstr-0.21					b4ac741d755
	21260 rpcwallet_tx_in_mempool-0.21			28ec9283de6	last=46bf0b7b5d8
	g213  gui_payrequest_copyaddr-0.18			d165eeec1fc
	g214  gui_payrequest_disablena-0.18+knots	4853dd20a7e
	21327 p2p_ignore_tx_in_ibd-0.21				093927be571	last=648c5c73aef
	(LAST-CHECK)	last=??? p2p_ignore_tx_in_ibd-22
	21359 rpc_fundraw_includeunsafe-0.21+knots	52b632873e7
	g205  gui_save_txview_reqview_columns-0.19	6facbfb184d
		# +gui#368
		# NOTE: Diff minimised
		# NOTE: gui#229 not applicable to backport
	g206  gui_peers_relayinfo-0.21+knots		60e29d15120
	g226  gui_peers_lastblocktx-0.21+knots		1c333eb7c65
	g230  gui_backup_formats-0.21+knots			557904a49bb	last=e91a3f39d01 gui_backup_formats
		# NOTE: To avoid conflict with wallettool_dump-0.21+knots, added 5ab50bc98db GUI: Omit DbDump option for backup of BDB wallets
	21595 cli_addrinfo-0.21+knots				409d1d8be73
		# NOTE: Adapted error message for Knots
	21602 rpc_listbanned_deltas-0.21			7774e201444
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	# Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	21780 rpc_maxmempool-0.21					0bc176fa910	last=040b280c661 rebroad/MaxMempoolRPC
	(CHECK-LAST)	last=??? rpc_maxmempool
		# + bugfix and applying limit immediately
	22072 autoreindex-0.21						66d83231979	last=602f4da9178
	22147 p2p_protect_last_outHB-0.21			8f7863d9729
	# AFTER CORE RELEASES: (PR unknown) taproot descriptors +22156? +22166?
	22159 conf_append_cxxflags-0.10				deede4f8965	last=fa14c6818f4 marco/2106-buildPattern
	# TODO, Ugly Hack w/ conflicts: g256  hebasto-g/210323-peers
	# Preferred simpler fix in gui#275: g330  jarolrod-g/prompt-icon-colorized
	g281  gui_console_fontsize_shortcuts-0.21+k	9b125b71d81
		# NOTE: Diff-minimised and moved AddButtonShortcut to avoid conflict with #553 later
	g293  gui_peers_services_wordwrap-0.18		d8b9433aeef
	g298  gui_peers_altrowcolor-0.21+knots_pt1	840c66b724f
	g307  gui_peers_altrowcolor-0.21+knots		7d9f56d4c76	last=fdf80937d1c hebasto-g/210501-stripes
	(CHECK-LAST)	last=??? gui_peers_rowcolouropt-22
	g309  gui_neticon_peerstab-0.18				f3e47ff2e91
		# NOTE: Fixed Qt5.5 compatibility
		# Diff-minimised
	g318  gui_peers_copyaddr-0.14				172639c9e05	last=65d1d351786 jarolrod-g/copy-addr-peer
	(CHECK-LAST)	last=??? gui_peers_copyaddr-22
		# NOTE: Added keyboard shortcut
		# NOTE: Fixed Qt5.5 compatibility
	g343  gui_instaprogress-0.19				c62ac024c54
	g362  kbshortcuts_context-0.21+knots		60fbd5be8e7	last=e4c916a0ea0 kbshortcuts_context
	22288 torcontrol_dnslookup-0.21				d8f8412dcc4	last=cdd51e8ee15
		# Diff-minimised
	22372 multinotify
# Non-progress functionality:
	8751  sort-multisigs-0.21					e06c15ceea1	last=e11cb50a09  # multisig sorting
	(CHECK-LAST)	last=??? sort-multisigs-22
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	9152 sweepprivkeys							9d6360908e1
	9245 ionice									52ed64216eb
	-    ionice_win								22b1c9241e8
	8501  old_stats_rpc-0.21					2fa33c1f65c	last=7af0ea43b2
	(CHECK-LAST)	last=??? old_stats_rpc-22
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-0.21						24601755a13	last=63fb11652f
	(CHECK-LAST)	last=??? old_stats_qt-22
		# Held back on old version due to conflict with RPC updates...
		TODO: Consider backporting menu ordering changes
	9504 dumpmasterprivkey-0.21					f9192d9a751	last=07fc81109a
	g444  gui_netwatch-0.21+knots				539fa817d21	last=3c8fe76f6ee gui_netwatch
	(CHECK-LAST)	last=??? gui_netwatch-22+knots
		# NOTE: Was #9849
		TODO: Ensure bugfix is in
	10615 multiwallet_rpc-0.21+knots			cc2b14bbbcf	last=5a10f8307a5 multiwallet_rpc
	(CHECK-LAST)	last=??? multiwallet_rpc-22+knots
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset to wallet-restricted users for now
	10554 zmq_wtx-0.21+knots					dad75802d23	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	(CHECK-LAST)	last=??? zmq_wtx-22+knots
	20551 rpc_onetry_conntype					7a1723439c5
		# NOTE: Originally based on #12674
	10593 relax_invblk_punishment-0.21+knots	040052148d5	last=a06d916c75a relax_invblk_punishment
	10350 filtered_witblock-0.21				5cb7a4a645a	last=3f388ddcd3 codeshark/MFWB_no_bump_2
	(CHECK-LAST)	last=??? filtered_witblock-22
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				e40fcaeb7fe	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.21							d2f6a3d7d5d	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	(CHECK-LAST)	last=??? rest_fee
	11803 bugfix_dumpwallet_hdkeypath			3b64c7195f0
	12965 scriptthreads-0.20					8d959f05d3c	last=dfab6c6866 jonas/2018/04/svt
	(CHECK-LAST)	last=??? scriptthreads
	13203 dsha256_power8-0.20					9703ce00ee9	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		6ceb71baa4c
	15218 postibd_flush							84b38613864	last=d2ecb70d64  # validation: Flush state after initial sync
	(CHECK-LAST)	last=??? postibd_flush-22+knots
		# TODO: Rewrite after #17487 is ready/safe to merge
	15428 tor_gui_pairing-0.21+knots			e509f51807e	# latest code now
	(CHECK-LAST)	last=??? tor_gui_pairing-22+knots
	15421 tor_subprocess-0.21+knots				3de8ab01bf5	last=58c6cafd3a1 tor_subprocess
	(CHECK-LAST)	last=??? tor_subprocess-22+knots
	# TODO: tor gitian bundle!
	15633 nohbcbfornonwit-0.21+knots			c48ce12aa19	last=ac897f0bd3a nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# TODO: 16490 marco/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d					ca0940d77b6
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning-0.21+knots		43dad5a3906	last=f016cd420df restore_vbits_warning
	20832 rpc_validateaddress_error-0.21.1		46b02eee06b
	16807 bech32_error_detection-0.21.1+knots	47e52930e8f	last=3bc568d6753 meshcollider/201909_bech32_error_detection
	(CHECK-LAST)	last=??? old_bech32_error_detection
	n/a   rpc_compat_error_index-0.21+knots		c0b669d2000
	(CHECK-LAST)	last=??? rpc_compat_error_index-22+knots
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	-     gui_bech32_errpos-0.21.1+knots		63858cb48e1
	(CHECK-LAST)	last=??? gui_bech32_errpos-22+knots
NM	16807 bech32_error_detection-0.21+knots		80ccc5ad7c5	last=54e107add41 meshcollider/201909_bech32_error_detection
NM	-     gui_bech32_errpos-0.21+knots			c0b3d61d95e
	17636 guisettings-0.21						d4da7377cb0	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo-0.21+knots			95572de08a2	last=cdbd38df131  # getgeneralinfo RPC
	(CHECK-LAST)	last=??? rpc_getgeneralinfo
	18223 blockfilter_v0-0.19					fbe06449a10	last=5561e7a0c79
	(CHECK-LAST)	last=??? blockfilter_v0
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	# ---- BEGIN IN SEQUENCE ----
	19089 cli_getinfo_mwbalances-0.21+knots		19e9d705f4c	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	(CHECK-LAST)	last=??? cli_getinfo_mwbalances
	19092 cli_getinfo_mw_total_balance-0.21+knots	aedba84cdb0	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=??? cli_getinfo_mw_total_balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock-0.21+k	a03387247fb	last=1e868bbbb1b
	(CHECK-LAST)	last=??? wallet_rpc_lastprocessedblock-22+k
	19117 rpc_getrpcwhitelist					4e5e20bd9ec
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.21+knots	bfaf26b19f1
	(CHECK-LAST)	last=??? getrpcwhitelist_wallets-22+knots
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	17167 whitelist_outgoing-mini-0.21+knots	d6b39ef5628	last=81622ba1229 whitelist_outgoing
	(CHECK-LAST)	last=??? whitelist_outgoing-mini-22+knots
		#TODO: Split this up?
		# NOTE: d756d0a01a6 needs legacyWhitelisted in minified version!
		# NOTE: Originally #10594
	g165  gui_peers_splitter_ss-0.21+knots		8ea7e7fbc3f
		# +g194 Save/restore RPCConsole geometry only for window
		# NOTE: Changed setting name since our splitters don't match Core's
		# TODO: Each release, see if we need to bump setting name (and figure out back compat?)
	# FIXME: text below QR Code doesn't fit bech32 with Console font!
# Non-upstreamed functionality:
	-     gui_payreq_textedit-0.21				4a9c6fc46e5 gui_payreq_textedit
	-     rpc_mempoolentry_txhash				011b11763f6
	-     walletnotify_w_win-0.21+knots			0fafbd4a598	ast=a291491d2fd walletnotify_w_win
	(CHECK-LAST)	last=??? walletnotify_w_win-22+knots
	14137 win_taskbar_progress					35568cf34dd	last=18eb4dbb8a
	-     restore_blockmaxsize					7cf11b880fc
	7107 qtnetworkport							dd2ad9343f6	last=1f37c87 origin-pull/7107/head
	7533  sendraw_force							1c4e51255a4
		# NOTE: partial re-PR in #20753 by Marco
	11082 rwconf								9eefbf8c5fb
	7510  rwconf_gui							31da64c50bc
	 559 accept_nonstdtxn						854677f3a98
	g153 const_max_digits						2db6298f46c
	 929 tbc									b92159120bd
		TODO: * 7d4412c2fd9 GUI: Fix comparison of character size for Tonal font detection
	 553  bugfix_qt_uri_amount_parser-0.17		2bef446009c	last=e3ad5956dda bugfix_qt_uri_amount_parser
	-     mining_priority-0.21					c1b36c3197d	last=59671b2e665 mining_priority
		# Didn't backport next_block_height passing (maybe consider when/if someday cs_main can be released)
		# Didn't backport platform-independent double serialisation
	5861 gui_restore_addresses					8fa52dc8120
	5891  qt_console_history_persist-0.21+knots	7ed83221a81	last=0cd5fc301d6 qt_console_history_persist
	7219  rbf_opts-0.21+knots					ec4af75863b	last=5d58ebcc60f fullrbf # missing 91786d16ccc + revert34ae6640174
	(CHECK-LAST)	last=??? fullrbf-22+knots
	12146 opt_wallet_segwit2					c84af5db7d7
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			71cc4a727ef	# Latest code now
	-     gui_request_payment_label-0.19		bd9ec2f9431
	-     gui_peers_sort_network-0.21+knots		a3e6f0ec5e2
	(CHECK-LAST)	last=??? gui_peers_sort_network-22
		TODO: Replace with fixed commit in gui_peers_sort_network-22
# Non-upstreamed Knots compatibility:
	-    preserve_unsupported_keyflags			8c461dcdced
	-    mempool_knots014_compat-0.21+knots		4d6b8b17d26	last=1befffc0b48 mempool_dat_extensible
		# NOTE: Load-only
NM	9422  mempool_dat_extensible_mod-0.21+knots	7ed6f1a62c7
	11413 rpc_feemode_explicit_compat-0.21+knots	ca8dbc1e33d last=??? rpc_feemode_explicit_compat-22
	-     netperms_implicit_addr-0.21+knots		14687738e62	last=d1ce634b708 netperms_implicit_addr
	12674 rpc_onetry_nonpriv-0.21+knots			b235a94b1ba	last=054c2214369 rpc_onetry_nonpriv-22+knots
	# TODO: add a bitcoinknots.conf ?
	TODO: save/restore peer column widths? (in 22)
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				66fa127a85b
	-     bytespersigopstrict-0.21+knots		42fef5047e8	last=0d0b8e71fbb bytespersigopstrict-22+knots
	9749  unique_spk_mempool-0.21+knots			6f7822ceed3	last=b6f4ce7b327 unique_spk_mempool-22+knots
	-     bloom_default-0.21+knots				d714d612b62
	-     enforce_checkpoints-0.21				d41dcd18f7c	last=1de4af3f6c7 enforce_checkpoints
	n/a   checkpoint_update-0.21				79d59f9403e
		TODO: update
	10282 timebomb_knots						c8b2793aff0
	-     rwconf_policy-0.21+knots				bae9992c73c	last=6fdce5896c0 rwconf_policy-22+knots
		# Include Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	NOTE TO SELF: Remove release-notes-prNNNNN.md files BEFORE the svg icon merge so it doesn't get added then removed in different patch files >_<
	7483  svg_icon-0.21+knots					469d40983b1	last=??? svg_icon-22+knots
		FIXME: s/movies/animation in sed command
# BRANDING:
	n/a   knots_branding-0.21					1ee7ca43f35	last=2237adedb3f knots_branding-0.21
	n/a   ver_dropzero-0.21
	TODO: this should be 21.1.1 I guess... and bump copyright year once we get to 2022+
#FIXME: check there's no univalue push_back(bool) - see #20424 and stash 8724e2fae4
#FIXME: Check there are no menu icons
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: Check that we aren't deprecating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
TODO: Make sure there's no f['"] in python code
	n/a  (cherrypick=e0968d0328b2877330)		c7a144c218c	# doc/{bips,files}
		TODO: gcp 3364d31c3b5 7fc3fe1a1ab + add Taproot UASF BIP
	n/a  (bump_version=Knots:20210629)			0a9a4537a5d  # DO NOT CHANGE for just fixes
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=96316586c91)				f1cc3f1e0b1  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		gd marco/2109-fixArgParse
	n/a  (cherrypick=33ee7963ad4)				6addc3eccab  # update manpages (build first)
	n/a  (cherrypick=936fd13cd23)				a886811721c  # translation update
# NOTE: use git diff --minimal for patches!
