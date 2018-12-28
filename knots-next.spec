timestamp 2018-12-28 03:02:11
lastapply no-merge

#.. checked up to PR #15045

checkout v0.17.1
@0.17.x-syslibs
	5872 subdir_incl_compat						fab56bbc56
	2241 sys_leveldb-0.17						8f71c67ab5
	5416 sys_libsecp256k1						470e5cde3d
	7485 sys_univalue_def						835bd1b30d
	5618 separate_utils_only-0.17.1				895c00e72d
	12246 separate_utils-0.17.1					e7b7320d18	last=a2a04a5abb separate_utils
	11622 bip70_disable-0.17					5dd29bbc25	last=7ecca66062
		# pulled rebase from 11622 + 14564
	13788 bugfix_asm_opt						6ee96c0463
	13789 bugfix_asm_pragmas					4bb4e1c000
	-     bugfix_asm_leveldb_check				a208ef963a
@0.17.x-knots
# TESTS:
	13724 symbol_check-0.17						75be66d7f6
	14036 travis_sanitizers-0.17				421f9bedc1
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							02e8945abd
# FIXES:
	14968 http_bind_error-0.17					78be09e03f								last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra-0.17			d107faad26
	9524 marco/Mf1701-qaPruning					f060307a06
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						e7c5de2e76
	10731 log_more_uacomment-0.17.1				e4da8b59c1	last=aaba5976bd log_more_uacomment
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	# ^ 11634 walletlocks-0.16						7914050bdb	last=491ec75b9f
		# held back annotations, and minimised patch
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
	14485 fadvise								dc804f8ac8
		# Was #12491
	14501 fsync_dir								347120a02f
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	13084 sipa/201804_keepnegone				7655a41bef
	# Requires 11739, which touches too much consensus logic: minimized 13120 MarcoFalke:Mf1805-segwitGenesisPolicy
	13159 handle-reopen-failed-0.17				0b84cad689
		# minimised diff
	13608 -										a599a3f94e  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs review: 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	13910 -										386938899d
	-     bugfix_rpc_getbalance_hacky-0.17.1	00b0abcba2
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	14818 bugfix_test_rpc_psbt-0.17.1			b038758689						last=c87fc71f7e bugfix_test_rpc_psbt
	14819 bugfix_test_mempool_accept			5805a4cc78
	14228 disable_systray_if_not_avail-0.13		2548a85a55
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	14517 fix_param_min_to_systray-0.15			9d059ba159						last=93009618b6
	# Needs review? 14594 qt: Fix minimized window bug on Linux
	14380 fix_unknown_change_size-0.17			7f725ee937
# FUNCTIONALITY:
	14066 gitian_power64-0.17					69ba45d274								last=02ba4890bb gitian_power64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.17.1					bf9c29aadd	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys-0.17.1					ce37482748	last=e341211bf7 sweepprivkeys
	9245 ionice									454b82fa0e
	-    ionice_win								14edba2667
	8501 old_stats_rpc-0.17.1					98e756b31d	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.17						5dab00ca28	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9332 pr9332-0.17							9b9f68b0b3										last=98ea64cf23  # Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					5fbfe0f6db
	9504 dumpmasterprivkey-0.17					c8739ca494	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch-0.17						d0777346f2	last=654f66d9e0 gui_netwatch
	10615 multiwallet_rpc						3e3258269e
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	10554 zmq_wtx-0.17.1						133d79dc78	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					9c96e27e6a
	10593 relax_invblk_punishment				b94fff3d72
	10594 whitelist_outgoing					53e0bbdc03
	10350 filtered_witblock-0.17				f21196114b	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								4687f179d7
	10730 scriptflag_strings-mini-0.17			4df309bb18	last=e2e183bc1f
	n/a   script_debugger-mini					72fdc1f40d	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	11256 rpc_mempoolentry_weight				7c1823ec81	last=d4b0d81b58
		# rebased to #14649 rpc_mempoolentry_weight
	-     rpc_mempoolentry_txhash				bde147ee02
	11413 explicit_fee-0.17						97d3c808f4	last=8cd3ffefbe kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.17				e6a90c56ac	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	11750 -										e5b73fb9f8 # Multiselect in coincontrol treewidget and display selected count
	11765 rest-blockhash-endpoint-0.17			fe3e7cf740	last=1323df9ff1 # [REST] added blockhash api, tests and documentation
		# FIXME: replace with 14353 if it gets merged?
	11770 rest_fee-0.17							edfa0ccb98	last=d074e0b8ca  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath-0.17.1	c112f20471	last=17d609ce26 bugfix_dumpwallet_hdkeypath
	12096 bumpfee_reduce_output-0.17			a07d3009f7	last=5b37cc17b4 kallewoof/better-bumpfee
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters, 14121
	12677 listunspent_ancestorinfo				8a26976af1
	# Not sure if safe with 0.16: 12559 promag/2018-02-avoid-cs_main-lock
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	12676 -										3e365f5788  # Show "bip125-replaceable" flag, when retrieving mempool entries
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.17						a0b5e32093	last=8c45d93b0e
	12783 disable_appnap-0.17					b7a65bccd4	last=1e0f3c4499
		# Retained older inhibitor too
	# TODO ? 12792 w/ renamed param
	12818 -										bb1279f480  # [qt] TransactionView: highlight replacement tx after fee bump
	12911 signrawtx_showfees-0.17				3bae99f6f3	last=4cd8db17d5 kallewoof/sign-show-fees
	12965 scriptthreads-0.17					36a25f41ec	last=dfab6c6866 jonas/2018/04/svt
	13008 rpc_mempool_vsize-0.17+knots			350dc594f8						last=3bc922d79c  # rpc: Rename size to vsize in mempool related calls
		# NOTE: Minified & made deprecation softer
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	13152 rpc_getnodeaddress-0.17				3e30e761aa							last=a2eb6f5405
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.17					15b0ee4d3a	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.17_asm_pragmas		e5c22e9aa2
	# TODO: Possible performance concern 13310 promag/2018-05-replayblocks-progress
	13339 walletnotify_w-0.17					7d9abdb935	last=71d70632ee promag/2018-05-walletnotify
		# held back cef0327afd..71d70632ee Windows porting due to copyright issues (and bugs?)
	# broken? 13399 rpc_submitheader-0.16								last=fa7d7dd34c marco/Mf1806-rpcBlockHeader
		# held back removal of duplicate-header submission check
	# Needs work: 13541 wallet/rpc: sendrawtransaction maxfeerate
	# Needs work: 13756 wallet: -avoidreuse feature for improved privacy
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# TBD (part of) 13926 [WIP] [Tools] bitcoin-wallet-tool
	# TESTS FAIL: 13932 achow101/psbt-util-rpcs
		# Rebased ba5f9058f6 as c75ca1a28c
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	13987 rpc_getpeerinfo_minfeefilter-0.17		a178b0ffd6					last=5778bf95d9 ajtowns/201808-peerinfo-minfee
	# Needs review: 13989 add avx512 instrinsic
	# Needs work: 13990 WIP: allow fee estimation to work with lower fees
	# Needs rationale: 14019 Import pubkeys when importing p2sh with importmulti
	# Changes wallet? 14021 Import key origin data through importmulti
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	14060 zmqhwm-0.17.1+knots					92c60236d9
		# NOTE: Needs explicit args added for wallettx merge
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	14137 win_taskbar_progress-0.17+knots		68ad53729c					last=18eb4dbb8a
	14133 mac_systray_showhide-0.17				37e2c8ab66
	14383 disablewallet_systray-0.17+knots		601e631af6
		#+15023 gui_node_rpcconsole-0.17
	14573 window_menu-0.17+knots				dfd5589276
		#+14979
	14410 getaddressinfo_ischange-0.17			9b8e4c8aed
	# too complex? 14454 Add SegWit support to importmulti
	# needs review: 14481 Add P2SH-P2WSH support to listunspent RPC (with changes?)
	# Needs review: 14491 Allow descriptor imports with importmulti
	14641 fundraw_minconf-0.17					d2077e289e								last=78c9eef211 promag/2018-11-fundrawtransaction
	14687 zmqkeepalive-0.17.1+knots				9b7594b5ee							last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# Needs review: 14929 net: Allow connections from misbehavior banned peers (as alternative to relaxed banning?)
	# needs completion: 14912 external signers WIP
	# needs review: 14898 nextpagepointer & list ordering options for listtransactions
	# CHANGES WALLET FORMAT, wait for Core: 15006
# Non-upstreamed functionality:
	-     restore_blockmaxsize					341b5cf2c9
	7107 qtnetworkport							d1e09aa575	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.17.1+knots				dcf6e53df6  # Latest code now
	11082 rwconf-0.17							3350ff3d48	last=31edb2c940 rwconf
	7510 rwconf_gui-0.17+knots					4f895d0dfa	# Latest code now
	5916 legacy_keyorigin						004f3fa7fd
	 559 accept_nonstdtxn						e1482d0b28
	 929 tbc									3bac94d8a8
	 553 bugfix_qt_uri_amount_parser			73202a3297
	-    mining_priority-0.17.1					ea99862732  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					52d182e768
	5891 qt_console_history_persist				186a6c2898
	7219 txrepl_fullrbf							c6dfcb30c7
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						370b5d2c96
	12146 opt_wallet_segwit2					a7b18054b1
	-     gui_wallet_displayname				fbfee0347e
	n/a  checkpoint_update-0.17					1c1f88277a
	# for 0.18: revert 14608 qt: Remove the "Pay only required fee..." checkbox
# POLICY:
	14970 dnsseed_emzy							e4b1648a9b
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				19dc5cdfe2
	-	 bytespersigopstrict-0.17.1+knots		496caf39e9
	9749 unique_spk_mempool-0.17.1+knots		e52fa51327
	-    rwconf_policy-0.17+knots				c3488b608e
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.17+knots					16f4d4e1b4
# BRANDING:
	n/a  knots_branding-0.17					dea7f2fc02
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
	n/a  (cherrypick=8358b599adc18aba52)		720b0c2b7a	# doc/{bips,files}
	n/a  (bump_version=Knots:20181228)			6de5a1e0de
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=9b2958cf99)				e2a01423d7  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=8068b12971)				ff3d85d4ee  # translation update
	n/a  (cherrypick=8f5b2aca94)				1d994af0ef	# update manpages (build first)
# NOTE: use git diff --minimal for patches!
