timestamp 2020-08-15 06:18:02
lastapply no-merge

#.. checked up to PR #19728 / gui #61

checkout origin/master
@0.20.x-syslibs
	5872 subdir_incl_compat						500e007903f
	2241 sys_leveldb							1417948c866
	5416 sys_libsecp256k1						c5a440728e9
	7485 sys_univalue_def						b9b4cf77ff4
	13789 bugfix_asm_pragmas					369a7f5afa3
	-     bugfix_asm_leveldb_check				02dc65eba04
	15155 test_external_bcli					9de9dca3491
	# Needs review: 20121 secp256k1_allow_bignum
@0.20.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							701d4ca9a34
	17402 travis_ppc64							aa3052ac519	last=1d684f05341 elichai/2019-11-powerpc64
	18750 -										29118b6ad18	last=ba8950ee013  # ignore_external_warnings
		# TODO: Address my own review comments if vasild doesn't in time
# FIXES:
	18818 fix_gitian_src_202004					57102d3df4c
	18902 fix_gitdir_again						3d6e49e807e
	18427 2020mingwthrd-mini					380c86e8d16	last=7fe49671dd4 2020mingwthrd
	18490 bugfix_symcheck_pe_case				e32605dd3c2
	17828 p2p_log_categories					7a40b3433d6	last=04960621582 practicalswift/log-categories
	14968 laanwj/2018_12_http_bind_error		a57f6aa8b6b	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					f1de252e1b4
	9524 marco/Mf1701-qaPruning					bd414d85961	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					7b23b0d08e7
	14485 fadvise								479d173ba1b
		# Was #12491
	14501 fsync_dir								fc8469acb68
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
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
	# Needs review: 17543 wallet: undo conflicts properly in case of blocks disconnection
	18095 -										c6dfc3206fd	last=2f06e9d12bb  # Fix crashes and infinite loop in ListWalletDir()
	18133 bugfix_qvalidlineedit					49b42b1e149
	18194 bugfix_gui_edit_sendaddr-mini			9fada3c674d	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs work: 18189 -  # Add error handling to all boost filesystem functions
	# Needs clarity? 18232 WIP test: Check that wait_until returns if time point is in the past
	18335 -										d87686f9b3a	last=8dd5946c0b7  # bitcoin-cli: print useful error if bitcoind rpc work queue exceeded
	# Needs concept ACK: 18466 -  # rpc: fix invalid parameter error codes for {sign,verify}message RPCs
	18729 intro_dont_change_user_prune			927b68d75c4
	18766 blocksonly_no_feeest-0.21				4c85e2551bc	last=4105c63a67a
		# diff-minimised
		# HELD BACK 33ca3590243...4105c63a67a due to refactor complication
	# Needs fixes: 18964  # rpc, wallet: Scan mempool after import*
	# Needs concept review & possible Knots adjustments: 19001 qt: bugfix unsupported QLocale languages
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19362 rpc_scantxoutset_reset_progress-0.17	663b923b439	last=8c4129b4540 prusnak/rpc-scantxoutset-reset-progress
	19502 bugfix_listwalletdir_errors-mini		48100d93e96	last=1e77a8d5a4f bugfix_listwalletdir_errors
	19419 listwalletdir_skip_data-0.21+knots	c25545c6d7c	last=3f9cc0cd736
		# NOTE: modified to use std::set and diff-minimise
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect
	# Needs review: g18    hebasto:200701-peer
	g20   hebasto-g/200702-tooltip				71aa9003e5c	last=6ed4bcabc1a
	# Needs review: 19645 ariard:2020-08-wtxid-replacement
	g43   hebasto-g/200803-encrypt				ad43955a127	last=20c9e035543
	# Needs review: g59 hebasto-g/200814-rpc
		# NOTE: WAS Needs fix?? 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
# FUNCTIONALITY:
	-     restore_win32-0.20+knots				9dbb4bb8313
	-     restore_linux32						275c3f2b076
		# NOTE: gitian only
	# 0.21 TODO: #19751 comes out of #14066 below
	14066 gitian_power64-0.20+knots				5d7416dc553	last=5155e99f455 gitian_power64
	# Need #14066 ? due to:
		#19525 z_separate_code-0.17					34141a5b841
			# NOTE: Carries a commit from master #14066 to avoid bogus .plt security check on PPC64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.20					b2b72634313	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							3c24aa35b17
	9245 ionice									13605834424
	-    ionice_win								ca85c802d4c
	8501 old_stats_rpc-0.20						406c8006f29	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.20						402b6f3f1a9	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible-0.20			ad1414bcc50 last=1befffc0b48 mempool_dat_extensible
		# 0.21 TODO: adapt test/functional/mempool_compatibility.py
		# Rebased in #19488
	9504 dumpmasterprivkey-0.20					3b7a3f8ac6f	last=07fc81109a
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							6319a2247ca
	10615 multiwallet_rpc-0.19					e6abc3c24b3	last=8c079fbff7c multiwallet_rpc
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	10554 zmq_wtx-0.20							76276a5d5b4	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	# needs concept compat with above & review: 17878 promag:2019-01-zmqpubwallettx
	12674 rpc_onetry_nonpriv					f0764bb161b
	10593 relax_invblk_punishment				4f45db31a80
	# Needs copyright header: 17311 RandyMcMillan:fix-background-svg
	# Needs fixing/review: 17303 MarcoFalke:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	10594 whitelist_outgoing-mini-0.20+knots	3cd212d495f	last=d465ea1e057 whitelist_outgoing
		#TODO: Split this up?
	10350 filtered_witblock-0.20				250f42bd6ce	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				57c4d73c76d
	14641 promag/2018-11-fundrawtransaction		33cd8edfcf1	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
		# NOTE: held back .gitignore nonsense change & relnotes
	TODO: Compatibility with merged #11413 explicit_fee-0.20+knots				1c65e068ee7	last=25dac9fa652 kallewoof/explicit-fee
		# NOTE: Dropped 4855bc80992 and 4e5fc19d9d9; diff-minimised and:
		# NOTE: Retained compatibility with "EXPLICIT" fee mode, and fixed upper/lower casing
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	11750 coincontrol_multiselect				1bb9bcd76e5	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-0.19							3805e99c89d	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			46b4bdc858b
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
		# NOTE: Competing with #15341
	12677 listunspent_ancestorinfo				b5d1f97cb72
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	12911 rpc_sign_show_fees					97135294f97	last=47b2ba29df2 kallewoof/sign-show-fees
		# NOTE: Rebased as #18479
	12965 scriptthreads-0.20					b324ae42770	last=dfab6c6866 jonas/2018/04/svt
	# Needs review are care (new index): 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.20					859d5652145	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
		FIXME: cherrypick f40dd1dda5e68af77a88abc214e7e1dfb40b04a1
	-     dsha256_power8-0.20_asm_pragmas		81da69b2979
	-     walletnotify_w_win					a7967686d4c
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	14137 win_taskbar_progress					e1dbdd78697	last=18eb4dbb8a
	# wait for Core?: 14707
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	15115 rm_send2self-mini						a5ff336f2ab	last=14bb8db698d rm_send2self
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	15218 postibd_flush							2b5ad4ecd2a	last=d2ecb70d64  # validation: Flush state after initial sync
		# Previously had moved init around to avoid conflict w/ 15367 (now merged)
		# TODO: Rewrite after #17487 is ready/safe to merge
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	15423 tor_socks_port						b7a42a9a040
	15428 tor_gui_pairing-0.20+knots			be06cae0e71	# latest code now
	15421 tor_subprocess-0.20+knots				7f54810b99d	last=f2add182487 tor_subprocess
	# TODO: tor gitian bundle!
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Waiting to be non-WIP: 15487 [WIP] descriptor based wallet serialization and import
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15633 nohbcbfornonwit						305eabd5a3a
		# NOTE: added test fix from sdaftuar/test-15633-2
		# NOTE: 2020-06, upstream was deleted, and origin-pull is NOT up to date!
	# USELESS Shared-lib 15717 Changes to support NAT-PMP
	# Needs work: 18077 hebasto/20200130-natpmp
		# NOTE: Diff-minimised rebase of 2d5d98ce0aa is at c6ff5633b56
		# TODO: Switch to rwconf?
	17795 gui_console_ctrl_d-0.20+knots			47d8d7a7209
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	# NEEDS FIXES: 15845 wallet_fastrescan-0.19							last=faee7b6581f marco/1904-walletFastRescan
		# TODO: Minify and test well
		# OR: 19116 pstratem:2020-05-29-generate-pubkeys
	15836 fee_histogram-0.20					6476c61e5dc	last=b94292a7cb jonas/2019/04/feeinfo
		# NOTE: removed extraneous Bitcoin-Qt.* files
	15861 restore_vbits_warning					ef496a36c32
	# Needs concept ACK and review: 15873 or 16523 Rpc removemempoolentry
	# Needs QA/review: 15946 jonasschnelli:2019/05/prune_blockfilter
		# NOTE: When merging, update GUI neutrino stuff to allow pruning+filters!
	17463 gui_custom_sendyes					06ef790c0b9
	15987 wallet_no_reuse-0.20+knots			fcee9d7e1ff
	-     rpc_gai_txids							b981a160cc4
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	18772 getblock_fees-0.20					89677d99147
	16083 rpc_getblock_prevouts_fees-0.20		7766bcdd2d6	last=dd83c4c925
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Renamed "fees" field to "fee"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# Needs mucho review: 16546 Sjors:2019/08/hww-box2 # -signer
		# NOTE: Bumps boost version!
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# Depends-on-16546: 16549 Sjors:2019/08/hww-qt
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs review (and BIP finalisation?): 19031 Implement ADDRv2 support (part of BIP155)
	16795 rpc_inferred_output_descriptors-0.20	593533e6b91	last=ef91078d672 instagibbs/decode_descriptor
	16807 bech32_error_detection-0.20+knots		9ba289863a6	last=54e107add41 meshcollider/201909_bech32_error_detection
		# NOTE: Minor diff-minimisation, dropped relnotes, added autodetect hack
	-     gui_bech32_errpos-0.20+knots			4c26070eb13  # Latest code
	# Needs concept ack: 16981 LarryRuane:reindex-speedup
	17034 psbt_ver_proprietary-0.20+knots		c688e87d5e5	last=ddaccbc7bbd achow101/bip174-extensions
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	# Needs signing provider stuff - 0.20?: 17211 achow101/fundtx-external-inputs
		# TODO: Move new param to options?
		# TODO: Diff-minimise
		# Partial rebase at f2fefb51511 (on v0.19.0 tag!)
	#TODO: Android packaging? #17227?
	# Needs review: 17268 JeremyRubin:mempool-experiments-2  # Epoch Mempool
	# Needs fix: 17355 za-kk:oct-19-17174
	TODO: Make sure this is sane as merged: 16432 gui_overview_privacy-0.20+knots		8cf7668fdcb	last=8d75115844b hebasto/20190721-privacy
		# TODO: low-priority updates 6920e1236b3..8d75115844b
		# NOTE: Held back ea1fb691c9c..dba83b9dab9
		# NOTE: Dropped monospace font / justify hack in privacy mode
		# Ensure copying balances isn't annoying
		# Should balances be forced monospace normally just for masking??
	# TODO: Split out 18960, 19010, 19044, 19070 (merged)
	18876 neutrino-0.20+knots					723cec97b7b	last=5488ce98cf2 8e5e184e3
		# NOTE: Held back cdf12ea6a5b itself since it demands users actively involved in index state
	18972 neutrino_whitelist-0.20+knots			b02540ef13d	last=f1ebb52cd43
		# NOTE: Excluded refactor
	16463 bip174_xpub-0.20+knots				8e6f8d3cc9c	last=ee0dd3ae1fc achow101/bip174-xpub
		# NOTE: Diff-minimised by excluding moveonly
	# TODO: Support Knots policies: Minimised 16490 marco/1907-rpcMempoolWhyReplacable
	# Needs review: 17428 p2p: Try to preserve outbound block-relay-only connections during restart
	# Needs review: 17529 rpc: Faster getblock using PureBlock
	17631 rest_blockfilter-0.20					bb71d390fea	last=16d8d2da598 matt/2019-11-filter-rest
		# NOTE: Dropped unrelated extra commits
	17636 guisettings-0.20						8319dbc82db	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	# Needs work & concept ACK: 17815 rpc: Make __cookie__ user immune to rpcwhitelist
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	17955 gui_uri_paste-0.20+knots				5053da42d85	last=0139b428923 emilengler/2020-01-paste-bitcoin-uri-button
	17958 rpc_getgeneralinfo-0.20+knots			4a3b2bf65d5	last=cdbd38df131  # getgeneralinfo RPC
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	# Needs review: 18000 -  # Coin Statistics Index
	18014 siphash_optimise_pr18014-0.19			e305c0a192e	last=9ed348ddea3 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks
	18223 blockfilter_v0-0.19					84182b53513	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	18238 ajtowns/202002-bump-notfound			8c1f5a7139f	last=a204d1586ca ajtowns/202002-bump-notfound
	# Needs work/review/completion: 18242 jonasschnelli:2020/03/net_v2
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# ---- BEGIN IN SEQUENCE ----
	# NOW MERGED: 18574, 18653, 18691, 18724, 18594
	19089 cli_getinfo_mwbalances-0.20+knots		9332257e9d8	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
		FIXME: invisible conflcit with merged 19405 rpc_netinfo_conncount_inout-0.20+knots	78f560f7558	last=94a792cc19f jonatack/in-and-out-connections
	19092 cli_getinfo_mw_total_balance-0.20+knots	b2bafd9cba3	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
		# Held back s/several/multiple (& comment changes) because why bother
	# ---- END IN SEQUENCE ----
	18570 wallet_rpc_lastprocessedblock-0.20	5fb71e64dce	last=1e868bbbb1b
	# Needs work? 18611 -  # cli: show default values in config args log
	# TODO: (conflicts with address reuse warning) 18789 achow101:create-unsigned-sendconfdialog OR these two:
		# 18655 achow101:split-bumpfeeaction
		# 18656 achow101:make-unsigned-button
	18689 rpc_dumptxoutset_hr-0.20				aa7b71901bd	last=82046cf7fa3
	18722 O_addrman_unordered_map-0.20			e7fba4623d9	last=d6e782174ec
	18728 intro_prune_size						ee19f9b631f
	19117 rpc_getrpcwhitelist					e5201e7568a
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-0.20+knots	c4e1b0ecbe6
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	TODO: Check for held-back of merged 18991 p2p_getaddr_cache-0.20+knots			17f457ef4d6	last=3bd67ba5a4e  # Cache responses to GETADDR to prevent topology leaks
		# Held back removal of addr from implicit flags (rebased in b78f81553d8a4)
	# Needs concept review: 19043 torcontrol: add -tortarget config
	19093 rpc_testmempoolaccept_fee-0.20		f0de7aa23d5	last=c9781e92a21  # RPC: testmempoolaccept returns transaction fee
	# 0.21 TODO: 19136 achow101:export-descriptor
	# Depends on refactor: 19137 achow101/dumpwalletrecords
	TODO: Check for permission flag conflicts in merged 19191 p2p_permission_download-0.20.1+knots	55fb5d4ac1c	last=fa0540cd46e marco/2006-netPerDow
		# IMPORTANT: Avoid conflicts with PF_ADDR or other permission flags (moved to 1<<18)
	19242 uaappend								d4ad2f71f8b
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
	19463 prune_locks-0.20+knots				50b13a85c7a	last=f4b2ed65ea5 prune_locks
	# Needs work: 19476 promag:2020-07-rpc-mempoolchanges
	# Needs work: 19485 # torcontrol: Create also a V3 ed25519-V3 onion address.
	# Needs review: 19521 # Coinstats Index (without UTXO set hash)
	# Needs work: g4    Sjors:2019/08/hww-qt
	# Needs work: g27   # top to bottom UI layout
	# Needs concept ACK: 19635 -ephemeraltoronion
	TODO: --enable-endomorphism in libsecp256k1
# Non-upstreamed functionality:
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     restore_rejectmsg-0.20+knots			f99fd33ae0a  # Latest code now
	-     restore_blockmaxsize					77a6f199fa5
	7107 qtnetworkport							bf7aeb32a35	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.20+knots				5999c6933c5  # Latest code now
	11082 rwconf								3858d1e74e1
	7510 rwconf_gui								16293b1e43e
		# 0.21 TODO: update neutrino option name
	-    rwconf_gui_plus						be0027f92b2
	-    preserve_unsupported_keyflags			830d18f021a
	 559 accept_nonstdtxn						1da672d42c9
	 929 tbc									c4756a6c311
	 553 bugfix_qt_uri_amount_parser			14443183ee8
	-    mining_priority						d75b4239f99  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					7765ac926bd
	5891 qt_console_history_persist-0.20+knots	c4aaf9bb86f	last=ea852deea35 qt_console_history_persist
	7219 rbf_opts-0.20+knots					da89337a123
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					dfe45d4f91d
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	10282 timebomb_knots						df904a5f8b2
	-     gui_wallet_displayname-0.19			ad59c0b3f14	# Latest code now
	-     gui_request_payment_label-0.19		d89e4408b1d
	n/a  checkpoint_update-0.20					5a868f43b54
# POLICY:
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				71333c3e4b5
	-    bytespersigopstrict-0.20+knots			f921debe480
	9749 unique_spk_mempool-0.20+knots			200fda55358
	-    bloom_default-0.20+knots				cdc7408913a
	-    rwconf_policy-0.20+knots				114a6a96f4c
		#FIXME 0.21: split actual policy changes out to another line
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	7483 svg_icon-0.20							4835bcd3444
# BRANDING:
	n/a  knots_branding-0.20					a65cba08b8d
#FIXME: Check there are no menu icons
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
#FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#TODO: check for 'false' instead of ALLOW_ANY in addArgs
#TODO: Check that we aren't deprcating anything in Core
#TODO: verify src tarball includes rendered_icons incl nsis-header
# TODO: Check build with -fno-common
	n/a  (cherrypick=6b32ed8eb2773d5aa0)		91ea84ade32	# doc/{bips,files}
	n/a  (bump_version=Knots:20200815)			c38be07358d
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=122a503033f)				9efbaf7ee8d  # release notes: write/update, including change log and credits
			# check travis for misspellings
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	# 0.21 TODO: Move manpages before ts (so manpages become part of branding patch)
	n/a  (cherrypick=b9a7c5d663b)				b0c69f9a261  # translation update
	n/a  (cherrypick=7b55b1058fd)				5f5b833b3c2  # update manpages (build first)
# NOTE: use git diff --minimal for patches!

# TODO: Try Snap package stuff documented in doc/release-process.md
