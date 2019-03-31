timestamp 2019-03-28 06:10:04
lastapply no-merge

#.. checked up to PR #15045

checkout 7bcf90cb01
@0.18.x-syslibs
	5872 subdir_incl_compat						8d02952dc5
	2241 sys_leveldb-0.17						ad8b47a71f
	5416 sys_libsecp256k1						9431f6a346
	7485 sys_univalue_def						68d5c1afea
	13788 bugfix_asm_opt						a89a982730
	13789 bugfix_asm_pragmas					417bbb2b56
	-     bugfix_asm_leveldb_check				d6fa287448
@0.18.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							e05acaeb4c
# FIXES:
	14968 laanwj/2018_12_http_bind_error		a557a2af18
	-     http_bind_error+extra					8261704f7f
	9524 marco/Mf1701-qaPruning					0482515b41
	10731 log_more_uacomment					d5d543625c
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	14485 fadvise								ff6b7f3165
		# Was #12491
	14501 fsync_dir								f9011e0e3a
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	13084 sipa/201804_keepnegone				e0d0819607
	13608 -										bd04861325  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs review: 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	-     bugfix_rpc_getbalance_hacky			0c15734378
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	14818 bugfix_test_rpc_psbt					c149f71838
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
# FUNCTIONALITY:
	14066 gitian_power64						177d8f6828
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.18					fec67ba0a7	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							54cf2c6aa2
	15704 win32_defines_globally
	9245 ionice									3cc8f13484
	-    ionice_win								3f14b2ea93
	8501 old_stats_rpc-0.18						22eee1203a	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.18						a66d251bd3	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible					a3a5333707
	9504 dumpmasterprivkey-0.18					bcc1eb350a	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							efe3f14ed1
	10615 multiwallet_rpc						0f022f1844
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	10554 zmq_wtx-0.18							45d6115d31	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					ea03333e2d
	10593 relax_invblk_punishment				0ff280e5a8
	10594 whitelist_outgoing					2de5c391b3
	10350 filtered_witblock-0.17				1ec90f1975	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								43b88be136
	10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	11256 rpc_mempoolentry_weight				9016c44308	last=d4b0d81b58
		# rebased to #14649 rpc_mempoolentry_weight
	-     rpc_mempoolentry_txhash				4ac64860bb
	11413 explicit_fee-0.17						9ee958e460	last=8cd3ffefbe kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	11750 -										22b0c49593 # Multiselect in coincontrol treewidget and display selected count
	11765 rest-blockhash-endpoint-0.17			1e74ec6462	last=1323df9ff1 # [REST] added blockhash api, tests and documentation
		# TODO: ^ needs to be a backward compatibility layer for 14353, and document deprecation
	11770 rest_fee-0.17							2fcfb53e3e	last=d074e0b8ca  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath-0.17.1	cc8a46f65f	last=17d609ce26 bugfix_dumpwallet_hdkeypath
	12096 bumpfee_reduce_output-0.17			2c9f95670b	last=5b37cc17b4 kallewoof/better-bumpfee
	12677 listunspent_ancestorinfo				e94e840cb5
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.17						6f33a8130a	last=8c45d93b0e
	# TODO ? 12792 w/ renamed param
	12911 signrawtx_showfees-0.17				c244e05b04	last=4cd8db17d5 kallewoof/sign-show-fees
	12965 scriptthreads-0.17					ae31010942	last=dfab6c6866 jonas/2018/04/svt
	13008 rpc_mempool_vsize-0.17+knots			c38dd8b58e	last=3bc922d79c  # rpc: Rename size to vsize in mempool related calls
		# NOTE: Minified & made deprecation softer
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.17					93c1f69e72	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.17_asm_pragmas		c93d46a320
	13339 walletnotify_w-0.17					835d6f86c2	last=71d70632ee promag/2018-05-walletnotify
		# held back cef0327afd..71d70632ee Windows porting due to copyright issues (and bugs?)
	# Needs work: 13541 wallet/rpc: sendrawtransaction maxfeerate
	# Needs work: 13756 wallet: -avoidreuse feature for improved privacy
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs review: 13989 add avx512 instrinsic
	# Needs work: 13990 WIP: allow fee estimation to work with lower fees
	# Needs rationale: 14019 Import pubkeys when importing p2sh with importmulti
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	14137 win_taskbar_progress-0.17+knots		89f6f8f532	last=18eb4dbb8a
	15023 gui_node_rpcconsole-0.17				c52c82eb6f  # PART OF c52c82eb6f
	14641 fundraw_minconf-0.17					a01f4e2dfc	last=78c9eef211 promag/2018-11-fundrawtransaction
	14687 zmqkeepalive-0.17.1+knots				106e00a4df	last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# needs completion: 14912 external signers WIP
	# needs review: 14898 nextpagepointer & list ordering options for listtransactions
	# CHANGES WALLET FORMAT, wait for Core: 15006
# Non-upstreamed functionality:
	-     restore_blockmaxsize					3c5d43ee60
	7107 qtnetworkport							e2c10b2bc4	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.17.1+knots				c2d1db0fa4  # Latest code now
	11082 rwconf-0.17							f327d3d64a	last=31edb2c940 rwconf
	7510 rwconf_gui-0.17+knots					de57a85c36	# Latest code now
	5916 legacy_keyorigin						9f0fa134b4
	 559 accept_nonstdtxn						c75b8f41dc
	 929 tbc									8a786470c7
	 553 bugfix_qt_uri_amount_parser			b7591fd219
	-    mining_priority-0.17.1					ff0b793b92  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					7501a70af8
	5891 qt_console_history_persist				acfbf6559d
	7219 txrepl_fullrbf							cd85811a08
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						6a405895cc
	12146 opt_wallet_segwit2					871a84fd1f
	-     gui_wallet_displayname				0b683f45dd
	n/a  checkpoint_update-0.17					79b61387b0
	# for 0.18: revert 14608 qt: Remove the "Pay only required fee..." checkbox
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				1d2b9dc385
	-	 bytespersigopstrict-0.17.1+knots		42b966de58
	9749 unique_spk_mempool-0.17.1+knots		a7f738f776
	-    rwconf_policy-0.17+knots				9e791a87ba
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.17+knots					acafbba7f0
# BRANDING:
	n/a  knots_branding-0.17					bc8d7f2785
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
	n/a  (cherrypick=8358b599adc18aba52)		ef1c8847d7	# doc/{bips,files}
	n/a  (bump_version=Knots:20181229)			d7d0aa3311
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=edf2c1ee88)				1abe270eeb  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=8068b12971)				bf06a386cc  # translation update
	n/a  (cherrypick=8f5b2aca94)				ab05daa871	# update manpages (build first)
# NOTE: use git diff --minimal for patches!
