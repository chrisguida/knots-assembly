timestamp 2020-08-15 06:18:02
#lastapply no-merge

#.. checked up to PR #19728 / gui #61

checkout bf0dc356ac4
@0.20.x-syslibs
TM	19097 bugfix_incl_qpainterpath-0.9			0521218641a
	5872 subdir_incl_compat						500e007903f
	2241 sys_leveldb							1417948c866
	5416 sys_libsecp256k1						c5a440728e9
	7485 sys_univalue_def						b9b4cf77ff4
	13789 bugfix_asm_pragmas-0.20				369a7f5afa3	last=14337d0d80b bugfix_asm_pragmas
	-     bugfix_asm_leveldb_check				02dc65eba04
	15155 test_external_bcli					9de9dca3491
	16564 -										7e9fe94ce00	last=9a19c9ada5  # Always define the raii_event_tests test suite
	# TODO: Check build with -fno-common
	19403 bugfix_conf_builtin_clzl-0.18			192a1904a55
@0.20.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							701d4ca9a34
	17402 travis_ppc64							aa3052ac519	last=1d684f05341 elichai/2019-11-powerpc64
	19613 travis_s390x-0.20						874115cdd4e
	18750 ignore_external_warnings-0.20+knots	29118b6ad18	last=ec1ea76247e
# FIXES:
	-     qa_fix_tz_nonia-0.20					c3205d0f36a
		# Part of #19008
	18556 drop_dist-0.20						aafa9b7e3d1
	18818 fix_gitian_src_202004-0.20			57102d3df4c	last=3897f3a2ec0 fix_gitian_src_202004
		# +part of #18741
	18902 fix_release_tarball-0.20				3d6e49e807e	last=83ecd1b15e8 fix_gitdir_again
	18427 2020mingwthrd-mini					380c86e8d16	last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case				e32605dd3c2
	17828 practicalswift/log-categories			7a40b3433d6	last=04960621582 practicalswift/log-categories
	14968 laanwj/2018_12_http_bind_error		a57f6aa8b6b	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					f1de252e1b4
	18287 fix_libevent_win_ipv6^				bc98aeddc21
	19375 fix_libevent_win_ipv6					027ca7bbdc1
	9524 marco/Mf1701-qaPruning					bd414d85961	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					7b23b0d08e7
	18437 -										d918a4403bb	last=182dbdf0f4b  # util: Detect posix_fallocate() instead of assuming
	14485 fadvise-0.20+knots					479d173ba1b	last=c063994a14f fadvise
		# Was #12491
	14501 fsync_dir								fc8469acb68
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	17204 fix_1neg-0.20							92bb4b984fc	last=dca28634d77 meshcollider/201910_1negate_rebase
		# based on 5af7625079 sipa/201804_keepnegone
		# WARNING: Subtle test rebase issue: signrawtransactionwithwallet in master allows for the test case, but not 0.20 because it isn't wallet-related
		#          This appears to be a regression in 0.20; see also #19737
	13608 -										c9dace04e15	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	-     bugfix_rpc_getbalance_hacky			dd9deca43e6
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			a44ac073781	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 promag:2019-01-loopexit
	# Needs review: 15909 Use 'CreateProcess' instead of 'wsystem' in 'runCommand' for Windows.
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	16525 rpc_unsigned_txver-0.18				e174d4d331c	last=e80259f197 matt/2019-07-unsigned-tx-ver
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
TM	17946 fix_gbt_buried						8c07dc5fe74
	18095 -										c6dfc3206fd													last=6307dfa87e3  # Fix crashes and infinite loop in ListWalletDir()
	18133 bugfix_qvalidlineedit					49b42b1e149
	18194 bugfix_gui_edit_sendaddr-mini			9fada3c674d	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs work: 18189 -  # Add error handling to all boost filesystem functions
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18335 cli_svcunavail-0.20					d87686f9b3a	last=8dd5946c0b7  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	18452 fix_waitfor-0.20						15cdebdf117	last=da73f1513a6
	# Needs concept ACK: 18466 -  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
m	18467 settxfee_maxtxfee-0.20				595bcdd3efc  # rpc: Improve documentation and return value of settxfee
	18729 intro_dont_change_user_prune			927b68d75c4
	18766 blocksonly_no_feeest-0.20				4c85e2551bc	last=300bf14002f
		# diff-minimised
		# HELD BACK 33ca3590243...300bf14002f due to refactor complication
	18727 qa_createwalletfromfile-0.20			f273ae7077d
	18850 fix_zapselecttx_sync-0.20^			a9f64d4f44c
	19493 fix_zapselecttx_sync-0.20				f55943e108f
	# Needs fixes: 18861 sipa:202004_private_getdata
	18896 bugfix_gui_pr18896-0.17				739fce2ba5d	last=1e9bfd4926a
	18956 win_min_version_flag-0.18				abbd8dbc2cd
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
TM	18982 bugfix_walletnotify_conflict-0.20		df79d6c40bb	last=7eaf86d3bfc
	# Conflicts with #17828? 18990 logmempoolrej-0.20
	18993 gui_console_longinput-0.8				dda663e4130	last=fc6a637a013  # qt: increase console command max length #18993
	# Needs concept review & possible Knots adjustments: 19001 qt: bugfix unsupported QLocale languages
	# Needs concept ack & care: 19011 jonasschnelli:2020/05/guilocks
	19169 rpc_listunspent_optscheck-0.15		0c9dd37a207	last=a99a3c0bd6d  # rpc: Validate provided keys for query_options parameter in listunspent
TM	19215 psbt_segwit_fix-0.20					064473d40d3	last=836d6fc375a achow101/psbt-segwit-fixes
		# NOTE: Diff-minimised
	19237 pubkey_size_check-0.20				56a158b263b	last=37ae687f95c elichai/2020-06-pubkey
	19241 help_checkpoint_num					c28c15830f9
NM	19243 misbehaving_limit-0.20				b5a319968c8	last=7f1e47de55e misbehaving_limit
	# Needs review: 19289 promag:2020-06-wallet-less-locks
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19362 rpc_scantxoutset_reset_progress-0.17	663b923b439				last=8c4129b4540 prusnak/rpc-scantxoutset-reset-progress
	19502 bugfix_listwalletdir_errors-mini		48100d93e96					last=4f0cbc4bc74 bugfix_listwalletdir_errors
	19419 listwalletdir_skip_data-0.20+knots	c25545c6d7c				last=caa418440dd
		# NOTE: modified to use std::set and diff-minimise
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Mostly-Redundant with #17828: 19526 log_category_chkblkhdr-0.20
		# Diff-minimised
	# Needs review: g18    hebasto:200701-peer
	g20   bugfix_intro_tooltipwrap-0.17			71aa9003e5c						last=6ed4bcabc1a hebasto-g/200702-tooltip
	g39   gui_recvaddr_defaultbtn-0.14			0d641d4bd1d						last=4ec49f8d1e2 hebasto-g/200721-prim
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	# Needs concept ack: 19655 rpc: Catch listsinceblock target_confirmations exceeding block count
	# Needs _careful_ review: 19670 sdaftuar:2020-08-improved-eviction
	g43   bugfix_encrypt_menu_state-0.20		ad43955a127					last=20c9e035543 hebasto-g/200803-encrypt
	# Needs review: g59 hebasto-g/200814-rpc
		# NOTE: WAS Needs fix?? 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
# FUNCTIONALITY:
	-     restore_win32-0.20+knots				9dbb4bb8313
	-     restore_linux32						275c3f2b076
	17929 gitian_linux_ldO2-0.20				493a23570cc
		# NOTE: gitian only
	14066 gitian_power64-0.20+knots				5d7416dc553	last=fb0dd8e3d72 gitian_power64
	19525 z_separate_code-0.17					5fdc94e929d
		# Added efac9b5c02b to avoid breaking PPC64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.20					16fdd36b668	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							371133b011b
	15704 win32_defines_globally				ed8dd3b57ab
	9245 ionice									800db8d7ed2
	-    ionice_win								0dbfd739a14
	8501 old_stats_rpc-0.20						eb4bb442a39	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.20						1b5f959db61	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible-0.20			35d6a70a162 last=1befffc0b48 mempool_dat_extensible
		# 0.21 TODO: adapt test/functional/mempool_compatibility.py
		# Rebased in #19488
	9504 dumpmasterprivkey-0.20					a537df1837b	last=07fc81109a
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							9bb07e6a09b
	10615 multiwallet_rpc						cae95b17c3a
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	10554 zmq_wtx-0.20							956cd1ed5c8	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	# Needs work... 19572 instagibbs:zmq_sequence_all
		# NOTE: c6b3fff27d2 has rebase (on top of mid-assemble)
	12674 rpc_onetry_nonpriv					9a45ef53119
	10593 relax_invblk_punishment				7f9bad17370
	# Needs copyright header: 17311 RandyMcMillan:fix-background-svg
	# Needs fixing/review: 17303 MarcoFalke:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	10594 whitelist_outgoing-mini-0.20+knots	6117702d13d	last=d465ea1e057 whitelist_outgoing
		#TODO: Split this up?
	10350 filtered_witblock-0.20				9b42a3cdfc3	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				6b2aa12a15f
	14641 promag/2018-11-fundrawtransaction		5a59883c90b	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
		# NOTE: held back .gitignore nonsense change & relnotes
	18275 wallet_no_change_explicitfee-0.20		158f51312cd	last=44cc75f80ee kallewoof/2003-wallet-error-on-feechange
	11413 explicit_fee-0.20+knots				06387208dfa	last=25dac9fa652 kallewoof/explicit-fee
		# FIXME: When rebasing, squash away the commit subject "test" (it belongs with the following commit!)
		# NOTE: Dropped 4855bc80992 and 4e5fc19d9d9; diff-minimised and:
		# NOTE: Retained compatibility with "EXPLICIT" fee mode, and fixed upper/lower casing
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	11750 coincontrol_multiselect				f19a49c9c7e	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.19							8adf4ea4ad1	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			a531703b9ef
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
		# NOTE: Competing with #15341
	12677 listunspent_ancestorinfo-0.20			25dc73c5e13	last=db9baad856a listunspent_ancestorinfo
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	12911 rpc_sign_show_fees					4f673e0f47d	last=47b2ba29df2 kallewoof/sign-show-fees
		# NOTE: Rebased as #18479
	12965 scriptthreads-0.20					94cab5cd334	last=dfab6c6866 jonas/2018/04/svt
	# Needs review are care (new index): 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.20					6cb5a950d91	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		7601c44040b
	-     walletnotify_w_win					dc1125f3101
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	14137 win_taskbar_progress					7efece3a98f	last=18eb4dbb8a
	14687 zmqkeepalive-0.19+knots				962ceae0184	last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	15115 rm_send2self-mini						bf677cfccec	last=14bb8db698d rm_send2self
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	15202 gui_closeallwallets-0.19				4850487af59
	# Needs review: 15204 promag:2019-01-openexternalwallet
	15218 postibd_flush							252a789bda7	last=d2ecb70d64  # validation: Flush state after initial sync
		# Moved init around to avoid conflict w/ 15367
		# TODO: Rewrite after #17487 is ready/safe to merge
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	15367 startupnotify-0.20					a8be108ebf6	last=128d9fe1e2e	# feature: Added ability for users to add a startup command
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						75310fd2afc
	15428 tor_gui_pairing-0.20+knots			d9aa51dbd30	# latest code now
	15421 tor_subprocess-0.20+knots				1ccae95dfb8	last=f2add182487 tor_subprocess
	# TODO: tor gitian bundle!
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Waiting to be non-WIP: 15487 [WIP] descriptor based wallet serialization and import
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15633 nohbcbfornonwit						636255da406
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# USELESS Shared-lib 15717 Changes to support NAT-PMP
	# Needs work: 18077 hebasto/20200130-natpmp
		# NOTE: Diff-minimised rebase of 2d5d98ce0aa is at c6ff5633b56
		# TODO: Switch to rwconf?
	15768 gui_ctrl_w-0.20						65f7ff5822a	last=f5a3a5b9ab3  # gui: Add close window shortcut
	17795 gui_console_ctrl_d-0.20+knots			1ec8eccf979
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	# Needs fixes, then careful review of (and drop last commit from) 15761 achow101:upgradewallet-rpc
	# NEEDS FIXES: 15845 wallet_fastrescan-0.19							last=faee7b6581f marco/1904-walletFastRescan
		# TODO: Minify and test well
		# OR: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram-0.20					9b813469566	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: removed extraneous Bitcoin-Qt.* files
	15861 restore_vbits_warning-0.20			9c53e7f7026 last=9de382aae41 restore_vbits_warning
	# Needs concept ACK and review: 15873 or 16523 Rpc removemempoolentry
	# Needs rebasing without settings.json and review: 15937 Add loadwallet and createwallet load_on_startup options
	# Needs QA/review: 15946 jonasschnelli:2019/05/prune_blockfilter
		# NOTE: When merging, update GUI neutrino stuff to allow pruning+filters!
	17463 gui_custom_sendyes					89e50f62dea
	15987 wallet_no_reuse-0.20+knots			b1f56c95daf
	-     rpc_gai_txids							5b94114c222
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	18772 getblock_fees-0.20					a974ea5db0d
	16083 rpc_getblock_prevouts_fees-0.20		cd65132e53f	last=dd83c4c925
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Renamed "fees" field to "fee"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# Needs review: 16378 Sjors:2019/07/send
	# Needs mucho review: 16546 Sjors:2019/08/hww-box2 # -signer
		# NOTE: Bumps boost version!
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# Depends-on-16546: 16549 Sjors:2019/08/hww-qt
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs review (and BIP finalisation?): 19031 Implement ADDRv2 support (part of BIP155)
	16795 rpc_inferred_output_descriptors-0.20	e92ec451ef6	last=ef91078d672 instagibbs/decode_descriptor
	16807 bech32_error_detection-0.20+knots		d74d6927fb5	last=54e107add41 meshcollider/201909_bech32_error_detection
		# NOTE: Minor diff-minimisation, dropped relnotes, added autodetect hack
	-     gui_bech32_errpos-0.20+knots			cb3cabe6dfc  # Latest code
	16939 ajtowns/201909-avoid-dns-if-addrman-populated	cad5be72285		last=96954d17948
		# If rebasing, diff-minimise too?
	# Needs concept ack: 16981 LarryRuane:reindex-speedup
	17034 psbt_ver_proprietary-0.20+knots		479c37e0f2d	last=ddaccbc7bbd achow101/bip174-extensions
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs signing provider stuff - 0.20?: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options?
		# TODO: Diff-minimise
		# Partial rebase at f2fefb51511 (on v0.19.0 tag!)
	# Needs review: 17219 Sjors:2019/10/change-without-keypool
		# NOTE: release notes in #19115
	#TODO: Android packaging? #17227 + #17396?
	# Needs review: 17268 JeremyRubin:mempool-experiments-2  # Epoch Mempool
	# Needs fix: 17355 za-kk:oct-19-17174
	16432 gui_overview_privacy-0.20+knots		577661d0bd7	last=8d75115844b hebasto/20190721-privacy
		# TODO: low-priority updates 6920e1236b3..8d75115844b
		# NOTE: Held back ea1fb691c9c..dba83b9dab9
		# NOTE: Dropped monospace font / justify hack in privacy mode
		# Ensure copying balances isn't annoying
		# Should balances be forced monospace normally just for masking??
	18877 neutrino_cfcheckpt-0.20+knots			71395160272
	# TODO: Split out 18960, 19010, 19044, 19070
	18876 neutrino-0.20+knots					ed2fb9f5001	last=5488ce98cf2 8e5e184e3
		# NOTE: Held back cdf12ea6a5b itself since it demands users actively involved in index state
		# TODO: redo with #19010
	18972 neutrino_whitelist-0.20+knots			bb3d0c36f16	last=f1ebb52cd43
		# NOTE: Excluded refactor
	16463 bip174_xpub-0.20+knots				d78cdc3c6f9	last=ee0dd3ae1fc achow101/bip174-xpub
		# NOTE: Diff-minimised by excluding moveonly
	# TODO: Support Knots policies: Minimised 16490 marco/1907-rpcMempoolWhyReplacable
	# Needs review: 17428 p2p: Try to preserve outbound block-relay-only connections during restart
	17509 gui_saveload_psbt-0.20+knots			bf5bbf15fb1	last=764bfe4cba3 Sjors/2019/11/gui-psbt-save
		# NOTE: Minified
	18027 gui_psbt_opts_dialog-0.20+knots		d63fc40c902	last=931dd476085 gwillen/feature-psbt-ops-dialog
		# NOTE: Dropped changes to error strings (at least some re-implemented on my own), and unrelated 931dd476085
		# NOTE: Held back efde5525704->11a0ffb29d1 because it shouldn't matter
	# Needs review: 17529 rpc: Faster getblock using PureBlock
	17631 rest_blockfilter-0.20					7ab1d25075d	last=16d8d2da598 matt/2019-11-filter-rest
		# NOTE: Dropped unrelated extra commits
	17636 guisettings-0.20						0f54ecab02a	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	# Needs work & concept ACK: 17815 rpc: Make __cookie__ user immune to rpcwhitelist
	# Needs work/review: 17918 emilengler:2020-01-hide-non-pkhash-addresses
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	17955 gui_uri_paste-0.20+knots				73581972a8b	last=0139b428923 emilengler/2020-01-paste-bitcoin-uri-button
	17958 rpc_getgeneralinfo-0.20+knots			dbd1c4b28de	last=cdbd38df131  # getgeneralinfo RPC
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	# Needs review: 18000 -  # Coin Statistics Index
	18014 siphash_optimise_pr18014-0.19			315c9c151c0	last=9ed348ddea3 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks
	# Needs review: 18038 -  # P2P: Mempool tracks locally submitted transactions to improve privacy
		# +18807 (WIP)
	18223 blockfilter_v0-0.19					7b28a045091	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	18238 ajtowns/202002-bump-notfound			252be8f1c13	last=a204d1586ca ajtowns/202002-bump-notfound
	# Needs work/review/completion: 18242 jonasschnelli:2020/03/net_v2
	# Needs concept review: 18244 Sjors:2020/03/rpc_coin_locks
	18309 -										07b3af3cee8	last=751a5c5d562  # zmq: Add support to listen on multiple interfaces
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# ---- BEGIN IN SEQUENCE ----
	18574 cli_getinfo_balances-0.20				3ee4758396d
	18653 qa_cli_rpcwait_pt1-0.20+knots			bfb7f404db1
	18691 qa_cli_rpcwait-0.20+knots				7c92c884705
	18724 qa_cli_rpcwallet-0.20+knots			4899460bbd5
	18594 cli_getinfo_mwbalances_pt1-0.20+knots	eb1e885faff	last=5edad5ce5d3 jonatack/cli-getinfo-multiwallet-balances
		# NOTE: Omitted 903b6c117f5 (refactor)
	19089 cli_getinfo_mwbalances-0.20+knots		84a97ebe467	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-0.20+knots	377d1e1af1e	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock-0.20	08bbf94930c	last=1e868bbbb1b
	# Needs work? 18611 -  # cli: show default values in config args log
	18654 rpc_psbtbumpfee-0.20					b11a1d2235e	last=79d6332e9e4 achow101/psbtbumpfee
		# NOTE: Held back de0ad3a23c5..70e8422b585
		# NOTE: Held back deprecation
	# TODO: (conflicts with address reuse warning) 18789 achow101:create-unsigned-sendconfdialog OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	18689 rpc_dumptxoutset_hr-0.20				7938c1e956c	last=82046cf7fa3
	18722 O_addrman_unordered_map-0.20			6cf83fbdd9b	last=d6e782174ec
	18728 intro_prune_size						0eb1987f257
	19117 rpc_getrpcwhitelist-0.20				5769beae547	last=94fad2edec5 rpc_getrpcwhitelist
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.20+knots	3d6a83a8bce
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	# Not needed: 18781 getrandomduration-0.20							last=0000ea32656 marco/2004-randDur
		# GetRandMicros seems just as well...
	18991 p2p_getaddr_cache-0.20+knots			72e4b12f121	last=3bd67ba5a4e  # Cache responses to GETADDR to prevent topology leaks
		# NOTE: Reordered test_runner to avoid conflict
		# Held back ded742bc5b9 (RPC change), 7cc0e8101f0 (non-evaluated effect), doxygen comment changes, and refactoring
		# Held back removal of addr from implicit flags (rebased in b78f81553d8a4)
	# Needs fixes: 19697  # Improvements on ADDR caching
	# Needs concept review: 19043 torcontrol: add -tortarget config
	19093 rpc_testmempoolaccept_fee-0.20		adf24e5bbee	last=c9781e92a21  # RPC: testmempoolaccept returns transaction fee
	# Needs consideration: 19109 sipa:202005_bloom_relay
	# 0.21 TODO: 19136 achow101:export-descriptor
	# Depends on refactor: 19137 achow101/dumpwalletrecords
	19142 verifydb_lv4_interrupt-0.20			d08486e6859
		# Diff-minimised
NM	19191 p2p_permission_download-0.20+knots	5b7c903dc3a
	19191 p2p_permission_download-0.20.1+knots	af68727e3ce				last=fa0540cd46e marco/2006-netPerDow
		# IMPORTANT: Avoid conflicts with PF_ADDR or other permission flags (moved to 1<<18)
		# Held back 111109a1e79...fa0540cd46e (help doc updates)
	19204 p2p_ibd_noinv-0.20					cf12574d1a3	last=fa525e4d1cf marco/2006-netInvWaste
		# NOTE: Dropped refactors, and diff-minimised
	19242 uaappend								76bf6d9e41d
	# Needs review: 19271 andrewtoth:warm-coinscache
	19328 rpc_gettxoutsetinfo_hash_type-0.20	3637014b81b
	19405 rpc_netinfo_conncount_inout-0.20+knots	0b5e9912cef			last=94a792cc19f jonatack/in-and-out-connections
		# NOTE: Requires +knots for invisible conflict with #19089
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
	19463 prune_locks-0.20+knots				f28408c5584							last=f4b2ed65ea5 prune_locks
	19473 param_networkactive-0.20				dcb4a149ed4
	# Needs work: 19476 promag:2020-07-rpc-mempoolchanges
	# Needs work: 19485 # torcontrol: Create also a V3 ed25519-V3 onion address.
	# TODO: 19501 -  # send* RPCs in the wallet returns the "fee reason"
	# Needs review: 19521 # Coinstats Index (without UTXO set hash)
	19550 rpc_getindexinfo-0.20					7b08c267401								last=47a5372d289
	# Needs consideration: 19569 sipa:202007_wtxid_followup
	# ---- BEGIN WTXID RELAY ----
	# Problematic due to risky conflicts with #18238
	#18044 wtxid_relay-0.20.1+knots							last=4daad798f3b jnewbery/2020-07-v20-wtxid-relay
	#	# really #19606
	#19569 sipa/202007_wtxid_followup minus refactoring?
	# ---- END WTXID RELAY ----
	19620 sdaftuar/2020-08-reject-unknown-wit-0.20	b7b8e68e670			last=107cf1515e6 sdaftuar/2020-08-reject-unknown-wit-0.20
	# Needs work: g4    Sjors:2019/08/hww-qt
	g6    peerdetails_no_trunc-0.18				e2cfc994f52
	# Needs work: g27   # top to bottom UI layout
	g34   gui_p2ppermissions-0.20				a3c3abbcadb							last=784ef8be41c
	# Needs concept ACK: 19635 -ephemeraltoronion
	19643 cli_netinfo-0.20						f5e6ed45f2a
	# Needs changes? 19658 jnewbery:2020-07-addrman-get
	# Needs concept review: 19723 sdaftuar/2020-08-feature-negotiation
	# Needs concept review: 19725 -  # [RPC] Add connection type to getpeerinfo, improve logs
	19728 addr_relay_branching-0.14				d827bce0b13							last=86d4cf42d97 sipa/202008_increase_addr_branching
# Non-upstreamed functionality:
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
m	-     restore_rejectmsg-0.20+knots			3e972a79e85						 # Latest code now
	-     restore_blockmaxsize					5d250911a02
	7107 qtnetworkport							1e4e5fc5c20	last=1f37c87 origin-pull/7107/head
m	7533 sendraw_force-0.20+knots				711f80f3c7f  # Latest code now
	11082 rwconf-0.20							d6300e8b70c	last=78bc86711a8 rwconf
	7510 rwconf_gui								c4c9e276523
		# 0.21 TODO: update neutrino option name
	-    rwconf_gui_plus						faa83cb57b4
	-    preserve_unsupported_keyflags			10268bee8bb
	 559 accept_nonstdtxn						0e5af073cbf
	 929 tbc									7a0f5c854a3
	 553 bugfix_qt_uri_amount_parser			e9841cb4c2d
	-    mining_priority						8614b80bd5f  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					493daee03f4
	5891 qt_console_history_persist-0.20+knots	2703b766202	last=ea852deea35 qt_console_history_persist
	7219 rbf_opts-0.20+knots					10eff2d2b59
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					c71e6f0a91d
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	10282 timebomb_knots						c882fc91088
	-     gui_wallet_displayname-0.19			272830f6b45	# Latest code now
	-     gui_request_payment_label-0.19		8ddc089ee86
	n/a  checkpoint_update-0.20					9fd3ffe8847
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				33665f43d0b
	-    bytespersigopstrict-0.20+knots			df6aa2504d8
	9749 unique_spk_mempool-0.20+knots			90a3e5e6439
	-    bloom_default-0.20+knots				bdced177507
	-    rwconf_policy-0.20+knots				fed4818281b
		#FIXME 0.21: split actual policy changes out to another line
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	7483 svg_icon-0.20							f879fb26118
# BRANDING:
	n/a  knots_branding-0.20					2132f7e92b0
#FIXME: Check there are no menu icons
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: check for 'false' instead of ALLOW_ANY in addArgs
#TODO: Check that we aren't deprcating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
	n/a  (cherrypick=6b32ed8eb2773d5aa0)		e4b876a98d2	# doc/{bips,files}
	n/a  (bump_version=Knots:20200815)			bc1ab114d70
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=122a503033f)				3652b86eb92  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=b9a7c5d663b)				2b34276c749  # translation update
	n/a  (cherrypick=7b55b1058fd)				95690c463e6  # update manpages (build first)
# NOTE: use git diff --minimal for patches!

# TODO: Try Snap package stuff documented in doc/release-process.md
