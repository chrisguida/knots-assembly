timestamp 2025-09-03 17:57:31
lastapply no-merge

#.. checked up to PR #33296 / gui #884 / knots #160

checkout v30.0rc1
@30.x-syslibs
# BUILD BUGS:
	# TODO: CMake 4 compat
		# https://bugs.gentoo.org/show_bug.cgi?id=958361
		# https://github.com/google/crc32c/commit/2bbb3be42e20a0e6c0f7b39dc07dc863d9ffbc07
# SYSLIBS:
	2241  sys_leveldb							a0ecf548285
		# Related: #32447
		# If https://github.com/bitcoin-core/leveldb-subtree/pull/52 is merged, this should possibly be adapted
	5416  sys_libsecp256k1						0de78dc8ead
	# TODO: sys_crc32c ??
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	n/a   rm_minisketch-29+syslibs				f6e0ddeab22
		# Implicitly includes most of #18818
		#30.xTODO# sys_libminisketch
	15155 test_external_bcli					a84a0a443b0
	30997 qt5qt6-29								3872919744d
		# Includes parts of gui#861 whitslack/qt6
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	n/a   (delete_release_notes_fragments)
@30.x-knotsfixes
# TESTS:
	# If needed: -     ci_knots-26							e2099d64846
	-     lint_relaxer-29+knots					1c6b5cf61c8
	-     nowarn_unreachable-code				8db24138af3
	# If needed: -     nowarn_unused-function				45a2e5951ce
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
	# If needed: -     ci_i686mp_clang15						955f1eeed99
	-     ci_gha_makejobs_8						8cd076e06ab
# FIXES:
	13789 asm_bypass_cxxflags					6ba82076749
	32217 fix_gitdir_foreign					829e7360c77
		# Was part of #18902
	#30.xTODO# Revert #32220 (cmake: Get rid of undocumented BITCOIN_GENBUILD_NO_GIT environment variable)
	-     relsrc_embed_tagname-29+knots			52c08c64519
		# Was part of #18902
	18427 2020mingwthrd-mini					52e30e24120	 # Latest code now
	18490 bugfix_symcheck_pe_case				87c6edc40bb
	14968 http_bind_error						4c94a57b317	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					98902ee54f1
		# NOTE: libevent-copied code more-or-less up to date as of 2025-04-04 112421c8fa4840acd73502f2ab6a674fc025de37 (upstream has added more portable TCP keepalive, setting keepalive interval to 5min, failure if setting keepalive or reusable fail, and merged 1a6dd1ff1b8 but not e8461128b8d,5a067073d77,45dd91f71f4)
	 9524  rpc_pruneblkchain0					4bf17a16144	last=88883ae13d
	10731 log_more_uacomment					2e933c464e8
	29614 bufferedfile_fclose					9d2ac4ddb66
	14485 fadvise-29+knots						bffc1241fd6  # Latest code now
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					744ec512987
	-     fix_rpc_arg_multiname					fb7b1a996ca
	-     bugfix_rpc_getbalance_hacky			a8c0a9147ab
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted -OR- 27539 Empact/2023-04-minimum-file-descriptor-18911
	# Needs review: 16050 promag:2019-05-importmulti-update
	18194 bugfix_gui_edit_sendaddr-mini			52280b91301	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				47502964b7e	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect OR 27245 fjahr/202303-pr19434 OR 27909
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	g152  gui_notify_setup_bg					6205c652e01
	-     bugfix_gui_drop_abc_confusing_hack	47fc261db8d
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	g236  gui_init_walleterror_cont				ccfc4419464
	-     rpc_addconnection_mainnet				a73ab129139
	32343 subproc_closefds						d2c3393106b
		# Was #30756
		# Replaces #22417 (Boost::Process variant)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				bb75733ea11
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs work: 32964 w0xlt/r_26573
		# Was #26573 darosior/taproot_over_dont_under_estimate
		# Was #23502 achow101/tr-low-fee-est
	# Needs work: 23534 achow101/no-change-fee-w-sffo
		# NOTE: If we're sending to someone else who is paying the tx fee, it actually makes sense?
	g506  qt_qrcode_sizefixes					7e2ee7ebafe
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	24066 -										a9418a47f41	last=89cb2b6d91e  # contrib/init: (OpenRC) use -daemonwait to wait for startup completion
	-     openrc_from_gentoo					7f44a33c81c
		# Other OpenRC updates from Gentoo:
		# - PIDDIR in /run instead of /var/run
		# - LOGDIR var added
		# - RPC cookie group-readable
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				da7d68cba67
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-28+knots			45e45dd5346	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	# Needs review: 24972 hebasto/220425-no-libtool
	g595  qt_handle_autostart_errors-0.15		f0647470a58	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	-   gui_psbt_error_msgbox					bd32acbd160
		# WAS: g599  ts_20220515-partial-25				5191aa16ac2	last=d9411324066 ts_20220515
			# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
			#TsTODO# Update with other commit (unit translations) when translations supported again
	32358 fix_subprocess_pr32358-28				fd0457bdfd0
	32567 fix_subprocess_pr32567-28				9cadd01d7cf	last=e63a7034f03 hebasto/250520-subprocess-backports
	29868 hww_windows-29						7a36f5685dc	last=3a18075aedd hebasto/240414-win-subprocess
		# NOTE: Retained `ENABLE_EXTERNAL_SIGNER` cmake option
		# Replaces: -     hww_windows-27						e1f9c1bbde8
			# Reverts #29489 & #28967
	# Check on #25561 (nonsense signed int overflow in leveldb?)
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	g633  -										af8adf57970	last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	g662  qt_fix_txview_202209					84c4612291e
		# Includes gui#368
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	# TODO: Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	# Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	# TODO: Sane fix for #24049
	g677 fix_qt_peers_na						f059ea17b1c
	# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs work: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-28+knots	aa279928aad	last=a6f567590b7
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	#30.xTODO# CAUTION: #27307 was merged, but "this appears to possibly show a higher balance than the user actually has for sure??" - investigate
	# Alternative to: 27434 pinheadmz/chaintips-invalid
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#30.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	-     qafix_assert_debug_log_create			91ac3341eda
	-     acceptstalefeeestimates_mainnet_opt	27c2a9e0a8d
		# Currently (28.1) needs qafix_assert_debug_log_create
	# Needs review: 27684 hebasto/230516-punish OR ???
	#30.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 forbid_nohelp-29						b5d33ff7540	last=bfc2bb6a270
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	# Needs review: 27912 -  # net: run disconnect in I2P thread
	# Needs work: 27973 maflcko/2306-byte-span-
	28029 fix_zmq_errhandling_202307-mini		8b12c7d4761	last=ba28af94bd5 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err		a67c6bf9589
	# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Needs review: 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	# Needs review: 28248 jonatack/2023-08-network-diversity
	28345 fix_bytespersigop_checks-mini			f832cbd25bd	last=6f627727739 fix_bytespersigop_checks
		#30.xTODO# NOTE: Excludes removal of buggy wrapper for diff-minimisation; needs checking manually (to ensure wrapper doesn't get used even in final/complete merge of all PRs) when assembly done; known issues: stash 172d7d7a9 or 81541e24c01
		# Related bug in #18479
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	28616 Sjors/2023/10/assume-unconfirmed		3f131e38266	last=3e281590c7d  # assumeutxo_unconfirmed_ux_Sjors-28
	-     assumeutxo_unconfirmed_ux-29			9c78260a377
	-     qt_recomm_confirms-0.9				9b7a9b39d9a
		# NOTE: Un-hardcoding 6 already taken care of in assumeutxo_unconfirmed_ux above (956546a1f2f)
	# Needs review & triage: 28678 sipa/202310_miniscript_assume
	# Needs review: g775 -  # gui: add used balance to overview page
	# Needs review: 28780 -  # log: torcontrol opt checks
	-     fix_keep_notmy_cookie					49ea6490746
		# Originally part of #28784, but regressed in d95dde9441f...7cb9367157e
	# Needs review: 28824 fix_asm_nodecimals-23								last=fde11cb0fa3 willcl-ark/asm-full-hex
		# FIXME: disambiguate opcodes too?
	28944 rpc_sendall_anti_fee_sniping-28		ebf6bd332f0	last=aac0b6dd79b ishaanam/sendall_anti_fee_sniping
	-     rpc_walletcfpsbt_antifeesniping-28+k	3d477da7b95
	(CHECK-LAST)	last=113ba106273 Sjors/2025/07/locktime
		# Includes tests from #32892
	29141 fix_rpcauth_blank						07e7273ab2c
	# Needs work: 29147 guix_attachable_sigs					ad4fe4b83a4
		# GPG discourages clearsign signatures!
		#30.xTODO# but windows has lots of problems with existing style...
		#30.xTODO# but deviating from Core signing may reduce participants?
	# Needs review: 29155 -  # wallet: move lock at the top of ReleaseWallet
	29175 -										30359d692f3	last=be8ae64b82e  # rpc: validate fee estimation mode case insensitive (fix_rpc_estmode_unset_case-24)
	# Needs work: g786  -  # FIX:When opening or autoloading wallets there should be clear messages about rescanning in progress and wallets' names.
	31551 bulk_block_rw-29+knots				9c1b259c06b
		# Optimisation, not fix - but simplifies #29307
	29307 AutoFile_error_check-29+knots			eef5c9b1e3a	last=c10e382d2a3 vasild/AutoFile_error_check
	# Needs work: g792 -  # Correct tooltip wording for watch-only wallets
	# Nothing to fix? 29589 -  # tests: fix OP_1NEGATE handling in CScriptOp
	29640 fix_tiebreak_on_disk-26				176d6e2a7b1	last=0465574c127 sr-gi/202403-block-tiebreak
		# IMPORTANT: Adds a UB bugfix
		# left off doc change (4caa38600e6)
	#30.xTODO# Needs review: 29652 ryanofsky/pr/noloc
	#30.xTODO# Needs review: 29664 mzumsande/202403_near_tip_stalling
	29678 fix_init_lowdisk_warning_reqd^		0dac5ea9cc5	last=c452d6c1efe fix_init_lowdisk_warning_reqd
	# Needs review: 29680 -  # wallet: fix unrelated parent conflict doesn't cause child tx to be marked as conflict
	# Needs review: 29770 fjahr/2024-03-check-undo-index
	# Needs review: 29796 fanquake/depends_0g_debug_flags
	-     fix_rpc_warnings_all-28				faa690604f8
	g815  fix_qt_privacy_before_open-23			d1f6741a92e	last=0dc337f73d0
		# Rewrote myself due to overcomplication and race bug in PR
	# Not worth it? 29963 hebasto/240425-guess-cc
	#30.xTODO# Needs review: 30079 ismaelsadeeq/05-2023-ignore-transactions-with-parents
		# Was: 25380 darosior/fee_estimator_disable_cpfp
	-     jonatack/2024-05-fix-cjdns-detection-in-AddNode	9058fb89db4	last=be4541abe59 jonatack/2024-05-fix-cjdns-detection-in-AddNode  # fix_cjdns_addnode_detect2-27+knots
	# Needs review: 30155 mzumsande/202405_replay_blocks
	#30.xTODO# Revert or semi-revert #30157 ?? (Mempool-influenced fee estimation)
	# Needs review & diff-minimising: 30207 mzumsande/202405_invalid_chains
	# Needs review & maybe wallet format finalization: 30221 achow101/wallet-no-chainstateflushed
		# +#32580 ?
	# Needs work: g823 -  # wallet: Improve error log color in the console
	-     detect_clang_bug96267					ffd86470c7e
	# Needs review: 30359 -  # Correct Error Code in OP_IF/OP_NOTIF Empty Stack Check
	# Needs review: 30469 fjahr/2024-07-csi-overflow-2
		# Was: 26426 fjahr/202210-coinstatsindex-overflow
	# Needs careful review: 30479 mzumsande/202407_fix_resetfailure
	# If needed? 30489 theuni/depends-zmq-patch
	# Needs review: 30972 BrandonOdiwuor/wallet-listreceivedby-fix
		# was: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	31275 fix_rpc_example_quoting_pr31275-24	6b5aa2cd846	last=7e93e292598
	# Needs work? (adds overhead) 31298 -  # rpc: combinerawtransaction now rejects unmergeable transactions
	# Needs work: 31349 vasild:test_log_internet_traffic
	# Needs work: 31378 furszy/2024_wallet_migration_multisig_crash
	# Needs review: 31404 furszy/2024_descriptors_infer_multisig
	# Needs careful review: 31405 mzumsande/202411_stricter_invalidblock_handling
		#+32843
	# Needs backport work: 31423 wallet_migrate_watchonly_only-29
	# Needs review/correctness per branch: Diff-minimise: 31449 -  # coins,refactor: Reduce getblockstats RPC UTXO overhead estimation
	#30.xTODO# Revert: Knots NOT AFFECTED: 31453 macos_exfat_warning-29+knots			25f0359c100	last=db3228042b2 willcl-ark/macos-exfat
		# Checking blocksdir unconditionally in case it's a mountpoint
		# Dropped doc change
		# Added warning before leaving GUI firstrun screen
		# Only affects macOS 14.x (13.x and 15.x unaffected)
		# Knots gets rid of likely-buggy macOS-specific AllocateFileRange in fix_preallocate, which fixed this
	# Needs review: 31514 -  # wallet: allow lable for external descriptor & disallow label for ranged descriptors
	# Not strictly a bug? 31603 brunoerg/2025-01-descriptor-pk
	# Needs work? 31610 l0rinc/l0rinc/gettransaction-rpc-doc
	# Needs work: 31615 -  # Ensure assumevalid is always used during reindex
	#30.xTODO# 31622 achow101/psbt-sighashes
	31727 miniscript_nonfatal_pr31727-29		5ec3ce0749b	last=3693e4d6ee0 !hodlinator/2025/04/31727_followup
		# Includes fixes from #32255
	# Needs review? 31734 -  # miniscript: account for all StringType variants in Miniscriptdescriptor::ToString()
	# Needs review? 31774 -  # crypto: Use secure_allocator for AES256_ctx
	# Needs work & importance: 31775 -  # rpc: collect transaction fees on generateblock
	# Needs review: 31785 Sjors/2025/02/create_new_block
	# Needs review: 31807 theuni/fix-dupe-kernel-symbols
	# 31912 workaround_buggy_rndrrs-28			36e11bb93cc	last=2498dd8dbd5  # random: Check GetRNDRRS is supported in InitHardwareRand to avoid infinite loop
		# Held back 585aba6eec8..2498dd8dbd5 (2x diff for basically the same thing)
	# Needs review? 31835 -  # validation: set BLOCK_FAILED_CHILD correctly
	# Needs work: 31888 midnightmagic/fix-linearize-gjpyn
	# Needs review: 31929 hodlinator/2025/02/stop_http_robust
	31958 -										1b194dc64c6	last=32dcec269bf  # rpc: add cli examples, update docs  # docfix_rpc_wallet_cf_psbt-24
	31979 -										9c2ba644265	last=f708498293c  # torcontrol: Limit reconnect timeout to max seconds and log delay in whole seconds  # tor_backoff_max-26
	# Needs review: 32051 jonatack/2025-03-addnode-p2p
	32073 netinactive_dont_downgrade-26			73e71aa6cb8
	# Needs concept & review: 32123 -  # wallet: make coinbase that will mature on the next block available for selection
	# Needs review: 32143 -  # Fix 11-year-old mis-categorized error code in OP_IF evaluation
	# Needs review: 32159 willcl-ark/pcp-default-multipart
	32176 tor_rnd_stream_isolation-28			b8f992ff32b
		# Omitted renaming variable
	# Needs review: 32180 mzumsande/202403_ibd_lastcommonblock
	32185 fix_dbwrapper_batch_header_size-26	9a3e987c02d
		# Only the fix, without the bumped LevelDB version dep
	# Needs review: 32186 -  # descriptor: handle listdescriptors(private=true) for taproot descriptors having partial keys
	# Needs review: 32199 maflcko/2504-time
	# Needs backport work: 32273 -  # wallet: Fix relative path backup during migration
	# Needs review: 32313 l0rinc/l0rinc/reenable-coins-sanitizers
	32344 fix_wallet_nonranged_pr32344-22		e1105d80b60	last=97d383af6d5
	32351 qafix_nonrecurs_FindChallenges-28		5c9d232aa8b
		# Fix only
	32355 fix_block_full_enough					fae59848ca9
	# Needs review: 32367 hebasto/250428-enable-lang
	-     fix_fs_error_utf8-23					c7c558250da
		# Alternative to core#32383 hebasto/250429-fs-error
	32414 fix_reidxcs_periodic-25				25587d794f9	last=c1e554d3e58 andrewtoth/reindex-flush
		# Fix only
		# TODO: consider performance refactor?
	# Simplified rewrite of? 32528 maflcko/2505-1
		# Was (unreleased) #31135 jonatack/2024-10-verification-progress or #31177 polespinasa/verificationProgress
	32539 fix_rpcallowip_cjdns-29				4e9efa449c6	last=12ff4be9c72 pinheadmz/rpcallowip-rfc4193
	# Needs work: 32577 hebasto/250521-subprocess-split
		# FIXME: Ensure this gets resolved before #32566 is merged
	#30.xTODO# If #32566 is merged, test extensively with Windows quoting nonsense
	# Needs review: 32606 davidgumberg/5-23-25-ignore-unsolicited
	# Needs review and simplification? 32636 davidgumberg/5-27-2025-create-refactor
	# Needs careful review: 32646 instagibbs/2025-05-fillblock-mutated
	32682 fix_wallet_fillpsbt_nothrow-28		e62a71bc283
		# Diff-minimised only
	# Needs review: 32685 -  # wallet: Allow read-only database access for info and dump commands
	32736 fix_listwalletdir_err-23				3b5c7ad20d2
	# Needs review: 32757 -  # net: Fix Discover() not running when using -bind=0.0.0.0:port
		# Was #31492 (not in any release)
	# Needs review: 32773 hebasto/250618-mkdir
	# Needs concept & review: 32788 achow101/desc-allow-H
		# Check for this impacting other Knots merges
	#30.xTODO# Needs review: 32821 -  # rpc: Handle -named argument parsing where '=' character is used
	32845 fix_rpc_nowallet_errors_pr32845-29	5bf1c1012b2
	# Needs concept & review: 32869 instagibbs/2025-07-invalid-cb-stall
	32878 fix_index_rewind_badassert_pr32878-19	162ea7dec7d
		# Fix only; left off invasive test
	32987 fix_gui_reindex-29					661d3eca7ee
	# Needs review: 33014 b-l-u-e/fix-32849-descriptorprocesspsbt-internal-bug
	# Needs review: 33072 b-l-u-e/p2p-fix-nscore-overflow-24049
	# Part of, if translations are important: 33115 hebasto/250801-ts-files
	# Needs work: 33126 Ataraxia009/multi-client-support
		# NOTE: Rewrote in knots_branding
	# Needs concept/work: 33127 Ataraxia009/launch-crash-failure
	# Needs review: 33135 Sjors/2025/08/older-safety
	# Needs review: 33164 hebasto/250809-fallback-fallocate
		# NOT SUFFICIENT WITHOUT:
	33228 fix_preallocate						72889c574ab
		# Includes less-than-ideal workaround for https://github.com/bitcoin/bitcoin/issues/33128#issuecomment-3203396013
	33215 fix_debuglog_refs_hardcoded-28+knots	baceaf6a2f3
		# Includes gui#884 hebasto-g/250819-debuglog
	# Needs review? 33223 murchandamus/2025-08-tiebreak-SRD
	# Needs work: 33231 w0xlt/mulitple_binds
	# Needs review: 33268 achow101/zero-value-from-me
	# Needs review: 33296 Crypt-iQ/cmpctblock_assume_fix_09032025
	33310 wrkarnd_gcc_systemtap_ice
	-     fix_rpccookieperms_early				672a509ad20
	-     qt_intro_nojumpy						0395e3d216c
	-     restore_guix_ppc64le-28				5d9e7c64669
	-     qt_dialogs_less_modal					5477686ee34
	-     docfix_getorphantxs_vsize				810596f0ca9
		# Originally bundled in Knots with #30793 rpc_getorphantxs
	-     fix_guix_boost_mirror-29				52df20dd73c
	-     fix_qt_startup_unknown_unit			a0d6397ec2b
	-     fix_qt_psbtops_filename_amount		5638267617e
	k126  fix_qt_progressbar_fittext			fa2d43225a3
	k150  fix_rpc_mixed_params_edgecases		3c93d8c249c
		# Held back (4d24d60836f) support for positional options + named params (breaks tests)
	-     qt_nowalletpage_alerts-23				76e281b0ce7
	-     fix_alertnotify_winquoting			1723a4e8625
	#30.xTODO# "Knots feature request: system notification for a txn should show the net wallet balance delta assuming the txn confirms, not whatever it does now that gives me a heart attack every time I use a large-ish UTXO lol" -Jason (currently only the first send of a sendmany is shown) https://github.com/bitcoin-core/gui/issues/853
	# TODO: prunenotify to run a command after each prune (eg, for fstrim or such)
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	# FIXME: https://twitter.com/tchjntr/status/1788332365887995925
		# weird bitcoin.conf results in:
		#	ASSERT failure in QList<T>::operator[]: "index out of range", file /bitcoin/depends/x86_64-w64-mingw32/include/QtCore/qlist.h, line 575
	# TODO: ensure that rejecting a tx also rejects dependents in the orphan pool
	#30.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
#@30.x-knots-lts-deps
	-     upd_qt5-29							d77f9d28a5f
		# 5.15.17 Opensource released: https://lists.qt-project.org/pipermail/announce/2025-May/000557.html
		# Includes patch for CVE-2025-4211 (not upstream; simpler and safer)
		# 5.15.19 (not available) fixes other bugs, but no CVEs that affect us (unless we start using Qt for XML or HTTP2)
	#30.xTODO# FIXME -     depends_qt5kde
	# Needs review: 32655 fanquake/sqlite_3_50_0
	# Needs review: 32665 fanquake/boost_shrink
@30.x-knots
# PERFORMANCE:
	# Needs review: 24158 JeremyRubin/epoch-mempool-reorg-updates
	# Needs review: 24589 -  # sha512.cpp improvements
	# Probably a bad idea: 24712 -  # wallet: reduce coin selection iterations
	# Knots doesn't support MSVC builds: 24773 Enable AVX2 implementation of SHA256 for MSVC builds
	# Needs work: 24901 -  # mempool: reduce lookups, insertions to cache in UpdateForDescendants
	# Needs review: 24926 -  # mempool: use mapNextTx.lower_bound in removeRecursive
	# Needs review: 25236 -  # wallet: use vector instead of list for transactions
	# Needs review & diff-minimising: 25297 -  # wallet: speedup transactions sync, rescan and load not flushing to db constantly
	# Needs review: 32740 danielabrozzoni/upforgrabs/25968
		# Was (not in Knots): 25968 sipa/202208_headerssync_optimize
	# Unclear benefit: 26375 zmq_optimise_duplread-27+k			3f9e56d77af	last=7b631dc9b19 andrewtoth/no-read-zmq
		# Several improvements in Knots branch
		# Post-#26415(merged), it's unclear if this is an improvement or potentially a performance loss: we either readback raw (from OS cache), or serialize CBlock
	# Needs review: 26486 sipa/202211_batchnotfound
	# Opt-in & needs review: 26951 pstratem/2023-01-23-gcsfilter
	# Needs review: 26966 furszy/2022_parallelize_blockfilter_index_2
	# Needs review: 27006 furszy/2022_reduce_cs_main_scope_blockindex_nfile
	# Needs concept/review: 27050 -  # p2p, validation: Don't download witnesses for assumed-valid blocks when running in prune mode
	# Needs review: 27427 -  # validation: Replace MinBIP9WarningHeight with MinBIP9WarningStartTime
	# Needs review? Part of? 28226 martinus:2023-08-more-CBufferedFile
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 -										c41bedd50df	last=42b25bbd939  # opti_merkle_mutation-0.17
	28592 -										d3fb919478c last=b81f37031c8  # txrelayrate_14txps-26
		# TODO: Make configurable? Or is that even sane?
	# MSVC: Needs review: 29036 theuni/msvc_fast_byteswap
	# Needs review?? 29159 -  # Update net.h bigger TCP socket using larger buffer
	# Needs review: 29473 -  # optimization: Speed up Base58 encoding by 400% by 64-bit preliminary byte packing
	# Needs review: 29491 fjahr/2024-02-batch-validation-updated
	# Needs review: 29578 brunoerg/2024-03-addrman-getaddr
	29602 opti_IsSpace_pr29602-29				21875576e81
	# TODO: Revert #29815 ? (ie, use OS provided optimised timingsafe_bcmp)
	30059 dbfilesize_param-29.1					ed00e3ba242	last=c283a572145 dbfilesize_param
	-     dbfilesize_64-29.1+knots				4205028a6df
	# Needs review: 30317 -  # WIP Simplify SipHash
	# Needs review: 30325 -  # optimization: Switch CTxMemPool::CalculateDescendants from set to vector to reduce transaction hash calculations
	# Needs review: 30370 fjahr/2024-07-pr28945
		# Was (never in Knots) #28945
	# Needs review? 30442 paplorinc/paplorinc/siphash
	# Needs review: 30610 sipa/202408_force_sync
	30611 chainstate_write_hourly-29+knots		7ac62a9c1df	last=e976bd30450 andrewtoth/write-chainstate-every-hour
		# Includes new tests from core#32414
		# TODO: Make interval configurable
	# Needs Knots review & diff-minimise: 30987 davidgumberg/zero_after_free_allocator_change
	# Needs review: 31132 andrewtoth/threaded-inputs
	# Needs review: 31144 l0rinc/l0rinc/optimize-xor
		# 30.x rebase (on old latest_knots) in 5ee1dbcb681
	31179 ismaelsadeeq/10-2024-add-reserve-to-univalue	8d2b1b3f4c4	last=5d82d92aff7  # opti_rpc_uv_reserve-25
	31645 opti_dbbatchsize_64-29				726390be112	last=b6f8c48946c l0rinc/l0rinc/utxo-dump-batching
		# Held back 868413340f8...b6f8c48946c (reduce to 32 MiB) for now
		# TODO: Test even higher or incrementing-as-we-flush
	# Needs review: 31682 l0rinc/l0rinc/optimize-CheckBlock-input-duplicate-check
	# Needs Review? 31714 mzumsande/202501_simpler_segwit_check
	# Needs reivew: 31868 l0rinc/lorinc/block-serialization-optimizations
	# Needs review: 31875 l0rinc/l0rinc/sorted-BatchWrite
	# Needs work: 32023 -  # wallet: removed duplicate call to GetDescriptorScriptPubKeyMan
		# +#32475
	# Needs review: 32128 -  # Draft: CCoinMap Experiments
	# Needs review: 32150 murchandamus/2025-03-rewrite-BnB
	32279 opti_script_inline_36b-29				94ddd1cdff6	last=d5104cfbaeb l0rinc/l0rinc/prevector-size
	# Needs careful review: 32473 sipa/202504_sighash_cache
	32487 opti_readblock_hash_once-29			f3d935c3fb1
	-     netproc_check_blockhash				42bc17c792a
	# Needs review: 32497 opti_merkle_reserves-21							last=39b6c139bd6 l0rinc/l0rinc/pre‑reserve-merkle-leaves-to-max
	# Needs careful review: 32532 l0rinc/l0rinc/short-circuit-known-script-types
	# Needs review: 32645 theStack/202505-fs-use_ftruncate_on_openbsd
		# NOTE: ftruncate does not guarantee allocation normally? and we don't want to truncate!
	# Needs work: 32692 -  # TODO: Dynamic scriptcheck thread count
	# Needs review: 32730 furszy/2025_net_avoid_traversing_block_twice
	# Needs review: 32791 -  # checkqueue: implement a new scriptcheck worker pool with atomic variables
	32827 opti_removeForBlock_empty-28			18102a04fdc	last=249889bee6b l0rinc/l0rinc/empty-mempool-IBD
	# Needs work/review: 32885 pstratem/2025-07-05-lockless-isibd
	# Needs review: 33031 achow101/lasthardened-cache-migratewallet
	# Needs Qt5 compat: 33217 rm_xinerama-23									last=e9623be19ad fanquake/drop_xinerama
		# Broken backport to 30.x in #33238
	# Needs review: 33253 ajtowns/202508-cache-friendly-compactblock
	#30.xTODO# 33264 kevkevinpal/reduceScopeOfGetBlockTemplateLock
	# TODO: dumptxoutset doesn't return until chain is rolled back forward
# SOFTFORK:
	# TODO: 31989 CheckTemplateVerify
		# Was #21702 (never in Knots)
	# TODO: 28550 jamesob/2023-09-covtools-softfork
	# TODO: 29050 stevenroose/txhash
	# TODO: 29198 reardencode/lnhance
	# TODO: 29221 -  # Implement 64 bit arithmetic op codes in the Script interpreter
	# TODO: 29247 -  # Reenable OP_CAT
	# TODO: 29269 -  # Add OP_INTERNALKEY for Tapscript
	# TODO: 29270 -  # Implement OP_CHECKSIGFROMSTACK(VERIFY)
	# TODO: 29280 -  # Implement OP_CHECKTEMPLATEVERIFY
	# TODO: https://github.com/jamesob/bitcoin/tree/2025-06-ctv-csfs CTV+CSFS combined
	# TODO? 30018 -  # Implement BIP 118 validation (SIGHASH_ANYPREVOUT)
	# TODO? 32080 -  # OP_CHECKCONTRACTVERIFY
	# TODO? 32247 jamesob/2025-04-csfs
	# Needs community support: 33163 -  # BIP360 quantum
# FUNCTIONALITY:
	#-     rm_kernel_lib							84b7c6adf43
		# TODO: Support libbitcoinkernel (see 9da0bc3eba7 history for incomplete attempt)
			# When restoring libbitcoinkernel support, adjust libbitcoinconsensus reverts to make it interact with --with-libs (see 7ad32d39d76)
	-     rm_multiprocess						b7edbefc5be
		# TODO: Support libmultiprocess
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
	# Needs fixing/review: 17303 maflcko:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees					311e2a53cb3	last=47b2ba29df2 !origin-pull/12911/head
		# Dropped rel notes file
		# NOTE: Originally #12911
		#30.xTODO# FIXME: "feerate" fails to account for sigops (see 21d85b5c0e); most of a fix in stash 835c2d3afba
	# Needs review and care (new index): 13014 jonasschnelli/2018/04/txindex_prune
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15836 fee_histogram+pr15836_api				b66ef9894ec	last=b94292a7cb jonasschnelli/2019/04/feeinfo
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
	22693 getaddressinfo_txids					d649b03395c
	g562  wallet_warn_reuse_gui					76598022300
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# Needs work? 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				46499cc78fa	last=a0d0807abc2 neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		d9111df627c
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-27+knots		e7c731bc7c1	last=409c2e34522 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr-29+knots			ccefcccdcf8	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								75bcb149e83
		# ALSO: Fixes uacomment test, promotes uacomment to non-debug, and includes -uaspoof
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							31b884cdfd6
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	19873 mempressure-29+knots					f74d806474e	last=5b43cc77824 mempressure
		# TODO: LevelDB flushing causes burst of memory usage; consider that here; see #31645
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			7d91a062d67	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-28+knots				31cb569f99b	last=1002e2d0d7f jonatack/setfeerate
	# OR (evaluate): 31278 -  # wallet, rpc: Settxfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
		# TODO? Reduce internal changes and move to Knots compat??
	20407 rpcauthfile-29+knots					e383e26fdbc	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						4a27c88592d	last=cf940f0e5f5
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					59e1641ab0b	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	g363  qt_peers_directionarrow-25+knots		3acae4d666d	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						24396bde48d	last=1af20831806 Sjors/2021/05/hww-toggle
	# Needs work? 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21260 rpcwallet_tx_in_mempool-29+knots		b7452f15dd6	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					ac6ff73bd45
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						5a9eb76a030	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex-29+knots					cf2b768d765	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt				e4cab0527cb	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
		# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							05f22347c13
	24963 rpc_walletprocesspsbt_options-26		8d7787aa571	last=40143bafb52 rpc_walletprocesspsbt_options
		# Diff-minimised (and uses merge for rpcarg_type_per_name)
		# Held back f43f992b731...40143bafb52:
			#* 40143bafb52 QA: rpc_psbt: Test that the wrong type cannot be given to named params
			#* 7cd0315bc40 RPC: Strictly enforce the type of parameters passed by name
	-     rpc_descriptorprocesspsbt_opts		dcadc6e6a05
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	# Needs review: 25621 -  # rpc/wallet: Add details and duplicate section for simulaterawtransaction
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs review: g410  benthecarman-g/uppercase-uri
	23362 importfromcoldcard					d5799239e85	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates-29+knots			9c5b8ab1cbc	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06 (FlushFeeEstimates lock on m_cs_fee_estimator)
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			b9fb29bc8bc	last=ad431ff5d18
		# TODO? change to logarithmic scale? 8398d247f4e
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip					59ffb329261	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	# Needs work: g866 rebroad-g/trafficgraphwidget-rebased
	g820  qt_fontsel_qrcodes-27+knots			8d249ad1090	last=b14c9d0572e qt_fontsel_qrcodes
	# TODO: qt_fontsel_console
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	-     verifymsg_bip137_and_electrum			17934fc889c
		# NOTE: Fully reverts gui#819 in anticipation of #24058
	24058 bip322-29+knots						c4e550ce5b5	last=29b28d07fa9 kallewoof/202201-bip322
		# gui#819 fully reverted above in anticipation of this
	#30.xTODO# signmessagewithprivkey updates for BIP137+Electrum+BIP322
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-29			dee9fd868ea	last=97a69e232be
		# +RPC doc fix
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
	# Needs review: 24539   # Add a "tx output spender" index
	# TODO? BIP 179 (tho... Lightning) - upstream first to get translations?
	# Needs work: 24897 w0xlt/silent_payment_021
	# Needs work: 24950 -  # Add config option to set max debug log size
	# Needs work: 24952 -  # rpc: Add sqlite format option for dumptxoutset
	# Concept NACK? 25026 -  # rpc: Make pruneblockchain fetch old blocks if height is lower than pruned height
	# TODO? Needs careful review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku ???
	25183 rpc_fundraw_segwitonly				5be51bb0d0f	last=9e7fd5c0fe3
		# Currently just an old version for Knots 23.0 compatibility (held back 1c5cfd84b3d...9e7fd5c0fe3)
		# Fixed tests with inspiration from 9e7fd5c0fe3
		# TODO: update without breaking compatibility? (new code looks buggy tho - needs rewrite?) (also, filtering by "input type" doesn't really make sense, though segwit filtering does)
	# Needs concept: 25261 -  # rpc: fetch multiple headers in getblockheader()
		# Was: Needs API review: 23330 JeremyRubin/header-fetch
	#30.xTODO# 25269 -  # wallet: re-activate the not triggered "AmountWithFeeExceedsBalance" error
	# Needs concept review: 25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
		# Concept unsure: Hides logline by default; but maybe we want that with more info included?
	# Needs review: 25366 w0xlt/desc_rpc
		# Besides the private key issue (removed; conceptual issues), RPC doc also has "addresses" where there would be a single address (in a details Object)
	# Needs work: 25434 w0xlt/bypass-timelocks
		# NOTE: Was #21413 glozow/2021-03-bypass-timelocks (never in Knots)
		# Also #25570 ?
	# Needs completion & review: 25718 fjahr/2022-07-allowinbound
	# Needs concept/review: 25747 w0xlt/desc_file
		# If merged, consider multiwallet_rpc restrictions
	# Needs work: 25776 1440000bytes/bumpfee-inputs
	# Needs work: 25923 jonatack/2022-08-statestats
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	# Needs review (or leave external?): 26052 -  # contrib: Add script to colorize logs
	# Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	# Minimised: 26162 Sjors/2022/09/taproot
	#30.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	# Needs review: 26174 w0xlt/list_address_book
	-     whitelist_outgoing_auto				2d643b04bcb
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme	a2d4d86689d	last=d8434da3c14
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 rpc_disconnectnode_subnet				0edc91d4bcc	last=23f4c2cb452 brunoerg/2022-11-disconnectnode-subnet
		# Refactored tests (to be more deterministic) and added support for disconnecting a single IP without subnet specified
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	27034 rpc_importaddr_for_descwallet-27+k	883f7d0d710	last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
		# Diff-minimised & tweaked to avoid breaking #23362
	27052 rpc_getpeerinfo_lastblockann-28		07eabfbc28b	last=cbe4603a902 LarryRuane/2023-02-getpeerinfo
		# Avoided changing internal data structures
	27216 rpc_getaddressinfo_isactive			20325a1073c	last=85f83339dda pinheadmz/used-addr-ui
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-29+knots						413a4285f4f	last=91771366a3d apoelstra/2023-03--codex32
		# See #32652 if #29136 is merged
		# Diff-minimised, doc bug fixed & tweaked to avoid breaking #23362
	# Needs concept & review: 33043 w0xlt/codex32
	# Needs work: 27409 ryanofsky/pr/1data
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	27600 p2p_forceinbound-28+knots				e2fb9a86cc6	last=8c2026848da pinheadmz/whitebind-evict
		# Reverted forceinbound limit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27770 rpc_getblockfileinfo-28+knots			3a310d4bf24	last=5090771f326 furszy/2023_rpc_getblockfileinfo
	#30.xTODO# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
	# Needs review & BIP finality & might have wallet changes: 28202 josibake/implement-bip352-receiving
		# Note alternative (approach NACK'd) in #28453
		# OR #32966 Eunovo:2025-implement-bip352-receiving
	# Needs review & BIP finality: 27827 josibake/silent-payments-base-pr-slim-down
	# Needs review & concept: 28241 Sjors/2023/08/silent-index
	# NOTE: If adding new output types (eg, Silent Payments?), need #33065 (rpc, wallet: replace remaining hardcoded output types with FormatAllOutputTypes)
	# Needs review: 27837 furszy/2023_introduce_block_request_tracker
		# Prior work & maybe has an anti-feature?: 27836 furszy/2023_rpc_fetchblock_improvements
	# Needs work: 27854 -  # [WIP] add a stratum v2 template provider
		# OR #28983 OR #29432 OR #30315+???
	# Needs review & compat checking: 27859 -  # Mempool: persist mempoolminfee accross restarts
	# Needs review: g753 -  # Add new "address type" column to the "receiving tab" address book page
	# Needs review and concept: 28463 mzumsande/202308_increase_block_relay
		# Why not just increase inbound capacity to max anyway?
	# Needs concept/review? 28806 ajtowns/202311-depinfo-scriptflags
	# Needs concept/review: g777 -  # gui: getrawtransaction implementation
	# Needs concept/review: 28930 -  # wallet: Add scan_utxo option to getbalances RPC
	# Needs review and/or optionality: 28977 murchandamus/2023-11-gutter-guard-selector
	29016 rpc_listmempooltxs-29+knots			044b512f8a6	last=07008477b81 niftynei/nifty/listmempoolentry
		# Includes typo fixup in comment that annoys linter
	# Needs review? 29054 achow101/descriptor-sethdseed
	# Needs concept + review: 29129 brunoerg/2023-12-externalsigner-account-parameter
	# Needs review or minimal impact: 29136 achow101/sethdseed-void-descriptor
		# See #32652 if merged
		# Also #32861 ??
	# Needs final interface: 29163 rpc_help_detail-22								last=c6b68c29707 LarryRuane/2024-01-help-detailed
	# or (newer): 29163 rpc_helpdetail-24									last=56830469303 LarryRuane/2024-01-help-detailed
		# Left off top commit changing rpc_help test behaviour
	# Needs concept & review: 29278 -  # RPC: Wallet: Add maxfeerate and maxburnamount startup option
	# Needs work: 29396 -  # rpc: getdescriptorinfo also returns normalized descriptor
	# Needs review: 29415 vasild/private_broadcast
		# TODO: Extend RPC to allow overriding private broadcast config option
	# Needs concept/review: 28926 willcl-ark/2023-07-getnetmsgstats (OR...)
		# Was #27534 -  # rpc: add 'getnetmsgstats', new rpc to view network message statistics
	# Buggy & maybe waste of RAM? Needs review?? 29418 vasild/getnetmsgstats
	# Needs concept & work: 29468 -  # rpc: method removeprunedfunds should take an array of txids
	-     manpages_seealso_notself				468867a8aaa
		# Originally bundled into #29585
	# Needs review & wallet compat check: 31244 achow101/musig2-desc
		# Needs #3313 too?
	# Needs review: 32724 w0xlt/musig2_tests
	# Needs review & wallet compat check: 29675 achow101/musig2
	#30.xTODO# 29954 rpc_getmpinfo_policy_pr29954-28+knots				last=d165ac8779b kristapsk/getmempoolinfo-permitbaremultisig-maxdatacarriersize
		# Or maybe this is unnecessary with a get/set policy RPC method?
	#30.xTODO# -     rpc_getmpinfo_policy_coreetc-28+knots
	# Needs review: 29959 laanwj/2024-04-qtsowrap-wayland (needs also #29923)
	# Needs review: 30080 -  # wallet: add coin selection parameter add_excess_to_recipient_position for changeless txs with excess that would be added to fees
	# Needs review & Core release (wallet format): 30243 -  # Tr partial descriptors
	#30.xTODO# Needs concept? 30341 willcl-ark/psbt-strip-derivs-combine
	# Needs concept? 30381 willcl-ark/addnode-failure
	# Needs review? g832 -  # Improve user dialog when signing multisig psbts
	# Needs review/optional? 30572 ariard/reject-unsolicited-txn
		# Was #21224
	30635 rpc_waitfornewblock_tip_param-29		99cdb3fa41f	last=c6e2c31c551 Sjors/2024/08/waitforblock
	# Needs review: 30685 hebasto/240820-control-flow
	30713 tdb3/relevant_blocks_in_scanblocks_status	771f38d4a5c	last=5b2d0216d87  # rpc_scanblocks_status_results-28
	#30.xTODO# Mitigate #30717 breaking compatibility with no-longer-debug opts
	# Needs work? 30727 jonatack/2024-08-add-address-type-to-getaddressinfo
	30860 bashcomp_bcli_generate-29				a29ec7810ef	last=abf6ad42bdb BrandonOdiwuor/bash-completion
		# Bugfix + Left off re-generation until later
	30886 rpc_descrprocesspsbt_prevtxs-28+knots	0125b96f50a	last=87ceb610a72 instagibbs/2024-09-updateutxo_psbt
		# Avoided doc-code move
	# Needs work: 31086 dnsseed_cdecker-28								last=5b823920836 cdecker/202442-re-add-bitcoinstats-seed
	# Needs work? 31252 rpc_TxToUniv_witScript-28								last=4e128d4f9b2
		# Alternative: 31256 naiyoma/feature/rpc-show-redeemscript-in-P2WSH-and-P2SH
	# Needs concept ACK: 31353 jonatack/2024-11-total-wallet-balance
	31560 rpc_dumptxoutset_fifo-29+knots		08b2d9151b3	last=145dc34dc05 theStack/202412-dumptxoutset-allow_write_to_named_pipe
		# Only the FIFO capability, left out the bundled scripts
	# Needs work? 31668 -  # Added rescan option for import descriptors
	31672 peer_cpu_load-29+knots				e1acc5f8e87	last=b25b40ebd5f vasild/peer_cpu_load
	31845 pruneduringinit-29+knots				20b478132ff	last=d4a3abf6d43 pruneduringinit
	31886 netinfo_local_svcs-29+knots			ccbbf5e00f3	last=721a051320f jonatack/2025-02-netinfo-services
	# Needs work: 31936 -  # rpc: Support v3 raw transactions creation
	31953 bumpfee_full_rbf-29+knots				e4cb0912021	last=fa86190e6ed maflcko/2502-fullrbf-follow-up
		# Was: 26454 petertodd/2022-feebump-without-optin
		# NOTE: Added warning to GUI and made RPC behaviour change optional
	32200 socks_tor_error_codes-0.18			ef7776445a5
	# Needs work? 32297 ryanofsky/pr/ipc-cli
	32423 hash_rpcuserpass-29+knots				01ddf8b6aca	last=e49a7274a21 laanwj/2025-05-remove-rpcpassword-deprecation
		# Left out refactoring
	32425 proxy_per_net-29						b6759ef9558	last=e98c51fcce9 vasild/proxy_per_network
		# Left out doc updates/reformatting
	32429 doc_rpc_keypoolrefill_pr32429-23		7a0ca065635
	# Needs work: 32468 -  # rpc: generatetomany
	# Needs concept & review: 32471 -  # Fix listdescriptors true fails with 'Can't get descriptor string' in non-watch-only descriptor wallet
	# Needs review; 32489 achow101/export-watchonly-wallet
	# Needs review: g872 achow101-g/export-watchonly-wallet-gui
	# Needs work: g870 -  # Expose AssumeUTXO Load Snapshot Functionality To The GUI
	# Needs concept & work: 32501 BrandonOdiwuor/removeprunedfunds-array
	# Needs review: 32517 pinheadmz/wallet-gettransaction-ischange
	32540 rest_spenttxouts-26					bafdba9a1c2
		# +32842
	# Needs concept review: 32541 -  # index: store per-block transaction locations for efficient lookups
	# Needs review: 32638 l0rinc/l0rinc/read-block-hash-check
	# WIP: 32741 rpc_getpeerinfo_nodeid-28							last=9393b33325e
		# OR #32972 ?
	# TODO: Review ParseHDKeypath change: Part of: 32784 Sjors/2025/06/gethdkey
	32844 rpc_gettxoutproof_segwit-27+knots		1add226bf59	last=23edd3db4f1 rpc_gettxoutproof_segwit
	# WIP: 32857 Sjors/2025/07/no_script_path
	# Needs review: 32896 ishaanam/wallet_v3_txs
	33004 def_natpmp_true-29					49299a11685
	# Needs review & wallet format release: 33008 Sjors/2025/07/bip388-register
	#30.xTODO# Revert #33069 (wallet: Add Support for BIP-353 DNS-Based Bitcoin Address via External Resolver) ?
	# Needs concept: g882 -  # qt: add shift key modifier to clear command history when clearing the console
	# Needs review: 33191 ajtowns/202508-sendtemplate1
	33230 rpc_cli_hashorheight-29				926e7b7e8a6	last=aabf1f60938 achow101/cli-strong-or-json
		# Left off test changes
	# Needs work? 33259 rpc_getblockchaininfo_bgvalidation-26				last=c1f545248ea  # rpc, logging: add backgroundvalidation to getblockchaininfo
	#30.xTODO# 33290 Sjors/2025/08/missing_capnp
	-     qt_createunsigned_use_psbtops			74d90403d5e
		# NOTE: invisible (unmerged) dependency on qt_dialogs_less_modal
	# TODO: Some RPC way to report if settings are default?
	# TODO: sats/vB feerate in GUI: https://x.com/billsmith4lyfe/status/1869097896823713819?t=DH2Z02nl6V_nTQp5znmbgA&s=09
	# TODO: "I have a UPS" mode to avoid flushing frequently even while pruning
	
	# TODO: GUI block template view
	# TODO: Build next-block template from mempool + N MB txs (to replace empty blocks for local miner)
	# TODO: Extend IsUnspendable safely
		# eg based on https://github.com/bitcoin/bitcoin/pull/29981
	# TODO: IPv6 Pinholing (see #30005)
# Non-progress functionality:
	8751  sort-multisigs-28+knots				92df63e0250	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					940083bb392	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys-29+knots					44cbcf82a5f
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
		# NOTE: Now also includes mintxfee in getwalletinfo for testing purposes
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245 ionice-29+knots						bfb0eeb83f2
		# low prio: p2p requests, loading/verifying blocks on disk
		# normal prio: connecting blocks, indexes, user requests
	-    ionice_win-29+knots					10892b57b57
	8501  old_stats_rpc-29						6831a10e62d	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-29+knots					10ed65e4763	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504  rpc_dumpmasterprivkey					9d35fae3d99	last=07fc81109a
	g444  gui_netwatch-29+knots					16723559d17	 # Latest code now
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-29+knots				5c69db144c7  # latest code now
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet/etc to wallet-restricted users for now
		# TODO: Allow absolutely-denied RPC calls if a RPC whitelist is being used
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
	10554 zmq_wtx-29+knots						2bb50c8a7a4	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
		# Extended doc/zmq a bit to match additions from #14060 and #23471
		#30.xTODO# Stop using boost signals!
	20551 rpc_onetry_conntype					734e3a6c7fe
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment				dc1bfd6539c
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
	10350 filtered_witblock-28				85f79922ccd	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				ff60a62e953	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								af2c3b55714	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			72f0d6f0454
	12965 scriptthreads-29+knots				c44ee00eacd	last=dfab6c6866 jonasschnelli/2018/04/svt
	13203 dsha256_power8-29						61d7257f766	last=3b402e0738 TheBlueMatt/2018-05-asm
		# NOTE: Stripped out benchmark change
		#30.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	15218 postibd_flush-28						aa4ebc8adc2	last=8887d28a014  andrewtoth/flush-after-ibd
	15428 tor_gui_pairing-29+knots				8a117f403ab	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-29+knots				8199cb732ff	# Latest code now
		# FIXME: fix automatic tor outbound using subprocess
		# FIXME: -netinfo doesn't show tor if inbound-only?
	# TODO: tor guix bundle!
	#30.xTODO# 16490 maflcko/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support TRUC & Knots policies
	17795 gui_console_ctrl_d-26+knots			dc8978346fe
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					c03159ce063
	n/a   rpc_compat_error_index-25+knots		7c110eec893
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos						4f4b6cee694
	17636 guisettings-0.21						cf6c6f777ed	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					ddfc03bec8b	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						ee6183dd3b4	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances-29				bc62061f1a7	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-29+knots	eec7f5b926a	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=71bfa1fb715 cli_getinfo_mw_total_balance-26
	19117 rpc_getrpcwhitelist					21530d27430
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-29+knots		27db55e59be
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-29+knots		fac2587a469
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan-g/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	# Needs concept & review: Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
	30951 v2onlyclearnet-29+knots				8857e6d203a	last=27e90008835
		# Made a hidden option
	# Needs review: 32065 vasild/i2p_early_create_session
	# Needs review & concept: 32726,32728 -  # Add initial OpenAPI/Swagger specification for Bitcoin Core RPC and REST interfaces
	# Needs review: 33044 fanquake/19513_rebased
	-     font_for_money_global					5f7ec5a5b49
	k157  qt_darkmode-29+knots					e3837f86c17	last=2c15a2071f6 bigshiny90/v29.1-knots-rc1-guifixes
	(CHECK-LAST)	last=aa6b9665628 bigshiny90/gui-darkmode-updates  # knots#160
	# TODO: validaterawtransaction with UTXO lookup (and fee calc) ?
	# TODO: Guix: When glibc 2.36+ is required, use -Wl,-z,pack-relative-relocs
# Non-upstreamed functionality:
	-     rm_tarball_ci-29+knots				7c56cb2b99b
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	-     restore_upnp-29.1+knots				81360fdd41b
		# NOTE: Includes #30301 theuni/miniupnp-228-bump
		#30.xTODO# Revert #32500
	n/a   restore_feefilter_opt					22e9d95fd02
	-     gui_payreq_textedit					be2e1f1539a
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				cf311d552e9
	# FIXME: -     walletnotify_w_win-27+knots			c892f8b6dbf	# Latest code now
		# FIXME: this is broken :(
	14137 win_taskbar_progress					c2d2f4107ee	last=18eb4dbb8a
		# NOTE: Could drop /official_releases/archive/ change, but keeping it ensures a conflict when the version gets bumped, so we can update the sha256 hash
	-     restore_blockmaxsize					79e86dc8f7d
		# TODO?? blockreservedsize option
	#30.xTODO# Revert #32654 (deprecate blockmaxweight)
	7107  qtnetworkport-29.1+knots				45316cf3d9f	last=1f37c87d8f2 origin-pull/7107/head
		# FIXME: Unbind IPv6 on the other port, if its IPv4 bind failed
	7533  sendraw_force-29.1+knots				16e3faace5e last=2627c0937f8 sendraw_force
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532,#29060 if merged
		# TODO: 1d3fdc1adde Support ignoring various rejection reasons in PackageMempoolChecks
			# error message change impacts a bunch of functional tests; and submitpackage currently lacks support for ignore_rejects anyway
	11082 rwconf-29+knots						c7bc896125f # Latest code now
		#30.xTODO# Squash fixes
		#30.xTODO# Deprecate with settings.json better?
	7510  rwconf_gui-29.1+knots					662e7f22125
		#30.xTODO# Squash fixes
		#30.xTODO# Move blockreconstructionextratxn (and others?) from rwconf_policy?
		# TODO: when we can enable block filters post-pruning, revert 81d696e132c
	559   accept_nonstdtxn						211d3bf5011
		#30.xTODO# Revert or redefine #29843 if it got merged
	929   tbc									cbe5f87ea0e
	n/a   tbc_font								8dfefb8a627
		# Includes ff7b90dc729 Embedded font: Rename to avoid confusion in font selector  (fix_qt_fontsel_confusion)
	 553 bugfix_qt_uri_amount_parser			591831142cb
	5861 gui_restore_addresses					be9545fef04
	5891  qt_console_history_persist			479f46ceaa3	last=0cd5fc301d6 qt_console_history_persist
	-     net_identify_librerelay				5430192f451
	-     net_identify_utreexo					3197cb1b1f9
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					e2ca8192cfa
		# TODO: Split out legacy address preference to be more explicit
		# FIXME? descriptor wallet migration doesn't take this into account?
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname_wo_dat			42de6d9c093	# Latest code now
	-     gui_request_payment_label-0.19		3374173ecd6
	-     gui_peers_sort_network-23				b049f31da8b
	-     gui_peers_no_net_column				9f8af8fe3f0
	# 22439 guix_in_gitian-23+knots				2014b1271e3	last=ebda0463748 achow101/guix-in-gitian
		# FIXME: If restoring, test that this still works (WIP fixes in stash fa8517a9112 but need rebase too)
	-     rpc_getblockfrompeer_future			b653764d7b3
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		ffb0acc7be9
		# Prior Knots bundled this in with #20295
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
	32547 mining_avoid_block_copy-29+knots		5e2faf0f44f	last=7d05ec01d4e mining_avoid_block_copy
	-     gbt_rpc_options-29+knots				139f8e58902
	# TODO: pre-cache GBT call after new block?
	#30.xTODO# RPC to get/set policy configs
		# https://github.com/bitcoinknots/bitcoin/issues/115
	#30.xTODO# -     miningcbtag-27+knots
		# TODO: add to rwconf_policy: 4b38a3031ab GUI/Options: Add miningcbtag via settings
	-     blockview-29+knots					572745d0f5f
		#30.xTODO# need to revert or find alternative source for fee info
	#-     mapport_default_on-27+knots			a32f282230d
		# Re-disabled in light of continued security issues
	#30.xTODO# Look into making the patches tarball in guix
	-     restore_libconsensus					41e50ca22f4
		# +Needs review: 24994 hebasto/220426-consensus
	# TODO: bump dbcache to 1 TB on systems we can detect memory pressure! - after testing
		# https://github.com/bitcoinknots/bitcoin/issues/70
	# TODO: GUI & first run dbcache setup?
	-     rpccookieperms_log_improvements-29+k	bf517bc83a8
	# Needs work: n/a   macos_dmg-27							d26ae740b99
		# Reverts #28432, #28932, and #28973, and includes fix_dmg_openfinder
		# 30.xTODO: revert macos ZIP only: #29733
		# TODO: Investigate if we can compress again by reverting #24031 using patches in https://bugzilla.mozilla.org/show_bug.cgi?id=935237
		# FIXME: Probably incompatible with MERGED #31407 macos_notarization ?
		# TODO? 17311 RandyMcMillan:fix-background-svg
	# Needs review: 31065 danielabrozzoni/20241008_rest_broadcast
	33023 qa_cb_extratxs-25						3c3a9df3f5d	last=841b3c2e966 bigshiny90/compactblocks-extratxs-tests-core
		# Held back f9c6331cb26...841b3c2e966 for now
	#30.xTODO# Revert #32450 ?
	#30.xTODO# Revert #32510 or replace extratxn pool
	#30.xTODO# Consider reverting #33050 ? (and #33183?)
# Non-upstreamed policy options (default off):
	30232 refactor_isstandardtx_mpopts-29+knots	68c2d3d03fb
	-     pol_acceptunknownwitness				e39fca20239
	-     mining_priority						d11a62cc165	# Latest code now
		#30.xTODO# FIXME: Should blockmintxfee apply to blockprioritysize??
		# If mempool-knots.dat is ever extended to store easily manipulatable data, port Xor stuff over
		# Reverts (needed and better performance & memusage): d0cd2e804ec [refactor] rewrite BlockAssembler inBlock and failedTx as sets of txids
		# Reverts (needed for lock logic): 192dac1d337 [refactor] Cleanup BlockAssembler mempool usage
	7219  rbf_opts-29+knots						108fd1105d0	# Latest code now
	-     truc_opts-29+knots					df9aa98a121
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	29309 permitbarepubkey-29+knots				82bdecc6088	last=1dfe27e49ab
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     bytespersigopstrict-29+knots			fbd97489734
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	9749  unique_spk_mempool-29+knots			e3c98b32bfc
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     dustdynamic-29.1+knots				9d53339a24a
	# ---- BEGIN DATACARRIER ---- (OLGA not backported)
	28408 match_more_datacarrier-29+knots		64791f208d3	last=4d2ec0671a3 match_more_datacarrier
		#30.xTODO# TODO: Delete TBD "maxdatacarriersize" from #29954 (see b02aab950af) (or at least fix the description)
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
		# TODO? Revise byte counting to consider input/output waste
	-     datacarriercost-29+knots				4baf376ec16
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		#30.xTODO# Add tests and make sure boundaries are correct
	-     acceptnonstddatacarrier-29+knots		6858598a5fd
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# FIXME: Data before OP_RETURN (and non-push opcodes??) should count the data as non-standard (but can't predict everything, so wait until there's a need? 75f1652b447)
	# ---- END DATACARRIER ----
	k136  pol_permitephemeral					f410cccee7b
		# Also includes permitbare{anchor,datacarrier} options
		# FIXME: prioritisetransaction shouldn't block dust txs (but also shouldn't blindly bypass policy by promoting ephemeral to non-ephemeral!)
	# TODO: Filter for output value < tx fee * N - https://twitter.com/DoctorBuzz1/status/1741622696327205176
	# TODO: Impose accurately-calculated (not just guessing witness size) dust limit on Taproot _spends_ (only Taproot because there should be a more sensible spend path available in theory)
		# https://github.com/bitcoinknots/bitcoin/issues/113
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     rejecttokens-29.1+knots				ae573f24daa
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Currently filters just Runes
	k78   rejectparasites-29.1+knots			75fa64ac325	last=d978324923a
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Currently filters just CAT-21
		# GUI component & default-on moved into rwconf_policy below
		# Rewrote unit test to be more comprehensive
	# TODO: #30964 & LR alternative options
	# TODO: NO APPARENT USAGE: filter HG: https://pbs.twimg.com/media/GDV-H8UWkAAsckl?format=jpg&name=large
	# TODO: CBRC-20 https://twitter.com/bitoordileone/status/1734654996539457666 - INSCRIPTION-WRAPPED: https://mempool.space/tx/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9
	# TODO? All-ASCII data storage (inefficient)
	# TODO? If any input is dust, limit output count to < input count? (or lower?)
	# TODO: Stacks (OP_RETURN X2... - most are 80 bytes long, some 55, few 19)
	# TODO: "OLGA" file storage: https://github.com/mikeinspace/stamps/blob/main/OLGA.md https://github.com/CounterpartyXCP/Forum/blob/1e362f7f8668654d0241fe5b1f1c1c330a8b4368/cip-0033.md
	# TODO? Procedural approve/deny/discount/penalize policy scripting?
		# https://github.com/bitcoinknots/bitcoin/issues/61
	# TODO: k119  Draft: Add support for Lua-based TX filtering
		# Classifier scripts; could be set for valid (dangerous), track for fee estimation, relay, mine [decided at mine-time so multiple policies possible?; at a lower priority?], etc
	# Needs concept ACK and review: k107 Retropex/maxfee
	# Needs concept ACK: 29843 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	-     maxscriptsize-29+knots				1b5aa777d6c
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Alternate to(?) #29769
	# Needs concept & impl: Policy: limit script sigops to N (default to MAX_OPS_PER_SCRIPT which is consensus pre-taproot)
	# Needs concept & impl: Policy: limit any witness stack items to N elements (like MAX_STANDARD_P2WSH_STACK_ITEMS)
	# TODO? Ordislow??
	# TODO? Spam filter for stuff like https://mempool.space/tx/4ec38548aa67f6a2efbbc3cf34ab49dc5c275d9701ab0b58696baee9f555c45a
	# TODO: Whitelisting model for non-SPK scripts
	# TODO: -blockpreference=smaller|larger,lessdata|moredata (or match our own policies?)
	# TODO: allow txs from reorg'd-out blocks to bypass policy?
	# TODO: prioritise txs from reorg'd-out blocks?
	# TODO: some way to prioritise Lightning channel activity?
	# TODO? Https://Github.Com/Petertodd/Bitcoin/Commit/04c8e449a34e74e048bf5751d13592a22763ff7e (see email dated 2025-03-19 8:27pm) [bitcoindev] Standard Unstructured Annex
	# TODO? k146 Option to reduce effective fee by dust for each anchor/op_ret
	k148  minrelaymaturity-29.1+knots			7d6a9a79597
	# TODO? k147 Option to factor coin-age priority into vsize
	#30.xTODO# Revert or make optional changes to OP_RETURN policies like #32359,#32381,#32406
		#30.xTODO# Ensure #32790 doesn't break
	# Needs review? 32453 JeremyRubin/unsigned_annex
	-     pol_maxtxlegacysigops-29.1+knots		237c01eb120
		# Made user-configurable and overridable
	-     blockreconstructionextratxnsize		5dd73cb17a3
	k162  qt_bad_external_signer_msg-22			c90ba30538e	last=111c401fc5a bigshiny90/fix-invalid-scriptsigner-errordialog
# Non-upstreamed Knots compatibility:
	#30.xTODO# maybe revert #33214 rpc: require integer verbosity; remove boolean 'verbose'
	#30.xTODO# maybe revert #32721 achow101:remove-deprecated-balances
	#30.xTODO# -     compat_bumpfee_require_replacable
		# 5777b0d6319 RPC/Wallet: bumpfee: Default require_replacable=true if local mempool policy is not full RBF
		# e32b75202da RPC/Wallet: Check deprecatedrpc=require_replacable in bumpfee method, to match previous behaviour
		# 386e285943d (rebase on c79ee09a786 needed)
		# c79ee09a786 RPC/Wallet: Add "require_replacable" option to bumpfee method, to match previous behaviour
		# 1f1259d318d GUI/Wallet: Warn if bumping the fee on a non-BIP125 transaction
	-     compat_rpc_dumptxoutset_hr			0249d74dfe7
		# FIXME: 'type' param attempts to parse as JSON ? (with 28.x bitcoin-cli tho)
		# FIXME: 'rollback' param rejects height ?
	-     compat_jsonrpc_weirdversions			0d0c9e19a6a
	29530 rpc_getpeerinfo_misbehaving_score-29+k	5c911ba2a8e	last=87efb6f0cfd
		# NOTE: Held back 976d61c974e...87efb6f0cfd which degrades docs and adds a test incompatible with Knots
		# Deprecated in Knots 28.1
	-     rpccookieperms_octal_compat-29+knots	835d6d41bc9
	-     zmq_ipc_uri_compat					5d6dadb373d	last=0b1762c90d1 origin-pull/28020/head
		# Backward compatibility with #28020 URI format supported by Knots 25.1+
	#30.xTODO# Check on #29942 removal of -datacarrier, possibly revert?
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-29			1ad630c9cf4
		#30.xTODO# consider deprecating it
		# Effectively reverts #24505, #27869, #28597, and gui#764
		#30.xTODO# revert? #32438 refactor: Removals after bdb removal ... #32440 #32448 #32449 #32452 #32459 #32476 #32481 #32511 #32459 #32523 #32569 #32596 #32618 #32619? #32620? #32758 #32768? #32944? #32977?(might need #33041 to replace it?) #32990? #33032? (replace #33064->#27593??) #33075 #33082? #33161 #33179
		#30.xTODO# revert #28710  Remove the legacy wallet and BDB dependency
		#30.xTODO# revert #31250  wallet: Disable creating and loading legacy wallets
	14641 fundraw_min_conf_deprecated-25+knots	3e7e0decffa	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			9897db72251
	-     netperms_implicit_addr				b4868055e38
	-     rpc_getblockfrompeer_nodeid_compat	42c940800c8
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-29+k		7fdc4b27ae9
		#30.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	-    1day_default_conftarget				1a11eba0790
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	# Disabled just to be safe: -     bloom_default-29+knots				401f2f03e86
		# Take typo fix from def_bloom_local_only
	-     def_bloom_local_only					732cff2b771
		# NOTE: Includes typo fix
	-     wallet_avoid_newerchange				a8243fba8ff
	-     enforce_checkpoints					a2615c7ac93
		#30.xTODO# Revert #31649
	n/a   checkpoint_update-29					dbf12165071
		# TODO: Do https://github.com/bitcoin/bitcoin/pull/31940/files ?
		#30.xTODO# Revert #25725 (Remove mainnet checkpoints)
	# TODO: revert #28354 ?
	10282 softwareexpiry						e0c971059ef
	-     rwconf_policy-29.1+knots				5e98ced6e47
		# Includes Knots policy changes for simplification of final rebase process
		#30.xTODO# Ensure LimitOrphanTxSize sets everything needed still
		#30.xTODO# Check on block assembly GetArgs like blockmintxfee/etc
		#TODO: Add segwit wallet stuff?
		#TODO: Get GUI settings for dustdynamic to select ratio box & focus text area when you click their labels
		#30.xTODO# QTreeWidget or similar for GUI Options dialog?
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	#30.xTODO# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
	# Needs review/options: 26348 -  # Make P2SH redeem script "IF .. PUSH <x> ELSE ... PUSH <y> ENDIF CHECKMULTISIG .. " standard
	# Needs refactoring to only happen for -acceptnonstdtxn(?): 26398 instagibbs/relax_too_small_tx_equality
	# Needs review & optionality: 26451 sdaftuar/2022-11-fixrbf
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		7a98c804c5c
	7483  svg_icon-29.1+knots					4a62c5cbdfa
		# Consider: https://github.com/bitcoinknots/bitcoin/pull/54
# BRANDING:
	# n/a   copyright_2025-28						19e67dd9efa
	n/a   font_ocrbitcoin						b6cfba192f3
	n/a   knots_branding-29						3d8747b0910
		#30.xTODO# Review security policy
		# FIXME: Get NSIS using OCR-Bitcoin
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#30.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#30.xTODO# Ensure #32514 is applied to Knots changes
# TODO: Ensure no #include <config/bitcoin-config.h>
# TODO: Check that we aren't deprecating anything in Core
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
# TODO: Check that no git Author lines are a mix due to GIT_AUTHOR_NAME no longer allowing emails: git log v27.1.. | grep '^Author.*luke-jr' | grep -v Dashjr
	n/a   (cherrypick=6ee0b3ec0fc)				da40d1a238d	# doc/{bips,files}
		# TODO: Update with bump_version below !!!!
	n/a  (bump_version=knots20250903)			72b3991901d
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist		26504f6ba0d
	n/a   (cherrypick=ab2e9ce0575)				59dd80edc0c  # release notes: write/update, including change log and credits
		# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge [gk]?\d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# When re-added, #28824 notes in 9db5d23d559
		# When re-added, #33259 notes in 32695dff9e6
	n/a  (cherrypick=88a83c3f0f5)				271fd206893  # update manpages (build first)
		# WARNING: Need to build as CMAKE_BUILD_TYPE=Release to avoid 'lock' log level being in manpages/config
		#30.xTODO# check all applicable build options are enabled (see also #33085, plus miniupnpc)
		# also example bitcoin.conf and bitcoin-cli bash-completion
	#30.xTODO# n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: Upload to Transifex with * d9411324066 (ts_20220515, origin-pull-g/599/head) GUI: Support translating Bitcoin units
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @30.x-knots-android
	# 32262 hebasto/250413-android

@30.x-knots-extratests
	31367 dergoegge/2024-11-ci-ulimit-s
	31410 hebasto/241203-multiwallet
	33180 fanquake/asan_strict_string
