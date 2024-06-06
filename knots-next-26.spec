timestamp 2024-06-04 17:30:54
#lastapply no-merge

#.. checked up to PR #30225 / gui #820

checkout v26.1
@26.x-syslibs
# BUILD BUGS:
	# Needs review: 23609 hebasto/211126-reduce
	5872 subdir_incl_compat						517e84c15db
	29362 fix_objcxxflags_pr29362-26			1f0ca2cea82	last=17861b9cd59 hebasto/240201-objcxx
		FIXME: Address https://github.com/bitcoin/bitcoin/pull/29362#issuecomment-1964389168
	-     fix_evhttp_util_nodep-25				bff25d2f97f
	29859 fix_ac_atomic_double-22				be89cb46852
	Triage: 30216 hebasto/240602-libevent
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb							492d15bf29d
	5416  sys_libsecp256k1-26					259dcb7e012	last=7c70b396b1d sys_libsecp256k1
	# TODO: sys_crc32c ??
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	#27.xTODO: sys_libminisketch
	13789 bugfix_asm_pragmas					5de4b81c017
		# Should revert #28893 if merged?
	15155 test_external_bcli					f29878dc855
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	# ---- BEGIN qt6 SUPPORT, TODO ----
	# NOTE: Partial qt6 backport in WIP_qt6-23
	# Needs review: 24813 hebasto/220409-appcheck        # Qt 6 (4/n)
	# TODO: tbc uses QRegExpValidator
	# Needs work/splitting-up: 24798 hebasto/220406-qt6
	# Needs review: 25191 hebasto/220523-qt6-mac
	# ---- END qt6 SUPPORT ----
	#28.xTODO# Revert #29904
	n/a   (delete_release_notes_fragments)
@26.x-knotsfixes
# TESTS:
	-     ci_knots-26							fd493422771
	29441 ci_parallel_pr29441-26				76d42a01e93
	28372 fix_fuzz_coinsel_pr28372-26			373c5a19537
	-     lint_relaxer-26+knots					2b540596402
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
	# As needed: 29740 -  # ci: Print tsan errors to stderr
	# Triage: 29753 furszy/2024_test_fix_p2p_node_network_failure
	# Triage: 29788 maflcko/2404-ci-bcfcc-
	# Triage: 29832 fanquake/revert_29788
	# Triage: 30193 -  # ci: move ASAN job to GitHub Actions from Cirrus CI
# FIXES:
	18818 guix_reltar_autogen_distclean			510ed993763	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again						3bcab14451d
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					80e67ed30c8	last=df5ece3e064 2020mingwthrd
	18490 bugfix_symcheck_pe_case				48a5ba6bcc5
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 http_bind_error						618a7c24267	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					8e1fe24ec0c
		# NOTE: libevent-copied code up to date as of 2023-11-22 cfb2b89a1d0642abd6389913e237f49c662502e4
	 9524  rpc_pruneblkchain0					79b87d35c9a	last=88883ae13d
	10731 log_more_uacomment					de725342027
	29614 bufferedfile_fclose-26				80841406c14	last=aec5e0f558a bufferedfile_fclose
	14485 fadvise-26+knots						803e535fdd4	last=289e88b3133 fadvise
	(CHECK-LAST)	last=79e4722e62a fadvise-27+knots (after addressing FIXME below)
		# Was #12491
		FIXME: Non-trivial merge with bufferedfile_fclose-26 fails to actually close m_src (gdd fadvise-26+knots fadvise-27+knots)
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					5659f14cee6
	-     bugfix_rpc_getbalance_hacky			18965ffe570
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
	18194 bugfix_gui_edit_sendaddr-mini			96b24841992	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	g658  intro_dont_change_user_prune			03d9b5d9233
		# Was #18729
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				cd84aa231e1	last=3f9cc0cd736 Saibato/wallet_351
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
	g152  gui_notify_setup_bg					4998a9afe78
	-     bugfix_gui_drop_abc_confusing_hack	fb33db4b164
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				0308929148a
	-     rpc_addconnection_mainnet				14216e91d04
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22417 bpchild_closefds						f95414b7776
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
		# NOTE: Currently uses ENABLE_EXTERNAL_SIGNER in place of USE_BOOST_PROCESS (not defined until #15421 merged)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				8906207569d
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs work: 23502 achow101/tr-low-fee-est
		# "rebase" in #26573 for post-#26567 refactor
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	g506  qt_qrcode_sizefixes					ec363d379da
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs review: 24066 whitslack/openrc-daemonwait
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	# Needs work: 24313 Sjors/2022/02/displayaddress						last=803387f054d
		# TODO: make sure this doesn't break compatibility (and fix review bugs)
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				5ac9a975f93
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-25+knots			be60ee83b52	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	# Needs review: 24972 hebasto/220425-no-libtool
	# Needs review: 24994 hebasto/220426-consensus
	g595  qt_handle_autostart_errors-0.15		3bf9249983b	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	g599  ts_20220515-partial-25				2bee2521267	last=d9411324066 ts_20220515
		# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
		#26.xTODO# Update with other commits that are beneficial
	-     boost_171_177_workarounds				41ee93f9fcf
		# NOTE: Originally part of #25111 hww_windows replaced by #25696 (merged)
	#27.xTODO# Check if we need to revert #29489 (related to hww_windows???)
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
	# Not clear this fixes anything: 25273 achow101/use-preset-tx-things
		#+29065+29272
	# Needs review: 25380 darosior/fee_estimator_disable_cpfp
	#27.xTODO# Check on #25561
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	# Needs review: 25698 -  # crypto: avoid potential buffer overread in ChaCha20::SetKey
	g633  -										b45041870c6	last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	# Needs review: 25938 mzumsande/202208_fixed_cjdns
	g662  qt_fix_txview_202209					85790d1e298
		# Includes gui#368
	#26.xTODO# Needs review: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	#26.xTODO# Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	# TODO: Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	#26.xTODO# Sane fix for #24049
	g677 fix_qt_peers_na						9a101d72211
	# Needs work/review: 26426 fjahr/202210-coinstatsindex-overflow
	#26.xTODO# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs review: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-25+knots	8d1b8e744ee	last=a6f567590b7
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	#26.xTODO# Needs backport? 26762 hebasto/221228-queue  # Make CCheckQueue RAII-styled
	#26.xTODO# Too minor? 26903 pstratem/2023-01-17-baseindex-commit-error
	#26.xTODO# Needs triage & review: 26950 fanquake:check_for_SecureZeroMemory
	27039 fix_reindex_readonly_blkfiles-26		7507b1364f9
	#26.xTODO# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	# Needs review: 27307 -  # wallet: track mempool conflicts with wallet transactions
		# CAUTION: Even merged, this appears to possibly show a higher balance than the user actually has for sure??
	#26.xTODO# Alternative to: 27434 pinheadmz/chaintips-invalid
	# TODO: Needs work? g722 -  # Wallet : Allow user to navigate options while encrypting at creation
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	# Needs concept/review: 28016 -  # p2p: gives seednode priority over dnsseed if both are provided
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#26.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	-     acceptstalefeeestimates_mainnet_opt	c868eff4234
	#26.xTODO# Needs review: 27684 hebasto/230516-punish OR ???
	#26.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 -										5b7188dfc5d	last=bfc2bb6a270  # forbid_nohelp-0.19
	27815 -										c6da3059a99	last=244e6c8db81  # cli_forbid_multihelper-22
	# Needs review: 27820 -  # Sanitizing ports of -rpcconnect and -rpcport.
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	#26.xTODO# Needs review: 27912 -  # net: run disconnect in I2P thread
	27935 qafix_banman_conditionalcmp-23		17fe217c93c
	# Needs review: 27969 -  # bumpfee: ignore WALLET_INCREMENTAL_RELAY_FEE when user specifies fee_rate
	# Needs work: 27973 maflcko/2306-byte-span-
	# Needs work: 27991 fanquake/instrument_libsecp
	28020 -										c61732775d9	last=0b1762c90d1  # exclude ipc scheme from port check (fix_zmq_ipc_noportcheck-25)
	-     zmq_unix_uri_compat-25				20ea6f034cd
	g742 qt_err_fixg741_in_g742-21				58f215ef927
	(CHECK-LAST)	last=4fcbd58ba59 qt_ambig_uri_refs  # NOTE: also could impact #28554
		# NOTE: Explicitly mentions BIP 21 (we support BIP 20)
	28029 fix_zmq_errhandling_202307-mini		9edad69540c	last=07086589b27 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err		9de16a02a53
	# Not a fix: 28076 no_std_fs_directly-25+k							last=7777034e96a maflcko/2307-fs-lint-
		# Fix-only, diff-minimised
		# "I don't think anything here is a bug fix" -maflcko, https://github.com/bitcoin/bitcoin/pull/28076#issuecomment-1682450942
	#26.xTODO# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Needs concept: 28205 theStack/202308-netprocessing-reallow_fetching_of_genesis_block
	#26.xTODO# 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	#26.xTODO# Triage #28248
	29946 jsonrpc_content_type-26+mini			f0644e1b77c	last=f90a84d6150 jsonrpc_content_type
		# Rebased in Core as #30215 (merged unmodified)
	#26.xTODO# Needs review (wallet compat?) 28307 furszy/2023_invalid_segwit_redeem_script_limit
	28345 fix_bytespersigop_checks-mini			39a0f361e17	last=78a256505f3 fix_bytespersigop_checks
		#26.xTODO# NOTE: Excludes removal of buggy wrapper for diff-minimisation; needs checking manually (to ensure wrapper doesn't get used even in final/complete merge of all PRs) when assembly done
	28340 -										acede199ab6	last=0244416aacb  # security: restrict abis in bitcoind.service
	# Needs review & diff-minimising: 28366 -  # Fix waste calculation in SelectionResult
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	g752  fix_qt_cmdhelp_mention_uri-0.17		29c20c7c1f5	last=ede5014c445
		# NOTE: Rewrote to be simpler and avoid BIP21 mention (Knots supports BIP20 too)
	28486 fix_test_winsock_init-26				218ede5b10b
	#26.xTODO# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	#26.xTODO# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# QA only? 28546 ryanofsky/pr/mig  # bugfix: watchonly wallets created after migration have incorrect height values
	28554 fix_rpc_getnetworkhashps_heightchk-25	7d59444a3c5	last=9ac114e5cd9
		# diff-minimised & kept compatible
	g758  -										4dbdc47cc9a	last=9d37886a3b6  # qt_nodewindow_chainname-22
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	28564 fix_conf_fuzzbin_main-24				8a9699273cb	last=b228803dcff fix_conf_fuzzbin_main
	28610 fix_wallet_migrate_entireaddrbook-26	33fd20d72d3
	#27.xTODO# Needs review and relevance: 28616 Sjors/2023/10/assume-unconfirmed
	28649 reliable_socks5_pr28649-26			33163154b73
	# Needs review & triage: 28678 sipa/202310_miniscript_assume
	# Needs review: 28724 achow101/cleanup-accidental-watchonly-mkeys
	# Needs review/diff-minimising? 28737 -  # doc: Fix bugprone-lambda-function-name errors
	g773 fix_qt_unlock_watchonly-0.20			9f392cdf6b6	last=517c7f9cba3 achow101-g/gui-skip-encryption-check-for-watchonly
	# Not worth it? 28771 achow101/lcov-opts
	# Not worth it? 28774 vasild/avoid_returning_reference_to_mutex_guarded_member
	# Needs review: 28776 BrandonOdiwuor/gui_overview_page_add_used_balance
	# -- Needs review: g775 -  # gui: add used balance to overview page
	# Needs review: 28780 -  # log: torcontrol opt checks
	# As needed: 28782 -  # test: Add missing sync on send_version in peer_connect
	-     fix_keep_notmy_cookie-26.1+knots		91ebfad5931	last=4842324b7d0 fix_keep_notmy_cookie
		# Originally part of #28784, but regressed in d95dde9441f...7cb9367157e
	# Meh? 28822 -  # test: Add missing wait for version to be sent in add_outbound_p2p_connection
	# Needs review: 28824 fix_asm_nodecimals-23								last=fde11cb0fa3 willcl-ark/asm-full-hex
		# FIXME: disambiguate opcodes too?
	# TODO: 28834 -  # net: Attempts to connect to all resolved addresses on addnode
	# libmultiprocess (not supported by Knots yet): 28846 fanquake/fixup_multiprocess_arm64
	28848 fix_rpc_submitpkg_all_results-26		906b8bd6bb6
	28849 fix_qa_v2t_pr28849-26					29263fd50fa
	28868 fix_wallet_migrate_pr28868-26			62b7e01a8c0
	-     fix_doc_upnp_def_post26896			1344300494a	last=92f88a96290 fanquake/redundant_upnp_ifdef
		# Alternative to #28874
	28936 dnsseed_petertoddnet-25				e5eb2d7024d
	28944 sendall_antifeesniping-26				25c101b1f14	last=fa1fa351584 ishaanam/sendall_anti_fee_sniping
	28946 fix_keep_notmy_pidfile-26.1+knots		14a9af7659d
	#27.xTODO# FIXME: real fix for issues in #28967 (OR #28981?) -- NOT A REAL BUG IN PRACTICE, revert the removal?
		# See also #29868
	28976 fix_wallet_migrate_blank-26+knots		b4dfe3cbd0d
		#+29367
	# Needs review: 28979 ishaanam/sendall_ancestor_aware_funding
	# FIXME: rpc_net test fails! 28998 rpc_addpeeraddress_return_error-26
	29022 fix_btx_replacable_blank-21			b0d45d03bc0
	29027 fix_wallet_keyparsecheck_pr29027-26	b8042ae8457
	# MSVC: 29044 hebasto/231209-msvc-qt
	g780  fix_qt_txview_prG780-25				87a06746a28	last=b2e531e70a8
	29141 fix_rpcauth_blank						25e07bdf5f2
	29253 fix_wallet_dbguard_pr29253-26			870ac94622d
	29112 fix_wallet_single_batch_only-26+knots	2e19bf6c33f
	# Needs review: 29124 achow101/fix-double-keypath
	# Needs work? 29144 fix_init_empty_settingsjson-23					last=725a1fc7a7d furszy/2023_empty_settings_file
		#+29301
	29691 dnsseed_dashjr_2024					5029faa1646
NM	29147 guix_attachable_sigs					b7df3ed03fc
	# Needs work: 29147 guix_attachable_sigs					ad4fe4b83a4
		# GPG discourages clearsign signatures!
	# Needs review: 29155 -  # wallet: move lock at the top of ReleaseWallet
	29184 rpc_scanblocks_ffp_named				b19edb5a071
	29175 fix_rpc_estmode_unset_case-24			43c05b45541	last=be8ae64b82e
	29177 fix_conf_latomic_check-25				ed5766cc0d8
	# Triage: 29192 sipa/202401_serfloat_weaken_test
	29237 fix_depends_PATH_w_spaces-26			48c1e73e2bb
	(CHECK-LAST)	last=92f7e7f3633 maaku/allow-spaces-in-path
		# Was: 28733 fix_depends_PATH_w_spaces-22
	29243 fix_wallet_cleanup_handler_pr29243-23	d9db329674f
	29249 depends_gen_id_nm-25					74887fb7aa9
	29262 fix_rpc_loadtxoutset_race-26			7a329e4716a
	# Triage part of: 29275 maflcko/2401-prev-it-
	# Needs review: g786  -  # FIX:When opening or autoloading wallets there should be clear messages about rescanning in progress and wallets' names.
	g788  qt_peers_sessionid_tooltip_prg788-26	ce11132294a	last=3bf00e13609  # debugwindow: update session ID tooltip
	29302 clarifydoc_rpc_wtx_replace-25			bea205c3046
	29307 AutoFile_error_check-26				fbd4b3103c6	last=661b7d84b54 vasild/AutoFile_error_check
		# NOTE: Held back 55439903212...13f540d60b5 due to crashing CI
	#27.xTODO# Needs review: 29331 -  # redeclare nChainTx to use uint64_t
	29434 fix_rpc_feerate_overflow-26			c4d52ee1912
	# Needs work: g792 -  # Correct tooltip wording for watch-only wallets
	# Needs review? g795 -  # Keep focus on "Hide" while ModalOverlay is visible
	g797  fix_qa_guibug796-25					66fffc1113d
	29480 log_rand_during_init-0.20				36fadc3ace3	last=88468a8afcd
		# Needs careful backport (basically rewritten)
	29493 subtree_update_crc32c-24				59b09fa41a8
	28805 qafix_v2t_pr28805-26					9eaddfae5b3
	# Needs review: 29521 -  # cli: Detect port errors in rpcconnect and rpcport
	g801  fix_qt_clntmdl_at_shutdown_prg801-21	f00d9892c62
	-     rpc_loadtxoutset_hide-26				aa2c7fadfe0
		#27.xTODO# This should probably be removed
	29586 wallet_migrate_null_walletname_bak-26+k	896efa03ef8
	(CHECK-LAST)	last=8a16b8f6a4e wallet_migrate_null_walletname_bak-26
	(CHECK-LAST)	last=6e242420273 wallet_migrate_null_walletname_bak-27
	# Nothing to fix? 29589 -  # tests: fix OP_1NEGATE handling in CScriptOp
	# Nothing to fix: 29615 theStack/202403-test-fix_GetSigOpCount_accurate_counting_bip16
	# Compatibility break, needs review: 29612 fjahr/2024-03-pr26045-reopen
	#26.xTODO# Needs work? 29640 -  # Fix tiebreak when loading blocks from disk (and add tests for comparing chain ties)
	#26.xTODO# Needs review: 29652 ryanofsky/pr/noloc
	# Meh, only test_bitcoin-qt: g803  hebasto-g/240305-appname
	29658 fix_qt_help_on_console_x_newline		fd3a76e8ded
	#26.xTODO# Needs review: 29664 mzumsande/202403_near_tip_stalling
	# Diff-minimise (or not worth it?): 29671 fjahr/2024-03-pr26903-reopen
	29678 fix_init_lowdisk_warning_reqd-25		0ab7aa47bbe	last=847ad93f4dc fix_init_lowdisk_warning_reqd
	# Needs review: 29680 -  # wallet: fix unrelated parent conflict doesn't cause child tx to be marked as conflict
	# Needs work: 29720 maflcko/2403-rpc-int-wrap-
	29726 fix_assumeutxo_reindex_pr29726-26		02fd519df55
	(CHECK-LAST)	last=acf242b0629 fix_assumeutxo_reindex_pr29726-27
	29747 fix_depends_qt_mingw_dbg_link-24		16e26c1e59e
	# Needs review: 29770 fjahr/2024-03-check-undo-index
	# Needs review: 29796 fanquake/depends_0g_debug_flags
	# Needs review: 29798 vasild/logging_cleanup
	-     fix_rpc_warnings_all-21				1786b3c3d4e
	29850 dnsseed_maxips_32-26					1d00999f660	last=f2e3662e57e laanwj/2024-04-dnsseeds-up-to-32
	29853 fix_psbt_sign_insane_pr29853-26		3aa8a37ef81	last=4d8d21320eb darosior/2404_miniscript_crash
		# 26.x backport in #29854
	29855 psbt_nonwit_utxo_chkearly-24			7ffd2428b17	last=9e13ccc50ee achow101/psbt-check-outpoint
	#27.xTODO# 29867 furszy/2024_index_fix_race
	# Not worth it? 29870 maflcko/2404-rpc-SighashFromStr-
	# Needs review/concept: 29877 0xB10C/2024-04-tracing-cast-duration-to-µs
	29892 fix_uv_float_test_pr29892-26			67ec9e25705
		# 27.x rebase in #29888
	# Needs review: 29913 furszy/2024_fix_reconsiderblock_bestheader
	g812  fix_qt_feebump_psbt-25				b087fc70270	last=671b7a32516 furszy-g/2024_gui_fix_create_unsigned_tx_fee_bump
	g813  fix_qt_proxy_port_in_ip-26			fff5939bc49	last=10c5275ba45 willcl-ark-g/2024-03-proxy-validate
	g815  fix_qt_privacy_before_open-25			5310d15a915	last=d3da5025f61
		TODO: switch to simpler fix_qt_privacy_before_open-23 ?
	# Not worth it? 29963 hebasto/240425-guess-cc
	# Needs broader testing: 29984 laanwj/2024-04-iff-loopback
	29985 fix_depends_qt_zlib_t64-26			abd7f86f19b
	# Wait for confirmation: 30007 dnsseed_achow101-25								last=ee218aa9a9e achow101/my-dns-seed
	g819  qt_signmsg_msgs_legacyonly-0.20		a5e0eac8f22	last=fb9f150759b willcl-ark-g/signmessage-error-fix
	# Needs review: 30065 sr-gi/2024-05-fdcount
	#27.xTODO# Needs review: 30079 ismaelsadeeq/05-2023-ignore-transactions-with-parents
	28155 net_addnode_improve_pr28155-26		3862bff8ad4
	30085 fix_cjdns_addnode_detect-26+knots		412c40493d3	last=d0b047494c2 jonatack/2024-05-fix-cjdns-detection-in-GetAddedNodeInfo
	(CHECK-LAST)	last=ac5c3179242 fix_cjdns_addnode_detect-27
	-     fix_cjdns_addnode_detect2-26+knots	282d1ffcfdc	last=be4541abe59 jonatack/2024-05-fix-cjdns-detection-in-AddNode
	(CHECK-LAST)	last=9f05a705fc6 fix_cjdns_addnode_detect2-27
	30094 rf_rpc_move_unival_pr30094-24			62c15473e88	last=b77bad309e9 willcl-ark/move-univalue-only
	30097 theuni/sha2asan
	# Might not apply to <=27.x (which lacks #30095): 30099 hebasto/240514-mingw-tl
	# Needs review: 30132 TheCharlatan/preserveIndexOnRestart
	# Needs review: 30147 -  # contrib: Fixup verify-binaries OS platform parsing
	30151 hebasto/240522-upnp-dl
	# Needs review: 30155 mzumsande/202405_replay_blocks
	# Not worth it? 30169 maflcko/2405-fuzz-stdlib-match-err
	# Needs review & diff-minimising: 30207 mzumsande/202405_invalid_chains
	# Needs review & maybe wallet format finalization: 30221 achow101/wallet-no-chainstateflushed
	
	#26.xTODO# QScrollArea and/or QTreeWidget for GUI Options dialog?
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	#26.xTODO# FIXME: https://twitter.com/tchjntr/status/1788332365887995925
		# weird bitcoin.conf results in:
		#	ASSERT failure in QList<T>::operator[]: "index out of range", file /bitcoin/depends/x86_64-w64-mingw32/include/QtCore/qlist.h, line 575
	#26.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
#@26.x-knots-lts-deps
	29732 depends_qt_update-26					b7d8f6e1c6a
	(CHECK-LAST)	last=38fc092d97e depends_qt_update-27
		TODO: Bump to #30198
	#26.xTODO# FIXME -     depends_qt5kde
	# Needs review & relevance: 28627 fanquake/zeromq_4_3_5
	# Needs review & relevance: 29991 fanquake/sqlite_3_45_3
	Triage: 30217 hebasto/240603-boost
@26.x-knots
# PERFORMANCE:
	n/a   rm_minisketch-26+k					fc085bc6726
		# When removing this, check for fix in #29823
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
	#27.xTODO# Needs review: 26008 achow101/improve-many-desc-ismine
	# Needs #26316 first & review: 26326 andrewtoth/remove-read-lock-in-net
	26375 zmq_optimise_duplread-26+k			3f9e56d77af	last=7b631dc9b19 andrewtoth/no-read-zmq
	(CHECK-LAST)	last=e24dbe6469b zmq_optimise_duplread-27+k
		# Several improvements in Knots branch
	#27.xTODO# Needs review: 26415 andrewtoth/read-raw-block
	# Needs review: 26486 sipa/202211_batchnotfound
	# Opt-in & needs review: 26951 pstratem/2023-01-23-gcsfilter
	# Needs review: 26966 furszy/2022_parallelize_blockfilter_index_2
	# Needs review: 27006 furszy/2022_reduce_cs_main_scope_blockindex_nfile
	# Needs concept/review: 27050 -  # p2p, validation: Don't download witnesses for assumed-valid blocks when running in prune mode
	# Needs review: 27427 -  # validation: Replace MinBIP9WarningHeight with MinBIP9WarningStartTime
	# Needs review? Part of? 28226 martinus:2023-08-more-CBufferedFile
	# Needs review? 28233 andrewtoth/sync-on-periodic
	# Needs review: 28280 andrewtoth/sync-dirty
	-     dbcache_1TB-0.13						781e77f8599
		# Inspired by #28358 Sjors/2023/08/double-your-coins---cache (needs work)
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 -										c387269d617	last=42b25bbd939  # opti_merkle_mutation-0.17
	28592 txrelayrate_14txps-26					ef7b0d1547e last=22c2b52c122
		#26.xTODO# Make configurable? Or is that even sane?
	# Needs fixing rebase: 28799 wallet_cache_descriptor_id-25
	# Diff-minimise? 28894 furszy/2023_wallet_batch_keypool_creation
	# Needs review: 28923 theStack/202311-add_SignTransaction_benchmark
	# Needs review: 28945 martinus/2023-11-improve-ccoinsviewcache-reallocatecache
	# Needs review: 28955 furszy/2023_index_blockfilter_cache_header
	# Needs review: 28987 furszy/2023_wallet_zaptx
	# MSVC: Needs review: 29036 theuni/msvc_fast_byteswap
	# Needs backport: 29114 -  # util: Faster std::byte (pre)vector (un)serialize
	# Needs review?? 29159 -  # Update net.h bigger TCP socket using larger buffer
	# Too big a diff: 29169 fanquake/libsecp256k1_0_4_1
	# Not worth it (kernel only): 29180 theuni/kernel-sha2-optims
	# Needs more careful review: 29436 addrman_select_networks-26						last=7edb07ca800 brunoerg/2024-02-addrman-select-networks
	# Needs review: 29458 -  # optimization: Speed up TryParseHex by 300%
	# Needs review: 29473 -  # optimization: Speed up Base58 encoding by 400% by 64-bit preliminary byte packing
	# Needs review: 29491 fjahr/2024-02-batch-validation-updated
	# Needs review: 29578 brunoerg/2024-03-addrman-getaddr
	# Needs review: 29602 -  # refactor: Optimize IsSpace function for common non-whitespace characters
	29606 opti_ToLowerUpper_reserve-23			1afdb6562d1
	# Worth doing? Needs review: 29607 -  # refactor: Reduce memory copying operations in bech32 encoding/decoding
	# Revert #29815 ? (ie, use OS provided optimised timingsafe_bcmp)
	30059 dbfilesize_param						b2799bed1a6
	30039 dbfilesize_128						7ff0d1ee4a4	last=3e32d23c9e0
		# Note: Upstream PR uses std::max with LevelDB's current default, in case LevelDB changes theirs to larger
	# Needs review: 30093 -  # refactor: reserve memory allocation for transaction outputs
	30115 theuni/easy-univalue-moves
	# Too much churn: 30120 fanquake/secp256k1_0_5_0
# SOFTFORK:
	# TODO: 21702 CheckTemplateVerify
	# TODO: 28550 jamesob/2023-09-covtools-softfork
	# TODO: 29050 stevenroose/txhash
	# TODO: 29198 reardencode/lnhance
	# TODO: 29221 -  # Implement 64 bit arithmetic op codes in the Script interpreter
	# TODO: 29247 -  # Reenable OP_CAT
	# TODO: 29269 -  # Add OP_INTERNALKEY for Tapscript
	# TODO: 29270 -  # Implement OP_CHECKSIGFROMSTACK(VERIFY)
	# TODO: 29280 -  # Implement OP_CHECKTEMPLATEVERIFY
	# TODO? 30018 -  # Implement BIP 118 validation (SIGHASH_ANYPREVOUT)
# FUNCTIONALITY:
	# Broken: 24448 guix_linux_i686_compat				e8a7da94969	last=c76ac9d57f2 guix_linux_i686
		# test2: export of symbol _IO_stdin_used not allowed!
		# test2: libutil.so.1 is not in ALLOWED_LIBRARIES!
		#'test2: failed EXPORTED_SYMBOLS LIBRARY_DEPENDENCIES
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
	# Needs fixing/review: 17303 maflcko:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					b928d07b7ef	last=47b2ba29df2 !origin-pull/12911/head
		# Dropped rel notes file
		# NOTE: Originally #12911
		#26.xTODO# FIXME: "feerate" fails to account for sigops (see 21d85b5c0e)
	# Needs review and care (new index): 13014 jonasschnelli/2018/04/txindex_prune
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs review: 15093 rpc: Change importwallet to return additional errors
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
	15836 fee_histogram+pr15836_api				3944a11b9e9	last=b94292a7cb jonasschnelli/2019/04/feeinfo
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
	22693 getaddressinfo_txids-26				3a151159938	last=a00bc6f395e getaddressinfo_txids
	g562  wallet_warn_reuse_gui-26				2d5e9c6f17f	last=25ea55c25d7 wallet_warn_reuse_gui
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				b26e348fb16	last=ff459b5b55f neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		63659cd720e
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-26+knots		0364f7ce259	last=409c2e34522 elichai/2020-01-siphash
	(CHECK-LAST)	last=5622dd16ecf siphash_optimise_pr18014-26
	(CHECK-LAST)	last=21a3dd41987 siphash_optimise_pr18014-27+knots
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonasschnelli/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr-26				9d46cdf4b67	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
	(CHECK-LAST)	last=ce9524f0b5d rpc_dumptxoutset_hr
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								ddb2be3c698
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							615e6dbd8f8
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure-26						f149e4f77de	last=1a01c955860 mempressure
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			a634aad9ab2	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-26+knots				dcdc29186ec	last=1002e2d0d7f jonatack/setfeerate
	(CHECK-LAST)	last=09c51e7f7df rpc_setfeerate-27+knots
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
		# TODO? Reduce internal changes and move to Knots compat??
	20407 rpcauthfile-26+knots					9b3dd8bc333	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						758975b749a	last=cf940f0e5f5
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					7e754e1e24a	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							7d229a8501e
	g363  qt_peers_directionarrow-25+knots		181c62838e0	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						d5056ae86dd	last=1af20831806 Sjors/2021/05/hww-toggle
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise-25					74cb4fa735a	last=8fd77528194 getblock_optimise
		# Context: 17529 rpc: Faster getblock using PureBlock
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 rpcwallet_tx_in_mempool-26+knots		05c7e969f16	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats-24					4bda86eb3c8	last=15680a2e73d gui_backup_formats
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						166db54c9a5	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex-26						067c89d9d1f	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
	(CHECK-LAST)	last=43c9a1772e2 autoreindex
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	22159 conf_append_cxxflags-23				4d5c0ba83ca	last=fa14c6818f4
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt-25				9e2dca9d051	last=fdf80937d1c hebasto-g/210501-stripes
	(CHECK-LAST)	last=9166bb76d5c gui_peers_rowcolouropt
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
		# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							5ce6b865aab
	24963 rpc_walletprocesspsbt_options-26		0a55cc0e87d	last=f43f992b731 rpc_walletprocesspsbt_options
		# Diff-minimised (and uses merge for rpcarg_type_per_name)
	-     rpc_descriptorprocesspsbt_opts-26+k	0a98dc634fe
	(CHECK-LAST)	last=615033cfb8a rpc_descriptorprocesspsbt_opts-27.1+k
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
	23362 importfromcoldcard					141debe29d5	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates					80e5a8d6375	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06 (FlushFeeEstimates lock on m_cs_fee_estimator)
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			5c25677ff9f	last=ad431ff5d18
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip					4b29a07c003	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	g497  qt_fontsel-25+knots					08c27287393	last=a17fd33edd1 qt_fontsel
	g820  qt_fontsel_qrcodes-25+knots			48513e20fb6	last=b14c9d0572e qt_fontsel_qrcodes
	(CHECK-LAST)	last=2393def608d qt_fontsel_qrcodes-27+knots
	# TODO: qt_fontsel_console
	# Needs work? g505  -  # RPCConsole: add hidePeersDetail() button and functionality
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	#27.xTODO?# Needs review & BIP changes: 24058 kallewoof/202201-bip322
		# TODO: Revert gui#819
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-26			2a50c10a940	last=97a69e232be
		# +RPC doc fix
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
	# Needs concept ack: g553 w0xlt-5/change_error_background
		# CAUTION: requires theming changes for gui#537
	# Needs work & complex test rebasing: 24539   # Add a "tx output spender" index
		# Partial rebase w/ stash at a1237c9a1851a8fc431467a0861c1d37b61566af
		# NOTE: When rebasing (now that #21726 is merged), need to restore AllowPrune func ?
	# Not worth it? 24615/24569/24556 guix on non-x86
	# Needs review: 24824 -  # net: create IP to ASN database from file - makeseeds.py
	# TODO? BIP 179 (tho... Lightning) - upstream first to get translations?
	# Needs work: 24897 w0xlt/silent_payment_021
	# Needs work: 24950 -  # Add config option to set max debug log size
	# Needs work: 24952 -  # rpc: Add sqlite format option for dumptxoutset
	# Concept NACK? 25026 -  # rpc: Make pruneblockchain fetch old blocks if height is lower than pruned height
	# Needs triage & review: 25038 glozow/package-rbf
	#26.xTODO# Needs careful review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku ???
	25183 rpc_fundraw_segwitonly-26				3ad552d43e5	last=9e7fd5c0fe3
	(CHECK-LAST)	last=90bbbbfd48c rpc_fundraw_segwitonly
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
	g626 qt_node_localaddrs-25					9f3f724f687	last=c47f01bf25e
	(CHECK-LAST)	last=c47f01bf25e qt_node_localaddrs-26
		# NOTE: qt_node_localaddrs-26 didn't exist when Knots 26.x forked off
	# Needs completion & review: 25718 fjahr/2022-07-allowinbound
	# Needs concept/review: 25747 w0xlt/desc_file
	# Needs work: 25776 1440000bytes/bumpfee-inputs
	# Needs concept/review: 25907 achow101/upgrade-to-tr-2
	# Needs work: 25923 jonatack/2022-08-statestats
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	# Needs review (or leave external?): 26052 -  # contrib: Add script to colorize logs
	-     guix_shell_compat-24					47f28109275
		# More compatible alternative to #26077 fanquake/guix_shell_over_environment
	28167 rpccookieperms-26+knots				12bd173e987	last=740f3438595 willcl-ark/2023-07-rpccookie-perms
	(CHECK-LAST)	last=??? rpccookieperms-27+knots
		# Was #26088 (not in a Knots release)
		# Added lots of improvements
		#27.xTODO# Update ce9df2aba3e...740f3438595
	# Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	#26.xTODO# Minimised: 26162 Sjors/2022/09/taproot
	#26.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	#26.xTODO# Needs review: 26174 w0xlt/list_address_book
	27114 whitelist_outgoing-mini-26+knots		bbf9ae1c2d8	last=0a533613fb4
		# NOTE: Originally #10594, then #17167
		# Left off test framework refactoring commit (08c1af96e6f) and reverted gArgs caching refactor (ab6c001ec96)
		# Non-trivial revert of 5883a8911a5 net: store `-whitelist{force}relay` values in `CConnman`
		# Also includes change of default from incoming to in+out
		# Made 'out' apply to non-manual outgoing too (backward compat)
		# Restored older functional test (not sure why PR removed it)
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme	06833764dc9	last=d8434da3c14
	# Needs option/work: 26454 petertodd/2022-feebump-without-optin
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 brunoerg/2022-11-disconnectnode-subnet^	24230aadd5e	last=23f4c2cb452
	(CHECK-LAST)	last=23f4c2cb452 rpc_disconnectnode_subnet
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs review: 26839 -  # Add support for RNDR/RNDRRS for AArch64 on Linux
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	26990 bcli_validation-24					307b4498f70	last=cf7dd3564a3
		# Didn't bother rebasing for 755320f75f2...cf7dd3564a3 trivial changes
	27034 rpc_importaddr_for_descwallet-26+k	7b19a88fb58	last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
	(CHECK-LAST)	last=f72496a06a9 rpc_importaddr_for_descwallet-27+k
		# Diff-minimised & tweaked to avoid breaking #23362
	# Needs review: 27052 LarryRuane/2023-02-getpeerinfo (maybe GUI port too?)
	# Needs review & API breakage considerations: 27101 pinheadmz/jsonrpc-2.0
	27216 rpc_getaddressinfo_isactive-26.2		d66317dddf5	last=85f83339dda pinheadmz/used-addr-ui
	(CHECK-LAST)	last=bb8a78beced rpc_getaddressinfo_isactive
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-26+knots						743b27d90b1	last=91771366a3d apoelstra/2023-03--codex32
	(CHECK-LAST)	last=34b60740abb codex32-27+knots
		# Diff-minimised, doc bug fixed & tweaked to avoid breaking #23362
	# Needs review: 27375 pinheadmz/tor-unix-domain-socket
		#+29649
	# Needs review? 27679 pinheadmz/zmq-unix-domain-socket
		# Duplicates #28020 with a different URI format
	# Needs work: 27409 ryanofsky/pr/1data
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	27600 p2p_forceinbound-26+knots				5aae9988b8c	last=8c2026848da pinheadmz/whitebind-evict
	(CHECK-LAST)	last=c1a90cda6fa p2p_forceinbound-27+knots
		# Reverted forceinbound limit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27770 rpc_getblockfileinfo-26+knots			71e21759302	last=5090771f326 furszy/2023_rpc_getblockfileinfo
	#27.xTODO# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
	# Needs review & BIP finality & might have wallet changes: 28202 josibake/implement-bip352-receiving
		# Note alternative (approach NACK'd) in #28453
	# Needs review & BIP finality: 27827 josibake/silent-payments-base-pr-slim-down
	# Needs review & concept: 28241 Sjors/2023/08/silent-index
	# Needs work & maybe removing an anti-feature?: 27836 furszy/2023_rpc_fetchblock_improvements
	# Needs review: 27837 furszy/2023_introduce_block_request_tracker
	# Needs work: 27854 -  # [WIP] add a stratum v2 template provider
		# OR #28983 OR #29432
	# Needs review & compat checking: 27859 -  # Mempool: persist mempoolminfee accross restarts
	# Needs review: Ensure fully optional (opt-in?): 27877 -  # wallet: Add CoinGrinder coin selection algorithm
	#27.xTODO# Make disabled by default: 28052 maflcko/2306-fs_stuff-
	# Needs review? 28207 maflcko/2308-xor-memepool-
	# Needs review: g753 -  # Add new "address type" column to the "receiving tab" address book page
	# Needs review: 28461 fanquake/windows_ssp_roundup
	# Needs review and concept: 28463 mzumsande/202308_increase_block_relay
		# Why not just increase inbound capacity to max anyway?
	# Needs concept/review? 28806 ajtowns/202311-depinfo-scriptflags
	# Needs work: g777 -  # gui: getrawtransaction implementation
	28885 rpc_getpriotxs_modfee-26				3381e6e5f92
	# Needs concept/review: 28926 willcl-ark/2023-07-getnetmsgstats
		# Was #27534 -  # rpc: add 'getnetmsgstats', new rpc to view network message statistics
	# Needs concept/review: 28930 -  # wallet: Add scan_utxo option to getbalances RPC
	#27.xTODO# 28950 instagibbs/2023-11-submitpackage-max-fee-burn
		# +#29722 ?
		# +#29735
	# Needs review and/or optionality: 28977 murchandamus/2023-11-gutter-guard-selector
	29016 rpc_listmempooltxs-26+knots			4a5e8fb0a40	last=07008477b81 niftynei/nifty/listmempoolentry
		# Includes typo fixup in comment that annoys linter
	# Needs review? 29054 achow101/descriptor-sethdseed
	29058 v2t_manual_netinfo_pr29058-26			d9acca60d04
	(CHECK-LAST)	last=072dd93ccb7 fix_netinfo_v2t_safety-27
		# +#29212+#29657 bugfixes
	29117 wallettool_dump_just_db-26+knots		f40437da913	last=d83bea42d1f achow101/dump-without-making-wallet
		# Omitted first commit that could be dangerous
	#26.xTODO# Needs concept + review: 29129 brunoerg/2023-12-externalsigner-account-parameter
	# Needs review or minimal impact: 29130 achow101/createwalletdescriptor-without-new-records
	# Needs review or minimal impact: 29136 achow101/sethdseed-void-descriptor
	# Needs final interface: 29163 rpc_help_detail-22								last=c6b68c29707 LarryRuane/2024-01-help-detailed
	# or (newer): 29163 rpc_helpdetail-24									last=56830469303 LarryRuane/2024-01-help-detailed
		# Left off top commit changing rpc_help test behaviour
	29239 rpc_addnode_v2t_default-26			7df32c3009e
	# Needs concept & review: 29278 -  # RPC: Wallet: Add maxfeerate and maxburnamount startup option
	29347 net_v2t_default-26					0c6dcd7f813
		# +Rewrote doc update in #29452
	# Needs work: 29396 -  # rpc: getdescriptorinfo also returns normalized descriptor
	# Needs review: 29415 vasild/private_broadcast
	# Buggy & maybe waste of RAM? Needs review?? 29418 vasild/getnetmsgstats
	# Needs concept & work: 29468 -  # rpc: method removeprunedfunds should take an array of txids
	# Needs review: 29519 mzumsande/202202_fix_assumeutxo_block_download
	29530 rpc_getpeerinfo_misbehaving_score-26	710942fd596
	# Needs work: 29553 fjahr/2024-03-dumptxoutset-height
	29585 manpage_see_also-23+knots				75af99797c4	last=7c3ac598dd9 fanquake/list_other_pages_in_man
		# Added fix so manpages don't "see also" themselves (diff-minimised from what posted to the PR)
	# Needs review & wallet compat check: 29675 achow101/musig2
	29686 manpage_desc-26+knots					68c1d8fc43e	last=b680c1c6ffd willcl-ark/manpage-desc
	(CHECK-LAST)	last=65283ac6f4c manpage_desc-27+knots
	29687 bcli_err_noconn_helphint-0.17			6dbf5463fe4	last=69d6fd676e9 willcl-ark/improve-cli-error
	29695 gcc_branch_protection_default-26		d221bb9c051	last=7850c5fe20a fanquake/gcc_12_branch_protection_default
	# API change: 29845 stickies-v/2024-04/make-warnings-arr
		# When merged upstream, adapt deprecaterpc to behave like fix_rpc_warnings_all-21
	# TODO: Configurable 29873 glozow/2024-04-truc-25k
	#26.xTODO# 29954 kristapsk/getmempoolinfo-permitbaremultisig-maxdatacarriersize
		# Extend to other options?
		# TODO: Fix datacarriersize description
		# TODO:  b02aab950af RPC/Mempool: getmempoolinfo: Return many more mempool options
		# Concept fixup: new RPC method entirely since they don't change often?
	# TODO: 29959 laanwj/2024-04-qtsowrap-wayland (needs also #29923)
	#27.xTODO# Needs review and split from NAT-PMP removal? 30043 laanwj/2024-05-pcp
	30062 rpc_getrawaddrman_asmap-26			30fdc9e99c3	last=f80c47c3e83 brunoerg/2024-04-asmap-getrawaddrman
		TODO: +#30183 iff API change is adopted (triage) - IF NOT, COPY BRANCH AND ROLL BACK
		#27.xTODO# Try backporting tests
	# Needs review: 30080 -  # wallet: add coin selection parameter add_excess_to_recipient_position for changeless txs with excess that would be added to fees
	
	# TODO: GUI block template view
	# TODO: Build next-block template from mempool + N MB txs (to replace empty blocks for local miner)
	# TODO: Extend IsUnspendable safely
		# eg based on https://github.com/bitcoin/bitcoin/pull/29981
	# TODO: IPv6 Pinholing (see #30005)
# Non-progress functionality:
	8751  sort-multisigs-26+knots				251ac55512c	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					f04bc704bb1	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152  sweepprivkeys-26+knots				fd4a7fa1c62	last=c3c1e3c06dc sweepprivkeys
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245  ionice-26								2b7034b45fd	last=07805b9e990 ionice
	-     ionice_win-26							e48b550c13c	last=8f397d99cd2 ionice_win
	8501  old_stats_rpc-26						83fd945defe	last=7af0ea43b2
	(CHECK-LAST)	last=5560cd011b4 old_stats_rpc-27
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-26+knots					7ce97c35256	last=63fb11652f
	(CHECK-LAST)	last=9434da024e5 old_stats_qt-27+knots
		# Held back on old version due to conflict with RPC updates...
	9504  rpc_dumpmasterprivkey					c50695dd61e	last=07fc81109a
	g444  gui_netwatch-26+knots					3741a7820a6	last=5ac68573293 gui_netwatch-27+knots
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-26+knots				e4ba0cf9c2d	last=c0c7858202f multiwallet_rpc-27+knots
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet to wallet-restricted users for now
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
	10554 zmq_wtx-26+knots						9043c2cae9f	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	(CHECK-LAST)	last=b3840fc028e zmq_wtx-27+knots
		# Extended doc/zmq a bit to match additions from #14060 and #23471
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype-26+knots			6fea3acaa1e	last=9eba1eca8f3 rpc_onetry_conntype
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment-26.1+knots	5727ad7157d	last=177bffa5e78 relax_invblk_punishment
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
		# TODO: Consider rebasing on #29575 ?
	10350 filtered_witblock-25				d0e319ed92a	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
	(CHECK-LAST)	last=316844ce83f filtered_witblock-27
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				d2030802785	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-26							3c32d6d5697	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	(CHECK-LAST)	last=b071344ac04 rest_fee
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			50f53bb1845
	12965 scriptthreads-26+knots				f34fef58afc	last=dfab6c6866 jonasschnelli/2018/04/svt
	(CHECK-LAST)	last=dfab6c6866 scriptthreads
		TODO: Rewrote for 27.x, check if needed to fix anything
	13203 dsha256_power8-25						4fb23e68f6e	last=3b402e0738 TheBlueMatt/2018-05-asm
	(CHECK-LAST)	last=5fa767af29c dsha256_power8-27
		# NOTE: Stripped out benchmark change
		#27.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	-     dsha256_power8_asm_pragmas-25			6938e1bc6b4
	(CHECK-LAST)	last=f368bdee5d8 dsha256_power8_asm_pragmas-27
	15218 postibd_flush-26						b8a38fcf7b8	last=011d9b70f37
	(CHECK-LAST)	last=58823fcbb21 postibd_flush-27
	15428 tor_gui_pairing-26+knots				9718528c5fd	last=76ca37ea493 tor_gui_pairing-27+knots
	(CHECK-LAST)	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-26+knots				c875f9d58c9	last=83610be4be0 tor_subprocess-27+knots
		# FIXME: fix automatic tor outbound using subprocess
		# FIXME: -netinfo doesn't show tor if inbound-only?
		#28.xTODO# Revert #29844 if still using boost::process?
	# TODO: tor guix bundle!
	# TODO: 16490 maflcko/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d-26+knots			03b3b3ef08f
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					ee1a4df08e2
	n/a   rpc_compat_error_index-25+knots		7b910f7f39b
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos-26+knots			b6c9779c2c2 last=539beeaae85 gui_bech32_errpos
	17636 guisettings-0.21						db11c49ec9f	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					9612ad2e42c	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0-26						013703ac225	last=5561e7a0c79
	(CHECK-LAST)	last=b85232d7462 blockfilter_v0
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances				c90a3ed14dc	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-26		17c873148c5	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=614133144a1 cli_getinfo_mw_total_balance-27+knots
	19117 rpc_getrpcwhitelist					3794f1f3c40
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-26+knots		60aaf990499	last=e4b49e22da5 getrpcwhitelist_wallets-27+knots
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-26+knots		c0ffbef6715	last= wallettool_dump_warning-27+knots
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	#26.xTODO# Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
	# Needs concept & review: 29523 -  # Wallet: Add max_tx_weight to transaction funding options (take 2)
		# WAS (never in Knots): #29264 instagibbs/2024-01-max-tx-weight
	# TODO: Guix: When glibc 2.36+ is required, use -Wl,-z,pack-relative-relocs
# Non-upstreamed functionality:
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	n/a   restore_feefilter_opt-26				8e42311a7b0	last=e981b95fb61 restore_feefilter_opt
	-     gui_payreq_textedit					20bbcf27d67
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash-25			b839336b5da	last=2f7b38db868 rpc_mempoolentry_txhash
	-     walletnotify_w_win-26+knots			24f3d207098	last=2bad09b2fe3 walletnotify_w_win-27+knots
	14137 win_taskbar_progress-26+knots		1f4925cf5fc	last=18eb4dbb8a
	(CHECK-LAST)	last=c64a26ef482 win_taskbar_progress-27.1+knots
		# NOTE: Could drop /official_releases/archive/ change, but keeping it ensures a conflict when the version gets bumped, so we can update the sha256 hash
	-     restore_blockmaxsize-25				d112238fc73	last=3029c19637c restore_blockmaxsize
		#27.xTODO# FIXME: 5f3f3c321ed fixup! Restore blockmaxsize option, allowing to limit mined blocks by byte size
	7107  qtnetworkport-26+knots				e4744fb01d5	last=1f37c87d8f2 origin-pull/7107/head
	(CHECK-LAST)	last=07e7cb053d4 qtnetworkport-27+knots
	7533  sendraw_force-26+knots				041cf8be982 last=2627c0937f8 sendraw_force
	(CHECK-LAST)	last=324fa4666b9 sendraw_force-27+knots
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532,#29060 if merged
	11082 rwconf-26+knots						7293f1dff4a	last=7c812c86d4b rwconf-27+knots
		#27.xTODO# Squash fixes
		#27.xTODO# Deprecate with settings.json better?
	7510  rwconf_gui-26+knots					447a68a21e5	last=68eb671c662 rwconf_gui-27+knots
	559   accept_nonstdtxn						4e6a8cfa5c7
		#28.xTODO# Revert or redefine #29843 if it got merged
		#27.xTODO# FIXME: Also bypasses other policies
	 929 tbc									a39febb8c2c
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
	 553 bugfix_qt_uri_amount_parser			4d55210514d
	-     mining_priority-26+knots				51b430ca389 last=78eb474c565 mining_priority
		#26.xTODO# FIXME: Lots of lock warnings from clang! (did I already fix these?)
		#26.xTODO# FIXME: Should blockmintxfee apply to blockprioritysize??
	5861 gui_restore_addresses					b6ea305b748
	5891  qt_console_history_persist			7170d2ce47a	last=0cd5fc301d6 qt_console_history_persist
	7219  rbf_opts-26+knots						3bd712cb918	# Latest code now
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2-26.1+knots			700efc65b56	last=79bdfebe3f9 opt_wallet_segwit2
		# TODO: Split out legacy address preference to be more explicit
		#27.xTODO# Revert gui#808 ??
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			d101fcd2f89	# Latest code now
	-     gui_request_payment_label-0.19		0cd9344a14d
	-     gui_peers_sort_network-23				a01e91a1ad6
	-     gui_peers_no_net_column				266bf97a8ae
	22439 guix_in_gitian-23+knots				0c0bb3497f7	last=ebda0463748 achow101/guix-in-gitian
	-     rpc_getblockfrompeer_future			4d0cff581a0
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		bdf99a3fa84
		# Prior Knots bundled this in with #20295
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
	#26.xTODO# Needs concept acceptance & testing: -     gbt_rpc_options-26.1+knots
	#27.xTODO# Needs concept & writing: default UPnP/NAT-PMP to enabled
		# NOTE: Need to revert #28874 conditionals
	#26.xTODO# Look into making the patches tarball in guix
	#27.xTODO# Restore libbitcoinconsensus? #29189 #29748 #29787 #29797
	# TODO: bump dbcache to 1 TB on systems we can detect memory pressure! - after testing
# Non-upstreamed policy options (default off):
	#27.xTODO# Try using #29086 to rebase policy options up here?
# Non-upstreamed Knots compatibility:
	#28.xTODO# Check on #29942 removal of -datacarrier, possibly revert?
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-26			6549c6a9292
		# Effectively reverts #24505, #27869, #28597, and gui#764
		#27.xTODO# revert #28710  Remove the legacy wallet and BDB dependency
	14641 fundraw_min_conf_deprecated-25+knots	1e16c81aeb5	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			d2e7d59122e
	-     netperms_implicit_addr				2444ff67460
	# IMPOSSIBLE with v2transport param: 12674 rpc_onetry_nonpriv-25+knots			ecaf5bf309f
	-     rpc_getblockfrompeer_nodeid_compat	fdf41f50814
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-25+k		8675ab9e396
		#27.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	29309 permitbarepubkey-26+knots				95798904ec8	last=1dfe27e49ab
	(CHECK-LAST)	last=62533f58876 permitbarepubkey-27+knots
	-    1day_default_conftarget				f5f988a0566
	-     bytespersigopstrict-26+knots			ff70ccc811f	last=fe69581700c bytespersigopstrict-27+knots
	9749  unique_spk_mempool-26+knots			5cbe31047e3	last=82a6f7effbd unique_spk_mempool-27+knots
	-     dustdynamic-26+knots					9036dec2fb9	last=31e0c3b480b dustdynamic-27+knots
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	28408 match_more_datacarrier-26+knots		c33339e615d	last=4d2ec0671a3 match_more_datacarrier
	(CHECK-LAST)	last=562e347b8b7 match_more_datacarrier-27+knots
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
		# Revise byte counting to consider input/output waste
	#26.xTODO# Filter for output value < tx fee * N - https://twitter.com/DoctorBuzz1/status/1741622696327205176
	#26.xTODO# Impose accurately-calculated (not just guessing witness size) dust limit on Taproot _spends_ (only Taproot because there should be a more sensible spend path available in theory)
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     datacarriercost-26+knots				b22014a90b2	last=8265420c727 datacarriercost-27+knots
		#26.xTODO# Add tests and make sure boundaries are correct
	-     acceptnonstddatacarrier-26.1+knots	8bcd075a027	last=8c9287e2fae acceptnonstddatacarrier-27+knots
	-     rejecttokens-26.1+knots				e1c2f4d1456	last=22b3ccf986f rejecttokens-27+knots
		# Currently filters just Runes
	k78   rejectparasites-26.1+knots			1c1fcdba83a	last=d978324923a
	(CHECK-LAST)	last=7761f15b69c rejectparasites-27+knots
		# Currently filters just CAT-21
		# GUI component & default-on moved into rwconf_policy below
		# Rewrote unit test to be more comprehensive
	#27.xTODO# NO APPARENT USAGE: filter HG: https://pbs.twimg.com/media/GDV-H8UWkAAsckl?format=jpg&name=large
	#27.xTODO# CBRC-20 https://twitter.com/bitoordileone/status/1734654996539457666 - INSCRIPTION-WRAPPED: https://mempool.space/tx/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9
	#26.xTODO# All-ASCII data storage (inefficient)
	#27.xTODO# If any input is dust, limit output count to < input count? (or lower?)
	# TODO: Stacks (OP_RETURN X2... - most are 80 bytes long, some 55, few 19)
	#27.xTODO# Discount privacy txs?
	#27.xTODO# Procedural approve/deny/discount/penalize policy scripting?
	# Needs concept ACK: 29843 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	-     bloom_default-26+knots				eb63b3e2582	last=d354ea94d62 bloom_default-27
	-     wallet_avoid_newerchange				ba356b861f7
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	-     maxscriptsize-26+knots				0f59d45cfc0	last=a5458fb4abd maxscriptsize-27+knots
		# Alternate to(?) #29769
	#26.xTODO# Needs concept & impl: Policy: limit script sigops to N (default to MAX_OPS_PER_SCRIPT which is consensus pre-taproot)
	#26.xTODO# Needs concept & impl: Policy: limit any witness stack items to N elements (like MAX_STANDARD_P2WSH_STACK_ITEMS)
	#27.xTODO# Ordislow??
	#26.xTODO# Spam filter for stuff like https://mempool.space/tx/4ec38548aa67f6a2efbbc3cf34ab49dc5c275d9701ab0b58696baee9f555c45a
	#26.xTODO# Whitelisting model for non-SPK scripts
	#26.xTODO# -blockpreference=smaller|larger,lessdata|moredata (or match our own policies?)
	-     enforce_checkpoints					ea5691f019e
	n/a   checkpoint_update-26					29127ba4642	#26.xTODO# last=70996dfdd9b checkpoint_update-0.21
		#26.xTODO# Add new checkpoint
		#27.xTODO# Revert #25725 (Remove mainnet checkpoints)
		TODO: Update from checkpoint_update-27
	10282 timebomb_knots-26.1					345024a23c6	last=e482c8caa0d timebomb_knots
	-     rwconf_policy-26+knots				8d509aa8ca8	last=d767735e0b0 rwconf_policy-27+knots
		# Includes Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: Get GUI settings for dustdynamic to select ratio box & focus text area when you click their labels
		#TODO: squash fixups
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
	# Needs review/options: 26348 -  # Make P2SH redeem script "IF .. PUSH <x> ELSE ... PUSH <y> ENDIF CHECKMULTISIG .. " standard
	# Needs refactoring to only happen for -acceptnonstdtxn(?): 26398 instagibbs/relax_too_small_tx_equality
	# Needs review/concept: 29001 instagibbs/2023-12-ephemeral-anchors
		# Problematic: 26403 instagibbs/ephemeral-anchors
	# Needs review & optionality: 26451 sdaftuar/2022-11-fixrbf
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)
	n/a   macos_dmg-26.1						b05c5f8afad
		# Reverts #28432, and includes fix_dmg_openfinder
		#27.xTODO# revert macos ZIP only: #28932 #28973 #29733
		# NOTE: temporarily reintroduces .tiff file
		# TODO: Investigate if we can compress again by reverting #24031 using patches in https://bugzilla.mozilla.org/show_bug.cgi?id=935237
	7483  svg_icon-26.1+knots					b695e9923cb
		# Consider: https://github.com/bitcoinknots/bitcoin/pull/54
		FIXME: https://github.com/bitcoinknots/bitcoin/issues/79
	n/a   tbc_font-26.1+knots					14adc77e64f
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/
# BRANDING:
	n/a   knots_branding-26.1					0136d7571df
		#26.xTODO# Review security policy
	n/a   copyright_2024-26						af40b27af69
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#26.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#26.xTODO# Check macOS zip impact on tuffy font etc
#	FIXME: macOS can't even run builds?!
# TODO: Check that we aren't deprecating anything in Core
# TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Check #26039 doesn't break anything
# TODO: Ensure std::filesystem isn't introduced (see #28076)
#27.xTODO# Ensure options arguments use new OBJ_NAMED_PARAMS type: git grep '"options.*OBJ,'
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
#27.xTODO# git grep noban_tx_relay (needs #27114)
	n/a  (cherrypick=4de10e83babc036d91)		c73f86e10b9	# doc/{bips,files}
	n/a  (bump_version=Knots:20240604)			b6e90958caa
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist		28f53e51930
	n/a   (cherrypick=87fdade84dc)				f56f1ed1cd6  # release notes: write/update, including change log and credits
		FIXME: Don't mention updated translations if they're not actually being updated!
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# When re-added, #28824 notes in 9db5d23d559
		#27.xTODO# Include the deleted notes from 0bc1f4b5c7b
	n/a  (cherrypick=928f49526a6)				cc2146f5590  # update manpages (build first)
		# also example bitcoin.conf
	#26.xTODO# n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: Upload to Transifex with * d9411324066 (ts_20220515, origin-pull-g/599/head) GUI: Support translating Bitcoin units
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @26.x-knots-android

#@26.x-knots-extratests

