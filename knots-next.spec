timestamp 2019-05-01 06:44:15
lastapply no-merge

#.. checked up to PR #15928

checkout v0.18.0
@0.18.x-syslibs
	5872 subdir_incl_compat						6c5a8384b7
	2241 sys_leveldb-0.17						5a559d82a7
	5416 sys_libsecp256k1						25eb45dedc
	7485 sys_univalue_def						1c81b9312d
	13788 bugfix_asm_opt						82531ed555
	13789 bugfix_asm_pragmas					4e40e9b340
	-     bugfix_asm_leveldb_check				5b92e74444
	15155 test_external_bcli					06be98ae91
@0.18.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							86d0a02988
	# Needs review: 15134 practicalswift:unsigned-char
	15888 test_wallet_implicitsegwit			d89b6ca3b2
	15920 nowallet_hiddenargs_linter-0.18		c0fca3337a
# FIXES:
	15913 bugfix_nowallet_avoidpspends-0.18		a8d0fba07b
	14968 laanwj/2018_12_http_bind_error		dfb7af4b2e
	-     http_bind_error+extra					d40c9b245e
	9524 marco/Mf1701-qaPruning					8ad0a770fd
	10731 log_more_uacomment					b3c26d3780
	14485 fadvise								849065fb57
		# Was #12491
	14501 fsync_dir								dc5d4affe1
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	13084 sipa/201804_keepnegone				0f2a1a86e2
	13608 -										4f6e5c8055  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs fix?? 13674 -													# Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	-     bugfix_rpc_getbalance_hacky			02c4027b72
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	14818 bugfix_test_rpc_psbt					98fa08acd3
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			5e6dfa810f
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 promag:2019-01-loopexit
	15558 dnsoneatatime-0.18					3a4d56e1a5								last=9f36b04fa0 sipa/201903_dnsoneatatime
		# NOTE: Diff-minimised
	15600 lockedpool_dontdump					da41c1aa89
	15651 tor_standard_port						9dca0e5f2a
	15650 fallocate_check-0.18+knots			47496119f7						last=5d35ae3326
	15896 qa_pkgname-0.18						564d03d978									last=fcc443b636 qa_pkgname
	15897 qa_mininode_headers					e711ae6691
	# Needs review: 15909 Use 'CreateProcess' instead of 'wsystem' in 'runCommand' for Windows.
	15911 wcreatefundedpsbt_rbf_fix-0.18		383d986cd2					last=609685107b
# FUNCTIONALITY:
	14066 gitian_power64-0.18					bcecd532f4	last=0c0550a01f gitian_power64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.18					0d00f4560f	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							ce82a395ba
	15704 win32_defines_globally				4ff0cf2ccc
	9245 ionice									3b33123d3a
	-    ionice_win								7c9e8965e8
	8501 old_stats_rpc-0.18						b36e0bd0e1	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.18						e9cff742d4	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible					7f4b597254
	9504 dumpmasterprivkey-0.18					e321b988b7	last=07fc81109a
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							fe943e4b10
	10615 multiwallet_rpc						39d30fe38b
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	10554 zmq_wtx-0.18							287dbf2da5	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					c510abcd41
	10593 relax_invblk_punishment				37d0787fd6
	10594 whitelist_outgoing					182ae11ccf
	10350 filtered_witblock-0.17				2f88d8fe26	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	11256 rpc_mempoolentry_weight				97ecdc612b	last=d4b0d81b58
		# rebased to #14649 rpc_mempoolentry_weight
	-     rpc_mempoolentry_txhash				1b50730244
	11413 explicit_fee-0.18						a3e1e7caf9	last=b91af41525 kallewoof/explicit-fee
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	11750 coincontrol_multiselect				3842e3b7b6	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11765 rest_blockhash_compat-0.18			fd05f8917b	last=1323df9ff1 # [REST] added blockhash api, tests and documentation
		# Superceded by blockhashbyheight, so now just a backward compatibility hack
	11770 -										c33b7d19ab  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			0eb278563f
	# Complicated, needs maturity in git and careful rebasing: 15557 instagibbs:bumpall
	12096 bumpfee_reduce_output-0.18			263cd98509	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
		# NOTE: Competing with #15341
	12677 listunspent_ancestorinfo				4a1e1746f6
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.17						d2e51ecfa3	last=8c45d93b0e
	# TODO ? 12792 w/ renamed param
	12911 signrawtx_showfees-0.18				f34c0c28a2	last=bba2e57c76 kallewoof/sign-show-fees
	12965 scriptthreads-0.18					05bbd2ef5e	last=dfab6c6866 jonas/2018/04/svt
	15637 rpc_mempool_vsize-0.18+knots			5ece0928ce	last=e16b6a7188  # rpc: Rename size to vsize in mempool related calls
		# NOTE: Minified & made deprecation softer
		# NOTE: was #13008
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.17					8ec4ece3b3	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.17_asm_pragmas		89dbdc80ff
	13339 walletnotify_w-0.18					ad69c97f07	last=71d70632ee promag/2018-05-walletnotify
		# held back cef0327afd..71d70632ee Windows porting due to copyright issues (and bugs?)
	13541 sendraw_maxfeerate-0.18				8bfac8824e							last=7abd2e697c kallewoof/sendrawtransaction-maxfeerate
		# MODIFIED
		#+15618 removal of accidentally-merged code
		#+15770 rpc: Validate maxfeerate with AmountFromValue
	# Needs work: 13756 wallet: -avoidreuse feature for improved privacy
	# Needs work: 13836 clearmempool RPC
	# Needs review: 13903 Significantly reduce GetTransaction cs_main locking
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs review: 13989 add avx512 instrinsic
	# Needs work: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14032 Add p2p layer encryption with ECDH/ChaCha20Poly1305
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	14137 win_taskbar_progress-0.18+knots		274299b8b7	last=18eb4dbb8a
	15023 gui_node_rpcconsole-0.18+knots		56c1caf04f	last=f33efa8ec5 gui_node_rpcconsole  # PART OF c52c82eb6f
	14641 fundraw_minconf-0.18					506a5e09e5	last=a3991b7c0b promag/2018-11-fundrawtransaction
		# NOTE: backported 2 lines from #15557's 0ea47ba7b3 as 76cd3c48e2
		# NOTE: held back .gitignore nonsense change & relnotes
	14687 zmqkeepalive-0.18+knots				cba3ec51fa	last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# needs completion: 14912 external signers WIP + 15876
	# needs review: 14898 nextpagepointer & list ordering options for listtransactions
	# CHANGES WALLET FORMAT, wait for Core: 15006 achow101:create-encrypted-wallet
	# Needs review, changes wallet format: 15064 bip70_merchant_to_to
	# unsure: 15084 gui: don't disable the sync overlay when wallet is disabled
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	15115 rm_send2self-mini						8040c3be1b									last=ecf3d5323e rm_send2self
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Not ready: 15150 promag:2019-01-consolewalletselector
	# Not ready: 15157 rpc: Bumpfee units change, satoshis to BTC
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review/revision: 15202 promag:2019-01-closeallwallets
	# Needs review: 15204 promag:2019-01-openexternalwallet
	15218 postibd_flush-0.18					286dfcd156								last=b32fca5c21  # validation: Flush state after initial sync
		# Moved init around to avoid conflict w/ 15367
	# Let Core go first? 15224 sipa:201901_rand_strengthen
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	15323 getmempoolinfo_loaded-0.18			7a958747f8						last=effe81f750
		# Held back refactoring
	15367 -										4a4ab8b454													# feature: Added ability for users to add a startup command
	15371 -										f0ea5479a5													# gui: Uppercase bech32 addresses in qr codes
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# TODO: 15421 tor_subprocess
	#	Needs boost::process check
	15423 tor_socks_port						1dcebaa50f
	15428 tor_gui_pairing-0.18+knots			5ad7ba28fe						# latest code now
	# TODO: tor gitian bundle!
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review: 15427 sipa:201902_utxoupdatepsbtdesc
	# Needs review: 15450 achow101:gui-create-wallet
	# Exposes too much info to RPC? 15483 rpc: Adding a 'logpath' entry to getrpcinfo
	# Waiting to be non-WIP: 15487 [WIP] descriptor based wallet serialization and import
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15505 sdaftuar:2019-02-notfound-requests
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	15566 bcli_chain-0.18						2597ce945f
		# NOTE: Retained "testnet" key
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15633 nohbcbfornonwit-0.18					f42c2d5784								last=fb791ef082 gmaxwell/201803-nohbcbfornonwit
		# NOTE: added test fix
	# Needs review and use case? 15703 sipa:201903_secp256k1
	# USELESS Shared-lib 15717 Changes to support NAT-PMP
	15730 getwalletinfo_scanning-0.18			b7f9f784bb						last=008896693c promag/2019-04-getwalletinfo-scanning
	# Needs concept ack: 15756 promag:2019-04-tools-shortcuts
	# Needs concept ack: 15759 sdaftuar:2019-03-blocksonly-edges
	# Needs review: 15768 -													# gui: Add CMD+W shortcut in macOS
		# NOTE: Cannot make platform-independent w/o considering non-systray main window hiding
		# NOTE: Probably dialogs should be closed, not simply hidden
	# Needs fixes, then careful review of (and drop last commit from) 15761 achow101:upgradewallet-rpc
	# Needs review: 15845 MarcoFalke:1904-walletFastRescan
	15836 mempoolinfo_feehistogram-0.18			88e4feee9b						last=c97a9ddd4a jonas/2019/04/feeinfo
	15861 restore_vbits_warning					21b36a220b
	# Complex rebase: 15870 MarcoFalke:1904-walletRescanPruned (w/ modifications?)
	# Needs concept ACK and review: 15873 Rpc removemempoolentry
	# Needs concept ACK and review: 15886 hebasto:20190424-send-confirmation-dialog
# Non-upstreamed functionality:
	-     restore_blockmaxsize					19b06e74de
	7107 qtnetworkport							5ab40de7f8	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.18+knots				7ff174789e  # Latest code now
	11082 rwconf								9d9fb5ce77
	7510 rwconf_gui-0.18+knots					9f6ef50383	# Latest code now
	5916 legacy_keyorigin						993418d40d
	 559 accept_nonstdtxn						de4bba6215
	 929 tbc									ab98fe03d8
	 553 bugfix_qt_uri_amount_parser			f29cf10634
	-    mining_priority						9bc66e224d  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					29d903aa30
	5891 qt_console_history_persist				ca48e8303e
	7219 txrepl_fullrbf							31b2b70d2d
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					60b0b58283
	10282 timebomb_knots						f92d2136c9
	-     gui_wallet_displayname				218c919244
	-     recv_addrbook_refer_button-0.9		4ee8d4b680
	n/a  checkpoint_update-0.18					d03e23ac2a
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				ce4c98ac77
	-	 bytespersigopstrict-0.18+knots			374c2f87ef
	9749 unique_spk_mempool-0.18+knots			ca8fd67be9
	15846 sendtofuture-0.18+knots				6a4295cebd							last=c634b1e207 sipa/201904_futuresegwitstandard
		# NOTE: made optional, and added to rwconf_policy
	-    rwconf_policy-0.18+knots				7abe014468
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.18+knots					1f6f88361c
# BRANDING:
	n/a  knots_branding-0.18					99f412928f
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
	n/a  (cherrypick=15b62fa32bd3eaced3)		0ae06b6f7c	# doc/{bips,files}
	n/a  (bump_version=Knots:20190501)			ad4970f973
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=f01a43acea)				bac07a1073  # release notes: write/update, including change log and credits
			# Document #11765 being superceded:
			#	HTTP_BAD_REQUEST -> HTTP_NOT_FOUND
			#	English errors more or less detailed
			#	hash -> blockhash in JSON reply
			#	Hex result is reversed
			# Document removal of script debugger again
			# Document update 158c6ea2c0f1ab39e6843ab49e54d31f32cdc3dd
			# check travis for misspellings
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=943d2bd98d)				08b413d5f0  # translation update
	n/a  (cherrypick=a31010bd73)				e359a4cb92	# update manpages (build first)
# NOTE: use git diff --minimal for patches!

# TODO: Try Snap package stuff documented in doc/release-process.md
