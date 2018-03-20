timestamp 2018-02-24 20:14:58
lastapply no-merge

#.. checked up to PR #12558

checkout v0.16.0
@0.16.x-syslibs
	5872 subdir_incl_compat						fc9f50d046
	2241 sys_leveldb							e3ab3ceb16
	5416 sys_libsecp256k1						1d38d78d4f
	7485 sys_univalue_def						027bc28176
	5618 separate_utils_only					9d3b7993ba
	12246 separate_utils
	7339 opt_libevent-0.16						e7e2488213
	11622 bip70_disable-0.16					5dbcd1a73d	last=7ecca66062
@0.16.x-knots
# TESTS:
	-    travis_nolibevent						2f096f65f4
# FIXES:
	9524 marco/Mf1701-qaPruning					8d37c7a0bb
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						b62c04406f
	10731 log_more_uacomment					9104b40f1d
	# Too much churn/risk: 11596 chainactive_locking-0.16				c949b13d71	last=617c3188d5
		# held back 8ce8e75cd7-358dfc51e0 which is just a comment change and annotations, to minimise diff
		# held back a496a43699->ef997d66cc removal of double locking cs_main
	# too much churn/bugs, probably irrelevant:
	# ^ 11634 walletlocks-0.16						7914050bdb	last=491ec75b9f
		# held back annotations, and minimised patch
	# Needs review? 12172 jtimon/b16-bugfix-savemempool
	12432 clear_all_coinctl-0.16							last=f506c0a7f8
	12479 rawmempool_spentby-0.16							last=1dfb4e7d75  # RPC: Add child transactions to getrawmempool verbose output
	12491 fadvise-0.16										last=5259c72a76  # Try to use posix_fadvise with CBufferedFile
	12495 leveldb_max_open_files-0.16						last=21e2144a31  # Increase LevelDB max_open_files on 64-bit POSIX systems
		# held back changes to developer doc file
	12501 text_customfee-0.16								last=0bc095efd8  # [qt] Improved "custom fee" explanation in tooltip
	12573 bugfix_no_clz-0.16  # Fix compilation when compiler do not support __builtin_clz*
# FUNCTIONALITY:
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs-0.16					df6cffed47	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sort_multisigs			435a063f0e	last=127ec180bd sweepprivkeys
	12196 sweepprivkeys+scantxoutset						last=3835de0da4 jonas/2017/12/utxo_sweep
	9245 ionice									63041adffd
	-    ionice_win								9df27e8828
	8501 old_stats_rpc-0.16						828af4e879	last=7af0ea43b2
		# Held back on old version due to conflict with GUI updates...
	8550 stats_qt-0.16							47ef592135	last=63fb11652f
		# NOTE: partial rebase at https://github.com/jonasschnelli/bitcoin/pull/9 ??? OLDER THAN CURRENT NOW
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					140852f1a6
	9991 listreceivedbyaddress-filtered+knots	f8598965c4	last=f087613719  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey-0.16					0b370e9ac7	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							239afe1d1e
	11383 multiwallet_gui-0.16+knots			cbaf625196	last=f5aa574c37 multiwallet_gui
	10615 multiwallet_rpc						f0e200c20f
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10554 zmq_wtx-0.16							5316e0003c	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	12674 rpc_onetry_nonpriv
	10593 relax_invblk_punishment				ee052bf276
	10594 whitelist_outgoing					ede93391aa
	10350 filtered_witblock-0.16				ee55b7d144	last=3f388ddcd3 codeshark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	10729 scriptex								7ece29590e
	10730 scriptflag_strings-mini				b828bc08be	last=97cae3915f
	n/a   script_debugger-mini					b13b502e4e	last=1d3ed0c48a script_debugger
	# Needs work: 11200 achow101/gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	-     rpc_mempoolentry_txhash				a2c58f6cb9
	11256 rpc_mempoolentry_weight-0.16+knots	0ae7920df4	last=d4b0d81b58
	11413 explicit_fee-0.16									last=ff9f32eeac kallewoof/explicit-fee  # [wallet] [rpc] sendtoaddress: Add explicit feerate option to sendtoaddress
	11471 gui_sendtoself_label-0.16				7c64ef38db	last=c23bd2892b
	11491 -													# [gui] Add proxy icon in statusbar
	11653 rpc_getsignaturehash+knots			6bc34f035c	last=0a688c4f61 NicolasDorier/getsignaturehash
	11658 ibd_prune_extra						f7eb8d892c
		# Consider replacing with 12404...
	# Closed before released in Knots... 11666 rpc_signinput / NicolasDorier/signinput
	# Needs thought/Concept ACK: 11708 signrawtx_wsh-0.16								last=576624ce95
	# Not ready: 11742 testmempoolaccept-0.16							last=faa03a6dad
		# test fails, RPC includes int instead of bool, etc
	11750 - # Multiselect in coincontrol treewidget and display selected count
	11765 - # [REST] added blockhash api, tests and documentation
	11770 rest_fee-0.16										last=935b364978  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	11803 bugfix_dumpwallet_hdkeypath
	# 11872? MarcoFalke:Mf1712-rpcCreateRawSortedOuts (what's the use case?)
	12080 promag/2018-01-searchaddressbook
	12096 bumpfee_reduce_output-0.16						last=8430032df2 kallewoof/better-bumpfee
	12136 psbt-0.16											last=85fbed49e6 achow101/psbt
	12208 gui_legacy_bech32
	12240 rpc_mempool_fees-0.16								last=450ec6eed9  # [rpc] Introduced a new `fees` structure that aggregates all sub-field fee types denominated in BTC
	# When ready & has a way to use it: 12254 BIP 158 Compact Block Filters
	12257 avoidpartialspends-0.16							last=a011e8bfdb kallewoof/feature-addrgrouped-coinselect
	12321 decodescript-p2wsh-0.16							last=4f933b3d23  # p2wsh and p2sh-p2wsh address in decodescript
	12421 send_to_txhistory-0.16
	12568 zero_dustrelayfee_opt
	12580 gui_vsize-0.16
	12677 listunspent_ancestorinfo-0.16						last=daeb431011 listunspent_ancestorinfo
# Non-upstreamed functionality:
	-     restore_blockmaxsize					64a04dbf61
	7107 qtnetworkport							c94d8a6dd7	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					12cfec6d9d  # Latest code now
	11082 rwconf-0.16							e91bf830e6	last=148c4ec24e rwconf
	7510 rwconf_gui-0.16+knots					2f5d4369d0	# Latest code now
	5916 keyorigin								c5f583dfdc
	 559 accept_nonstdtxn						1243d2838c
	 929 tbc									d84d257f1c
	 553 bugfix_qt_uri_amount_parser			d7f460d856
	-    mining_priority-0.16					5db805e1ee  # NOTE: now the latest code, rebased
	5861 gui_restore_addresses					f63829b67c
	5891 qt_console_history_persist				c5df60c17f
	7219 txrepl_fullrbf							333528ea38
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots						647f952869
	12146 opt_wallet_segwit2
	n/a  checkpoint_update						106849c664
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	-    1day_default_conftarget
	-	 bytespersigopstrict+knots				0b671f305d
	9749 unique_spk_mempool+knots				c2cabb6288
	-    rwconf_policy-0.16+knots				c45bdb9b2a
		#TODO: Add segwit wallet stuff?
		#TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon-0.16+knots					d4266f2cc2
# BRANDING:
	n/a  knots_branding							b31017ae44
FIXME: Check includes use <>
TODO: Check if any pushKV do booleans
+    bool pushKV(const std::string& key, bool val_) __attribute__((deprecated)) {
         UniValue tmpVal((bool)val_);
         return pushKV(key, tmpVal);
     }
	n/a  (cherrypick=af9c353c0dd6012e91)		3921a4b3cc	# doc/{bips,files}
	n/a  (bump_version=Knots:20180224)			3e23b17b68
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=38ee93d976)				b0dc9e2e3e  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=e82aca5f8c)				89aa6c3923  # translation update
	n/a  (cherrypick=8d8e7db1ab)				4c3f4e6fed	# update manpages
# NOTE: use git diff --minimal for patches!
