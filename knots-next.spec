timestamp 2018-10-15 09:39:42
lastapply no-merge

#.. checked up to PR #14101

checkout v0.17.0.1
@0.17.x-syslibs
	5872 subdir_incl_compat						c134703e62
	2241 sys_leveldb-0.17						3510c4e6eb
	5416 sys_libsecp256k1						f79618bee8
	7485 sys_univalue_def						79f1d9208d
	5618 separate_utils_only					0c45680e8e
	12246 separate_utils-0.17					c09d510d89	last=a2a04a5abb separate_utils
	13788 bugfix_asm_opt						4324338adf
	13789 bugfix_asm_pragmas					b8d31df2f8
	-     bugfix_asm_leveldb_check				54a0d3a45b
@0.17.x-knots
# TESTS:
	13724 symbol_check-0.17
	14036 travis_sanitizers-0.17
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer
# FIXES:
	14618 http_debug_rejects-0.15							last=ab8c6f24d2
	9524 marco/Mf1701-qaPruning					891509bbdf
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						938ce42c1a
	10731 log_more_uacomment-0.17				71ccec6290	last=aaba5976bd log_more_uacomment
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	# ^ 11634 walletlocks-0.16						7914050bdb	last=491ec75b9f
		# held back annotations, and minimised patch
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
	14485 fadvise								1c929547a4
		# Was #12491
	14501 fsync_dir								b22514b73f
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	13084 sipa/201804_keepnegone				80751fee66
	# Requires 11739, which touches too much consensus logic: minimized 13120 MarcoFalke:Mf1805-segwitGenesisPolicy
	13159 handle-reopen-failed-0.17				56be2f61a6
		# minimised diff
	13608 -										6fc500c51d  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs review: 13674 Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	13910 -
	14596 bugfix_createMS_named_addresstype0.17				last=d8bf1071cf bugfix_createMS_named_addresstype
	-     bugfix_rpc_getbalance_hacky-0.17
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	14403 revert_qt_poodle
	14818 bugfix_test_rpc_psbt-0.17							last=c87fc71f7e bugfix_test_rpc_psbt
	14819 bugfix_test_mempool_accept
# FUNCTIONALITY:
	14066 gitian_power64-0.17								last=02ba4890bb gitian_power64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.17					1d3cc741e6	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys-0.17						ed43377924	last=e341211bf7 sweepprivkeys
	9245 ionice									3400eeb80d
	-    ionice_win								3303deb376
	8501 old_stats_rpc-0.17						e8fc393fa6	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.17						74347db52f	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9332 pr9332-0.17										last=98ea64cf23  # Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					d787eb624d
	9504 dumpmasterprivkey-0.17					4c84494958	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch-0.17						ded9e72741	last=654f66d9e0 gui_netwatch
	10615 multiwallet_rpc						e646c77988
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	10554 zmq_wtx-0.17							5f5cc19ac3	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					dd2a168c2a
	10593 relax_invblk_punishment				e7398a9b8d
	10594 whitelist_outgoing					20d5c10ce0
	10350 filtered_witblock-0.17				e3c0fcef0a	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								a6d4274f12
	10730 scriptflag_strings-mini-0.17			98813105ab	last=e2e183bc1f
	n/a   script_debugger-mini					019bcb76b8	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	11256 rpc_mempoolentry_weight				3e005b804a	last=d4b0d81b58
		# rebased to #14649 rpc_mempoolentry_weight
	-     rpc_mempoolentry_txhash				e79db541a0
	11413 explicit_fee-0.17						472b79c25e	last=8cd3ffefbe kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.17				4bfb75be0c	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	11750 -										3b3fbcbb3e # Multiselect in coincontrol treewidget and display selected count
	11765 rest-blockhash-endpoint-0.17			7fca723689	last=1323df9ff1 # [REST] added blockhash api, tests and documentation
	11770 rest_fee-0.17							7ba67d2910	last=d074e0b8ca  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath-0.17		51d373acca	last=17d609ce26 bugfix_dumpwallet_hdkeypath
	12096 bumpfee_reduce_output-0.17			5d92f4453b	last=5b37cc17b4 kallewoof/better-bumpfee
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters
	12677 listunspent_ancestorinfo				2642343fb6
	# Not sure if safe with 0.16: 12559 promag/2018-02-avoid-cs_main-lock
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	12676 -										d0871f6a99  # Show "bip125-replaceable" flag, when retrieving mempool entries
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.17						3a58144b6c	last=8c45d93b0e
	12783 disable_appnap-0.17					389dc7a96f	last=1e0f3c4499
		# Retained older inhibitor too
	# TODO ? 12792 w/ renamed param
	12818 -										a1c7d44271  # [qt] TransactionView: highlight replacement tx after fee bump
	12911 signrawtx_showfees-0.17				613381e9c4	last=4cd8db17d5 kallewoof/sign-show-fees
	12965 scriptthreads-0.17					ec38b2650d	last=dfab6c6866 jonas/2018/04/svt
	13008 rpc_mempool_vsize-0.17+knots						last=3bc922d79c  # rpc: Rename size to vsize in mempool related calls
		# NOTE: Minified & made deprecation softer
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	13152 rpc_getnodeaddress-0.17							last=a2eb6f5405
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.17					6a93a81e3e	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.17_asm_pragmas		7d916e293f
	# TODO: Possible performance concern 13310 promag/2018-05-replayblocks-progress
	13339 walletnotify_w-0.17					10c0ad0430	last=71d70632ee promag/2018-05-walletnotify
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
	13987 rpc_getpeerinfo_minfeefilter-0.17					last=5778bf95d9 ajtowns/201808-peerinfo-minfee
	# Needs review: 13989 add avx512 instrinsic
	# Needs work: 13990 WIP: allow fee estimation to work with lower fees
	# Needs rationale: 14019 Import pubkeys when importing p2sh with importmulti
	# Changes wallet? 14021 Import key origin data through importmulti
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	14060 zmqhwm-0.17+knots
		# NOTE: Needs explicit args added for wallettx merge
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs work: 14090 [windows] progress bar in task bar
# Non-upstreamed functionality:
	-     restore_blockmaxsize					7b4ef75162
	7107 qtnetworkport							86a22ede93	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.17+knots				821e79eca8  # Latest code now
	11082 rwconf-0.17							7ac8e5584d	last=31edb2c940 rwconf
	7510 rwconf_gui-0.17+knots					f5d2f52fba	# Latest code now
	5916 legacy_keyorigin						6e769279fa
	 559 accept_nonstdtxn						f07335d45f
	 929 tbc									065b18ab4a
	 553 bugfix_qt_uri_amount_parser			99f0b1f4ca
	-    mining_priority-0.17					9a90dc34e7  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					525633a9d5
	5891 qt_console_history_persist				90c6f0a538
	7219 txrepl_fullrbf							a9fd5b6577
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						db079c9033
	12146 opt_wallet_segwit2					d855625b12
	-     gui_wallet_displayname
	n/a  checkpoint_update-0.17					a9c8a9ef4c
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				82becc9391
	-	 bytespersigopstrict-0.17+knots			fa99fdb901
	9749 unique_spk_mempool-0.17+knots			df8e9047db
	-    rwconf_policy-0.16+knots				2786f6f8d6
		NOTE: prune moved to rwconf_gui
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	-    txrepl_fullrbf_default+knots			f5c7ca2cd9	last=61fae13df1 txrepl_fullrbf_default
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.16+knots					2a4168de17
# BRANDING:
	n/a  knots_branding-0.16					ef04113ea1
FIXME: Check includes use <>
FIXME: Check hidden_args has anything removed (possibly conditional)
	n/a  (cherrypick=1a7c7b4b97ee6bd79c)		17c327ad76	# doc/{bips,files}
	n/a  (bump_version=Knots:20180730)			2f197b2b7b
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=950bd75f29)				0a1f46883d  # release notes: write/update, including change log and credits
DOCUMENT libevent now required ? and protobuf/bip70 too
DOCUMENT 	MISSING PARTS 12196 sweepprivkeys+scantxoutset			52dfb4735e	last=be98b2d9a8 jonas/2017/12/utxo_sweep
			# modified to remove scan-by-address garbage
			# held back feature removals
DOCUMENT dropped #11653
DOCUMENT dumpwallet hdmasterkeyid replaced by hdseedid
DOCUMENT listreceivedby* key_origin deprecation
DOCUMENT #11413 changed from sat/kB to BTC/kB
NOTE: avoidpartialspends=false now has behaviour change
MERGE 9271166a8a relnotes
MERGE doc/release-notes-*.md
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=6c11f79434)				11d53f8eb1  # translation update
	n/a  (cherrypick=fa03d8db65)				427450894c	# update manpages (build first)
# NOTE: use git diff --minimal for patches!
