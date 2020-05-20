timestamp 2020-05-04 20:11:06
lastapply no-merge

#.. checked up to PR #18867

checkout origin/0.20
@0.20.x-syslibs
	5872 subdir_incl_compat						3dce4412b12
	2241 sys_leveldb							5ef0d062931
	5416 sys_libsecp256k1						3a75e059dd3
	7485 sys_univalue_def						34d525a0efa
	13789 bugfix_asm_pragmas-0.20				42302b9b565	last=14337d0d80b bugfix_asm_pragmas
	-     bugfix_asm_leveldb_check				7343cea2d59
	15155 test_external_bcli					e5ee5cbd543
	16564 -										32f49042fd2	last=9a19c9ada5  # Always define the raii_event_tests test suite
@0.20.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							931ebfa1f80
	17402 travis_ppc64							228a9f05aa4	last=1d684f05341 elichai/2019-11-powerpc64
	# TODO: ? Restore Valgrind/s390x Travis jobs: https://github.com/bitcoin/bitcoin/pull/18899 https://github.com/bitcoin/bitcoin/pull/18905
	18724 qa_cli_rpcwallet-0.20
# FIXES:
	18556 drop_dist-0.20
	18818 fix_gitian_src_202004-0.20						last=3897f3a2ec0 fix_gitian_src_202004
		# +part of #18741
	18902 fix_release_tarball-0.20							last=83ecd1b15e8 fix_gitdir_again
	18427 2020mingwthrd-mini								last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case
	17828 practicalswift/log-categories			506d59c2b8a	last=04960621582 practicalswift/log-categories
	14968 laanwj/2018_12_http_bind_error		0afbbc1b23c	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					c1facf98c54
	18287 fix_libevent_win_ipv6					162bac47c59
	9524 marco/Mf1701-qaPruning					2617c80565b	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					b91935a2f33
	18437 -													last=182dbdf0f4b  # util: Detect posix_fallocate() instead of assuming
	14485 fadvise-0.20+knots					c196c18b9c4	last=c063994a14f fadvise
		# Was #12491
	14501 fsync_dir								4b2d9b4aafe
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	17204 meshcollider/201910_1negate_rebase	d64ab583d72	last=45af54fbdc8 meshcollider/201910_1negate_rebase
		# based on 5af7625079 sipa/201804_keepnegone
	13608 -										3f9f71a66a3	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs fix?? 13674 -													# Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	-     bugfix_rpc_getbalance_hacky			a9a2a926669
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			041d228a769	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 promag:2019-01-loopexit
	# Needs review: 15909 Use 'CreateProcess' instead of 'wsystem' in 'runCommand' for Windows.
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Likely impossible: 16199 fix coinjoin sends in RPC
	16525 rpc_unsigned_txver-0.18				f45e6d4aa2a	last=e80259f197 matt/2019-07-unsigned-tx-ver
	# Needs review: 17457 bugfix_multiwallet_coincontrol
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	# Needs to be just a bugfix: 17597 qt: Fix height of QR-less ReceiveRequestDialog
	17946 fix_gbt_buried						247f7bf9191
	# Needs review: 18095 -  # Fix crashes and infinite loop in ListWalletDir()
	18133 bugfix_qvalidlineedit					adad02360a6
	# Needs careful review: 18192 bugfix_addressbook_change
	18194 bugfix_gui_edit_sendaddr-mini			a54995ed86f	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs work: 18189 -  # Add error handling to all boost filesystem functions
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18335 -													last=4bb892cec23  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	18452 fix_waitfor-0.20									last=da73f1513a6
	# Needs concept ACK: 18466 -  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	18467 -													last=38677274f93  # rpc: Improve documentation and return value of settxfee
	18729 intro_dont_change_user_prune
	18766 blocksonly_no_feeest-0.20							last=33ca3590243
		# diff-minimised
	# Needs review: 18850 -  # Fix ZapSelectTx to sync wallet spends
	# Needs fixes: 18861 sipa:202004_private_getdata
# FUNCTIONALITY:
	-     restore_win32							f7147699d7d
	-     restore_linux32
	17929 gitian_linux_ldO2-0.20
		# NOTE: gitian only
	14066 gitian_power64-0.20+knots					a0682b1c6d9	last=fb0dd8e3d72 gitian_power64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.20					71fa5983da9	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							69942579878
	15704 win32_defines_globally				651c437399e
	9245 ionice									a835a4f3a7b
	-    ionice_win								1eb8a97cb8b
	8501 old_stats_rpc-0.20						7849380be7a	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.20						23537cb5322	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible					5eb5fb7bf25
	9504 dumpmasterprivkey-0.20					b2f9fe8cc74	last=07fc81109a
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							bfb9857e5ec
	10615 multiwallet_rpc						e2bd3bdd652
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	10554 zmq_wtx-0.20							6f452db941a	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	12674 rpc_onetry_nonpriv					548ed42c93e
	10593 relax_invblk_punishment				0c990aa1bae
	# Needs copyright header: 17311 RandyMcMillan:fix-background-svg
	# Needs fixing/review: 17303 MarcoFalke:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	10594 whitelist_outgoing-mini-0.20+knots	95b7e4c506a	last=d465ea1e057 whitelist_outgoing
		#TODO: Split this up?
	10350 filtered_witblock-0.20				ee4bf72196f	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				8d801bd6ade
	14641 promag/2018-11-fundrawtransaction		58d9c58687f	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
		# NOTE: held back .gitignore nonsense change & relnotes
	18275 wallet_no_change_explicitfee-0.20					last=44cc75f80ee kallewoof/2003-wallet-error-on-feechange
	11413 explicit_fee-0.20+knots				80ba6c30043	last=53342290f47 kallewoof/explicit-fee
		# NOTE: Dropped 4855bc80992 and 4e5fc19d9d9; diff-minimised and:
		# NOTE: Retained compatibility with "EXPLICIT" fee mode, and fixed upper/lower casing
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	11750 coincontrol_multiselect				fa0386c248d	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.19							dc7af418af8	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			3ea3c529412
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
		# NOTE: Competing with #15341
	12677 listunspent_ancestorinfo				e3760b3b80f
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	12911 rpc_sign_show_fees					05ebb9adbe7	last=47b2ba29df2 kallewoof/sign-show-fees
		# NOTE: Rebased as #18479
	12965 scriptthreads-0.20					fe21944c5b4	last=dfab6c6866 jonas/2018/04/svt
	# Needs review are care (new index): 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.20					9bf2c8c00b4	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.20_asm_pragmas		f636f29dd67
	-     walletnotify_w_win
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs review: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	14137 win_taskbar_progress					b610a34da31	last=18eb4dbb8a
	14687 zmqkeepalive-0.19+knots				cac95fd51b5	last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# needs review: 14898 nextpagepointer & list ordering options for listtransactions
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	15115 rm_send2self-mini						94ec464a399	last=14bb8db698d rm_send2self
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Not ready: 15150 promag:2019-01-consolewalletselector
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review/revision: 15202 promag:2019-01-closeallwallets
	# Needs review: 15204 promag:2019-01-openexternalwallet
	15218 postibd_flush							6aefc9da6e4	last=d2ecb70d64  # validation: Flush state after initial sync
		# Moved init around to avoid conflict w/ 15367
		# TODO: Rewrite after #17487 is ready/safe to merge
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	15367 -										3567de0e582	last=4b6987c85d8	# feature: Added ability for users to add a startup command
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						1fcfd051da3
	15428 tor_gui_pairing-0.20+knots			0bfc25eab88	# latest code now
	15421 tor_subprocess-0.20+knots				e7ddfa8a4d3	last=f2add182487 tor_subprocess
	# TODO: tor gitian bundle!
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Waiting to be non-WIP: 15487 [WIP] descriptor based wallet serialization and import
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15505 sdaftuar:2019-02-notfound-requests
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15633 nohbcbfornonwit						ef50f754927	last=fb791ef082 gmaxwell/201803-nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
	# USELESS Shared-lib 15717 Changes to support NAT-PMP
	# Needs work: 18077 hebasto/20200130-natpmp
		# NOTE: Diff-minimised rebase of 2d5d98ce0aa is at c6ff5633b56
		# TODO: Switch to rwconf?
	15768 gui_ctrl_w-0.20						9c52fd0a4c1	last=f5a3a5b9ab3  # gui: Add close window shortcut
	17795 gui_console_ctrl_d-0.20+knots			299a1cf9c83
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	# Needs fixes, then careful review of (and drop last commit from) 15761 achow101:upgradewallet-rpc
	# NEEDS FIXES: 15845 wallet_fastrescan-0.19							last=faee7b6581f marco/1904-walletFastRescan
		# TODO: Minify and test well
	15836 fee_histogram-0.20					1fe42b9c815	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: removed extraneous Bitcoin-Qt.* files
	15861 restore_vbits_warning-0.20			6f1c5b1da81 last=9de382aae41 restore_vbits_warning
	# Needs concept ACK and review: 15873 or 16523 Rpc removemempoolentry
	# Needs rebasing without settings.json and review: 15937 Add loadwallet and createwallet load_on_startup options
	# Needs QA/review: 15946 jonasschnelli:2019/05/prune_blockfilter
		# NOTE: When merging, update GUI neutrino stuff to allow pruning+filters!
	17463 gui_custom_sendyes
	15987 wallet_no_reuse-0.20+knots			864b8322e3d
	-     rpc_gai_txids							81ecb2e1120
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	18772 getblock_fees-0.20
	16083 rpc_getblock_prevouts_fees-0.20		2cf8730b711	last=dd83c4c925
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Renamed "fees" field to "fee"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# Needs review: 16377 Sjors:2019/07/walletcreatefundedpsbt_addinputs
	# Needs review: 16378 Sjors:2019/07/send
	# Needs mucho review: 16546 Sjors:2019/08/hww-box2 # -signer
		# NOTE: Bumps boost version!
	# needs completion: 15876
	# Depends-on-16546: 16549 Sjors:2019/08/hww-qt
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs review (and BIP finalisation?): 16748 dongcarl:2019-07-addrv2v4
	16795 rpc_inferred_output_descriptors-0.20	fb5b42b8478	last=dcd5c4a5773 instagibbs/decode_descriptor
	16807 bech32_error_detection-0.20+knots		f94326eb003	last=54e107add41 meshcollider/201909_bech32_error_detection
		# NOTE: Minor diff-minimisation, dropped relnotes, added autodetect hack
	-     gui_bech32_errpos-0.20+knots			547af169965  # Latest code
	# Meh, needs review? 16939 ajtowns:201909-avoid-dns-if-addrman-populated
	# Needs concept ack: 16981 LarryRuane:reindex-speedup
	17034 psbt_ver_proprietary-0.20				fbeea35914e	last=19200a775a7 achow101/bip174-extensions
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs signing provider stuff - 0.20?: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options?
		# TODO: Diff-minimise
		# Partial rebase at f2fefb51511 (on v0.19.0 tag!)
	# Needs review: 17219 Sjors:2019/10/change-without-keypool
	#TODO: Android packaging? #17227 + #17396?
	# Needs review: 17268 JeremyRubin:mempool-experiments-2  # Epoch Mempool
	# Needs fix: 17355 za-kk:oct-19-17174
	16432 gui_overview_privacy-0.20+knots		01a221dac9d	last=6920e1236b3
		# NOTE: Held back ea1fb691c9c..dba83b9dab9
		# NOTE: Dropped monospace font / justify hack in privacy mode
		# Ensure copying balances isn't annoying
		# Should balances be forced monospace normally just for masking??
	18877 neutrino_cfcheckpt-0.20+knots
	18876 neutrino-0.20+knots					012949c76ce	last=5488ce98cf2 8e5e184e3
		# NOTE: Held back cdf12ea6a5b itself since it demands users actively involved in index state
		# TODO: redo with #19010
	18972 neutrino_whitelist-0.20+knots						last=51e9de5b435
	16463 bip174_xpub-0.20+knots				c2962442602	last=8ae43e849c7 achow101/bip174-xpub
		# NOTE: Diff-minimised by excluding moveonly
	# TODO: Support Knots policies: Minimised 16490 marco/1907-rpcMempoolWhyReplacable
	# Needs review: 17428 p2p: Try to preserve outbound block-relay-only connections during restart
	17509 gui_saveload_psbt-0.20+knots			10e48579513	last=764bfe4cba3 Sjors/2019/11/gui-psbt-save
		# NOTE: Minified
	18027 gui_psbt_opts_dialog-0.20+knots		6719aab1141	last=562800b8155 gwillen/feature-psbt-ops-dialog
		# NOTE: Dropped changes to error strings
	# Needs review: 17529 rpc: Faster getblock using PureBlock
	17631 rest_blockfilter-0.20					98dbf80046a	last=16d8d2da598 matt/2019-11-filter-rest
		# NOTE: Dropped unrelated extra commits
	17636 guisettings-0.20						c0f3baf5cda	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	# Needs work & concept ACK: rpc: Make __cookie__ user immune to rpcwhitelist #17815
	# Needs work/review: 17918 emilengler:2020-01-hide-non-pkhash-addresses
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	17955 gui_uri_paste-0.20+knots				e584afcc743	last=fa5887c5231 emilengler/2020-01-paste-bitcoin-uri-button
	17958 rpc_getgeneralinfo-0.20+knots			9df4b5ec9f7	last=cdbd38df131  # getgeneralinfo RPC
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	# Needs review: 18000 -  # Coin Statistics Index
	18014 siphash_optimise_pr18014-0.19			fae5dafc31f	last=de0c7fccb4b elichai/2020-01-siphash
		# NOTE: Dropped benchmarks
	# Needs review: 18038 -  # P2P: Mempool tracks locally submitted transactions to improve privacy
		# +18807 (WIP)
	# Needs review & BIP finality: 18044 sdaftuar:2020-01-wtxid-inv
	18223 blockfilter_v0-0.19					af5409ac311	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	18238 ajtowns/202002-bump-notfound			e48828fbabb	last=a204d1586ca ajtowns/202002-bump-notfound
	# Needs work/review/completion: 18242 jonasschnelli:2020/03/net_v2
	# Needs concept review: 18244 Sjors:2020/03/rpc_coin_locks
	18309 -													last=751a5c5d562  # zmq: Add support to listen on multiple interfaces
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs interface changes: 18453 jonatack:call-getbalances-for-getinfo-balance
	18574 cli_getinfo_balances-0.20
	18594 cli_getinfo_mwbalances-0.20						last=2e7d8b9bf58 jonatack/cli-getinfo-multiwallet-balances
	18570 wallet_rpc_lastprocessedblock-0.20				last=1e868bbbb1b
	# Needs work? 18611 -  # cli: show default values in config args log
	18654 rpc_psbtbumpfee-0.20								last=61d6e410e00 achow101/psbtbumpfee
		# NOTE: Partially rewrote to minimise diff/merge issues
	18789 achow101:create-unsigned-sendconfdialog OR these two:
	18655 achow101:split-bumpfeeaction
	18656 achow101:make-unsigned-button
	18689 -  # rpc: allow dumptxoutset to dump human-readable data
	18722 -  # addrman: improve performance by using more suitable containers
		TODO: exclude benchmark
	18728 intro_prune_size
	18827 brakmic:getrpcwhitelist
	18830 brakmic:getrpcinfo
	# Needs review: 18849 jb55:zeroalloc
# Non-upstreamed functionality:
	-     restore_blockmaxsize					ab64cadc3f0
	7107 qtnetworkport							46b01d384bc	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.20+knots				9c9ea7f80bd  # Latest code now
	11082 rwconf								41b9f119bb7
	7510 rwconf_gui								4cddb2d955c
		# 0.21 TODO: update neutrino option name
	-    rwconf_gui_plus-0.19+knots				5463b9e08fd
	-    preserve_unsupported_keyflags			907d9c37864
	 559 accept_nonstdtxn						cba789cceb1
	 929 tbc									88155f05a9f
	 553 bugfix_qt_uri_amount_parser			fc596062efd
	-    mining_priority						840235f5c49  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					5448798f7cb
	5891 qt_console_history_persist-0.19+knots	1257cc2b3e8	last=ea852deea35 qt_console_history_persist
	7219 rbf_opts-0.19+knots					e8ad31b9e4e
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					64e578fe3b2
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	10282 timebomb_knots						4c18de9f7fb
	-     gui_wallet_displayname-0.19			190666227ad	# Latest code now
	-     gui_request_payment_label-0.19		ecc9b39284d
	n/a  checkpoint_update-0.19					471acd7bfc3
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				3601f544269
	-    bytespersigopstrict-0.19+knots			d93712a1875
	9749 unique_spk_mempool-0.19+knots			031015ce77a
	-    bloom_default-0.19+knots				df61037d315
	-    rwconf_policy-0.19+knots				eb669c5e944
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	7483 svg_icon-0.19							bc35ebccb7e
		FIXME: using `git archive` to make source tarball means we need to append generated files!
# BRANDING:
	n/a  knots_branding-0.19					77761a69811
#FIXME: Check there are no menu icons
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: check for 'false' instead of ALLOW_ANY in addArgs
	n/a  (cherrypick=9600fe90fb2e446cac)		f63eb318b5e	# doc/{bips,files}
	n/a  (bump_version=Knots:20200304)			fa2f7c2d6bd
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=49c5b0fdd44)				176adbc13c5  # release notes: write/update, including change log and credits
			# check travis for misspellings
			gs a29b9939b65:doc/release-notes-11413.md
			gs fdd577dfc5d:doc/release-notes-18570.md
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=f33596fe405)				80d7a0e9d6d  # translation update
	n/a  (cherrypick=39c23bfb7cb)				3dd81e63cba	# update manpages (build first)
# NOTE: use git diff --minimal for patches!

# TODO: Try Snap package stuff documented in doc/release-process.md
