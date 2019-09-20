timestamp 2019-08-23 19:59:31
#lastapply no-merge

#.. checked up to PR #16696

checkout v0.18.1
@0.18.x-syslibs
	5872 subdir_incl_compat						139bbb90fc
	2241 sys_leveldb-0.17						b70901dd30
	5416 sys_libsecp256k1						e10dd743a5
	7485 sys_univalue_def						db89c5a22a
	13788 bugfix_asm_opt						be758cfb7f
	13789 bugfix_asm_pragmas					c7a18326b3
	-     bugfix_asm_leveldb_check				e0cdc298d7
	15155 test_external_bcli					65f35c7f7d
	15970 bugfix_threadlocal_check-0.16
	16564 raii_event_test_fix-0.14							last=b2c8450e6c
@0.18.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							7206a1000d
	# Needs review: 15134 practicalswift:unsigned-char
	15888 test_wallet_implicitsegwit			4d67b75415
	15920 nowallet_hiddenargs_linter-0.18		9d8657290b
# FIXES:
NM	15913 bugfix_nowallet_avoidpspends-0.18		e4d1fde05d
	14968 laanwj/2018_12_http_bind_error		547767d717
	-     http_bind_error+extra					ecd0e8da29
	9524 marco/Mf1701-qaPruning					178af41a49
	10731 log_more_uacomment					a4d5169930
	14485 fadvise								49cf3fced8
		# Was #12491
	14501 fsync_dir								d0007e0fc5
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	13084 sipa/201804_keepnegone				a5f2346ed6
	13608 -										1d0021a77f  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs fix?? 13674 -													# Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	-     bugfix_rpc_getbalance_hacky			7c154a978e
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
TM	14818 bugfix_test_rpc_psbt					1854893c5c
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			262f205c83
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 promag:2019-01-loopexit
	15558 dnsoneatatime-0.18					df2729525b	last=6170ec5d3a sipa/201903_dnsoneatatime
		# NOTE: Diff-minimised
NM	15600 lockedpool_dontdump					616c756d2e
	15651 tor_standard_port						b038090435
	15650 fallocate_check-0.18+knots			dc381477b7	last=5d35ae3326
	15896 qa_pkgname-0.18						60b37a9fb7	last=fcc443b636 qa_pkgname
	15897 qa_mininode_headers					e4e7278854
	# Needs review: 15909 Use 'CreateProcess' instead of 'wsystem' in 'runCommand' for Windows.
	15911 wcreatefundedpsbt_rbf_fix-0.18		0361c96384	last=d6b3640ac7
		# NOTE: Held back removal of "fallback to" since that's not really part of this fix
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	16646 test_without_upnp-0.17
	# Needs review: 16050 promag:2019-05-importmulti-update
	16090 peerdetail_vertspacer-0.18  # Qt: Add vertical spacer to peer detail widget
	# Needs review: 16161 util: Fix compilation errors in support/lockedpool.cpp
	# Likely impossible: 16199 fix coinjoin sends in RPC
	16212 bugfix_rm_addrdb_tmpfile-0.17
	# Needs review AND CARE MERGING: 16507 instagibbs:feefilter_match_mempool
	16525 rpc_unsigned_txver-0.18							last=e80259f197 matt/2019-07-unsigned-tx-ver
	16578 qapp_dummy_argv-0.18.1
# FUNCTIONALITY:
	14066 gitian_power64-0.18					2cffda4afd	last=0c0550a01f gitian_power64
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
m	8751 sort-multisigs-0.18					423894f629	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							7516c660b5
	15704 win32_defines_globally				71083ca1b0
	9245 ionice									481f0b1811
	-    ionice_win								900bac5f30
	8501 old_stats_rpc-0.18						89249c44ef	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.18						98cabb0a3f	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible					211580c192
	9504 dumpmasterprivkey-0.18					516d0f9fb3	last=07fc81109a
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							b0fcca6c3e
	10615 multiwallet_rpc						acb7557715
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	10554 zmq_wtx-0.18							56286d74a6	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					5878f860d4
	10593 relax_invblk_punishment				ff31141b72
m	10594 whitelist_outgoing-0.18				9ed15cac6c
		# 0.9 TODO: Revert 16555
	10350 filtered_witblock-0.17				461d614dbc	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	11256 rpc_mempoolentry_weight-0.17			a2eebb9211	last=d4b0d81b58
	-     rpc_mempoolentry_txhash				cdbd81c59c
	# Only if needed: 16566 tolowerupper_string-0.18
		# NOTE: Only added new functions, didn't remove/change old ones
	11413 explicit_fee-0.18						a7c5575359	last=f54e33dc81 kallewoof/explicit-fee
		# NOTE: Updated to c109001c9b with ac046e805c (HELD BACK)
		# NOTE: Retained compatibility with "EXPLICIT" fee mode, and fixed upper/lower casing
		# TODO: Relnotes changes - case insensitivity, (is RBF default new??)
		# 0.19 TODO: Rebase/squash fixups (keep compat with "EXPLICIT"!)
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	11750 coincontrol_multiselect				6e72d82a06	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11765 rest_blockhash_compat-0.18			52de94498f	last=1323df9ff1 # [REST] added blockhash api, tests and documentation
		# Superceded by blockhashbyheight, so now just a backward compatibility hack
	11770 -										c1c594490a  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			115ef72659
	# Complicated, needs maturity in git and careful rebasing: 15557 instagibbs:bumpall
m	12096 bumpfee_reduce_output-0.18			848577505c	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
		# NOTE: Competing with #15341
	12677 listunspent_ancestorinfo				d758005bf1
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.17						1beed551c4	last=8c45d93b0e
	# TODO ? 12792 w/ renamed param
	12911 signrawtx_showfees-0.18				36a7196e0d	last=bba2e57c76 kallewoof/sign-show-fees
	12965 scriptthreads-0.18					21b59a99f0	last=dfab6c6866 jonas/2018/04/svt
	15637 rpc_mempool_vsize-0.18+knots			51d7f34669	last=e16b6a7188  # rpc: Rename size to vsize in mempool related calls
		# NOTE: Minified & made deprecation softer
		# NOTE: was #13008
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.17					db181f3987	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.17_asm_pragmas		9e09a78f24
	13339 walletnotify_w-0.18					11f3777ed3	last=15a0ad0bb4 promag/2018-05-walletnotify
		# held back cef0327afd..15a0ad0bb4 Windows porting due to copyright issues (and bugs?)
	13541 sendraw_maxfeerate-0.18				4bd6c3b990	last=7abd2e697c kallewoof/sendrawtransaction-maxfeerate
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
	14137 win_taskbar_progress-0.18+knots		98aa8e66f9	last=18eb4dbb8a
	15023 gui_node_rpcconsole-0.18+knots		f86f92b5ef	last=f33efa8ec5 gui_node_rpcconsole  # PART OF c52c82eb6f
m	14641 fundraw_minconf-0.18					0bea20be04	last=a3991b7c0b promag/2018-11-fundrawtransaction
		# NOTE: backported 2 lines from #15557's 0ea47ba7b3 as 76cd3c48e2
		# NOTE: held back .gitignore nonsense change & relnotes
	14687 zmqkeepalive-0.18+knots				8b22e36ac2	last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# needs completion: 14912 external signers WIP + 15876
	# needs review: 14898 nextpagepointer & list ordering options for listtransactions
	# CHANGES WALLET FORMAT, wait for Core: 15006 achow101:create-encrypted-wallet
		# +16394 achow101/fix-born-enc
	# Needs review, changes wallet format: 15064 bip70_merchant_to_to
	# unsure: 15084 gui: don't disable the sync overlay when wallet is disabled
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	15115 rm_send2self-mini						890be96ed6	last=ecf3d5323e rm_send2self
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Not ready: 15150 promag:2019-01-consolewalletselector
	# Not ready: 15157 rpc: Bumpfee units change, satoshis to BTC
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review/revision: 15202 promag:2019-01-closeallwallets
	# Needs review: 15204 promag:2019-01-openexternalwallet
	15218 postibd_flush-0.18					b5fc890bc5	last=d2ecb70d64  # validation: Flush state after initial sync
		# Moved init around to avoid conflict w/ 15367
	# Let Core go first? 15224 sipa:201901_rand_strengthen
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	15323 getmempoolinfo_loaded-0.18			7589250729	last=effe81f750
		# Held back refactoring
	15367 -										57c3fe8f9a	# feature: Added ability for users to add a startup command
	15371 -										6686923d4a	# gui: Uppercase bech32 addresses in qr codes
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# TODO: 15421 tor_subprocess
	#	Needs boost::process check
	15423 tor_socks_port						98ec95d386
	15428 tor_gui_pairing-0.18+knots			c61ac82b66	# latest code now
	# TODO: tor gitian bundle!
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review: 15427 sipa:201902_utxoupdatepsbtdesc
	# Needs review: 15450 achow101:gui-create-wallet
	# Exposes too much info to RPC? 15483 rpc: Adding a 'logpath' entry to getrpcinfo
	# Waiting to be non-WIP: 15487 [WIP] descriptor based wallet serialization and import
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15505 sdaftuar:2019-02-notfound-requests
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	15566 bcli_chain-0.18						594467ed65
		# NOTE: Retained "testnet" key
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15633 nohbcbfornonwit-0.18					73fba0e037	last=fb791ef082 gmaxwell/201803-nohbcbfornonwit
		# NOTE: added test fix
	# Needs review and use case? 15703 sipa:201903_secp256k1
	# USELESS Shared-lib 15717 Changes to support NAT-PMP
	15730 getwalletinfo_scanning-0.18			72a702efb2	last=b6c748f849 promag/2019-04-getwalletinfo-scanning
	# Needs concept ack: 15756 promag:2019-04-tools-shortcuts
	# Needs concept ack: 15759 sdaftuar:2019-03-blocksonly-edges
	# Needs review: 15768 -													# gui: Add CMD+W shortcut in macOS
		# NOTE: Cannot make platform-independent w/o considering non-systray main window hiding
		# NOTE: Probably dialogs should be closed, not simply hidden
	# Needs fixes, then careful review of (and drop last commit from) 15761 achow101:upgradewallet-rpc
	# Needs review: 15845 MarcoFalke:1904-walletFastRescan
	15836 mempoolinfo_feehistogram-0.18			e9eccaafe7	last=b94292a7cb jonas/2019/04/feeinfo
	15861 restore_vbits_warning					1e8243e594
	# Complex rebase: 15870 MarcoFalke:1904-walletRescanPruned (w/ modifications?)
	# Needs concept ACK and review: 15873 Rpc removemempoolentry
	# Needs concept ACK and review: 15886 hebasto:20190424-send-confirmation-dialog
	# Needs rebasing without settings.json and review: 15937 Add loadwallet and createwallet load_on_startup options
	15932 rpc_getblock_relax_lock-0.18			8e5a518c6f	last=faea56400d marco/1905-rpcBlockNoLock
		# NOTE: Held back lock annotations/asserts in case other callers don't respect the expectations
	15623 expose_readundo-0.18
	14802 getblockstats_wo_txindex-0.18  # rpc: faster getblockstats using BlockUndo data
	# Needs backport of other stuff: 15930 rpc_getbalances-0.18								last=eeee1497ac marco/1904-rpcWalletBalances
		# NOTE: excluded various refactoring and deprecation
	# Needs QA/reivew: 15946 jonasschnelli:2019/05/prune_blockfilter
	15986 gdi_checksum-0.18
	15987 wallet_no_reuse-0.18+knots						last=545af217ae wallet_no_reuse
	-	  rpc_gai_txids-0.18								last=621796da61 rpc_gai_txids
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	16083 rpc_getblock_prevouts_fees-0.18+knots				last=dd83c4c925
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Renamed "fees" field to "fee"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	16185 rpc_gettx_decode-0.18								last=9965940e35  # gettransaction: add an argument to decode the transaction
	16248 whitelist_permissions-0.18.1+knots
		# Minimised diff/API change
		# includes bugfix 16618 NicolasDorier/fix/noban-banned
		# includes bugfix 16631 NicolasDorier/fix/default-whiterelay
		# TODO: maybe add 16629?
	# FIXME: Minor revision needed? 16373 instagibbs:bump_psbt
	# Needs review: 16377 Sjors:2019/07/walletcreatefundedpsbt_addinputs
	# Needs review: 16378 Sjors:2019/07/send
	# Needs review maybe: 16512 achow101:joinpsbt-rand
	# Needs concept ACK and review: 16523 -  # Add removemempoolentry RPC to evict transactions from the mempool
	# Needs mucho review: 16546 Sjors:2019/08/hww-box2 # -signer
	# Depends-on-16546: 16549 Sjors:2019/08/hww-qt
	# Probably requires 0.19? CHECK CAREFULLY 16554 fanquake/test_openssl_include
	# FIXME: Needs rebase on HasPermission etc FIXME: Breaks p2p_blocksonly ; 16682 blocksonly_violators-0.18.1						last=5ff415d9af jnewbery/2019-08-disconnect-blocksonly-violators
	16695 getctxstats_final_height-0.18  # rpc: Add window final block height to getchaintxstats
	# Kept last to avoid rebase conflicts
# Non-upstreamed functionality:
	-     restore_blockmaxsize					1dbbc0ec2c
	7107 qtnetworkport							37c2c835eb	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.18+knots				a2d7d286b6  # Latest code now
m	11082 rwconf-0.18							25849bae73	# Latest code now
	7510 rwconf_gui-0.18+knots					3d8e677c0f	# Latest code now
	5916 legacy_keyorigin						900a0a4ba4
	 559 accept_nonstdtxn						6290ba420f
	 929 tbc									4a67984691
	 553 bugfix_qt_uri_amount_parser			a8ddb52871
	-    mining_priority						7441128513  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					a0f3b362d6
	5891 qt_console_history_persist				de26fdf0ec
	# 0.19 TODO: Revert 16171 to restore opt-in RBF option
	7219 txrepl_fullrbf							3775514e83
	# TODO: some way to add UA comments via rwconf
m	12146 opt_wallet_segwit2					30484295d7
	10282 timebomb_knots						b1ebfba56c
m	-     gui_wallet_displayname-0.18			11c8ba9186	# Latest code now
	-     recv_addrbook_refer_button-0.9		c867e094f2
	n/a  checkpoint_update-0.18					0a993c9993
	# 0.19 TODO: revert "Request payment" rename
	16153 traffic_antialias-0.18  # Qt: Add antialiasing to traffic graph widget
	# NEEDS FIXUP/REPLACE 16432 qt: Add privacy to the Overview page
	# Requires complex FlatFile refactoring: Parts of? 14121+16442 Neutrino
	# Needs review: 16463 achow101:bip174-xpub
	# Needs to be rational: Minimised 16490 marco/1907-rpcMempoolWhyReplacable
	# TODO: Needs work? 16492 rpc: Add feeRate argument to bumpFee RPC
	# 0.19 TODO: Semi-Revert 15711+16497 (leave it default for Segwit wallets)
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				42ac1def4e
	-	 bytespersigopstrict-0.18+knots			cc7dd07c7d
m	9749 unique_spk_mempool-0.18+knots			405e820d5b
	15846 sendtofuture-0.18+knots				42874aa95b	last=c634b1e207 sipa/201904_futuresegwitstandard
		# NOTE: made optional, and added to rwconf_policy
	-    rwconf_policy-0.18+knots				971541b989
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	# 0.19 TODO: Revert #16152 (disable bloom by default)
	# Needs review/optionality: 16421 TheBlueMatt:2019-07-lightning-policy-bump
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.18+knots					f895baf6fa
# BRANDING:
	n/a  knots_branding-0.18					bf23ad4632
	FIXME: do we need 16595?
#FIXME: Check includes use <>
CHECK: Ensure that all new RPC params increment the param count checks (since that's automagic on master)
#FIXME: Check hidden_args has anything removed (possibly conditional)
	n/a  (cherrypick=15b62fa32bd3eaced3)		2ff17d1019	# doc/{bips,files}
	n/a  (bump_version=Knots:20190823)			f9d6f03e9f
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=abba613227)				f80967ffb4  # release notes: write/update, including change log and credits
			# b/doc/release-notes-14802.md
			# origin-pull/16525/head doc/release-notes-16525.md
			# doc/release-notes-16695.md
			# origin-pull/16185/head
			# check travis for misspellings
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=943d2bd98d)				bdbe9f59e5  # translation update
	n/a  (cherrypick=a31010bd73)				5e1c2d13f5	# update manpages (build first)
# NOTE: use git diff --minimal for patches!

# TODO: Try Snap package stuff documented in doc/release-process.md
