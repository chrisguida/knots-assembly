timestamp 2020-01-04 02:05:41
#lastapply no-merge

#.. checked up to PR #17860

checkout origin/0.19
@0.19.x-syslibs
	5872 subdir_incl_compat						29544b57e27
	2241 sys_leveldb							c94b5102231
	5416 sys_libsecp256k1						83cd1097b13
	7485 sys_univalue_def						655aae06d16
	13789 bugfix_asm_pragmas					a0c292cc2fd
	-     bugfix_asm_leveldb_check				ebda9cb965d
	15155 test_external_bcli					cb6e480140f
	16564 raii_event_test_fix-0.14				b815cdf468b	last=9a19c9ada5
TM	17450 bugfix_pr17450-0.19					9042cd5b937
TM	17654 boost_1_72_compat-0.19				a3dca843b30
@0.19.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							e13ddc3a1fd
	15888 test_wallet_implicitsegwit			957748c8dd9
	17402 travis_ppc64-0.18						efca75db899	last=1d684f05341 elichai/2019-11-powerpc64
# FIXES:
	17762 net_log_category_exc-0.19				625b5fafbab
		# Completely rewrote to minimise impact on 0.19
	17828 log_categories_validation-0.19+knots	062f5b03c1e	last=443e105f7ae practicalswift/log-categories
	14968 laanwj/2018_12_http_bind_error		efc4cc2d518	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					99a135b79a6
	9524 marco/Mf1701-qaPruning					4d044e0fc41	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					b3ed643d9f8
	14485 fadvise								bd7a97d3112
		# Was #12491
	14501 fsync_dir								292793ee3cc
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	17204 bugfix_keepnegone-0.13				e162b3892e4	last=0946a703273 meshcollider/201910_1negate_rebase
		# based on 5af7625079 sipa/201804_keepnegone
	13608 -										be84f2c69f3	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs fix?? 13674 -													# Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	-     bugfix_rpc_getbalance_hacky			56056cac6ee
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			ef19f8f7053	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 promag:2019-01-loopexit
	# Needs review: 15909 Use 'CreateProcess' instead of 'wsystem' in 'runCommand' for Windows.
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Needs review: 16161 util: Fix compilation errors in support/lockedpool.cpp
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review AND CARE MERGING: 16507 instagibbs:feefilter_match_mempool
	16525 rpc_unsigned_txver-0.18				913ca0a80b6	last=e80259f197 matt/2019-07-unsigned-tx-ver
	# Worth the diff? 16963 promag:2019-09-fix-loadwallet-signal-uniqueptr
	# Needs reivew: 17156 achow101:psbt-fuzz-fix
	17180 sendamount_tooltip-0.11				394636c0e15
		# JeremyCrookshank:sendamounttooltip
		# + 17226 promag:2019-10-payamount-tooltip
	17258 fix_rpc_listsinceblock_conflicts-0.19	5db9297d771	# adamjonas:listsinceblock-filter-conflicts
	# Not needed?: 17366 qa_reset_segwitheight-0.19
	17427 fix_qmeta_size_t-0.18					2e75c1b60b8	last=1828c6f05fc
		# Held back comment/formatting changes
	17474 bugfix_gui_netlimited_svcbit			65ef34b78a7	last=4341bffb6ef bugfix_gui_netlimited_svcbit+refactor
	# Needs review: 17457 bugfix_multiwallet_coincontrol
	17524 fix_unspendable_psbt-0.19				99fdc1305c1
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	# Needs to be just a bugfix: 17597 qt: Fix height of QR-less ReceiveRequestDialog
	17621 fix_iud_keywide-0.19					dc95386a7fa	last=09502452bbb instagibbs/actually_no_reuse
	17643 fix_bumpfee_uninitread-0.19			b8280a7f2cd
	17728 fix_scantxoutset_args-0.19			5c99a4a16d8
	# Needs reivew: 17843 wallet: Reset reused transactions cache
	17946 fix_gbt_buried						72e19972b4e
# FUNCTIONALITY:
	FIXME: Restore win32 gitian builds! revert faf666f8148eeb305a9c4f78459aff2c7268016b
	14066 gitian_power64						ec80f3746ff
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.19					beefe28fa71	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							2863fd8edaf
	15704 win32_defines_globally				9a9f5cdfd8d
	9245 ionice-0.19							f23cd77e848	last=e1276957ed2 ionice
	-    ionice_win-0.19						91dfb292f0a
	8501 old_stats_rpc-0.19						e14906b5c17	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.19						46dea09b557	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible					c8be732ca93
	9504 dumpmasterprivkey-0.18					6400f18613b	last=07fc81109a
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							f4b7244f807
	10615 multiwallet_rpc						882ed06729d
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	10554 zmq_wtx-0.19							512f2e96f63	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					3f1beb11bbb
	10593 relax_invblk_punishment				4888324ad5f
	# Needs copyright header: 17311 RandyMcMillan:fix-background-svg
	# Needs fixing/review: 17303 MarcoFalke:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
#TODO: Split this up
	10594 whitelist_outgoing-mini-0.19+knots	accd958dccb	last=b7463a900cd whitelist_outgoing
	10350 filtered_witblock-0.19				7aefa53696c	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				d1763cc493d
	11413 explicit_fee-0.19						2bebb4eeb31	last=9721534f1c9 kallewoof/explicit-fee
		# NOTE: Held back 97636cd371c..473ce2dcfdf -  see 670a101e362db0e3a346719e905fd6ab1cfd4fc4 branch for min feerate error
		# NOTE: Updated to c109001c9b with ac046e805c (HELD BACK)
		# NOTE: Retained compatibility with "EXPLICIT" fee mode, and fixed upper/lower casing
		# TODO: Relnotes changes - case insensitivity, (is RBF default new??)
		# 0.19 TODO: Rebase/squash fixups (keep compat with "EXPLICIT"!)
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	11750 coincontrol_multiselect				4371f2c0158	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.19							280aabcc310	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			a6ae4935203
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
		# NOTE: Competing with #15341
	12677 listunspent_ancestorinfo				a200cffa2c8
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.19						aa69598d0ec
	# TODO ? 12792 w/ renamed param
	12911 signrawtx_showfees-0.19				1f3ed3a36fe	last=345f8f9d1b1 kallewoof/sign-show-fees
	12965 scriptthreads-0.19					8c5b5701f54	last=dfab6c6866 jonas/2018/04/svt
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.17					31bd050ce45	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.17_asm_pragmas		8b1f3eaf99b
	13339 walletnotify_w-0.19					fc814dc1301	last=56d2307446b promag/2018-05-walletnotify
		# held back 826718490fb..1c335d5828e disabling on Windows
		# held back cef0327afd..15a0ad0bb4 Windows porting due to copyright issues (and bugs?) - No longer applicable?
		# Removed WIN32 conditional
		# Changed '"'"' to '\''
		# Test improvements: eaeb6fb7efd
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs review: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	14137 win_taskbar_progress					e90506552a7	last=18eb4dbb8a
	15023 gui_node_rpcconsole-0.19+knots		a2ea6688ac2	last=f33efa8ec5 gui_node_rpcconsole
	14641 fundraw_minconf-0.19					20da664aa60	last=a3991b7c0b promag/2018-11-fundrawtransaction
		# NOTE: held back .gitignore nonsense change & relnotes
	14687 zmqkeepalive-0.19+knots				be8c60c06c0	last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# needs completion: 14912 external signers WIP + 15876
	# needs review: 14898 nextpagepointer & list ordering options for listtransactions
	# CHANGES WALLET FORMAT, wait for Core: 15006 achow101:create-encrypted-wallet
		# +16394 achow101/fix-born-enc
	15084 gui_nowallet_modaloverlay-0.19		37a0bb40c8d	last=b3b6b6f62fc  #gui: don't disable the sync overlay when wallet is disabled
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	15115 rm_send2self-mini						66d458d0ed0	last=ecf3d5323e rm_send2self
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Not ready: 15150 promag:2019-01-consolewalletselector
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review/revision: 15202 promag:2019-01-closeallwallets
	# Needs review: 15204 promag:2019-01-openexternalwallet
	15218 -										860cc1525f5	last=d2ecb70d64  # validation: Flush state after initial sync
		# Moved init around to avoid conflict w/ 15367
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	15367 startupnotify-0.19+knots				ca5156ce105	last=4b6987c85d8	# feature: Added ability for users to add a startup command
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# TODO: 15421 tor_subprocess
	#	Needs boost::process check
	15423 tor_socks_port						cb310eb6e9b
	15756 -										d213dafeb47	last=091747b46ec promag/2019-04-tools-shortcuts
	15428 tor_gui_pairing-0.19+knots			5b8d09c0e6f	# latest code now
	# TODO: tor gitian bundle!
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Waiting to be non-WIP: 15487 [WIP] descriptor based wallet serialization and import
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15505 sdaftuar:2019-02-notfound-requests
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15633 nohbcbfornonwit						eb0dd0e21b9	last=fb791ef082 gmaxwell/201803-nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
	# USELESS Shared-lib 15717 Changes to support NAT-PMP
	15768 gui_ctrl_w-0.19						58cdb26c0cc	last=77b0232fcb0	# gui: Add close window shortcut
	17795 gui_console_ctrl_d-0.19+knots			90ae0210bd5
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	# Needs fixes, then careful review of (and drop last commit from) 15761 achow101:upgradewallet-rpc
	# NEEDS FIXES: 15845 wallet_fastrescan-0.19							last=faee7b6581f marco/1904-walletFastRescan
		# TODO: Minify and test well
		# NOTE: Needs #17366
	15836 jonas/2019/04/feeinfo					24c56bc2676	last=b94292a7cb jonas/2019/04/feeinfo
		FIXME: git rm Bitcoin-Qt.*
	15861 restore_vbits_warning					63d1f20f662
	# Needs concept ACK and review: 15873 or 16523 Rpc removemempoolentry
	# Needs rebasing without settings.json and review: 15937 Add loadwallet and createwallet load_on_startup options
	# Needs QA/review: 15946 jonasschnelli:2019/05/prune_blockfilter
	15987 wallet_no_reuse-0.19+knots			9f8e1c9c80d	last=391c5d9a972 wallet_no_reuse
	-     rpc_gai_txids-0.19					f78432716ec	last=621796da61 rpc_gai_txids
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	16083 rpc_getblock_prevouts_fees-0.19		59f9d2cd996	last=dd83c4c925
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Renamed "fees" field to "fee"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# TODO: 16373 bump_psbt-0.19+knots								last=9bdf420ecc3 instagibbs/bump_psbt
		# NOTE: Moved `add_to_wallet` param into `options`
		# CURRENT BRANCH STATUS UNKNOWN
	# Needs review: 16377 Sjors:2019/07/walletcreatefundedpsbt_addinputs
	# Needs review: 16378 Sjors:2019/07/send
	# Needs mucho review: 16546 Sjors:2019/08/hww-box2 # -signer
	# Depends-on-16546: 16549 Sjors:2019/08/hww-qt
	# FIXME: Needs rebase on HasPermission etc FIXME: Breaks p2p_blocksonly ; 16682 blocksonly_violators-0.18.1						last=5ff415d9af jnewbery/2019-08-disconnect-blocksonly-violators
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs intense review: 16702 p2p: supplying and using asmap to improve IP bucketing in addrman
	# Needs review (and BIP finalisation?): 16748 dongcarl:2019-07-addrv2v4
	16795 rpc_spk_decode_desc-0.18				a439ac6e97d	last=dcd5c4a5773 instagibbs/decode_descriptor
	16807 bech32_error_detection-0.19+knots		aab3d39d958	last=19e9def6902 meshcollider/201909_bech32_error_detection
		# NOTE: Minor diff-minimisation, dropped relnotes, added autodetect hack
# TODO: Add bech32 error detect GUI
	# Meh, needs review? 16939 ajtowns:201909-avoid-dns-if-addrman-populated
	16964 gui_sendcoins_yes-0.19+knots			d791163d315	last=a649cc6a17b instagibbs/sendcoins_yes
		# + #17463 implicitly
	16944 gui_send_psbt-0.19+knots				ed6b0d01ac1	last=c6dd565c882 Sjors/2019/08/gui-send-psbt
		# NOTE: If removing, also drop #17587
	17587 gui_watchonly_balance-0.19+knots		31ed2f437b1
	# Needs concept ack: 16981 LarryRuane:reindex-speedup
	17034 bip174_versions-0.18					5e9c2b5314c	last=dd1a5cac06e achow101/bip174-extensions
	17056 desc_sortedmulti-0.19					add48f7dbed	last=4bb660be90a achow101/sortedmulti-desc
		# Held back doc/relnotes
# TODO: Do we want a multi67 too? (Can descriptors deviate from Core?)
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	17125 gui_verifymsg_tips-0.7				9863af566c1  # gui: Add toolTip and placeholderText to --sign--verify message fields
	17186 gui_signmsg_tip-0.7					d2aa3213ace  # gui: Add placeholder text to the sign message field
	17195 gui_sendamt_placeholder-0.10			1d890822db4  # gui: send amount placeholder value
	#TODO: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options?
		# TODO: Diff-minimise
		# Partial rebase at f2fefb51511 (on v0.19.0 tag!)
	# Needs review: 17219 Sjors:2019/10/change-without-keypool
	#TODO: Android packaging? #16110 + #17227 + #17396?
	# Needs review: 17268 JeremyRubin:mempool-experiments-2  # Epoch Mempool
	# Needs fix: 17355 za-kk:oct-19-17174
	17360 gui_fee_hide_tooltip-0.11				803b3477573
	17437 rpc_wtx_blockheight-0.19				3074b807e41
	16432 gui_overview_privacy-0.19+knots		87fc6470bb6	last=ea1fb691c9c
		# NOTE: Dropped monospace font / justify hack in privacy mode
		# Ensure copying balances isn't annoying
		# Should balances be forced monospace normally just for masking??
	16442 neutrino-0.19+knots					61be9bd759d	last=459aead0e66
	# TODO: Diff-minimise: 16463 achow101:bip174-xpub
	# TODO: Support Knots policies: Minimised 16490 marco/1907-rpcMempoolWhyReplacable
	# TODO: Rework 17132 over Tor for Knots only (and maybe generic alert instead of update-specific)
	# Needs review: 17428 p2p: Try to preserve outbound block-relay-only connections during restart
	# TODO: 17492 instagibbs/gui_bump_psbt
	# Needs review/undraft: 17509 gui: save and load PSBT
	# TODO 17529 rpc: Faster getblock using PureBlock
	17631 rest_blockfilter-0.19					e8d30213c37	last=3ab6abcc4dd matt/2019-11-filter-rest
		# NOTE: Dropped unrelated extra commits
	17636 guisettings_opt-0.19					59a6abab328	last=5266efa964b emilengler/2019-11-guisettings
	# Needs work: rpc: Make __cookie__ user immune to rpcwhitelist #17815
# Non-upstreamed functionality:
	-     restore_blockmaxsize					cd1524fce7e
	7107 qtnetworkport							7c4f5374b38	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.19+knots				e1abac3209a  # Latest code now
	11082 rwconf-0.19							fcebdd4f879	last=956a76cc852 rwconf
	7510 rwconf_gui-0.19+knots					dc4cff40dfa	last=8ff7132eef3 rwconf_gui  # accidentally rebased on master :)
	-    rwconf_gui_plus-0.19+knots				5e5122c6dee
	-    preserve_unsupported_keyflags			662dcea6da5
	 559 accept_nonstdtxn						e9a7ace3456
	 929 tbc									141e8d672cc
	 553 bugfix_qt_uri_amount_parser			d0f7e68500e
	-    mining_priority						8883f192d19  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					4f1b78fdab1
	5891 qt_console_history_persist-0.19+knots	65a00063f86	last=ea852deea35 qt_console_history_persist
	7219 rbf_opts-0.19+knots					0f84b26124e
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					43946395be7
	10282 timebomb_knots						112f35a113f
	-     gui_wallet_displayname-0.19			081249b7274	# Latest code now
	-     gui_request_payment_label-0.19		4b2b8876f21
	n/a  checkpoint_update-0.19					eaec9c219a2
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				8d9611e3a15
	-    bytespersigopstrict-0.19+knots			6e2aa1182aa
	9749 unique_spk_mempool-0.19+knots			9b96faf1599
	-    bloom_default-0.19+knots				ed8d913be1e
	-    rwconf_policy-0.19+knots				291bc8d0326
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.19							bed51c71669
# BRANDING:
	n/a  knots_branding-0.19					88bb449295d
#FIXME: Check there are no menu icons
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: check for 'false' instead of ALLOW_ANY in addArgs
	n/a  (cherrypick=9600fe90fb2e446cac)		03e2845c453	# doc/{bips,files}
	n/a  (bump_version=Knots:20200104)			58e82d1e2b4
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=9fc3c810bff)				bb56b215bd8  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=44c11925250)				101af2f7133  # translation update
	n/a  (cherrypick=f3a34217c00)				c94cedc20e1	# update manpages (build first)
# NOTE: use git diff --minimal for patches!

# TODO: Try Snap package stuff documented in doc/release-process.md
