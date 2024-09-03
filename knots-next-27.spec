timestamp 2024-09-02 19:23:14
#lastapply no-merge

#.. checked up to PR #30791 / gui #833

checkout v27.1
@27.x-syslibs
# BUILD BUGS:
	5872 subdir_incl_compat						f41289db2b9
	29577 fix_objcxxflags_pr29577-27			990080d6c6b
		# Was #29362 - build: Add missed definition for AM_OBJCXXFLAGS
	-     fix_evhttp_util_nodep-25				23e0821ee70
	30283 upnp_228_compat-22					2d213fc7c89
	30633 fanquake/gcc_15_fixup
		# 27.x backport in #30558
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb-26+knots					97b8727d34e	last=87e5c2dd815 sys_leveldb
	5416  sys_libsecp256k1-27					5bb4fd232d3	last=4684e2971d0 sys_libsecp256k1
	# TODO: sys_crc32c ??
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	#28.xTODO# sys_libminisketch
	13789 bugfix_asm_pragmas					2dc1722f600
	15155 test_external_bcli					37442ac71a2
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
@27.x-knotsfixes
# TESTS:
	-     ci_knots-26							e2099d64846
	-     lint_relaxer-26+knots					6db3eb08b9d
	-     nowarn_unreachable-code				51bbc98f621
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
	# Triage: 29753 furszy/2024_test_fix_p2p_node_network_failure
	# Triage: 29788 maflcko/2404-ci-bcfcc-
	# Triage: 29832 fanquake/revert_29788
	# Triage: 30193 -  # ci: move ASAN job to GitHub Actions from Cirrus CI
	-     ci_i686mp_clang15						955f1eeed99
	#28.xTODO# Triage: Revert #30487 ?
	30519 ci_tsan_pr30519-25					5b8466ae234  # ci: add _LIBCPP_REMOVE_TRANSITIVE_INCLUDES to TSAN (libc++) job
	30552 qafix_msgtx_defarg-0.16				41dc1937283
# FIXES:
	18818 guix_reltar_autogen_distclean			c94474f3235	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again						9776ecce7e8
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					80273d0b65c	last=df5ece3e064 2020mingwthrd
	18490 bugfix_symcheck_pe_case				1831cb0f26a
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 http_bind_error						4a49b781729	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					3194917f143
		# NOTE: libevent-copied code up to date as of 2023-11-22 cfb2b89a1d0642abd6389913e237f49c662502e4
	 9524  rpc_pruneblkchain0					62bc7893de2	last=88883ae13d
	10731 log_more_uacomment-26					dc3babb6e24	last=1852b4b8910 log_more_uacomment
	29614 bufferedfile_fclose					88984d839a5
	14485 fadvise-27+knots						66a302ecfce	last=289e88b3133 fadvise
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					7f56a80d34d
	-     bugfix_rpc_getbalance_hacky-26		e9da9c1ce34	last=d23524372a0 bugfix_rpc_getbalance_hacky
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
	18194 bugfix_gui_edit_sendaddr-mini			6fc457d1891	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data-26			ad13fdc3544	last=3f9cc0cd736 Saibato/wallet_351
	(CHECK-LAST)	last=283cd1f0650 listwalletdir_skip_data
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
	g152  gui_notify_setup_bg					d44bd1d60a6
	-     bugfix_gui_drop_abc_confusing_hack	3aafa6192ad
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	g236  gui_init_walleterror_cont				98b54851815
	-     rpc_addconnection_mainnet				bb10caddb8e
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22417 bpchild_closefds						10578517720
	(CHECK-LAST)	last= subproc_closefds
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
		# NOTE: Currently uses ENABLE_EXTERNAL_SIGNER in place of USE_BOOST_PROCESS (not defined until #15421 merged)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				2721ee51431
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs work: 23502 achow101/tr-low-fee-est
		# "rebase" in #26573 for post-#26567 refactor
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	g506  qt_qrcode_sizefixes					9a8307f04dd
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs review: 24066 whitslack/openrc-daemonwait
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	24313 Sjors/2022/02/displayaddress						last=803387f054d
		TODO: make sure this doesn't break compatibility (and fix review bugs)
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				cccb0d2a3d1
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-25+knots			fc65c373140	last=68a041dd12b
	(CHECK-LAST)	last=35cdcb3309d fix_rpc_docs_pr24718-28+knots
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	# Needs review: 24972 hebasto/220425-no-libtool
	# Needs review: 24994 hebasto/220426-consensus
	g595  qt_handle_autostart_errors-0.15		5c0f60b428f	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	g599  ts_20220515-partial-25				5191aa16ac2	last=d9411324066 ts_20220515
	(CHECK-LAST)	last=6d470565c4c gui_psbt_error_msgbox
		# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
		#28.xTODO# Update with other commits that are beneficial
	-     boost_171_177_workarounds				efb08b49fda
		# NOTE: Originally part of #25111 hww_windows replaced by #25696 (merged)
	-     hww_windows-27						e1f9c1bbde8
		# Reverts #29489 & #28967
	# TODO: 29868 hebasto/231130-replace-bp
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
	# Needs review: 25380 darosior/fee_estimator_disable_cpfp
	# Check on #25561
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	# Needs review: 25698 -  # crypto: avoid potential buffer overread in ChaCha20::SetKey
	g633  -										90464484be3	last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	# Needs review: 25938 mzumsande/202208_fixed_cjdns
	g662  qt_fix_txview_202209					2f61f8d7809
		# Includes gui#368
	# TODO: Needs review: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	# TODO: Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	# TODO: Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	# TODO: Sane fix for #24049
	g677 fix_qt_peers_na						9721684acb5
	# Needs work/review: 26426 fjahr/202210-coinstatsindex-overflow
	# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs review: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-25+knots	c2d076bab68	last=a6f567590b7
	(CHECK-LAST)	last=200d869e952 qt_reqs_multiselect_pr684-28+knots
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	26950 fanquake/check_for_SecureZeroMemory
	27039 fix_reindex_readonly_blkfiles-26		807e5d1abd3
	# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	Maybe? 27307 -  # wallet: track mempool conflicts with wallet transactions
		# CAUTION: Even merged, this appears to possibly show a higher balance than the user actually has for sure??
		# TODO: Include fix/optimisation in #30115 & #30365
	# Alternative to: 27434 pinheadmz/chaintips-invalid
	g722 -  # Wallet : Allow user to navigate options while encrypting at creation
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	# Needs concept/review: 28016 -  # p2p: gives seednode priority over dnsseed if both are provided
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#27.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	-     acceptstalefeeestimates_mainnet_opt-26	bbb9bb4db98	last=a303cde2fd1 acceptstalefeeestimates_mainnet_opt
	# Needs review: 27684 hebasto/230516-punish OR ???
	#27.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 -										950ac4a8bec	last=bfc2bb6a270  # forbid_nohelp-0.19
	27815 -										a4577ff98f0	last=244e6c8db81  # cli_forbid_multihelper-22
	# Needs review: 27820 -  # Sanitizing ports of -rpcconnect and -rpcport.
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	# Needs review: 27912 -  # net: run disconnect in I2P thread
	27969 -  # bumpfee: ignore WALLET_INCREMENTAL_RELAY_FEE when user specifies fee_rate
	# Needs work: 27973 maflcko/2306-byte-span-
	# Needs work: 27991 fanquake/instrument_libsecp
	28020 -										af6f1fc637f	last=0b1762c90d1  # exclude ipc scheme from port check (fix_zmq_ipc_noportcheck-25)
	(CHECK-LAST)	last= zmq_ipc_uri_compat
	-     zmq_unix_uri_compat-25				5046420859c
	-     qt_ambig_uri_refs						aa00950ddee
		# Prior to 27.x, part was included with gui#742 qt_err_fixg741_in_g742-21
	28029 fix_zmq_errhandling_202307-mini		2c40a9537fb	last=07086589b27 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err		dd0993e91b7
	# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Needs concept: 28205 theStack/202308-netprocessing-reallow_fetching_of_genesis_block
	# 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	# Triage #28248
	29946 jsonrpc_content_type-26+mini			d4ad3db85ff	last=f90a84d6150 jsonrpc_content_type
		# Rebased in Core as #30215 (merged unmodified)
	TODO: Part of (wallet compat?) 28307 furszy/2023_invalid_segwit_redeem_script_limit
	28345 fix_bytespersigop_checks-mini-26		f3f4732db4a	last=6f627727739 fix_bytespersigop_checks
		#27.xTODO# NOTE: Excludes removal of buggy wrapper for diff-minimisation; needs checking manually (to ensure wrapper doesn't get used even in final/complete merge of all PRs) when assembly done; known issues: stash 172d7d7a9
	28340 -										d0a6cbda5ed	last=0244416aacb  # security: restrict abis in bitcoind.service
	Needs diff-minimising: 28366 -  # Fix waste calculation in SelectionResult
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	#28.xTODO# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	#28.xTODO# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	28564 fix_conf_fuzzbin_main					2c54011535c
	#28.xTODO# Needs review and relevance: 28616 Sjors/2023/10/assume-unconfirmed
	# Needs review & triage: 28678 sipa/202310_miniscript_assume
	# Needs review: 28724 achow101/cleanup-accidental-watchonly-mkeys
	# Needs review: 28776 BrandonOdiwuor/gui_overview_page_add_used_balance
	# -- Needs review: g775 -  # gui: add used balance to overview page
	# Needs review: 28780 -  # log: torcontrol opt checks
	-     fix_keep_notmy_cookie-27				faa45a4509b	last=50b7a50a61c fix_keep_notmy_cookie
		# Originally part of #28784, but regressed in d95dde9441f...7cb9367157e
	# Needs review: 28824 fix_asm_nodecimals-23								last=fde11cb0fa3 willcl-ark/asm-full-hex
		# FIXME: disambiguate opcodes too?
	28834 -  # net: Attempts to connect to all resolved addresses on addnode
	28874 fanquake/redundant_upnp_ifdef			55b5aa9af32	last=92f88a96290
	28944 rpc_sendall_anti_fee_sniping-27		b2de75c9a45	last=b11d00d54ed ishaanam/sendall_anti_fee_sniping
	# FIXME: rpc_net test fails! 28998 rpc_addpeeraddress_return_error-26
	29141 fix_rpcauth_blank						ea301cd9260
		#27.xTODO# reconcile with #30401
	# Needs review: 29124 achow101/fix-double-keypath
	# Needs work: 29147 guix_attachable_sigs					ad4fe4b83a4
		# GPG discourages clearsign signatures!
		TODO: but windows has lots of problems with existing style...
	# Needs review: 29155 -  # wallet: move lock at the top of ReleaseWallet
	29175 -										732060336d2	last=be8ae64b82e  # rpc: validate fee estimation mode case insensitive (fix_rpc_estmode_unset_case-24)
	# Needs review: g786  -  # FIX:When opening or autoloading wallets there should be clear messages about rescanning in progress and wallets' names.
	g788  -										4ed18b2f9d1	last=3bf00e13609  # debugwindow: update session ID tooltip
	29307 AutoFile_error_check-27				689b2cdc64b	last=4533445fd7d vasild/AutoFile_error_check
	(CHECK-LAST)	last= AutoFile_error_check-28
	# Needs work: g792 -  # Correct tooltip wording for watch-only wallets
	g795  -										c826054e30a	last=992b1bbd5da  # Keep focus on "Hide" while ModalOverlay is visible
	29480 -										63f3808fc0d	last=88468a8afcd  # log_rand_during_init-0.20
		# Needs careful backport (basically rewritten)
	29521 cli_check_portnum-23					01c7b67a794
	-     rpc_loadtxoutset_hide-26				0989753653e
		#28.xTODO# This should probably be removed if assumeutxo is supported on mainnet
	29586 wallet_migrate_null_walletname_bak-27	27b4b43fd7e
	# Nothing to fix? 29589 -  # tests: fix OP_1NEGATE handling in CScriptOp
	# Nothing to fix: 29615 theStack/202403-test-fix_GetSigOpCount_accurate_counting_bip16
	# Compatibility break, needs review: 29612 fjahr/2024-03-pr26045-reopen (relnotes in #30167)
	#27.xTODO# Needs review? 29640 -  # Fix tiebreak when loading blocks from disk (and add tests for comparing chain ties)
	#27.xTODO# Needs review: 29652 ryanofsky/pr/noloc
	# Meh, only test_bitcoin-qt: g803  hebasto-g/240305-appname
	Maybe? 29656 -  # redeclare nChainTx to use uint64_t
	29658 fix_qt_help_on_console_x_newline		5fdad6eb80a
	#27.xTODO# Needs review: 29664 mzumsande/202403_near_tip_stalling
	# Diff-minimise (or not worth it?): 29671 fjahr/2024-03-pr26903-reopen
	29678 fix_init_lowdisk_warning_reqd-25		4b237d549ef	last=c452d6c1efe fix_init_lowdisk_warning_reqd
	# Needs review: 29680 -  # wallet: fix unrelated parent conflict doesn't cause child tx to be marked as conflict
	#28.xTODO# If assumeutxo supported: 29720 maflcko/2403-rpc-int-wrap-
		# +#30544
	29726 fix_assumeutxo_reindex_pr29726-27		76da6fd53e3
	# Needs review: 29770 fjahr/2024-03-check-undo-index
	# Needs review: 29796 fanquake/depends_0g_debug_flags
	Triage: 29798 vasild/logging_cleanup
	-     fix_rpc_warnings_all-21				11d38164bdf	last=e4e4a81317c fix_rpc_warnings_all-28
	29850 dnsseed_maxips_32-26					562386600cb	last=f2e3662e57e laanwj/2024-04-dnsseeds-up-to-32
	29855 psbt_nonwit_utxo_chkearly-24			d7a8d4da4b8	last=9e13ccc50ee achow101/psbt-check-outpoint
	# Needs review/concept: 29877 0xB10C/2024-04-tracing-cast-duration-to-µs
	# Needs review: 29913 furszy/2024_fix_reconsiderblock_bestheader
	g815  fix_qt_privacy_before_open-23			1f4dee95456	last=260d6eb9272
		# Rewrote myself due to overcomplication and race bug in PR
	# Not worth it? 29963 hebasto/240425-guess-cc
	After broader testing: 29984 laanwj/2024-04-iff-loopback
	30007 dnsseed_achow101-25					965c91efaff	last=2721d64989c achow101/my-dns-seed
	g819  qt_signmsg_msgs_legacyonly-0.20		0eb28516de4	last=fb9f150759b willcl-ark-g/signmessage-error-fix
	# Needs review: 30065 sr-gi/2024-05-fdcount
	#27.xTODO# Needs review: 30079 ismaelsadeeq/05-2023-ignore-transactions-with-parents
	-     fix_cjdns_addnode_detect2-27+knots	285a22a37a7	last=be4541abe59 jonatack/2024-05-fix-cjdns-detection-in-AddNode
	# Might not apply to <=27.x (which lacks #30095): 30099 hebasto/240514-mingw-tl (replaced in 28.x with #30137)
	# FIXME Non-trivial: 30132 TheCharlatan/preserveIndexOnRestart
	# Not used for Knots: 30147 -  # contrib: Fixup verify-binaries OS platform parsing
	# Needs review: 30155 mzumsande/202405_replay_blocks
	#28.xTODO# Revert or semi-revert #30157 ?? (Mempool-influenced fee estimation)
	# Not worth it? 30169 maflcko/2405-fuzz-stdlib-match-err
	# Needs review & diff-minimising: 30207 mzumsande/202405_invalid_chains
	# Needs review & maybe wallet format finalization: 30221 achow101/wallet-no-chainstateflushed
	30245 fix_localonly_ipv6_proxy-22			f19b024c162
	# No real impact? 30255 maflcko/2406-logError
	30265 achow101/fix-listwalletdir-migrated-wallets
	# Needs work: g823 -  # wallet: Improve error log color in the console
	# Needs work: g824 achow101-g/gui-migrate-unloaded
	-     detect_clang_bug96267-27+knots		d59654cdd01	last=f032671adf9 detect_clang_bug96267
	# Needs concept (anti-feature?): 30309 furszy/2024_wallet_max_weight
	g826  qt_opts_maximizewindow				b13a6950122
	g827  qt_opts_stretch						664129c84de
	30355 fix_sqlite_trace_loglevel-26			c9685308512	last=46819f5df6d ajtowns/202406-walletlogtrace
	30357 fix_psbt_falsecomplete_pr30357-25		819846f00ba	last=7e36dca657c willcl-ark/walletprocesspsbt-no-finalize
	# Needs review: 30359 -  # Correct Error Code in OP_IF/OP_NOTIF Empty Stack Check
	30394 fix_selfconnect_race_pr30394-26		69186ad2c60
		# NOTE: Non-trivial backport of test taken from #30467
	# Needs review: 30410 mzumsande/202407_getblock_error
	30435 fix_shutdown_order_pr30435-27			b044c421cc8
	30436 fix_txidfromstring_length-27			b2891ee1bf6
		# NOTE: Doesn't include fix for #28970 (not in Knots 27.x)
	30444 rest_negative_chk_pr30444-27			53b0c9d2319
	30457 fix_rpc_getaddressinfo_opt_isscript-25	3f8f4822590
	# Needs review: 30465 hebasto/240716-deps-cmake
	# Needs review: 30469 fjahr/2024-07-csi-overflow-2
	# Needs review: 30479 mzumsande/202407_fix_resetfailure
	g828 fix_qt_menu_walletname_g828-0.19		d5cc2710489
	30482 rest_chk_truncated_txid-27+knots		d4bc5fd8199
		# Just the bugfix from, diff-minimised
	30485 fix_ldb_logging_pr30485-26			e8faae1e910	last=fa18fc70508 maflcko/2407-log-lint
	#28.xTODO# If assumeutxo supported: 30497 maflcko/2407-loadtxoutset-rpc-err
	#28.xTODO# Triage: 30508 hebasto/240723-zmq-pc
	#28.xTODO# If assumeutxo supported: 30516 fjahr/2024-07-au-blockheight-san
	# Needs review: 30529 ryanofsky/pr/listset
	# If needed? 30489 theuni/depends-zmq-patch
	30534 guix_no_bison_macwin-25				bf4f446992f
	g831 pablomartin4btc-g/gui-bringToFront-wayland-workaround
	30577 brunoerg/2024-07-miniscript-tointegral
	30621 furszy/2024_fix_blank_legacy_detection
	Without renames: 30659 furszy/2024_wallet_shutdown
	# Needs review: 30666 mzumsande/202404_invalidblock
	# Needs (concept?) review? 30678 fjahr/2024-08-backup-best
	# Needs work: 30679 tdb3/handle_invalid_rpcbind_port
	# Needs review? 30684 furszy/2024_init_negated_args_err
	Maybe simple rewrite? 30697 ismaelsadeeq/08-2024-prevent-race-condition-in-wallet
	#28.xTODO# Revert 10d56530e097cbf70f7ecbc464550d89b4d91b87 (disables ppc64le)
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	# FIXME: https://twitter.com/tchjntr/status/1788332365887995925
		# weird bitcoin.conf results in:
		#	ASSERT failure in QList<T>::operator[]: "index out of range", file /bitcoin/depends/x86_64-w64-mingw32/include/QtCore/qlist.h, line 575
	#27.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
#@27.x-knots-lts-deps
	Add in: 30774 fanquake/depends_qt_5_15_15
	30198 depends_qt_update-27					e87a47fdad4
		# Left out clang 18 patch (conflict-prone and shouldn't be needed)
		# +#30227
	#27.xTODO# FIXME -     depends_qt5kde
	# Needs review & relevance: 29991 fanquake/sqlite_3_45_3
	29707 dep_miniupnp_227-27					eae72297f88
		# Only the version bump
	# Needs review: 30301 theuni/miniupnp-228-bump
@27.x-knots
# PERFORMANCE:
	n/a   rm_minisketch-26+k					219de7b0860
	(CHECK-LAST)	last=18043c411cc rm_minisketch-28+k
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
	Needs #26316 first??? 26326 andrewtoth/remove-read-lock-in-net
	26415 apis_read_raw_block-27				d2eed7c6adf
		# Includes: 21319 getblock_optimise						74cb4fa735a
			# Context: 17529 rpc: Faster getblock using PureBlock
	# Unclear benefit: 26375 zmq_optimise_duplread-27+k			3f9e56d77af	last=7b631dc9b19 andrewtoth/no-read-zmq
		# Several improvements in Knots branch
		# Post-#26415, it's unclear if this is an improvement or potentially a performance loss: we either readback raw (from OS cache), or serialize CBlock
	# Needs review: 26486 sipa/202211_batchnotfound
	# Opt-in & needs review: 26951 pstratem/2023-01-23-gcsfilter
	# Needs review: 26966 furszy/2022_parallelize_blockfilter_index_2
	# Needs review: 27006 furszy/2022_reduce_cs_main_scope_blockindex_nfile
	# Needs concept/review: 27050 -  # p2p, validation: Don't download witnesses for assumed-valid blocks when running in prune mode
	# Needs review: 27427 -  # validation: Replace MinBIP9WarningHeight with MinBIP9WarningStartTime
	# Needs review? Part of? 28226 martinus:2023-08-more-CBufferedFile
	28233 opti_periodic_keep_cache-26			3e57dc351b4
	28280 andrewtoth/sync-dirty
	-     dbcache_1TB-0.13						9ca5b586969
		# Inspired by #28358 Sjors/2023/08/double-your-coins---cache (needs work)
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 -										a1f61b9ae79	last=42b25bbd939  # opti_merkle_mutation-0.17
	28592 -										b072106d716 last=22c2b52c122  # txrelayrate_14txps-26
		# TODO: Make configurable? Or is that even sane?
	28923 theStack/202311-add_SignTransaction_benchmark
	28955 furszy/2023_index_blockfilter_cache_header
		TODO: +#29867 furszy/2024_index_fix_race
	# MSVC: Needs review: 29036 theuni/msvc_fast_byteswap
	# Needs review?? 29159 -  # Update net.h bigger TCP socket using larger buffer
	# Needs more careful review: 29436 addrman_select_networks-26						last=7edb07ca800 brunoerg/2024-02-addrman-select-networks
	29458 -  # optimization: Speed up TryParseHex by 300%
	# Needs review: 29473 -  # optimization: Speed up Base58 encoding by 400% by 64-bit preliminary byte packing
	# Needs review: 29491 fjahr/2024-02-batch-validation-updated
	# Needs review: 29578 brunoerg/2024-03-addrman-getaddr
	# Needs review: 29602 -  # refactor: Optimize IsSpace function for common non-whitespace characters
	29606 opti_ToLowerUpper_reserve-23			4437c9aa99a
	Worth doing? 29607 -  # refactor: Reduce memory copying operations in bech32 encoding/decoding
	30059 dbfilesize_param						69e46c848f5
	30039 dbfilesize_128						1011fa8e307	last=3e32d23c9e0
		# Note: Upstream PR uses std::max with LevelDB's current default, in case LevelDB changes theirs to larger
	# Needs review: 30093 -  # refactor: reserve memory allocation for transaction outputs
	30115 easy_uv_moves_pr30115-27				e01f1b69f47
	# Too much churn: 30120 fanquake/secp256k1_0_5_0
	30253 opti_psbt_loop_pr30253-23				5d2f6239957
	# Needs review: 30317 -  # WIP Simplify SipHash
	30321 opti_rest_binary_copies-27+knots		037ed2959c4	last=1556d21599a
	30324 opti_getarg_printpriority-26			3a0edacac3a	last=323ce303086
	# Needs review: 30325 -  # optimization: Switch CTxMemPool::CalculateDescendants from set to vector to reduce transaction hash calculations
	#26.xTODO# Needs more careful review: 30326 -  # optimization: Reduce cache lookups in CCoinsViewCache::FetchCoin
	# Needs review: 30370 fjahr/2024-07-pr28945
		# Was (never in Knots) #28945
	# Needs review? 30442 paplorinc/paplorinc/siphash
	# Needs review: 30610 sipa/202408_force_sync
	# Needs review: 30611 andrewtoth/write-chainstate-every-hour
	30675 -  # http: set TCP_NODELAY when creating HTTP server
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
	18479 rpc_sign_show_fees					139fe3b8acb	last=47b2ba29df2 !origin-pull/12911/head
		# Dropped rel notes file
		# NOTE: Originally #12911
		#27.xTODO# FIXME: "feerate" fails to account for sigops (see 21d85b5c0e); most of a fix in stash 835c2d3afba
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
	15836 fee_histogram+pr15836_api-26			db1d17f316e	last=b94292a7cb jonasschnelli/2019/04/feeinfo
	(CHECK-LAST)	last=77d5685620b fee_histogram+pr15836_api
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
	22693 getaddressinfo_txids					db20da926da
	g562  wallet_warn_reuse_gui					c17b63857e2
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini-26			3616fb93a0d	last=a0d0807abc2 neutrino_whitelist
	(CHECK-LAST)	last=d3bcf469ce4 neutrino_whitelist-mini
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		a1d46ed0c5e
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-27+knots		b6a8530963a	last=409c2e34522 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonasschnelli/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr					c9897d1dfb6	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								6ae776378fe
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							23cec9161c9
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							46c62580a75
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			b3ec8ee0eef	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-27+knots				5df7a9c1191	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
		# TODO? Reduce internal changes and move to Knots compat??
	20407 rpcauthfile-26+knots					34d85510b80	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						c665334d232	last=cf940f0e5f5
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					1e3ae5f0e5d	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	g363  qt_peers_directionarrow-25+knots		42527f8ae81	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						fad927ae702	last=1af20831806 Sjors/2021/05/hww-toggle
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21260 rpcwallet_tx_in_mempool-26+knots		fdd855b6169	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					d86d4a6ee61
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						4c31471eb1a	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex							54a46fbc8da	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	22159 conf_append_cxxflags-23				e80311c47e1	last=fa14c6818f4
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt				c437609e0d5	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
		# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							a0e3d0a51f4
	24963 rpc_walletprocesspsbt_options-26		262df2a313e	last=f43f992b731 rpc_walletprocesspsbt_options
		# Diff-minimised (and uses merge for rpcarg_type_per_name)
	-     rpc_descriptorprocesspsbt_opts-27.1+k	e8be2a13403
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	22729 vasild/torbind
		+#30502
	# TODO? 25621 -  # rpc/wallet: Add details and duplicate section for simulaterawtransaction
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Only if Core merges (alternative makes more sense): 22776 kallewoof:202108-getbalances-tx
	# Needs BIP? 22838 achow101:multipath-descs
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs work: g410  benthecarman/uppercase-uri
	# Needs API review: 23330 JeremyRubin/header-fetch
	23362 importfromcoldcard					b1cb4ae6737	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates					df02a63b8c4	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06 (FlushFeeEstimates lock on m_cs_fee_estimator)
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			8a0ed84f1ae	last=ad431ff5d18
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip					a15f3828cf4	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	g820  qt_fontsel_qrcodes-27+knots			0e14f93fd0c	last=b14c9d0572e qt_fontsel_qrcodes
	# TODO: qt_fontsel_console
	g505  -  # RPCConsole: add hidePeersDetail() button and functionality
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	#27.xTODO?# Needs review & BIP changes: 24058 kallewoof/202201-bip322
		# TODO: Revert gui#819
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-26			afdbf00e02c	last=97a69e232be
		# +RPC doc fix
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
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
	#27.xTODO# Needs careful review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku ???
	25183 rpc_fundraw_segwitonly				1d474ea54b7	last=9e7fd5c0fe3
		# Currently just an old version for Knots 23.0 compatibility (held back 1c5cfd84b3d...9e7fd5c0fe3)
		# Fixed tests with inspiration from 9e7fd5c0fe3
		# TODO: update without breaking compatibility? (new code looks buggy tho - needs rewrite?) (also, filtering by "input type" doesn't really make sense, though segwit filtering does)
	# Needs concept: 25261 -  # rpc: fetch multiple headers in getblockheader()
	#27.xTODO# 25269 -  # wallet: re-activate the not triggered "AmountWithFeeExceedsBalance" error
	# Needs concept review: 25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
		# Concept unsure: Hides logline by default; but maybe we want that with more info included?
	# TODO: 25366 w0xlt/desc_rpc
		# Besides the private key issue (removed; conceptual issues), RPC doc also has "addresses" where there would be a single address (in a details Object)
	# Needs work: 25434 w0xlt/bypass-timelocks
		# NOTE: Was #21413 glozow/2021-03-bypass-timelocks (never in Knots)
		# Also #25570 ?
	g626 qt_node_localaddrs-26					c7dd3e84fa8	last=189c987386a
	# Needs completion & review: 25718 fjahr/2022-07-allowinbound
	# Needs concept/review: 25747 w0xlt/desc_file
	# Needs work: 25776 1440000bytes/bumpfee-inputs
	# Needs concept/review: 25907 achow101/upgrade-to-tr-2
	# Needs work: 25923 jonatack/2022-08-statestats
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	# Needs review (or leave external?): 26052 -  # contrib: Add script to colorize logs
	28167 rpccookieperms-27+knots				c7b352f872e	last=73f0a6cbd0b willcl-ark/2023-07-rpccookie-perms
		# Held back most of 9617e42a7b1..73f0a6cbd0b (func renames, refactoring; default to no-change/rely on umask)
		# Was #26088 (not in a Knots release)
		# Removed doc change
		# Added lots of improvements
	# Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	# Minimised: 26162 Sjors/2022/09/taproot
	#27.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	# Needs review: 26174 w0xlt/list_address_book
	27114 whitelist_outgoing-mini-26+knots		2222d5457dd	last=0a533613fb4
		# NOTE: Originally #10594, then #17167
		# Left off test framework refactoring commit (08c1af96e6f) and reverted gArgs caching refactor (ab6c001ec96)
		# Non-trivial revert of 5883a8911a5 net: store `-whitelist{force}relay` values in `CConnman`
		# Also includes change of default from incoming to in+out
		# Made 'out' apply to non-manual outgoing too (backward compat)
		# Restored older functional test (not sure why PR removed it)
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme	58040862840	last=d8434da3c14
	# Needs option/work: 26454 petertodd/2022-feebump-without-optin
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 rpc_disconnectnode_subnet				d9e244085b5	last=23f4c2cb452 brunoerg/2022-11-disconnectnode-subnet
		# Refactored tests (to be more deterministic) and added support for disconnecting a single IP without subnet specified
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	26990 bcli_validation-24					9c3a202713a	last=3d63fc976d6
		# Didn't bother rebasing for 755320f75f2...3d63fc976d6 trivial changes
	27034 rpc_importaddr_for_descwallet-27+k	958c76fa136	last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
		# Diff-minimised & tweaked to avoid breaking #23362
	# Needs review: 27052 LarryRuane/2023-02-getpeerinfo (maybe GUI port too?)
	Needs API breakage considerations: 27101 pinheadmz/jsonrpc-2.0
	27216 rpc_getaddressinfo_isactive			0b57113f4c9	last=85f83339dda pinheadmz/used-addr-ui
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-27+knots						8ab2add6de2	last=91771366a3d apoelstra/2023-03--codex32
		# Diff-minimised, doc bug fixed & tweaked to avoid breaking #23362
	27375 pinheadmz/tor-unix-domain-socket
		+29649
	# 27679 pinheadmz/zmq-unix-domain-socket
		# Duplicates #28020 with a different URI format
	# Needs work: 27409 ryanofsky/pr/1data
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	27600 p2p_forceinbound-27+knots				dbda0e998ab	last=8c2026848da pinheadmz/whitebind-evict
		# Reverted forceinbound limit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27770 rpc_getblockfileinfo-26+knots			98725af3571	last=5090771f326 furszy/2023_rpc_getblockfileinfo
	#27.xTODO# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
	# Needs review & BIP finality & might have wallet changes: 28202 josibake/implement-bip352-receiving
		# Note alternative (approach NACK'd) in #28453
	# Needs review & BIP finality: 27827 josibake/silent-payments-base-pr-slim-down
	# Needs review & concept: 28241 Sjors/2023/08/silent-index
	# Needs work & maybe removing an anti-feature?: 27836 furszy/2023_rpc_fetchblock_improvements
	# Needs review: 27837 furszy/2023_introduce_block_request_tracker
	# Needs work: 27854 -  # [WIP] add a stratum v2 template provider
		# OR #28983 OR #29432 OR #30315+???
	# Needs review & compat checking: 27859 -  # Mempool: persist mempoolminfee accross restarts
	#27.xTODO# Make disabled by default: 28052 maflcko/2306-fs_stuff-
		#+ #30607? +#30657 +#30669
	# Needs review: g753 -  # Add new "address type" column to the "receiving tab" address book page
	# Needs review and concept: 28463 mzumsande/202308_increase_block_relay
		# Why not just increase inbound capacity to max anyway?
	# Needs concept/review? 28806 ajtowns/202311-depinfo-scriptflags
	# Needs work: g777 -  # gui: getrawtransaction implementation
	# Needs concept/review: 28926 willcl-ark/2023-07-getnetmsgstats
		# Was #27534 -  # rpc: add 'getnetmsgstats', new rpc to view network message statistics
	# Needs concept/review: 28930 -  # wallet: Add scan_utxo option to getbalances RPC
	#27.xTODO# 28950 instagibbs/2023-11-submitpackage-max-fee-burn
		# +#29722 ?
		# +#29735
	# Needs review and/or optionality: 28977 murchandamus/2023-11-gutter-guard-selector
	28979 rpc_sendall_ancestor_aware-27+knots	02b0ef1f9a7
	29016 rpc_listmempooltxs-26+knots			2f5360dc558	last=07008477b81 niftynei/nifty/listmempoolentry
		# Includes typo fixup in comment that annoys linter
	# Needs review? 29054 achow101/descriptor-sethdseed
	29657 fix_netinfo_v2t_safety-27				f950b367506
	# Needs concept + review: 29129 brunoerg/2023-12-externalsigner-account-parameter
	29130 achow101/createwalletdescriptor-without-new-records
	# Needs review or minimal impact: 29136 achow101/sethdseed-void-descriptor
	# Needs final interface: 29163 rpc_help_detail-22								last=c6b68c29707 LarryRuane/2024-01-help-detailed
	# or (newer): 29163 rpc_helpdetail-24									last=56830469303 LarryRuane/2024-01-help-detailed
		# Left off top commit changing rpc_help test behaviour
	# Needs concept & review: 29278 -  # RPC: Wallet: Add maxfeerate and maxburnamount startup option
	# Needs work: 29396 -  # rpc: getdescriptorinfo also returns normalized descriptor
	# Needs review: 29415 vasild/private_broadcast
	# Buggy & maybe waste of RAM? Needs review?? 29418 vasild/getnetmsgstats
	# Needs concept & work: 29468 -  # rpc: method removeprunedfunds should take an array of txids
	# assumeutxo not supported: 29519 mzumsande/202202_fix_assumeutxo_block_download
	29530 rpc_getpeerinfo_misbehaving_score-26	dbf55fb8c38	last=87efb6f0cfd
		# NOTE: Held back 976d61c974e...87efb6f0cfd which degrades docs and adds a test incompatible with Knots
			# (Silently conflicts with f33cd8869dd (#27114): fix in 3a4ef30d880)
	# Needs work: 29553 fjahr/2024-03-dumptxoutset-height
	29585 manpage_see_also-23+knots				acb79094058	last=7c3ac598dd9 fanquake/list_other_pages_in_man
		# Added fix so manpages don't "see also" themselves (diff-minimised from what posted to the PR)
	# Needs review & wallet compat check: 29675 achow101/musig2
	29686 manpage_desc-27+knots					d65d8d596c8	last=f6171a8f1da willcl-ark/manpage-desc
		# Various fixups
	29687 bcli_err_noconn_helphint-0.17			a67add604d4	last=69d6fd676e9 willcl-ark/improve-cli-error
	29695 gcc_branch_protection_default-26		ecd2224cebc	last=7850c5fe20a fanquake/gcc_12_branch_protection_default
	TODO: Newer ver MERGED API change: 29845 stickies-v/2024-04/make-warnings-arr
		# When merged upstream, adapt deprecaterpc to behave like fix_rpc_warnings_all-21
	#27.xTODO# 29954 kristapsk/getmempoolinfo-permitbaremultisig-maxdatacarriersize
		# Extend to other options?
		# TODO: Fix datacarriersize description
		# TODO:  b02aab950af RPC/Mempool: getmempoolinfo: Return many more mempool options
		# Concept fixup: new RPC method entirely since they don't change often?
	# TODO: 29959 laanwj/2024-04-qtsowrap-wayland (needs also #29923)
	#27.xTODO# Needs review and split from NAT-PMP removal? 30043 laanwj/2024-05-pcp
	30062 rpc_getrawaddrman_asmap-26			73c5cba850a	last=1e54d61c469 brunoerg/2024-04-asmap-getrawaddrman
	(CHECK-LAST)	last=53f38f6fcee origin-pull/30183/head
		# +#30183
		#28.xTODO# Try backporting tests
	# Needs review: 30080 -  # wallet: add coin selection parameter add_excess_to_recipient_position for changeless txs with excess that would be added to fees
	# Needs review & Core release (wallet format): 30243 -  # Tr partial descriptors
	g825  gui_show_maxmempoolsize-27			7bbe4e7db6f	last=4a028cf54c0 theStack-g/gui_show_maxmempoolsize
	#27.xTODO# Needs concept? 30341 willcl-ark/psbt-strip-derivs-combine
	#27.xTODO# Needs concept? 30381 willcl-ark/addnode-failure
	# Needs review: 30433 fanquake/standard_branch_fedora
	30515 rpc_scantxoutset_blockhashetc-26		3a723935d68
	# Needs review? g832 -  # Improve user dialog when signing multisig psbts
	# Needs review/optional? 30572 ariard/reject-unsolicited-txn
		# Was #21224
	Needs rewrite? 30635 Sjors/2024/08/waitforblock
	# Needs review: 30685 hebasto/240820-control-flow
	Needs review? 30708 jamesob/2024-08-getdescriptoractivity
	Needs review? 30713 tdb3/relevant_blocks_in_scanblocks_status
	#28.xTODO# Mitigate #30717 breaking compatibility with no-longer-debug opts
	Needs work? 30727 jonatack/2024-08-add-address-type-to-getaddressinfo
	TODO: Some RPC way to report if settings are default?
	
	#28.xTODO# Support for sending tx with TRUC version
	# TODO: GUI block template view
	# TODO: Build next-block template from mempool + N MB txs (to replace empty blocks for local miner)
	# TODO: Extend IsUnspendable safely
		# eg based on https://github.com/bitcoin/bitcoin/pull/29981
	# TODO: IPv6 Pinholing (see #30005)
# Non-progress functionality:
	8751  sort-multisigs-26+knots				04a7c9549eb	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					5007845888e	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys							06f4c5e023e
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245 ionice									79f8728ef74
	-    ionice_win								449a1557c99
	8501  old_stats_rpc-27						c92a5fd01c1	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-27+knots					022054f96ee	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504  rpc_dumpmasterprivkey					bfb11cd2b21	last=07fc81109a
	g444  gui_netwatch-27+knots					764f2f765a6	 # Latest code now
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-27+knots				aee9437f8ea  # latest code now
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet to wallet-restricted users for now
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
	10554 zmq_wtx-27+knots						ba89fef85d3	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
		# Extended doc/zmq a bit to match additions from #14060 and #23471
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					6f7962e8fe8
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment				a1ecd0bd017
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
		# TODO: Consider rebasing on #29575 ?
	10350 filtered_witblock-27				e34c690a8e7	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				5fb23f0e254	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								69067895110	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			a2713e0eee2
	12965 scriptthreads-27+knots				7a203a9fd17	last=dfab6c6866 jonasschnelli/2018/04/svt
	13203 dsha256_power8-27						789dfcc340f	last=3b402e0738 TheBlueMatt/2018-05-asm
		# NOTE: Stripped out benchmark change
		#28.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	-     dsha256_power8_asm_pragmas-27			82181fbc222
	15218 postibd_flush-27						06b45666f77	last=8887d28a014
	15428 tor_gui_pairing-27+knots				dadc8ab723e	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-27+knots				b9d6192ad19	# Latest code now
		# FIXME: fix automatic tor outbound using subprocess
		# FIXME: -netinfo doesn't show tor if inbound-only?
		#28.xTODO# Revert #29844 if still using boost::process?
	# TODO: tor guix bundle!
	#27.xTODO# 16490 maflcko/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support TRUC & Knots policies
	17795 gui_console_ctrl_d-26+knots			cbd76d41ddf
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					02e002f2ca8
	n/a   rpc_compat_error_index-25+knots		cf58d738eae
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos						83275db302e
	17636 guisettings-0.21						6ffcebc35e7	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					b9440dda1c1	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						9490b48a48c	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances				7c84b8de8eb	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-27+knots	b58c6254bc9	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=71bfa1fb715 cli_getinfo_mw_total_balance-26
	19117 rpc_getrpcwhitelist					19034491b1f
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-27+knots		56c7ddf0543
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-27+knots		8a9a3fba770
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	# Needs concept & review: Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
	Needs concept: 29523 -  # Wallet: Add max_tx_weight to transaction funding options (take 2)
		# WAS (never in Knots): #29264 instagibbs/2024-01-max-tx-weight
	# TODO: Guix: When glibc 2.36+ is required, use -Wl,-z,pack-relative-relocs
# Non-upstreamed functionality:
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	n/a   restore_feefilter_opt					6c75f8d0f85
	-     gui_payreq_textedit					f772370c57d
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				7deffea9f09
	-     walletnotify_w_win-27+knots			da83b15cf1c	# Latest code now
	14137 win_taskbar_progress-27.1+knots		1b8c3e5b8e4	last=18eb4dbb8a
		# NOTE: Could drop /official_releases/archive/ change, but keeping it ensures a conflict when the version gets bumped, so we can update the sha256 hash
		FIXME: Qt 5.15.15 bump
	-     restore_blockmaxsize					eb03b17cdaf
	7107  qtnetworkport-27+knots				6987290598f	last=1f37c87d8f2 origin-pull/7107/head
	29306 truc_sibling_eviction-27+knots		d458a48294a	last=1342a31f3ab glozow/2024-01-sibling-eviction
	29873 truc_10k_vsize_limit-27+knots			8ae5943ccb5	last=154b2b2296e glozow/2024-04-truc-25k
	7533  sendraw_force-27+knots				af9a606041c last=2627c0937f8 sendraw_force
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532,#29060 if merged
	11082 rwconf-27+knots						e93252ffc47 # Latest code now
		#28.xTODO# Squash fixes
		#28.xTODO# Deprecate with settings.json better?
	7510  rwconf_gui-27+knots					dc0d41683c3
		#28.xTODO# Squash fixes
		#28.xTODO# Move blockreconstructionextratxn (and others?) from rwconf_policy?
		FIXME: turning on peerblockfilters after pruning has begun prevents starting at relaunch
	559   accept_nonstdtxn						e023124323e
		#28.xTODO# Revert or redefine #29843 if it got merged
	 929 tbc									24523ecf145
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
	 553 bugfix_qt_uri_amount_parser			41616f25bc5
	-     mining_priority						80f9bb7e36f	# Latest code now
		#27.xTODO# FIXME: Lots of lock warnings from clang! (did I already fix these?)
		#27.xTODO# FIXME: Should blockmintxfee apply to blockprioritysize??
		# If mempool-knots.dat is ever extended to store easily manipulatable data, port Xor stuff over
		# Reverts (needed and better performance & memusage): d0cd2e804ec [refactor] rewrite BlockAssembler inBlock and failedTx as sets of txids
	5861 gui_restore_addresses					d23e2a5ce91
	5891  qt_console_history_persist			5da2e77fab2	last=0cd5fc301d6 qt_console_history_persist
	7219  rbf_opts-27+knots						556b082f984	# Latest code now
		#28.xTODO# Revert #30594(partial) & #30592
	-     truc_opts-27+knots					52ebfb386c8
		#28.xTODO# Check if default/interaction values ought to be changed
	# TODO? -     net_identify_librerelay
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					40002696e50
		# TODO: Split out legacy address preference to be more explicit
		#28.xTODO# Revert gui#808 ??
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19+knots		5b04307a1e5	# Latest code now
	-     gui_request_payment_label-0.19		85139adb973
	-     gui_peers_sort_network-23				97e0290e085
	-     gui_peers_no_net_column				dc2d891dc28
	22439 guix_in_gitian-23+knots				2014b1271e3	last=ebda0463748 achow101/guix-in-gitian
	-     rpc_getblockfrompeer_future			7745976d104
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		bb0b7bc1289
		# Prior Knots bundled this in with #20295
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
	-     gbt_rpc_options-27+knots				99864fe613b
	TODO: pre-cache GBT call after new block?
	TODO: RPC to get/set policy configs
	-     miningcbtag-27+knots
	-     blockview-27+knots
NM	-     mapport_default_on-27+knots			a32f282230d
		# Re-disabled in light of continued security issues
	#27.xTODO# Look into making the patches tarball in guix
	-     undeprecate_libconsensus-27			d12a94481fb
		#28.xTODO# Restore libbitcoinconsensus? #29748 #29787 #29797 #29648 #30590
	# TODO: bump dbcache to 1 TB on systems we can detect memory pressure! - after testing
	n/a   macos_dmg-27							d26ae740b99
		# Reverts #28432, #28932, and #28973, and includes fix_dmg_openfinder
		#28.xTODO# revert macos ZIP only: #29733
		# TODO: Investigate if we can compress again by reverting #24031 using patches in https://bugzilla.mozilla.org/show_bug.cgi?id=935237
# Non-upstreamed policy options (default off):
	#28.xTODO# Try using #29086(MERGED)+#30232 to rebase policy options up here?
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	29309 permitbarepubkey-27+knots				e4a6d730757	last=1dfe27e49ab
	-     bytespersigopstrict-27+knots			f99d9396f6e
	9749  unique_spk_mempool-27+knots			04c00f7019d
	-     dustdynamic-27+knots					f50f599fb42
	28408 match_more_datacarrier-27+knots		8998d6dbd8d	last=4d2ec0671a3 match_more_datacarrier
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
		# Revise byte counting to consider input/output waste
	-     datacarriercost-27+knots				bce9d9cd75d
		#27.xTODO# Add tests and make sure boundaries are correct
	# TODO: Filter for output value < tx fee * N - https://twitter.com/DoctorBuzz1/status/1741622696327205176
	# TODO: Impose accurately-calculated (not just guessing witness size) dust limit on Taproot _spends_ (only Taproot because there should be a more sensible spend path available in theory)
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     acceptnonstddatacarrier-27+knots		0dd43ab9460
	-     rejecttokens-27+knots					d823de4ed7e
		# Currently filters just Runes
	k78   rejectparasites-27+knots				78086c1a806	last=d978324923a
		# Currently filters just CAT-21
		# GUI component & default-on moved into rwconf_policy below
		# Rewrote unit test to be more comprehensive
	# TODO: NO APPARENT USAGE: filter HG: https://pbs.twimg.com/media/GDV-H8UWkAAsckl?format=jpg&name=large
	# TODO: CBRC-20 https://twitter.com/bitoordileone/status/1734654996539457666 - INSCRIPTION-WRAPPED: https://mempool.space/tx/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9
	# TODO? All-ASCII data storage (inefficient)
	# TODO? If any input is dust, limit output count to < input count? (or lower?)
	# TODO: Stacks (OP_RETURN X2... - most are 80 bytes long, some 55, few 19)
	# TODO? Procedural approve/deny/discount/penalize policy scripting?
	# Needs concept ACK: 29843 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	-     maxscriptsize-27+knots				9b6c9313f78
		# Alternate to(?) #29769
	# Needs concept & impl: Policy: limit script sigops to N (default to MAX_OPS_PER_SCRIPT which is consensus pre-taproot)
	# Needs concept & impl: Policy: limit any witness stack items to N elements (like MAX_STANDARD_P2WSH_STACK_ITEMS)
	# TODO? Ordislow??
	# TODO? Spam filter for stuff like https://mempool.space/tx/4ec38548aa67f6a2efbbc3cf34ab49dc5c275d9701ab0b58696baee9f555c45a
	# TODO: Whitelisting model for non-SPK scripts
	# TODO: -blockpreference=smaller|larger,lessdata|moredata (or match our own policies?)
# Non-upstreamed Knots compatibility:
	#28.xTODO# Check on #29942 removal of -datacarrier, possibly revert?
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-26			5190456efbb
		# Effectively reverts #24505, #27869, #28597, and gui#764
		#28.xTODO# revert #28710  Remove the legacy wallet and BDB dependency
	14641 fundraw_min_conf_deprecated-25+knots	526d26b79b0	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			5be45ec7b3e
	-     netperms_implicit_addr				1732b4783aa
	# IMPOSSIBLE with v2transport param: 12674 rpc_onetry_nonpriv-25+knots			ecaf5bf309f
	-     rpc_getblockfrompeer_nodeid_compat	a4904d8b06e
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-25+k		9ce7e391094
		#28.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	-    1day_default_conftarget				71a27f0a62c
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	-     bloom_default-27						d67b05096ff
	-     wallet_avoid_newerchange				13f9c5d6772
	-     enforce_checkpoints					d3abd2373ec
	n/a   checkpoint_update-27					1c1a32354d5
		#28.xTODO# Revert #25725 (Remove mainnet checkpoints)
	10282 timebomb_knots						6deb5987eb8
	-     rwconf_policy-27+knots				cbc0b4b258b
		# Includes Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: Get GUI settings for dustdynamic to select ratio box & focus text area when you click their labels
		#27.xTODO# QTreeWidget or similar for GUI Options dialog?
		#28.xTODO# Revert #30352 + #30562 ?
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
	7483  svg_icon-27+knots						b1b7aca6b04
		# Consider: https://github.com/bitcoinknots/bitcoin/pull/54
	n/a   tbc_font-27+knots						cdac8494921
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/ But depends on the build-for-release-source code from svg_icon...
# BRANDING:
	n/a   knots_branding-27						fcc7fb5df1b
		#27.xTODO# Review security policy
		# NOTE: Includes #30308
		#28.xTODO# remove "nsis-header.bmp: Generate from SVG" (moved to svg_icon)
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#28.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
# TODO: Check that we aren't deprecating anything in Core
# TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Check #26039 doesn't break anything
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
# TODO: Check that no git Author lines are a mix due to GIT_AUTHOR_NAME no longer allowing emails: git log v27.1.. | grep '^Author.*luke-jr' | grep -v Dashjr
	n/a   (cherrypick=6e49826402a)				a1c656a5082	# doc/{bips,files}
		# TODO: Update with bump_version below !!!!
	n/a  (bump_version=Knots:20240902)			3164bc9d5cb
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist		c00938c3909
	n/a   (cherrypick=bd18588c33a)				247c167f3d5  # release notes: write/update, including change log and credits
		# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge [gk]?\d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# When re-added, #28824 notes in 9db5d23d559
		#28.xTODO# (when assumeutxo supported) Include the deleted notes from 0bc1f4b5c7b
	n/a  (cherrypick=540426ee9cc)				e933c45607c  # update manpages (build first)
		# also example bitcoin.conf
	#28.xTODO# n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: Upload to Transifex with * d9411324066 (ts_20220515, origin-pull-g/599/head) GUI: Support translating Bitcoin units
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @27.x-knots-android

#@27.x-knots-extratests

