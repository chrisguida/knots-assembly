timestamp 2019-08-23 19:59:31
lastapply no-merge

#.. checked up to PR #16922

checkout origin/0.19
@0.18.x-syslibs
	5872 subdir_incl_compat						434600ecad
	2241 sys_leveldb							b3b13f6369
	5416 sys_libsecp256k1						2b14d06dcf
	7485 sys_univalue_def						250baa60da
	13789 bugfix_asm_pragmas					6404ba7d9e
	-     bugfix_asm_leveldb_check				d3529cd537
	15155 test_external_bcli					05ac01eb15
	16564 raii_event_test_fix-0.14				6358a0d1c9	last=9a19c9ada5
@0.18.x-knots
# TESTS:
	# TODO why was this closed??? 14080 marco/Mf1808-travisSanThread
	-     lint_relaxer							72bfd12414
	# Needs review: 15134 practicalswift:unsigned-char
	15888 test_wallet_implicitsegwit			e5db67d94a
# FIXES:
	14968 laanwj/2018_12_http_bind_error		9d197f0974	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					af253f6c66
	9524 marco/Mf1701-qaPruning					1be48502ae	last=88883ae13d marco/Mf1701-qaPruning
	10731 log_more_uacomment					ee1783a25a
	14485 fadvise								a4db9bcd5b
		# Was #12491
	14501 fsync_dir								6ede1fd5bb
		# Was #12696
	# TODO: fsync_dir_pt2 after PR submitted & reviewed & tested
	13084 sipa/201804_keepnegone				fd7f1de223	last=5af7625079 sipa/201804_keepnegone
	13608 -										b34192bdae	last=876f49c6cd  # bitcoin-tx: Require that input amount is provided for witness transactions
	# Needs fix?? 13674 -													# Qt: Fix for bitcoin-qt becoming unresponsive during shutdown (issue #13217)
	-     bugfix_rpc_getbalance_hacky			58b6b3f646
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 14425 Net: Do not re-enable Onion network when it was disabled via onlynet
	15103 lightsword/getentropy-weak			f985848660	last=a7c7fee2e4 lightsword/getentropy-weak
	# Needs review: 15191 practicalswift:cs_LastBlockFile
	# Needs review: 15192 practicalswift:validation-cs_main
	# Needs review: 15363 promag:2019-01-loopexit
	# Needs review: 15909 Use 'CreateProcess' instead of 'wsystem' in 'runCommand' for Windows.
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted
	# Needs review: 16050 promag:2019-05-importmulti-update
	# Needs review: 16161 util: Fix compilation errors in support/lockedpool.cpp
	# Likely impossible: 16199 fix coinjoin sends in RPC
	# Needs review AND CARE MERGING: 16507 instagibbs:feefilter_match_mempool
# FUNCTIONALITY:
	14066 gitian_power64						6d990c68b6
	# not ready/deterministic: 13827 NSIS depends build
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.19					40af219ca8	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							97cd6e86fb
	15704 win32_defines_globally				0a83c3994e
	9245 ionice-0.19							b0568326a4	last=e1276957ed2 ionice
	-    ionice_win-0.19						060cf0ad7c
	8501 old_stats_rpc-0.19						6e84daee87	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 old_stats_qt-0.19						406317cf3e	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
	9422 mempool_dat_extensible					16f1a3cb13
	9504 dumpmasterprivkey-0.18					c1f213cf46	last=07fc81109a
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							db852ae251
	10615 multiwallet_rpc						16c4cd90dd
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	10554 zmq_wtx-0.19							af3259e141	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv					e990290011
	10593 relax_invblk_punishment				e37459ded9
#TODO: Split this up
	10594 whitelist_outgoing-mini-0.19+knots	f886df3bd1	last=dce108076d7 whitelist_outgoing  # via whitelist_outgoing-mini
	10350 filtered_witblock-0.19				7cb073403f	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				c29eeb585f
	11413 explicit_fee-0.19						3714c6806c	last=09b5155ecdb kallewoof/explicit-fee
		# NOTE: Held back 97636cd371c..473ce2dcfdf -  see 670a101e362db0e3a346719e905fd6ab1cfd4fc4 branch for min feerate error
		# NOTE: Updated to c109001c9b with ac046e805c (HELD BACK)
		# NOTE: Retained compatibility with "EXPLICIT" fee mode, and fixed upper/lower casing
		# TODO: Relnotes changes - case insensitivity, (is RBF default new??)
		# 0.19 TODO: Rebase/squash fixups (keep compat with "EXPLICIT"!)
	# n/a with #15115: 11471 gui_sendtoself_label-0.17				b0b4d9bbf3	last=c23bd2892b
	# dropped: 11653 rpc_getsignaturehash+knots			b4736e599f	last=0a688c4f61 NicolasDorier/getsignaturehash
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	11750 coincontrol_multiselect				f3be4da827	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 -										83746da5d2	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath			2d9fd86ada
	# Complicated, needs maturity in git and careful rebasing: 15557 instagibbs:bumpall
	# Needs significant rebase work: 12096 bumpfee_reduce_output-0.18			a5f9f682a4	last=086313c8b1 kallewoof/better-bumpfee
		# NOTE: Latest version is rebased for adding inputs, with serious issues
		# NOTE: Competing with #15341
	12677 listunspent_ancestorinfo				37da54f98e
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	12763 rpcwhitelist-0.19						68d8b186de	last=8c45d93b0e
	# TODO ? 12792 w/ renamed param
	12911 signrawtx_showfees-0.19				7035643906	last=bba2e57c76 kallewoof/sign-show-fees
	12965 scriptthreads-0.19					874c6e06f8	last=dfab6c6866 jonas/2018/04/svt
	# Maybe? 13014 jonasschnelli:2018/04/txindex_prune
	# Skip due to changing upstream code too much: 13442 sipa/201806_sse4intrin
	13203 dsha256_power8-0.17					9e854a5fe2	last=3b402e0738 matt/2018-05-asm
		# NOTE: Stripped out benchmark change
	-     dsha256_power8-0.17_asm_pragmas		8b4a5fb58f
	13339 walletnotify_w-0.19					98d4181322	last=826718490fb promag/2018-05-walletnotify
		# held back cef0327afd..15a0ad0bb4 Windows porting due to copyright issues (and bugs?) - No longer applicable?
		# Removed WIN32 conditional
		# Changed '"'"' to '\''
		# Test improvements: eaeb6fb7efd
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
	14137 win_taskbar_progress					99de8ff722	last=18eb4dbb8a
	15023 gui_node_rpcconsole-0.19+knots		75def5db94	last=f33efa8ec5 gui_node_rpcconsole
	14641 fundraw_minconf-0.19					486411af85	last=a3991b7c0b promag/2018-11-fundrawtransaction
		# NOTE: held back .gitignore nonsense change & relnotes
	14687 zmqkeepalive-0.19+knots				36c11d18bb	last=c276df7759
		# NOTE: modified to soft-fail only
	# wait for Core?: 14707
	# needs completion: 14912 external signers WIP + 15876
	# needs review: 14898 nextpagepointer & list ordering options for listtransactions
	# CHANGES WALLET FORMAT, wait for Core: 15006 achow101:create-encrypted-wallet
		# +16394 achow101/fix-born-enc
	# Needs review, changes wallet format: 15064 bip70_merchant_to_to
	# unsure: 15084 gui: don't disable the sync overlay when wallet is disabled
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	15115 rm_send2self-mini						e3663bbc4e	last=ecf3d5323e rm_send2self
	# Needs review (at least): 15129 rpc: Added ability to remove watch only addresses
	# Not ready: 15150 promag:2019-01-consolewalletselector
	# Not ready: 15157 rpc: Bumpfee units change, satoshis to BTC
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review/revision: 15202 promag:2019-01-closeallwallets
	# Needs review: 15204 promag:2019-01-openexternalwallet
	15218 -										ceb964d7db	last=d2ecb70d64  # validation: Flush state after initial sync
		# Moved init around to avoid conflict w/ 15367
	# Let Core go first? 15224 sipa:201901_rand_strengthen
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	15367 startupnotify-0.19+knots				4078797ded	last=4b6987c85d8	# feature: Added ability for users to add a startup command
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# TODO: 15421 tor_subprocess
	#	Needs boost::process check
	15423 tor_socks_port						e366a8e9f0
	15428 tor_gui_pairing-0.19+knots			053f9f08c2	# latest code now
	# TODO: tor gitian bundle!
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review: 15427 sipa:201902_utxoupdatepsbtdesc
	# Needs review: 15450 achow101:gui-create-wallet
	# Exposes too much info to RPC? 15483 rpc: Adding a 'logpath' entry to getrpcinfo
	# Waiting to be non-WIP: 15487 [WIP] descriptor based wallet serialization and import
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15505 sdaftuar:2019-02-notfound-requests
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15633 nohbcbfornonwit						6e6b51a203	last=fb791ef082 gmaxwell/201803-nohbcbfornonwit
		# NOTE: added test fix from sdaftuar/test-15633-2
	# Needs review and use case? 15703 sipa:201903_secp256k1
	# USELESS Shared-lib 15717 Changes to support NAT-PMP
	# Needs concept ack: 15756 promag:2019-04-tools-shortcuts
	# Needs concept ack: 15759 sdaftuar:2019-03-blocksonly-edges
	# Needs review: 15768 -													# gui: Add CMD+W shortcut in macOS
		# NOTE: Cannot make platform-independent w/o considering non-systray main window hiding
		# NOTE: Probably dialogs should be closed, not simply hidden
	# Needs fixes, then careful review of (and drop last commit from) 15761 achow101:upgradewallet-rpc
	# Needs review: 15845 MarcoFalke:1904-walletFastRescan
	15836 jonas/2019/04/feeinfo					a3f20f5696	last=b94292a7cb jonas/2019/04/feeinfo
	15861 restore_vbits_warning					37a59ac37c
	# Complex rebase: 15870 MarcoFalke:1904-walletRescanPruned (w/ modifications?)
	# Needs concept ACK and review: 15873 Rpc removemempoolentry
	# Needs concept ACK and review: 15886 hebasto:20190424-send-confirmation-dialog
		# NOTE: +16826 fix
	# Needs rebasing without settings.json and review: 15937 Add loadwallet and createwallet load_on_startup options
	# Needs backport of other stuff: 15930 rpc_getbalances-0.18								last=eeee1497ac marco/1904-rpcWalletBalances
		# NOTE: excluded various refactoring and deprecation
	# Needs QA/reivew: 15946 jonasschnelli:2019/05/prune_blockfilter
	15987 wallet_no_reuse-0.19+knots			aca83094ee	last=391c5d9a972 wallet_no_reuse
	-     rpc_gai_txids-0.19					4ea59f5b23	last=621796da61 rpc_gai_txids
	# Needs review/fixes? 16037 promag/2019-05-importwallet-pruned
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	16083 rpc_getblock_prevouts_fees-0.19		9bffa80d67	last=dd83c4c925
		# Renamed blockToJSON to avoid silent conversion of bool to new int verbosity param
		# Renamed "coinbase" field to "generated"
		# Renamed "fees" field to "fee"
		# Silenced warnings
		# Minimised diff (removed formatting changes)
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# FIXME: Minor revision needed? 16373 instagibbs:bump_psbt
	# Needs review: 16377 Sjors:2019/07/walletcreatefundedpsbt_addinputs
	# Needs review: 16378 Sjors:2019/07/send
	# Needs review maybe: 16512 achow101:joinpsbt-rand
	# Needs concept ACK and review: 16523 -  # Add removemempoolentry RPC to evict transactions from the mempool
	# Needs mucho review: 16546 Sjors:2019/08/hww-box2 # -signer
	# Depends-on-16546: 16549 Sjors:2019/08/hww-qt
	# Probably requires 0.19? CHECK CAREFULLY 16554 fanquake/test_openssl_include
	# FIXME: Needs rebase on HasPermission etc FIXME: Breaks p2p_blocksonly ; 16682 blocksonly_violators-0.18.1						last=5ff415d9af jnewbery/2019-08-disconnect-blocksonly-violators
	# TODO "WIP": 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs intense review: 16702 p2p: supplying and using asmap to improve IP bucketing in addrman
		# NOTE: deps on 16730
	# TODO: Needs diff-minimisation at least: 16727 instagibbs:feerate_bumpfee
	# Needs review (and BIP finalisation?): 16748 dongcarl:2019-07-addrv2v4
	16795 rpc_spk_decode_desc-0.18				0e03fd739b	last=9b9459640d instagibbs/decode_descriptor
	# TODO: 16807 meshcollider:201909_bech32_error_detection  (plus GUI?)
# Non-upstreamed functionality:
	-     restore_blockmaxsize					e6d0e514cf
	7107 qtnetworkport							0fae275651	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force-0.19+knots				19d9a62fee  # Latest code now
	11082 rwconf-0.19							f5d5d15cfa	last=956a76cc852 rwconf
	7510 rwconf_gui-0.19+knots					74d4579901	# Latest code now
	5916 legacy_keyorigin						4e26398609
	 559 accept_nonstdtxn						dd0f34238f
	 929 tbc									27b3ac8389
	 553 bugfix_qt_uri_amount_parser			e74e075536
	-    mining_priority						c7999022e4  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					4faaa5ad5a
	5891 qt_console_history_persist				7f5f2c835a
	# 0.19 TODO: Revert 16171 to restore opt-in RBF option
	7219 txrepl_fullrbf							e6803520a3
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					15f192dfb5
	10282 timebomb_knots						aca5337519
	-     gui_wallet_displayname-0.18+knots		9d8ff1e11d	# Latest code now
	-     recv_addrbook_refer_button-0.9		ccb7f4d528
	n/a  checkpoint_update-0.18					b6067d8662
	# 0.19 TODO: revert "Request payment" rename
	# NEEDS FIXUP/REPLACE 16432 qt: Add privacy to the Overview page
	# Requires complex FlatFile refactoring: Parts of? 14121+16442 Neutrino
	# Needs review: 16463 achow101:bip174-xpub
	# Needs to be rational: Minimised 16490 marco/1907-rpcMempoolWhyReplacable
	# TODO: Needs work? 16492 rpc: Add feeRate argument to bumpFee RPC
	# 0.19 TODO: Semi-Revert 15711+16497 (leave it default for Segwit wallets)
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget				6cd540a25f
	-	 bytespersigopstrict-0.18+knots			95d95fa3e3
	9749 unique_spk_mempool-0.18+knots			3a8aafc37e
	15846 sendtofuture-0.18+knots				4b92379ff1	last=c634b1e207 sipa/201904_futuresegwitstandard
		# NOTE: made optional, and added to rwconf_policy
	-    rwconf_policy-0.18+knots				eb81c91962
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
	# 0.19 TODO: Revert #16152 (disable bloom by default)
	# Needs review/optionality: 16421 TheBlueMatt:2019-07-lightning-policy-bump
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.18+knots					8f7b63e470
# BRANDING:
	n/a  knots_branding-0.18					8510f8d367
FIXME: Check there are no menu icons
#FIXME: Check includes use <>
#FIXME: Check hidden_args has anything removed (possibly conditional)
	n/a  (cherrypick=15b62fa32bd3eaced3)		7048a6755f	# doc/{bips,files}
	n/a  (bump_version=Knots:20190920)			ec3e4d8ce6
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=0595ac1bf8)				f4af8df41d  # release notes: write/update, including change log and credits
			# check travis for misspellings
		TODO: Dropping 11765 rest_blockhash_compat-0.18
		TODO: Dropping 12096 bumpfee_reduce_output-0.18
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while read g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge \d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=1f3359bfec)				c1de3c6279  # translation update
	n/a  (cherrypick=de8a068d8e)				c1182c9863	# update manpages (build first)
# NOTE: use git diff --minimal for patches!

# TODO: Try Snap package stuff documented in doc/release-process.md
