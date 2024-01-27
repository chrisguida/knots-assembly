timestamp 2024-01-23 04:33:34
lastapply no-merge

#.. checked up to PR #29292 / gui #790

checkout v26.0
@26.x-syslibs
# BUILD BUGS:
	# Needs review: 23609 hebasto/211126-reduce
	5872 subdir_incl_compat						0d2f1ba753f
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb							0a46aec36d8
	5416  sys_libsecp256k1						38be3bf3130
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	#26.xTODO: sys_libminisketch
	13789 bugfix_asm_pragmas					52874632dc1
		# Should revert #28893 if merged?
	15155 test_external_bcli					0f88ee0361c
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
@26.x-knotsfixes
# TESTS:
	# As needed: -     lint_relaxer							3f26eac129a
	#26.xTODO# -     ci_knots-25							998864d46e0
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
# FIXES:
	18818 guix_reltar_autogen_distclean			97b04fc017d	last=b5a164d9155 fix_gitian_src_202004
	18902 fix_gitdir_again						148d95ab845
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini					92b38619a9c	last=df5ece3e064 2020mingwthrd
	18490 bugfix_symcheck_pe_case				cb2d1032bd6
	# Maybe disabled by default? 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
	14968 http_bind_error						5c0444cd6df	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					9478c8709f5
		# NOTE: libevent-copied code up to date as of 2023-11-22 cfb2b89a1d0642abd6389913e237f49c662502e4
	 9524  rpc_pruneblkchain0					243a7d11f38	last=88883ae13d
	10731 log_more_uacomment					0b1f4bfaaa1
	14485 fadvise								8abba8c0517
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					810661711ac
	-     bugfix_rpc_getbalance_hacky			bee27b18423
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
	18194 bugfix_gui_edit_sendaddr-mini			263a7cd77aa	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	g658  intro_dont_change_user_prune			f9e06a728f7
		# Was #18729
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				2d50755582e	last=3f9cc0cd736 Saibato/wallet_351
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
	g152  gui_notify_setup_bg					1adb83ceb29
	-     bugfix_gui_drop_abc_confusing_hack	525b79ab2d7
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	# Needs review: 21161 ajtowns/202102-fee-bug-medianval
	g236  gui_init_walleterror_cont				113874f08b0
	-     rpc_addconnection_mainnet				7177d5ded16
	# Needs review: 22307 rebroad/DetectIngoredGetblocktxns
	22417 bpchild_closefds						743e8ea6e45
		# NOTE: Need #ifdef BOOST_POSIX_API around includes because Win64 headers are b0rked
		# NOTE: Currently uses ENABLE_EXTERNAL_SIGNER in place of USE_BOOST_PROCESS (not defined until #15421 merged)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				920a112ed39
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs careful review: 23169 -  # Initialize all members in FastRandomContext
	# Needs work: 23502 achow101/tr-low-fee-est
		# "rebase" in #26573 for post-#26567 refactor
	# Needs work: 23534 achow101/no-change-fee-w-sffo
	g506  qt_qrcode_sizefixes					d7f460d3617
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	# Needs review: 24066 whitslack/openrc-daemonwait
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	# Needs work: 24313 Sjors/2022/02/displayaddress						last=803387f054d
		# TODO: make sure this doesn't break compatibility (and fix review bugs)
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				be695233a1c
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-25+knots			4fb1641b022	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	# Needs review: 24972 hebasto/220425-no-libtool
	# Needs review: 24994 hebasto/220426-consensus
	g595  qt_handle_autostart_errors-0.15		2139b932588	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	g599  ts_20220515-partial-25				ddf8efb915b	last=d9411324066 ts_20220515
		# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
		#26.xTODO# Update with other commits that are beneficial
	-     boost_171_177_workarounds				ed3f6565587
		# NOTE: Originally part of #25111 hww_windows replaced by #25696 (merged)
	# TODO: 25136 -  # Checks -torcontrol for a valid host:port string
	# Not clear this fixes anything: 25273 achow101/use-preset-tx-things
		#+29065+29272
	# Needs review: 25380 darosior/fee_estimator_disable_cpfp
	#26.xTODO# Check on #25561
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	# Needs review: 25698 -  # crypto: avoid potential buffer overread in ChaCha20::SetKey
	g633  -										96059d17bbc	last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	# Needs review: 25938 mzumsande/202208_fixed_cjdns
	g662  qt_fix_txview_202209					2f064e8f664
		# Includes gui#368
	#26.xTODO# Needs review: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	#26.xTODO# Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	# TODO: Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	#26.xTODO# Sane fix for #24049
	g677 fix_qt_peers_na						8ae7771bb00
	# Needs work/review: 26426 fjahr/202210-coinstatsindex-overflow
	#26.xTODO# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs review: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-25+knots	7385341a1a5	last=a6f567590b7
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	#26.xTODO# Needs review? 26762 hebasto/221228-queue  # Make CCheckQueue RAII-styled
	#26.xTODO# Needs review: 26903 pstratem/2023-01-17-baseindex-commit-error
	#26.xTODO# Needs triage & review: 26950 fanquake:check_for_SecureZeroMemory
	#26.xTODO# Needs bugfix? (https://github.com/bitcoin/bitcoin/pull/27039/files#r1247267535) 27039 pinheadmz/reindex-read-only
	#26.xTODO# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	# Triage/Needs review 27295 brunoerg/2023-03-improv-deserialize-v2
	# Needs review: 27307 -  # wallet: track mempool conflicts with wallet transactions
	#26.xTODO# Alternative to: 27434 pinheadmz/chaintips-invalid
	# TODO: Needs work? g722 -  # Wallet : Allow user to navigate options while encrypting at creation
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	# Needs concept/review: 28016 -  # p2p: gives seednode priority over dnsseed if both are provided
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#26.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	-     acceptstalefeeestimates_mainnet_opt
	#26.xTODO# Needs review: 27684 hebasto/230516-punish OR ???
	#26.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 -										1826b4ef7cf	last=bfc2bb6a270  # forbid_nohelp-0.19
	27815 -										83731380072	last=244e6c8db81  # cli_forbid_multihelper-22
	# Needs review: 27820 -  # Sanitizing ports of -rpcconnect and -rpcport.
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	#26.xTODO# Needs review: 27912 -  # net: run disconnect in I2P thread
	# Needs review: 27969 -  # bumpfee: ignore WALLET_INCREMENTAL_RELAY_FEE when user specifies fee_rate
	# Needs work: 27973 maflcko/2306-byte-span-
	# Needs work: 27991 fanquake/instrument_libsecp
	28020 -										c9467913acb	last=0b1762c90d1  # exclude ipc scheme from port check (fix_zmq_ipc_noportcheck-25)
		#26.xTODO# Maybe rewrite without `rfind`
		# NOTE: #27679 also implements this, possibly with unix: prefix instead?
	# If needed: 28026 furszy/2023_fix_index_timeout
	#26.xTODO# Needs review: g742 john-moffett-g/2023_06_ExitOnLooseArgument
		# NOTE: Explicitly mentions BIP 21 (we support BIP 20)
	28029 fix_zmq_errhandling_202307-mini		f7f772f2d5f	last=07086589b27 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err		2ea81f12689
	# Not a fix: 28076 no_std_fs_directly-25+k							last=7777034e96a maflcko/2307-fs-lint-
		# Fix-only, diff-minimised
		# "I don't think anything here is a bug fix" -maflcko, https://github.com/bitcoin/bitcoin/pull/28076#issuecomment-1682450942
	#26.xTODO# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Needs concept: 28205 theStack/202308-netprocessing-reallow_fetching_of_genesis_block
	#26.xTODO# 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	#26.xTODO# Triage #28248
	#26.xTODO# FIXME: curl RPCdoc examples use wrong content type!
	#26.xTODO# Needs review (wallet compat?) 28307 furszy/2023_invalid_segwit_redeem_script_limit
	28345 fix_bytespersigop_checks-mini			1f3ef9a348b	last=78a256505f3 fix_bytespersigop_checks
		#26.xTODO# NOTE: Excludes removal of buggy wrapper for diff-minimisation; needs checking manually (to ensure wrapper doesn't get used even in final/complete merge of all PRs) when assembly done
	# Needs review? 28340 -  # security: restrict abis in bitcoind.service
	# Needs review & diff-minimising: 28366 -  # Fix waste calculation in SelectionResult
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	g752  fix_qt_cmdhelp_mention_uri-0.17		432f807d824	last=07bb7068cf9
		# NOTE: Rewrote to be simpler and avoid BIP21 mention (Knots supports BIP20 too)
	28486 fix_test_winsock_init-26
	#26.xTODO# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	#26.xTODO# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# Needs review: 28546 ryanofsky/pr/mig  # bugfix: watchonly wallets created after migration have incorrect height values
	28554 fix_rpc_getnetworkhashps_heightchk-25	9e1549c2ad7	last=9ac114e5cd9
		# diff-minimised & kept compatible
	g758  -										b42b1dab09d	last=9d37886a3b6  # qt_nodewindow_chainname-22
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	# Needs review: 28564 fix_conf_fuzzbin_main
	# Needs review? 28610 achow101/migrate-avoidreuse
	#26.xTODO# Needs review and relevance: 28616 Sjors/2023/10/assume-unconfirmed
	# Needs review/simplification: 28649 vasild/reliable_socks5_handshake
	# Needs review & triage: 28678 sipa/202310_miniscript_assume
	# Needs review: 28724 achow101/cleanup-accidental-watchonly-mkeys
	# Needs review/diff-minimising? 28737 -  # doc: Fix bugprone-lambda-function-name errors
	g773 fix_qt_unlock_watchonly-0.20			887878b37ac	last=517c7f9cba3 achow101-g/gui-skip-encryption-check-for-watchonly
	# Not worth it? 28771 achow101/lcov-opts
	# Not worth it? 28774 vasild/avoid_returning_reference_to_mutex_guarded_member
	# Needs review: 28776 BrandonOdiwuor/gui_overview_page_add_used_balance
	# -- Needs review: g775 -  # gui: add used balance to overview page
	# Needs review: 28780 -  # log: torcontrol opt checks
	# Needs review: 28782 -  # test: Add missing sync on send_version in peer_connect
	28784 fix_keep_notmy_cookie-26+knots		2362f3c6d63	last=7cb9367157e
		# Reverted regression from d95dde9441f...7cb9367157e
	28791 fix_assumeutxo_pr28791-26
	# Meh? 28822 -  # test: Add missing wait for version to be sent in add_outbound_p2p_connection
	# Needs review: 28824 fix_asm_nodecimals-23								last=fde11cb0fa3 willcl-ark/asm-full-hex
		# FIXME: disambiguate opcodes too?
	# Needs review: 28834 -  # net: Attempts to connect to all resolved addresses on addnode
	# Needs review & triage: 28846 fanquake/fixup_multiprocess_arm64
	# Needs review & triage: 28848 instagibbs/2023-11-submitpackage-results
	28849 fix_qa_v2t_pr28849-26
	# Needs review: 28868 achow101/test-migration-watchonly-spendable
	-     fix_doc_upnp_def_post26896			c5c82e96e5e	last=92f88a96290 fanquake/redundant_upnp_ifdef
		# Alternative to #28874
	# Needs triage & review: 28885 -  # refactor: followup to getprioritisedtransactions and delete a mapDeltas entry when delta==0
	# Needs review & triage: 28894 furszy/2023_wallet_batch_keypool_creation
	28920 fix_wallet_def_birthtime-26						last=b06b14e68d8 !fanquake/26_1_backports^^^
		# Diff-minimised by dropping leading refactor commit (and rebasing around it)
	28936 dnsseed_petertoddnet-25
	28944 sendall_antifeesniping-25							last=ed5cc12474a ishaanam/sendall_anti_fee_sniping
	28946 fix_keep_notmy_pidfile-26+knots
	# FIXME: real fix for issues in #28967 (OR #28981?) -- NOT A REAL BUG IN PRACTICE
	# Needs review (very minor fix): 28976 achow101/migrate-blank
	# Needs review: 28979 ishaanam/sendall_ancestor_aware_funding
	28994 fix_wallet_sffo_skip_bnb-26
		# Diff-minimised
	# Needs review? 28998 0xB10C/2023-12-addpeeraddress-return-error
	29003 fix_rpc_getrawtx_v3_unconf-26
	29022 fix_btx_replacable_blank-21
	# Needs review: 29027 brunoerg/2023-12-descriptor-fix-key-error
	# MSVC: 29044 hebasto/231209-msvc-qt
	g780  fix_qt_txview_prG780-25							last=b2e531e70a8
	29141 fix_rpcauth_blank
	#26.xTODO# Needs review: 29112 achow101/sqlite-concurrent-writes
	# Needs review: achow101/fix-double-keypath
	29127 mac_hardened_runtime-22
	# Needs work (drop goto): 29143 -  # wallet: add meaningful error message and fix test
	# Needs work? 29144 fix_init_empty_settingsjson-23					last=725a1fc7a7d furszy/2023_empty_settings_file
	29145 dnsseed_dashjr_2024
		#26.xTODO# Decide about changing to another domain
	29147 guix_attachable_sigs
	# Needs review: 29155 -  # wallet: move lock at the top of ReleaseWallet
	29184 rpc_scanblocks_ffp_named
	29175 fix_rpc_estmode_unset_case-24						last=be8ae64b82e
	29176 fix_wallet_EraseRecords_uaf-25
	29177 fix_conf_latomic_check-25
	# Triage: 29192 sipa/202401_serfloat_weaken_test
	29195 fix_clang_extwarns_pr29195-24
	#26.xTODO# https://github.com/bitcoin-core/crc32c-subtree/pull/6
	29237 fix_depends_PATH_w_spaces-26			4b1f2043949
	(CHECK-LAST)	last=92f7e7f3633 maaku/allow-spaces-in-path
		# Was: 28733 fix_depends_PATH_w_spaces-22
	29243 fix_wallet_cleanup_handler_pr29243-23
	29249 depends_gen_id_nm-25
	# Needs review: 29253 furszy/2024_wallet_db_dangling_txn
	29262 fix_rpc_loadtxoutset_race-26
	# Triage part of: 29275 maflcko/2401-prev-it-
	#26.xTODO# Needs review: 29284 sipa/202401_better_block_tiebreak
	# Needs review: g786  -  # FIX:When opening or autoloading wallets there should be clear messages about rescanning in progress and wallets' names.
	g788  qt_peers_sessionid_tooltip_prg788-26				last=3bf00e13609  # debugwindow: update session ID tooltip
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	#26.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)		407a2d32ac7
#@26.x-knots-lts-deps
	28769 depends_qt_update-26
	#26.xTODO# FIXME -     depends_qt5kde
	# Needs review & relevance: 28627 fanquake/zeromq_4_3_5
@26.x-knots
# PERFORMANCE:
	n/a   rm_minisketch-26+k					56c089e915d
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
	26375 zmq_optimise_duplread-26+k			76ce07a3470	last=7b631dc9b19 andrewtoth/no-read-zmq
	#26.xTODO# Needs review: 26415 andrewtoth/read-raw-block
	# Needs review: 26486 sipa/202211_batchnotfound
	# Opt-in & needs review: 26951 pstratem/2023-01-23-gcsfilter
	# Needs review: 26966 furszy/2022_parallelize_blockfilter_index_2
	# Needs review: 27006 furszy/2022_reduce_cs_main_scope_blockindex_nfile
	# Needs concept/review: 27050 -  # p2p, validation: Don't download witnesses for assumed-valid blocks when running in prune mode
	# Needs review: 27427 -  # validation: Replace MinBIP9WarningHeight with MinBIP9WarningStartTime
	# Needs review? Part of? 28226 martinus:2023-08-more-CBufferedFile
	# Needs review? 28233 andrewtoth/sync-on-periodic
	# Needs review: 28280 andrewtoth/sync-dirty
	-     dbcache_1TB-0.13						340c00784b6
		# Inspired by #28358 Sjors/2023/08/double-your-coins---cache (needs work)
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 -										b48610240c4	last=42b25bbd939  # opti_merkle_mutation-0.17
	28592 -										8de082c7735 last=80489ba6e84  # txrelayrate_14txps-21
		#26.xTODO# Make configurable? Or is that even sane?
	# Needs fixing rebase: 28799 wallet_cache_descriptor_id-25
	# Needs review: 28923 theStack/202311-add_SignTransaction_benchmark
	# Needs review: 28945 martinus/2023-11-improve-ccoinsviewcache-reallocatecache
	# Needs review: 28955 furszy/2023_index_blockfilter_cache_header
	# Needs review: 28987 furszy/2023_wallet_zaptx
	# MSVC: Needs review: 29036 theuni/msvc_fast_byteswap
	# Needs backport: 29114 -  # util: Faster std::byte (pre)vector (un)serialize
	# Needs review?? 29159 -  # Update net.h bigger TCP socket using larger buffer
	# Too big a diff: 29169 fanquake/libsecp256k1_0_4_1
	# Not worth it (kernel only): 29180 theuni/kernel-sha2-optims
	29200 i2p_ecies_x25519-25
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
	18479 rpc_sign_show_fees					7e29fa92470	last=47b2ba29df2 !origin-pull/12911/head
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
	15836 fee_histogram+pr15836_api				bb7f00d012b	last=b94292a7cb jonasschnelli/2019/04/feeinfo
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
	22693 getaddressinfo_txids-26+k				21208b9b577	last=03e8a66fc44 getaddressinfo_txids
		# NOTE: cd4e5ddaf7f...03e8a66fc44 simply squashes bugfix into 1st commit
	g562  wallet_warn_reuse_gui					937e84ba2fe
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				68df3d26ed1	last=ff459b5b55f neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		15cacac70c7
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-26+knots		bb93ccc5895	last=409c2e34522 elichai/2020-01-siphash
	(CHECK-LAST)	last=5622dd16ecf siphash_optimise_pr18014-26
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work/review/completion: 18242 jonasschnelli/2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr					353c03f4292	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								877baf1c3e7
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							ef6280f864f
	# Needs review: 18000 -  # Coin Statistics Index
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	# Needs review: 19860 -  # Improve diversification of new connections: privacy and stability
	19873 mempressure							8c38e853e2a
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			1a35df9bec6	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-26						6753f320098	last=1002e2d0d7f jonatack/setfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
		# TODO? Reduce internal changes and move to Knots compat??
	20407 rpcauthfile-26+knots					e7f3fe121b0	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	g149  intro_assumevalid						bf059f29d0c	last=cf940f0e5f5
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					c30afe9296d	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	20827 ibd_prune_max							da734954970
	g363  qt_peers_directionarrow-25+knots		e1bf459e203	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						a5a53e37248	last=1af20831806 Sjors/2021/05/hww-toggle
	# TODO: 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21319 getblock_optimise						e788404b696
		# Context: 17529 rpc: Faster getblock using PureBlock
	# Needs review/optional? 21224 ariard:2021-02-halt-processing-unrequested
	21260 rpcwallet_tx_in_mempool-26+knots		922505dfe54	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					d42a7ed5b4a
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						c433f09baba	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex							93ade4c20b7	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	22159 conf_append_cxxflags-23				6b03c7c157e	last=fa14c6818f4
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt				985de2209d0	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Too many TODOs: 22341 Sjors/2021/06/getxpub
		# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							bfa6e78d5ba
	24963 rpc_walletprocesspsbt_options-26		754b7e7a923	last=f43f992b731 rpc_walletprocesspsbt_options
		# Diff-minimised (and uses merge for rpcarg_type_per_name)
	-     rpc_descriptorprocesspsbt_opts-26+k
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
	23362 importfromcoldcard					d3edfcd2e9d	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates					b68bf580f9b	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06 (FlushFeeEstimates lock on m_cs_fee_estimator)
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			9237836df90	last=ad431ff5d18
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip					1a3ac2a6753	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	g497  qt_fontsel-25+knots					e2f6acb69ec	last=a17fd33edd1 qt_fontsel
	-     qt_fontsel_qrcodes-25+knots			3abe9b4fd63	 # latest code now
	# TODO: qt_fontsel_console
	# Needs work? g505  -  # RPCConsole: add hidePeersDetail() button and functionality
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	# Needs review & BIP changes: 24058 kallewoof/202201-bip322
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-26			3fc3c2c3516	last=97a69e232be
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
	25183 rpc_fundraw_segwitonly				56cc6aaef2a	last=9e7fd5c0fe3
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
	g626 qt_node_localaddrs-25					ba5db54361f	last=c47f01bf25e
	# Needs completion & review: 25718 fjahr/2022-07-allowinbound
	# Needs concept/review: 25747 w0xlt/desc_file
	# Needs work: 25776 1440000bytes/bumpfee-inputs
	# Needs concept/review: 25907 achow101/upgrade-to-tr-2
	# Needs work: 25923 jonatack/2022-08-statestats
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	# Needs review (or leave external?): 26052 -  # contrib: Add script to colorize logs
	-     guix_shell_compat-24					e425aec3426
		# More compatible alternative to #26077 fanquake/guix_shell_over_environment
	28167 rpccookieperms-26+knots				9213782194f	last=68a4a988e98 willcl-ark/2023-07-rpccookie-perms
		# Was #26088 (not in a Knots release)
		# Added lots of improvements
	# Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	#26.xTODO# Minimised: 26162 Sjors/2022/09/taproot
	#26.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	#26.xTODO# Needs review: 26174 w0xlt/list_address_book
	27114 whitelist_outgoing-mini-26+knots		024d8fc86d6	last=1d0216ed322
		# Held back 72013c25ada...6175a2ee096 for convenience (identical final states)
		# Held back 6175a2ee096...1d0216ed322 for being stupid (limit whitelisting to manual outbound peers)
		# NOTE: Originally #10594, then #17167
		# Left off test framework refactoring commit (caf5ff0c5a8) and reverted gArgs caching refactor (ab6c001ec96)
		# Also includes change of default from incoming to in+out
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme	e3f13ae6a73	last=d8434da3c14
	# Needs option/work: 26454 petertodd/2022-feebump-without-optin
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 brunoerg/2022-11-disconnectnode-subnet^	cb46f10006e	last=23f4c2cb452
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs review: 26839 -  # Add support for RNDR/RNDRRS for AArch64 on Linux
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	26990 bcli_validation-24					def292e8c7b	last=fa48d460334
		# Didn't bother rebasing for 755320f75f2...fa48d460334 trivial changes
	27034 rpc_importaddr_for_descwallet-26+k	05bd5f2f99b	last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
		# Diff-minimised & tweaked to avoid breaking #23362
	# Needs review: 27052 LarryRuane/2023-02-getpeerinfo (maybe GUI port too?)
	# Needs review & API breakage considerations: 27101 pinheadmz/jsonrpc-2.0
	27216 rpc_getaddressinfo_isactive			c951b6947f2	last=85f83339dda pinheadmz/used-addr-ui
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-26+knots						d3f7295b1a7	last=91771366a3d apoelstra/2023-03--codex32
		# Diff-minimised, doc bug fixed & tweaked to avoid breaking #23362
	# Needs review: 27375 pinheadmz/tor-unix-domain-socket
	# Needs review? 27679 pinheadmz/zmq-unix-domain-socket
		# Duplicates #28020 with a different URI format
	# Needs work: 27409 ryanofsky/pr/1data
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	#26.xTODO# Self-review: 27509 vasild/relay_tx_to_priv_nets
	27600 p2p_forceinbound-26+knots				431468d6648	last=8c2026848da pinheadmz/whitebind-evict
		# Reverted forceinbound limit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27770 rpc_getblockfileinfo-26+knots			c92323afe5a	last=5090771f326 furszy/2023_rpc_getblockfileinfo
	# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
	# Needs review & BIP finality & might have wallet changes: 28202 josibake/implement-bip352-receiving
		# Note alternative (approach NACK'd) in #28453
	# Needs review & BIP finality: 27827 josibake/silent-payments-base-pr-slim-down
	# Needs review & concept: 28241 Sjors/2023/08/silent-index
	# Needs work & maybe removing an anti-feature?: 27836 furszy/2023_rpc_fetchblock_improvements
	# Needs review: 27837 furszy/2023_introduce_block_request_tracker
	# Needs work: 27854 -  # [WIP] add a stratum v2 template provider
		# OR #28983
	# Needs review & compat checking: 27859 -  # Mempool: persist mempoolminfee accross restarts
	# Needs review: Ensure fully optional (opt-in?): 27877 -  # wallet: Add CoinGrinder coin selection algorithm
	#26.xTODO# Make disabled by default: 28052 maflcko/2306-fs_stuff-
	# Needs review? 28207 maflcko/2308-xor-memepool-
	# Needs review: g753 -  # Add new "address type" column to the "receiving tab" address book page
	#26.xTODO# hebasto-g/230911-bip324-peer-details
	# Needs review: 28461 fanquake/windows_ssp_roundup
	# Needs review and concept: 28463 mzumsande/202308_increase_block_relay
		# Why not just increase inbound capacity to max anyway?
	# Needs concept/review? 28806 ajtowns/202311-depinfo-scriptflags
	# Needs work: g777 -  # gui: getrawtransaction implementation
	# Needs concept/review: 28926 willcl-ark/2023-07-getnetmsgstats
		# Was #27534 -  # rpc: add 'getnetmsgstats', new rpc to view network message statistics
	# Needs concept/review: 28930 -  # wallet: Add scan_utxo option to getbalances RPC
	# Needs review: 28950 instagibbs/2023-11-submitpackage-max-fee-burn
	# Needs review and/or optionality: 28977 murchandamus/2023-11-gutter-guard-selector
	29016 rpc_listmempooltxs-26+knots						last=07008477b81 niftynei/nifty/listmempoolentry
	# Needs review? 29054 achow101/descriptor-sethdseed
	#26.xTODO# 29058 mzumsande/202312_manual_bip324
		# +#29212 bugfix
	29117 wallettool_dump_just_db-26+knots					last=d83bea42d1f achow101/dump-without-making-wallet
		# Omitted first commit that could be dangerous
	#26.xTODO# Needs concept + review: 29129 brunoerg/2023-12-externalsigner-account-parameter
	# Needs review or minimal impact: 29130 achow101/createwalletdescriptor-without-new-records
	# Needs review or minimal impact: 29136 achow101/sethdseed-void-descriptor
	29163 rpc_help_detail-22								last=c6b68c29707 LarryRuane/2024-01-help-detailed
		# Left off top commit changing rpc_help test behaviour
	29227 mempool_load_log_progress-24
	29239 sipa/202401_default_addnode_bip324
	Needs concept & review: 29264 instagibbs/2024-01-max-tx-weight
	Needs concept & review: 29278 -  # RPC: Wallet: Add maxfeerate and maxburnamount startup option
	
	# TODO: GUI block template view
	# TODO: Build next-block template from mempool + N MB txs (to replace empty blocks for local miner)
# Non-progress functionality:
	8751  sort-multisigs-26+knots				426c7c11321	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					165e1fb17df	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys							3496e755b78
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245 ionice									7f38312c696
	-    ionice_win								8f3ad020ec5
	8501  old_stats_rpc-26						68a8c2448c0	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-26+knots					f6b1eae17b3	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9504  rpc_dumpmasterprivkey					19bad943fb4	last=07fc81109a
	g444  gui_netwatch-26+knots					88124b8f99f	 # Latest code now
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-26+knots				f6d2ab6df60  # latest code now
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet to wallet-restricted users for now
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
		#26.xTODO# Add dc244382e5d QA: rpc_users: Test rpcauth wallet restrictions
	10554 zmq_wtx-26+knots						e2c665fd588	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
		# Extended doc/zmq a bit to match additions from #14060 and #23471
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	20551 rpc_onetry_conntype					08c473e6264
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment				77906ca1d59
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
	10350 filtered_witblock-25				18dcc385a7e	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				a9b32a89ff8	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								f6dadf8de3a	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			53f47aa30a3
	12965 scriptthreads-26+knots				399b678256e	last=dfab6c6866 jonasschnelli/2018/04/svt
	13203 dsha256_power8-25						bbf85ccc673	last=3b402e0738 TheBlueMatt/2018-05-asm
		# NOTE: Stripped out benchmark change
		#26.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	-     dsha256_power8_asm_pragmas-25			43028d98ec0
	15218 -										6e1ffe36dc9	last=0c7ee166463  # postibd_flush-25
	15428 tor_gui_pairing-26+knots				e3afcc98d21	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-26+knots				e4bc1dba681	# Latest code now
	# TODO: tor guix bundle!
	# TODO: 16490 maflcko/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support Knots policies
	17795 gui_console_ctrl_d-26+knots			3aa167a262c
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					0e50a093ee5
	n/a   rpc_compat_error_index-25+knots		5538e18b331
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos-26+knots			04919d68d86 last=539beeaae85 gui_bech32_errpos
	17636 guisettings-0.21						bbdf707df8d	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					e0c7bb7f391	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						c5aecd96fcb	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances				4ddff9c4717	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance			b8660118ea7	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	19117 rpc_getrpcwhitelist					d1443f02830
		# NOTE: Was #18827 before any Knots merge
		#26.xTODO# Extend dc244382e5d test
	-     getrpcwhitelist_wallets-26+knots		6b83f6e1864
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-26+knots		a1222a50e99
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	#26.xTODO# Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
# Non-upstreamed functionality:
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	n/a   restore_feefilter_opt					5919d15479a
	-     gui_payreq_textedit					05e5f19a79d
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				0a1184aeef3
	-     walletnotify_w_win-26+knots			a65f55575ca	# Latest code now
	14137 win_taskbar_progress-26+knots		7d894071ff8	last=18eb4dbb8a
	-     restore_blockmaxsize					be451f1b478
	7107  qtnetworkport-26+knots				9c7dec6c224	last=1f37c87d8f2 origin-pull/7107/head
	7533  sendraw_force-26+knots				e2a858f12ef last=2627c0937f8 sendraw_force
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532,#29060 if merged
	11082 rwconf-25+knots						0e725308ae7 # Latest code now
	7510  rwconf_gui-25+knots					8547325ff36
	559   accept_nonstdtxn-25+knots				f84d8616fa1
	 929 tbc									10d83963b58
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
	 553 bugfix_qt_uri_amount_parser			1e5df93d93b
	-    mining_priority						b48599f6d5f  # NOTE: now the latest code, rebased
		#26.xTODO# FIXME: Lots of lock warnings from clang! (did I already fix these?)
	5861 gui_restore_addresses					643e6f6ba1e
	5891  qt_console_history_persist			bcdfddecdb9	last=0cd5fc301d6 qt_console_history_persist
	7219  rbf_opts-25+knots						ef5614bee75	# Latest code now
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					72915ef061e
		# TODO: Split out legacy address preference to be more explicit
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname-0.19			5b622bc241a	# Latest code now
	-     gui_request_payment_label-0.19		3ecfd96bca0
	-     gui_peers_sort_network-23				38c6a5a42ce
	-     gui_peers_no_net_column				3f7ad7f8ca5
	22439 guix_in_gitian-23+knots				805b56d6c9c	last=ebda0463748 achow101/guix-in-gitian
	-     rpc_getblockfrompeer_future			1b389b71477
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		cfce0703d0c
		# Prior Knots bundled this in with #20295
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
	#26.xTODO# Needs concept acceptance: -     gbt_skip_validity_test
	# Needs concept & writing: default UPnP/NAT-PMP to enabled
		# NOTE: Need to revert #28874 conditionals
	#26.xTODO# Look into making the patches tarball in guix
# Non-upstreamed Knots compatibility:
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-25			790a86f1ce2
		# Effectively reverts #24505
		#26.xTODO# revert? #27869  wallet: Give deprecation warning when loading a legacy wallet
		#26.xTODO# revert? #28597  wallet: No BDB creation, unless -deprecatedrpc=create_bdb
		#26.xTODO# revert? gui#764  Remove legacy wallet creation
		#26.xTODO# revert #28710  Remove the legacy wallet and BDB dependency
	14641 fundraw_min_conf_deprecated-25+knots	9b6d7ab7821	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			7cfe7d551eb
	-     netperms_implicit_addr				36690d788bb
	12674 rpc_onetry_nonpriv-25+knots			ecaf5bf309f
	-     rpc_getblockfrompeer_nodeid_compat	55b3579eb4c
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-25+k		793aa1d84db
		#26.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				2c1b1d3e046
	-     bytespersigopstrict-25+knots			2de1a1eb574
	9749  unique_spk_mempool-25+knots			f5263caec05
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	28408 match_more_datacarrier-25+knots		699f8a809eb	last=abd19ad480f match_more_datacarrier
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
		# Revise byte counting to consider input/output waste
		TODO: Check docs for accuracy; REVERT AT LEAST PART OF #27832 (eg #29173)
	#26.xTODO# Filter for output value < tx fee * N - https://twitter.com/DoctorBuzz1/status/1741622696327205176
	#26.xTODO# Impose accurately-calculated (not just guessing witness size) dust limit on Taproot _spends_ (only Taproot because there should be a more sensible spend path available in theory)
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     datacarriercost-25+knots				06ff2c34e3b
		#26.xTODO# Add tests and make sure boundaries are correct
	TODO: bare p2pk filter
	TODO: filter runes?? https://rodarmor.com/blog/runes/ https://github.com/ordinals-wallet/rune/blob/main/src/rune.rs
	TODO: filter HG: https://pbs.twimg.com/media/GDV-H8UWkAAsckl?format=jpg&name=large
	TODO: CBRC-20 https://twitter.com/bitoordileone/status/1734654996539457666
	TODO: Discount privacy txs?
	TODO: Whitelist Whirlpool Tx0 and/or BIP47?
	TODO: Procedural approve/deny/discount/penalize policy scripting?
	# Needs concept ACK: 28334 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	-     bloom_default-0.21+knots				edc9ff33c65
	-     wallet_avoid_newerchange				bacea8923d4
	#26.xTODO# Revert #25725
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	-     maxscriptsize-25+knots				98c0265003e
	#26.xTODO# Needs concept & impl: Policy: limit script sigops to N (default to MAX_OPS_PER_SCRIPT which is consensus pre-taproot)
	#26.xTODO# Needs concept & impl: Policy: limit any witness stack items to N elements (like MAX_STANDARD_P2WSH_STACK_ITEMS)
	#26.xTODO# Ordisrespector equivalent (Ordislow??)
	#26.xTODO# Adaptive dust limit based on current fee rate?
	#26.xTODO# Spam filter for stuff like https://mempool.space/tx/4ec38548aa67f6a2efbbc3cf34ab49dc5c275d9701ab0b58696baee9f555c45a
	#26.xTODO# Whitelisting model for non-SPK scripts
	#26.xTODO# Exemptions for Samourai: https://code.samourai.io/whirlpool/Whirlpool/-/blob/whirlpool/ARCHITECTURE.md#2-create-tx0
	#26.xTODO# -blockpreference=smaller|larger,lessdata|moredata (or match our own policies?)
	-     enforce_checkpoints					271ea89d048
	n/a   checkpoint_update-25					ecdd83d1986	#26.xTODO# last=70996dfdd9b checkpoint_update-0.21
		#26.xTODO# Add new checkpoint
	10282 timebomb_knots						e3778785186
		FIXME: <cstdint> in clientversion.h
	-     rwconf_policy-25+knots				e3ba2d1e080
		FIXME: full rbf not default??
		# Includes Knots policy changes for simplification of final rebase process
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
		#26.xTODO# fix corepolicy default in --help to be 0 instead of 'false'
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
	n/a   (delete_release_notes_fragments)		3f1e47e06ff
	TODO: revert macos ZIP only? #28432 #28932 #28973
		NOTE: reverting temporarily reintroduces .tiff file
	-     fix_dmg_openfinder-24					83c590fab1b
		TODO: Merge into above revert?
	7483  svg_icon-25+knots						bbb36b36a96
		Consider: https://github.com/bitcoinknots/bitcoin/pull/54
		FIXME: Make configure error if source doesn't have rendered icon and can't generate
	n/a   tbc_font								cc499335148
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/
# BRANDING:
	n/a   knots_branding-25						0cb94913043
		#26.xTODO# Review security policy
		TODO: bump copyright year? #29222
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#26.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#26.xTODO# Check macOS zip impact on tuffy font etc
# TODO: Check that we aren't deprecating anything in Core
# TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Check #26039 doesn't break anything
# TODO: Ensure std::filesystem isn't introduced (see #28076)
#26.xTODO# Ensure options arguments use new OBJ_NAMED_PARAMS type: git grep '"options.*OBJ,'
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
#26.xTODO# git grep noban_tx_relay (needs #27114)
	n/a  (cherrypick=ee7ef94595a7793b6e)		ab6d532443f	# doc/{bips,files}
	n/a  (bump_version=Knots:20240103)			decc35f238b
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist		85dde742552
	n/a   (cherrypick=b5582b97bbf)				5961e01c91d  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# When re-added, #28824 notes in 9db5d23d559
	n/a  (cherrypick=ecb1be05c43)				aed49ce8989  # update manpages (build first)
		# also example bitcoin.conf
	#26.xTODO# n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @26.x-knots-android

@26.x-knots-extratests
	28805 qa_v2t_pr28805-26
	29179 glozow/2024-01-test-reorg-rescan

