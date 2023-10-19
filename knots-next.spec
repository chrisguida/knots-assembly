timestamp 2023-10-18 06:50:55
lastapply no-merge

#.. checked up to PR #28674 / gui #767

checkout v25.1
@25.x-syslibs
# BUILD BUGS:
	# Needs review: 23609 hebasto/211126-reduce
	5872 subdir_incl_compat						3a646ac6a6b
	# If needed (MSVC only?): 27892 MarcoFalke/2306-translate-copy-
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb							a96a241ab69
	5416  sys_libsecp256k1						f4a59d2a40f
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	#26.xTODO: sys_libminisketch
	13789 bugfix_asm_pragmas					5caf7787338
	15155 test_external_bcli					b020b0febcf
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	# ---- BEGIN qt6 SUPPORT, TODO ----
	# NOTE: Partial qt6 backport in WIP_qt6-23
	# Needs review: 24813 hebasto/220409-appcheck        # Qt 6 (4/n)
	# TODO: tbc uses QRegExpValidator
	# Needs work/splitting-up: 24798 hebasto/220406-qt6
	# Needs review: 25191 hebasto/220523-qt6-mac
	# ---- END qt6 SUPPORT ----
	n/a   (delete_release_notes_fragments)
@25.x-knotsfixes
# TESTS:
	-     lint_relaxer							c6a96c5159d
	-     ci_knots-25
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
	27529 fix_addrman_test_bigendian-23
	27542 qa_runtest_ripemd160-23  # test: add ripemd160 to test framework modules list
	# TODO: 28027 achow101/2023-07-test-wallet-back-compat-updates
	# TODO: 28028 MarcoFalke/2307-test-stderr-
# FIXES:
	18818 guix_reltar_autogen_distclean			04ef73ac671	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again						fe1576ba2d8
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					06b2e2cae97	last=df5ece3e064 2020mingwthrd
	18490 bugfix_symcheck_pe_case				5ef693738d0
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 http_bind_error						f61e704deeb	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					524a221b075
		# NOTE: libevent-copied code up to date as of 2021-07-16 c29f1dbe116c88434e77721ca215b8d2082b247f
	 9524  rpc_pruneblkchain0					b327b038e9d	last=88883ae13d
	10731 log_more_uacomment					e94a07f681b
	14485 fadvise								d13637180c8
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					894b5b40dfc
	-     bugfix_rpc_getbalance_hacky			60f5367f46a
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 or 19420 (libevent cleanup)
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted -OR- 27539 Empact/2023-04-minimum-file-descriptor-18911
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	18194 bugfix_gui_edit_sendaddr-mini			3e18bb2be29	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	g658  intro_dont_change_user_prune			bbc927c3c8e
		# Was #18729
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				68bd18dadc7	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect OR 27245 fjahr/202303-pr19434 OR 27909
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs review: 19793 ryanofsky/pr/badsalv
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	g152  gui_notify_setup_bg					05368bdfa90
	-     bugfix_gui_drop_abc_confusing_hack	10a38703175
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				3a6e53d4b5b
	-     rpc_addconnection_mainnet				3f030489ee0
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22417 bpchild_closefds						05121d01966
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
		# NOTE: Currently uses ENABLE_EXTERNAL_SIGNER in place of USE_BOOST_PROCESS (not defined until #15421 merged)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				32caa7dec63
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs work: 23502 achow101/tr-low-fee-est
		# "rebase" in #26573 for post-#26567 (yet unmerged) refactor
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	g506  qt_qrcode_sizefixes					d036a08f614
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs review: 24066 whitslack/openrc-daemonwait
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	# Needs work: 24313 Sjors/2022/02/displayaddress						last=803387f054d
		# TODO: make sure this doesn't break compatibility (and fix review bugs)
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				1ae167e21ee
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-25+knots			1ce1a6ef90b	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	24957 -										c2e6976a79f	last=c4981e7f63a  # fix_prune_during_loadblock-22
	# Needs review: 24972 hebasto/220425-no-libtool
	# Needs review: 24994 hebasto/220426-consensus
	g595  qt_handle_autostart_errors-0.15		e467470fa8b	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	g599  ts_20220515-partial-25				5a4ab415cfe	last=d9411324066 ts_20220515
		# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
		#26.xTODO# Update with other commits that are beneficial
	-     boost_171_177_workarounds
		# NOTE: Originally part of #25111 hww_windows replaced by #25696 (merged)
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
	# Needs concept ACK/review: 25158 -  # rpc, wallet: add abandoned field for all categories of transaction in ListTransaction
	# Needs review: 25193 -  # indexes: Read the locator's top block during init, allow interaction with reindex-chainstate
	# Not clear this fixes anything: 25273 achow101/use-preset-tx-things
	# Needs review: 25380 darosior/fee_estimator_disable_cpfp
	#25.xTODO# Check on #25561
	25634 fix_wallet_blank_unset_pr25634-25
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	# Needs review: 25698 -  # crypto: avoid potential buffer overread in ChaCha20::SetKey
	g633  -													last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	# Needs review: 25938 mzumsande/202208_fixed_cjdns
	g662  qt_fix_txview_202209
		# Includes gui#368
	#25.xTODO# Needs review: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	# Needs review: 26152 -  # Bump unconfirmed ancestor transactions to target feerate
	#25.xTODO# Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	#25.xTODO# Needs review: 26331 -  # Implement CCoinsViewErrorCatcher::HaveCoin and check disk space periodically
	# TODO: Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	#26.xTODO# Sane fix for #24049
	g677 fix_qt_peers_na
	# Needs work/review: 26426 fjahr/202210-coinstatsindex-overflow
	#26.xTODO# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs review: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-25+knots				last=a6f567590b7
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	#26.xTODO# Needs review? 26762 hebasto/221228-queue  # Make CCheckQueue RAII-styled
	26828 andrewtoth/assumeutxo-remove-fix					last=0e21b56a44d
	#26.xTODO# Needs review: 26903 pstratem/2023-01-17-baseindex-commit-error
	#26.xTODO# Needs triage & review: 26950 fanquake:check_for_SecureZeroMemory
	#25.xTODO# Needs bugfix? (https://github.com/bitcoin/bitcoin/pull/27039/files#r1247267535) 27039 pinheadmz/reindex-read-only
	#25.xTODO# Needs work/review: 27071 vasild/lookup_subnet_cjdns
	#25.xTODO# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	# Triage/Needs review 27295 brunoerg/2023-03-improv-deserialize-v2
	27302 ignoredconf_err_def0-25
		# NOTE: Changed default for -allowignoredconf to 0 for compatibility
	# Needs review: 27307 -  # wallet: track mempool conflicts with wallet transactions
	27411 p2p_selfadv_privacy_pr27411-25					last=e7cf8657e11 mzumsande/202303_advertise_nets
	#25.xTODO# Alternative to: 27434 pinheadmz/chaintips-invalid
	27501 rpc_getprioritisedtransactions-25
	27554 qa_bcwallet_envvar-25
	g696 qt_rpcconsole_switch_wallet_opened-25				last=99c0eb9701e
	g719 theStack-g/gui-nuke_cc_dust_label					last=a582b4141f0
	# TODO: Needs work? g722 -  # Wallet : Allow user to navigate options while encrypting at creation
	#25.xTODO# Needs review? g739 achow101-g/gui-dont-blank-noprivkeys
	# Not needed in 25.x? 27556 -  # wallet: fix deadlock in bdb read write operation
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	27577 seednode_delay_fixedseeds-24
		#25.xTODO# Check #28016
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#26.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	#26.xTODO# Needs review: 27602 -  # net processing: avoid serving non-announced txs as a result of a MEMPOOL message
		# Maybe not useful with #27675 ?  https://github.com/bitcoin/bitcoin/pull/27602#issuecomment-1682070095
	-     fee_est_stalecheck-25+knots
		# Modifications to #27622 to allow on mainnet, and enable by default
	27631 fix_qa_feature_taproot_pr27631-21
	n/a   fix_div0_connecttip_loadblocks_log-25
		# Affected code removed in #27673
	#25.xTODO# Needs review: 27684 hebasto/230516-punish OR ???
	27708 postinit_exit_failure_code-25
	27717 test_util_env-0.16
	# If needed? 27720 furszy/2023_index_init_race_bugfix
	#26.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	-     fix_qa_mempool_packages_legacywallet-25
		# Fix-only alternative to #27735 MarcoFalke/2305-mempool-legacy-wallet-
		# Bug affects 23.x+ only, regressed in #23371 which made MiniWallet require Taproot (which legacy wallets don't support)
	27747 fix_decodedest_err_bytes_plural-25
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 forbid_nohelp-0.19								last=bfc2bb6a270
	27815 cli_forbid_multihelper-22							last=244e6c8db81
	# Needs review: 27820 -  # Sanitizing ports of -rpcconnect and -rpcport.
	# Needs review: 27823 mzumsande/202306_feature_init_fix
		#+28612
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	27846 fix_wallet_SRD_target_change-25
	27863 net_continue_peerhunt_pr27863-24
	27905 fix_FMWC_dirty_index-23
	#26.xTODO# Needs review: 27912 -  # net: run disconnect in I2P thread
	#25.xTODO# Some good fix for 27915 (#27920? partial backport in d319eef6e46)
	# Needs review: 27969 -  # bumpfee: ignore WALLET_INCREMENTAL_RELAY_FEE when user specifies fee_rate
	# Needs work: 27973 MarcoFalke/2306-byte-span-
	27981 fix_p2p_stalling_pr27981
	# Needs work: 27991 fanquake/instrument_libsecp
	#26.xTODO# Needs review (& extra care for wallet?): 27997 darosior/miniscript_non_satisfiable
	28020 fix_zmq_ipc_noportcheck-25						last=0b1762c90d1  # exclude ipc scheme from port check
		#26.xTODO# Maybe rewrite without `rfind`
		# NOTE: #27679 also implements this, possibly with unix: prefix instead?
	# If needed: 28026 furszy/2023_fix_index_timeout
	#26.xTODO# Needs review: g742 john-moffett-g/2023_06_ExitOnLooseArgument
		# NOTE: Explicitly mentions BIP 21 (we support BIP 20)
	28029 fix_zmq_errhandling_202307-25+k					last=07086589b27 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err-25					last=017ab85cecc fix_getblockfrompeer_rereq_err
	28056 rpcdoc_gbt_lpid_data-22							last=f6a26196cfb
	# Not a fix: 28076 no_std_fs_directly-25+k							last=7777034e96a MarcoFalke/2307-fs-lint-
		# Fix-only, diff-minimised
		# "I don't think anything here is a bug fix" -MarcoFalke, https://github.com/bitcoin/bitcoin/pull/28076#issuecomment-1682450942
	28077 fix_i2p_accept_flood-24							last=5c8e15c451e vasild/i2p_accept_issue22759
	28123 fix_nonstring_onelinedesc-25						last=5e3e83b0055 fix_nonstring_onelinedesc
	#26.xTODO# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	#26.xTODO# Ensure bug introduced by #26467 is fixed: https://github.com/bitcoin/bitcoin/pull/26467#discussion_r1269177446
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Windows-only functional test fix: 28204 hebasto/230802-sqlite
	# Needs concept: 28205 theStack/202308-netprocessing-reallow_fetching_of_genesis_block
	#25.xTODO# 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	#25.xTODO# Triage #28248
	#25.xTODO# FIXME: curl RPCdoc examples use wrong content type!
	g749 fix_qt_min_walletloading-25						last=32db15450a9 furszy/2023_gui_start_minimized
	#26.xTODO# Needs review (wallet compat?) 28307 furszy/2023_invalid_segwit_redeem_script_limit
	28471 fix_pkg_eval_sigops_pr28471-25+knots
		# NOTE: Left off first commit for now since it would just get reverted in #28345
	28345 fix_bytespersigop_checks-25						last=78a256505f3 fix_bytespersigop_checks
		# NOTE: Excludes removal of buggy wrapper for diff-minimisation; needs checking manually when assembly done
	# Needs review? 28340 -  # security: restrict abis in bitcoind.service
	# Needs review & diff-minimising: 28366 -  # Fix waste calculation in SelectionResult
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	28427 fix_idx_coinstats_reorg_fail-22					last=c0bf6679120 furszy/2023_index_coinstats_fix_reverseblock
		# Left off tip adding nodiscard attributes
	g752  fix_qt_cmdhelp_mention_uri-0.17
		# NOTE: Rewrote to be simpler and avoid BIP21 mention (Knots supports BIP20 too)
	# Non-trivial? (but only affects testnet?) 28472 instagibbs/2023-09-immutible-m_limit
	#26.xTODO# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	#26.xTODO# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# Needs review: 28546 ryanofsky/pr/mig  # bugfix: watchonly wallets created after migration have incorrect height values
	28554 fix_rpc_getnetworkhashps_heightchk-25				last=435ff29c5be
		# diff-minimised
	g757  qt_addrbook_walletname-0.18						last=58c9b50a952
		# diff-minimised
	g758  qt_nodewindow_chainname-22						last=9d37886a3b6
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	# Needs review: 28564 fix_conf_fuzzbin_main
	28662 fix_202310_fuzz_missing_rpcs-23					last=8ad6b773ca5 fix_202310_fuzz_missing_rpcs
		#26.xTODO# n/a, remove this
	28587 descr_disallow_hybrid_pubkeys-24
	# Needs backport review: 28602 achow101/migrate-hybrid-keys
		# Backport in descr_disallow_hybrid_and_uncompr_pubkeys-25.1 (#28677)
	# TODO: 28609 achow101/reload-all-migrated
	Needs review? 28610 achow101/migrate-avoidreuse
	#26.xTODO# Needs review and relevance: 28616 Sjors/2023/10/assume-unconfirmed
	# Needs review/simplification: 28649 vasild/reliable_socks5_handshake
	g765  fix_qt_walletlist_at_shutdown-24
	g766  theStack-g/202310-gui-fix_input_size_estimation_for_taproot_spends
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	#25.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
#@25.x-knots-lts-deps
	28561 depends_qt_update-25.1+knots
	#26.xTODO# FIXME -     depends_qt5kde
	# Needs review & relevance: 28627 fanquake/zeromq_4_3_5
@25.x-knots
# PERFORMANCE:
	n/a   rm_minisketch-25+k					5ddaa57ea1b	last=4e2d2910342 rm_minisketch-23+k
		#26.xTODO# Probably need to drop this
	# Needs review: 24158 JeremyRubin/epoch-mempool-reorg-updates
	# Needs review: 24589 -  # sha512.cpp improvements
	# Probably a bad idea: 24712 -  # wallet: reduce coin selection iterations
	# Knots doesn't support MSVC builds: 24773 Enable AVX2 implementation of SHA256 for MSVC builds
	# Needs work: 24901 -  # mempool: reduce lookups, insertions to cache in UpdateForDescendants
	# Needs review: 24926 -  # mempool: use mapNextTx.lower_bound in removeRecursive
	# Needs review: 25232 -  # rpc: Faster getblock API
	# Needs review: 25236 -  # wallet: use vector instead of list for transactions
	# Needs review & diff-minimising: 25297 -  # wallet: speedup transactions sync, rescan and load not flushing to db constantly
	# Needs review: 25968 sipa/202208_headerssync_optimize
	#26.xTODO# Needs review: 26008 achow101/improve-many-desc-ismine
	# Needs #26316 first & review: 26326 andrewtoth/remove-read-lock-in-net
	26375 zmq_optimise_duplread-25+k						last=7b631dc9b19 andrewtoth/no-read-zmq
	#26.xTODO# Needs review: 26415 andrewtoth/read-raw-block
	# Needs review: 26486 sipa/202211_batchnotfound
	# Opt-in & needs review: 26951 pstratem/2023-01-23-gcsfilter
	# Needs review: 26966 furszy/2022_parallelize_blockfilter_index_2
	# Needs review: 27006 furszy/2022_reduce_cs_main_scope_blockindex_nfile
	# Needs concept/review: 27050 -  # p2p, validation: Don't download witnesses for assumed-valid blocks when running in prune mode
	27334 -												last=bfb9291a866  # util: implement noexcept move assignment & move ctor for prevector
	# Needs review: 27427 -  # validation: Replace MinBIP9WarningHeight with MinBIP9WarningStartTime
	# TODO: 27675 ajtowns/202305-droprecentinvbloom
	# Needs review? Part of? 28226 martinus:2023-08-more-CBufferedFile
	# Needs review? 28233 andrewtoth/sync-on-periodic
	# Needs review: 28280 andrewtoth/sync-dirty
	-     dbcache_1TB-0.13
		# Inspired by #28358 Sjors/2023/08/double-your-coins---cache (needs work)
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 opti_merkle_mutation-0.17						last=42b25bbd939
	28592 ajtowns/202310-txrelayrate
		#26.xTODO# Make configurable? Or is that even sane?
# SOFTFORK:
	# TODO: 21702 CheckTemplateVerify
	# TODO: 28550 jamesob/2023-09-covtools-softfork
# FUNCTIONALITY:
	24448 guix_linux_i686_compat				e8a7da94969	last=c76ac9d57f2 guix_linux_i686
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonasschnelli/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# not ready: 9745 [RPC] Getting confirmations command
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# Needs copyright header: 17311 RandyMcMillan:fix-background-svg
	# Needs fixing/review: 17303 MarcoFalke:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues (see #28505 for hacky "fix")
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					58494ba48db	last=47b2ba29df2 !origin-pull/12911/head
		# Dropped rel notes file
		# NOTE: Originally #12911
		#25.xTODO# FIXME: "feerate" fails to account for sigops (see 21d85b5c0e)
	# Needs review and care (new index): 13014 jonasschnelli/2018/04/txindex_prune
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	g119  rm_send2self-mini						5f0c6043003	last=099dbe4224e rm_send2self
		# NOTE: Originally #15115
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	# Needs review: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram+pr15836_api				d001a8627f4	last=b94292a7cb jonasschnelli/2019/04/feeinfo
	(CHECK-LAST)	last=c5e53d0d21f origin-pull/21422/head
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ? (or not, since it's been abandoned...)
		# TODO: Drop ec2326304e0 since it's not needed with changes made in 998c34d27e7
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
		# TODO: https://twitter.com/RandyMcMillan/status/1490107008443457538?t=Qc4LO63rRuWxErtRel06EQ&s=19
		# 			aka 4613c88c91f4f3846aa62c929ad73d1a3e6ac70e
	22693 getaddressinfo_txids					cf21d8928be
	g562  wallet_warn_reuse_gui					1fe81821269
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				b2999f33de0	last=21a7f5ad0cb neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		055826bebb2
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-0.21+knots	0bb929ebf49	last=409c2e34522 elichai/2020-01-siphash
		# NOTE: Held back 9ed348ddea3...19e28a41168 (theoretical bug doesn't affect us)
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonasschnelli/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr					196de74322c	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								c6fa3b51229
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							120c96e9b59
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Needs work: 26485 ryanofsky/pr/nonly
		# CAUTION: May cause conflicts w/ compatibility options
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							a6c4444899c
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			30a7f0f9263	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-25						7fd4e8a1563	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
	20407 rpcauthfile							accabd6d59e	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						01f67fb5b69	last=cf940f0e5f5
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					1f12d13fadf	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							7135a8a2aec
	g363  qt_peers_directionarrow-25+knots		418d63d0c21	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						d4e05c2df25	last=1af20831806 Sjors/2021/05/hww-toggle
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise						bcf986d0d05
		# Context: 17529 rpc: Faster getblock using PureBlock
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 rpcwallet_tx_in_mempool-25+knots		00751692d11	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					6a47e2cd43b
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						7ac16e22ad6	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex							a2f94dca829	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	22159 conf_append_cxxflags-23				fd74eb4a20a	last=fa14c6818f4
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt				b94a0f57896	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
		# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							7edb7a43520
	24963 rpc_walletprocesspsbt_options-25		7ebcda357a1	last=baf99a9c789 rpc_walletprocesspsbt_options
		# Diff-minimised
		#26.xTODO# Add to descriptorprocesspsbt
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	# Needs review: 22729 vasild/torbind
	# TODO? 25621 -  # rpc/wallet: Add details and duplicate section for simulaterawtransaction
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Only if Core merges (alternative makes more sense): 22776 kallewoof:202108-getbalances-tx
	# Needs BIP? 22838 achow101:multipath-descs
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs work: g410  benthecarman/uppercase-uri
	# Needs API review: 23330 JeremyRubin/header-fetch
	23362 importfromcoldcard					8d8aa6dc195	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates-25+knots			d2ca24d7dc1	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
	(CHECK-LAST)	last=12d00272c71 rpc_savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			d5f647c9615	last=ad431ff5d18
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip					190259f05c2	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	g497  qt_fontsel-25+knots					63f1348f70c	last=a17fd33edd1 qt_fontsel
	-     qt_fontsel_qrcodes-25+knots			b9996e59773	 # latest code now
	# TODO: qt_fontsel_console
	# Needs work? g505  -  # RPCConsole: add hidePeersDetail() button and functionality
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	# Needs review & BIP changes: 24058 kallewoof/202201-bip322
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-25			b53beb352aa	last=97a69e232be
		# +RPC doc fix
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
	# Needs concept ack: g553 w0xlt-5/change_error_background
		# CAUTION: requires theming changes for gui#537
	# Needs work & complex test rebasing: 24539   # Add a "tx output spender" index
		# Partial rebase w/ stash at a1237c9a1851a8fc431467a0861c1d37b61566af
		# NOTE: When rebasing post-#21726, need to restore AllowPrune func ?
	# Needs review: 24545 -  # BIP324: Enable v2 P2P encrypted transport
		# Triage: +28577+28588+28634+partof(28645)
	# Not worth it? 24615/24569/24556 guix on non-x86
	# Needs review: 24824 -  # net: create IP to ASN database from file - makeseeds.py
	# TODO? BIP 179 (tho... Lightning) - upstream first to get translations?
	# Needs work: 24897 w0xlt/silent_payment_021
	# Needs work: 24950 -  # Add config option to set max debug log size
	# Needs work: 24952 -  # rpc: Add sqlite format option for dumptxoutset
	# Concept NACK? 25026 -  # rpc: Make pruneblockchain fetch old blocks if height is lower than pruned height
	# Needs triage & review: 25038 glozow/package-rbf
	# Needs licensing/review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku
	25183 rpc_fundraw_segwitonly				68789264835	last=9e7fd5c0fe3
		# Currently just an old version for Knots 23.0 compatibility (held back 1c5cfd84b3d...9e7fd5c0fe3)
		# Fixed tests with inspiration from 9e7fd5c0fe3
		# TODO: update without breaking compatibility? (new code looks buggy tho - needs rewrite?) (also, filtering by "input type" doesn't really make sense, though segwit filtering does)
	# Needs concept: 25261 -  # rpc: fetch multiple headers in getblockheader()
	#26.xTODO# 25269 -  # wallet: re-activate the not triggered "AmountWithFeeExceedsBalance" error
	# Needs concept review: 25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
		# Concept unsure: Hides logline by default; but maybe we want that with more info included?
	# TODO: 25366 w0xlt/desc_rpc
		# Besides the private key issue (removed; conceptual issues), RPC doc also has "addresses" where there would be a single address (in a details Object)
	# Needs work: 25434 w0xlt/bypass-timelocks
		# NOTE: Was #21413 glozow/2021-03-bypass-timelocks (never in Knots)
		# Also #25570 ?
	g626 qt_node_localaddrs-25								last=c47f01bf25e
	25680 rpcdoc_legacywalletonly-25+knots
		# Reverted importaddress note change since old one was better and gets replaced later in #27034 anyway
	# Needs completion & review: 25718 fjahr/2022-07-allowinbound
	# Needs concept/review: 25747 w0xlt/desc_file
	# Needs work: 25776 1440000bytes/bumpfee-inputs
	# TODO: 25796 -  # rpc: add descriptorprocesspsbt rpc
		# Needs refactors in #25939 and #24963
	# Needs concept/review: 25907 achow101/upgrade-to-tr-2
	# Needs work: 25923 jonatack/2022-08-statestats
	# TODO: 25939 -  # rpc: In utxoupdatepsbt also look for the tx in the txindex
		# Untested backport of last commit only c11660a2ee8 (unsure if first commit is move-only or needed in some capacity; this backport still refactors quite a bit)
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	# Needs review (or leave external?): 26052 -  # contrib: Add script to colorize logs
	-     guix_shell_compat-24
		# More compatible alternative to #26077 fanquake/guix_shell_over_environment
	28167 rpccookieperms-25+knots							last=b4b0d2adc91 willcl-ark/2023-07-rpccookie-perms
		# Was #26088 (not in a Knots release); held back cc0d0aeca68...b4b0d2adc91
		# Added: Param syntax check & log when option is being used
		# NOTE: If #28076 gets merged, adapt std::filesystem usage
	# Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	#26.xTODO# Minimised: 26162 Sjors/2022/09/taproot
	#25.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	#26.xTODO# Needs review: 26174 w0xlt/list_address_book
	27114 whitelist_outgoing-mini-25+knots		7f46d1a059e	last=89460f993dd
		# NOTE: Originally #10594, then #17167
		# Left off test framework refactoring in last commit
		# Held back 1e09c265a95...89460f993dd for now (ugly diff)
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme			last=d8434da3c14
	# Needs option/work: 26454 petertodd/2022-feebump-without-optin
	# Needs work/compat: 26467 achow101/bumpfee-choose-change-txout
		# MERGED(26.x) WITH SERIOUS BUG: https://github.com/bitcoin/bitcoin/pull/26467#discussion_r1269177446
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 brunoerg/2022-11-disconnectnode-subnet^			last=23f4c2cb452
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs review: 26839 -  # Add support for RNDR/RNDRRS for AArch64 on Linux
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	27511 rpc_getaddrmaninfo-24								last=28bac81a346
	28565 -  # rpc: getaddrmaninfo followups
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	26990 bcli_validation-24								last=11e0a80b19a
	27034 rpc_importaddr_for_descwallet-25+k				last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
		# Diff-minimised & tweaked to avoid breaking #23362
	# Needs review: 27052 LarryRuane/2023-02-getpeerinfo (maybe GUI port too?)
	# Needs review & API breakage considerations: 27101 pinheadmz/jsonrpc-2.0
	# TODO: 27213 amitiuttarwar/2023-03-network-outbounds
		# NOTE: Rel notes in #28189
	27216 rpc_getaddressinfo_isactive-24					last=85f83339dda pinheadmz/used-addr-ui
	# Needs review (and Core merge first?): 27255 darosior/tapminiscript
		#+28651+remainingof(28602)
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-25+knots									last=91771366a3d apoelstra/2023-03--codex32
		# Diff-minimised, doc bug fixed
	# Needs review: 27375 pinheadmz/tor-unix-domain-socket
	# Needs review? 27679 pinheadmz/zmq-unix-domain-socket
		# Duplicates #28020 with a different URI format
	# Needs work: 27409 ryanofsky/pr/1data
	# TODO (non-trivial): 27460 MarcoFalke/2304-import-mempool-rpc-
		#+28289
		# relnotes from 28637
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	g740  qt_psbtdlg_ismine-21
	#26.xTODO# Self-review: 27509 vasild/relay_tx_to_priv_nets
	# Needs concept/review: 27534 -  # rpc: add 'getnetmsgstats', new rpc to view network message statistics
	# Needs review: 27596 jamesob/assumeutxo
		#+ just the very minor fix from #28562 (82e48d20)
		#+ Needs concept & review: 28569
		#+ Triage: 28589+28590+28608+28625+partof(28645)+28647+28652+28659+28666+28669+28670
	27600 p2p_forceinbound-25+knots							last=311902f2cf9 pinheadmz/whitebind-evict
		# Excluded top-commit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27761 p2p_log_stalling_ip-22
	27770 rpc_getblockfileinfo-25+knots						last=5110139d397 furszy/2023_rpc_getblockfileinfo
	27801 sqlite_trace-24									last=ff9d961bf38 ryanofsky/pr/sqtrace
	# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
	# Needs review & BIP finality & might have wallet changes: 28202 josibake/implement-bip352-receiving
		# Note alternative (approach NACK'd) in #28453
	# Needs review & BIP finality: 27827 josibake/silent-payments-base-pr-slim-down
	# Needs review & concept: 28241 Sjors/2023/08/silent-index
	# Needs work & maybe removing an anti-feature?: 27836 furszy/2023_rpc_fetchblock_improvements
	# Needs review: 27837 furszy/2023_introduce_block_request_tracker
	# Needs work: 27854 -  # [WIP] add a stratum v2 template provider
	# Needs review & compat checking: 27859 -  # Mempool: persist mempoolminfee accross restarts
	# Needs review: Ensure fully optional (opt-in?): 27877 -  # wallet: Add CoinGrinder coin selection algorithm
	# Needs review: 28060+28483+28052 MarcoFalke/2306-fs_stuff-
	28101 torcontrol_help_defport-23						last=9a84200cfc9
	#26.xTODO# Needs work/deps: 28196+28489+28525 sipa/202307_bip324_transport
	# Needs review? 28207 MarcoFalke/2308-xor-memepool-
	# Needs work: 28331 sipa/202308_bip324_integration
	28414 rpcwallet_processpsbt_finalhex-25+knots			last=2e249b92276 pinheadmz/psbt-final-process
		# Left out test refactoring to use the new feature & relnotes
	# Extends #25796, TODO: 28492 -  # RPC: descriptorprocesspsbt returns hex encoded tx if complete
	# Needs review: g753 -  # Add new "address type" column to the "receiving tab" address book page
	#26.xTODO# hebasto-g/230911-bip324-peer-details
	# Needs review: 28459 fanquake/mbranch_protection_arm_darwin
	# Needs review: 28461 fanquake/windows_ssp_roundup
	# Needs review and concept: 28463 mzumsande/202308_increase_block_relay
		# Why not just increase inbound capacity to max anyway?
	# TODO (build failure / missing dep?): 28523 rpc_getrawaddrman-25+knots						last=352d5eb2a9e 0xB10C/2023-09-verbose-getaddrmaninfo
	# Needs API finalisation: 28539 brunoerg:2023-09-taproot-libconsensus
		#TODO: minimise
# Non-progress functionality:
	8751  sort-multisigs-25+knots				c42c63f0c5c	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					614547cdc59	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys							7b2398d7c36
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245 ionice									0a0ecc14783
	-    ionice_win								c5ef9ca0e30
	8501  old_stats_rpc-25						9936cf72d91	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-25+knots					b784f359eea	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504  dumpmasterprivkey-25					95035ce6202	last=07fc81109a
	g444  gui_netwatch-25+knots					a44e7b33409	 # Latest code now
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-25+knots				664cc4b0fb1  # latest code now
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet to wallet-restricted users for now
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
		#26.xTODO# Add dc244382e5d QA: rpc_users: Test rpcauth wallet restrictions
	10554 zmq_wtx-25+knots						ad1bcb2928e	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
		# Extended doc/zmq a bit to match additions from #14060 and #23471
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					edca5b8af00
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment				432fae20806
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
	10350 filtered_witblock-25				abf017ad612	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				9add7811b6d	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								1cc702fa199	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			fea9d68f84d
	12965 scriptthreads-25+knots				0345cf11100	last=dfab6c6866 jonasschnelli/2018/04/svt
	13203 dsha256_power8-25						7610e2e0b16	last=3b402e0738 TheBlueMatt/2018-05-asm
		# NOTE: Stripped out benchmark change
		#26.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	-     dsha256_power8_asm_pragmas-25			3ba39b15ebb
	15218 postibd_flush-25						e194bb9b731	last=0c7ee166463
	15428 tor_gui_pairing-25+knots				723c1c46950	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-25+knots				6992e4922ed	# Latest code now
	# TODO: tor guix bundle!
	# TODO: 16490 MarcoFalke/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d-25+knots			bf517f7cdd2
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					5c81646f647
	n/a   rpc_compat_error_index-25+knots		84cf91ccb21
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos-25+knots			5bdd6ed25cb last=539beeaae85 gui_bech32_errpos
	17636 guisettings-0.21						c8db2908604	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					45249322ccb	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						b2b9c2f14a5	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances				03994a2e5e3	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance			91193606e68	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	26094 wallet_rpc_lastprocessedblock-25+k	c363d978f97	last=710b83938ab
	19117 rpc_getrpcwhitelist					bdbf8ecf130
		# NOTE: Was #18827 before any Knots merge
		#26.xTODO# Extend dc244382e5d test
	-     getrpcwhitelist_wallets-25+knots		7a2a3bc75cd
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-25+knots		6c8fdc9a690
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	#26.xTODO# Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
# Non-upstreamed functionality:
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	n/a   restore_feefilter_opt					b0a928d3f25
	-     gui_payreq_textedit					e2018a567ae
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				5ba35244a0b
	-     walletnotify_w_win-25+knots			2d3f0b887c9	# Latest code now
	14137 win_taskbar_progress-25.1+knots		6b06461d6b8	last=18eb4dbb8a
	-     restore_blockmaxsize					ed77d9b99c2
	7107  qtnetworkport-25+knots				c37c20d1ca7	last=1f37c87d8f2 origin-pull/7107/head
	7533  sendraw_force-25+knots				9746cd166d6 last=2627c0937f8 sendraw_force
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532 if merged
	11082 rwconf-25+knots						dbc972ce598 # Latest code now
	7510  rwconf_gui-25+knots					7342e194bdb
	559   accept_nonstdtxn-25+knots				2ad1e272d70
	 929 tbc									65ace212fac
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
	 553 bugfix_qt_uri_amount_parser			f110cdc6b5d
	-    mining_priority						79de7fcebc8  # NOTE: now the latest code, rebased
		#25.xTODO# FIXME: Lots of lock warnings from clang!
	5861 gui_restore_addresses					d435b0e1596
	5891  qt_console_history_persist			aaedbe6c41a	last=0cd5fc301d6 qt_console_history_persist
	7219  rbf_opts-25+knots						4eea3457d1a	# Latest code now
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					2a61c92f17e
		# TODO: Split out legacy address preference to be more explicit
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			f3109a9759d	# Latest code now
	-     gui_request_payment_label-0.19		45064c919be
	-     gui_peers_sort_network-23				d851c7b5730
	-     gui_peers_no_net_column				6d7c55fa917
	22439 guix_in_gitian-23+knots				b3670947f2d	last=ebda0463748 achow101/guix-in-gitian
	-     rpc_getblockfrompeer_future
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		b89d300855f
		# Prior Knots bundled this in with #20295
	#25.xTODO# revert #24031  build: don't compress macOS DMG -- FIXES #26176
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
# Non-upstreamed Knots compatibility:
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-25
		# Effectively reverts #24505
		#26.xTODO# revert? #27869  wallet: Give deprecation warning when loading a legacy wallet
		#26.xTODO# revert? #28597  wallet: No BDB creation, unless -deprecatedrpc=create_bdb
		#26.xTODO# revert? gui#764  Remove legacy wallet creation
	14641 fundraw_min_conf_deprecated-25+knots	67bb2fae2cb	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			2b802cfbcf9
	-     netperms_implicit_addr				3ec6f62de90
	12674 rpc_onetry_nonpriv-25+knots			1ac3b6f764a
	-     rpc_getblockfrompeer_nodeid_compat	f41b36c5abe
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-25+k		a71fc4dd708
		#26.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				d3686b812ea
	-     bytespersigopstrict-25+knots			1a34431caca
	9749  unique_spk_mempool-25+knots			68175ac94c1
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	28408 match_more_datacarrier-25+knots					last=abd19ad480f match_more_datacarrier
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     datacarriercost-25+knots
		#25.xTODO# Add tests and make sure boundaries are correct
	# Needs concept ACK: 28334 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	-     bloom_default-0.21+knots				4910b8c3600
	-     wallet_avoid_newerchange				a5e70c68636
	#26.xTODO# Revert #25725
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	#25.xTODO# Adapt existing limits to apply to Taproot?
	#25.xTODO# Ordisrespector equivalent (Ordislow??)
	#25.xTODO# -blockpreference=smaller|larger,lessdata|moredata (or match our own policies?)
	-     enforce_checkpoints					840dddd5a6e
	n/a   checkpoint_update-25					ec23e329857	#26.xTODO# last=70996dfdd9b checkpoint_update-0.21
		#26.xTODO# Add new checkpoint
	10282 timebomb_knots						28c6dff687b
	-     rwconf_policy-25+knots				85b37875e50
		# Includes Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
	# Needs review/options: 26348 -  # Make P2SH redeem script "IF .. PUSH <x> ELSE ... PUSH <y> ENDIF CHECKMULTISIG .. " standard
	# Needs refactoring to only happen for -acceptnonstdtxn(?): 26398 instagibbs/relax_too_small_tx_equality
	# Problematic: 26403 instagibbs/ephemeral-anchors
	# Needs review & optionality: 26451 sdaftuar/2022-11-fixrbf
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		7502bba0dc8
	7483  svg_icon-25+knots						edbcba95282
		#25.xTODO# TEST IN CI & GUIX
	n/a   tbc_font								9929a597b3d
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/
# BRANDING:
	n/a   knots_branding-25						0ef366334de
		#26.xTODO# Review security policy
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#25.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
# TODO: Check that we aren't deprecating anything in Core
#25.xTODO# verify src tarball includes rendered_icons incl nsis-header
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Check #26039 doesn't break anything
# TODO: Ensure std::filesystem isn't introduced (see #28076)
#26.xTODO# Ensure options arguments use new OBJ_NAMED_PARAMS type
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
	n/a  (cherrypick=ee7ef94595a7793b6e)		f6260178fc7	# doc/{bips,files}
	n/a  (bump_version=Knots:20231018)			3d04837ba68
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist		91954f0400c
	n/a  (cherrypick=735d2b4d8bb)				500a43eca75  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=e176316e332)				dd99e2b4305  # update manpages (build first)
		TODO: update bitcoin conf (like d68b6abeb84)
	n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
		BELOW TODO: ensure 26117 is fixed
# NOTE: use git diff --minimal for patches!

# TODO: @25.x-knots-android
