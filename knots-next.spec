timestamp 2017-06-02 22:08:57

#.. checked up to PR #10495

checkout v0.14.2rc1
@0.14.x-syslibs
	5872 subdir_incl_compat						4f8cf7a
	2241 sys_leveldb							10cc85d
	5416 sys_libsecp256k1						b23a49f
	7485 sys_univalue_def						2c1848c
	7522 bugfix_gitdir							d4ec6e5
	5618 separate_utils-0.14.x					d60f428	last=6d5b247 separate_utils
	7339 opt_libevent-0.14						e309982	last=3cc7b69 opt_libevent
@0.14.x-knots
# TESTS:
	-    travis_qt4_nolibevent					183550d
	9359 test_wallet_immature-0.14				441ef55	last=7ed143c	# Add test for CWalletTx::GetImmatureCredit() returning stale values.
# FIXES:
	9495 -										9669767 #JeremyRubin:checkqueue-control-lock
	9497 -										35bc768 #JeremyRubin:checkqueue-tests
	# broken: 9522 achow101/fix-decoderawtx
	9524 marco/Mf1701-qaPruning					abdaa7e
	9549 -										745f70a #practicalswift:avoid-potential-null-pointer-dereference-in-markblockasinflight
	9622 listsinceblock_removedtxs-0.14			913fd86	last=a8c56bf
		# Hold back (eg 44be568..d453b37) any new "allow_partial" ugliness
	9481 fee_warning-0.14						be69a9d
	10156 bugfix_restore_onscreen-0.14			6757870	last=b0c302b
	10196 prioritisetx_gbtcache-0.14			321992e	last=6a61424
	10234 list_banned_correctly-0.14			408c686	last=ea2c925
	9853  fixerrorcodes-0.14
	10376 disconnect_ban_fixes-0.14
		#+10234+10143p+9577
	10328 debianppa-0.14
	n/a   0.14.2_fixes_subst
		#10250+10265+10308+10445
	-    undeprecate_prioritymining				4b88b6f
# FUNCTIONALITY:
	 559 accept_nonstdtxn						a3e14aa
	 929 tbc									913fd6d
	 553 bugfix_qt_uri_amount_parser			95fc64d
	5861 gui_restore_addresses					1f836fd
	5891 qt_console_history_persist				debb57d
	5916 keyorigin-0.14							ffe6c36
	7061 jonas_rpc_rescan-0.14					31b0b95 last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							bba5bf2	last=1f37c87 origin-pull/7107/head
	9592 gui_rbf_checkbox-0.14					3c75e07
		#+10242
	9672 rpc_rbf								b1a0e12	# WAS 7159 with last=b64ebaf
	7219 txrepl_fullrbf							9392c6c
	7533 sendraw_force							aa96b56
	7510 rwconf+knots							f66d5fa
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 -										eb29869
	-    trivial_blockmaxsize_mainnet			d538944
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 getblock-extraverbose-0.14				631e007	last=b779f30  # getblock extraverbose
	8751 sort-multisigs							47cf78e last=30f2ac9  # multisig sorting
	9017 instagibbs_p2shp2wpkhstuff_partial		b65c705	last=6a67000  # replacing 8992; removed sign/verify message stuff
m	8952 listunspent_query_options-0.14+knots	281e97b	last=11ee5ec  # Add query options to listunspent RPC call
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sendraw_force			db96f15
	9245 ionice									1f662ff
	8501 stats_rpc-0.14							fc97f52
	8550 stats_qt-0.14							6105cee	last=251ee28
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	# useless? 9402  # Allow per network configuration file
	9422 mempool_dat_extensible-0.14			ef5c380
	9500 achow101/help-rpc-autocomplete			10d8fd0
m	9991 listreceivedbyaddress-filtered-0.14+k	e52444d last=c262be5  # listreceivedbyaddress Filter Address; was #9503
	9504 achow101/dumpmasterprivkey				440991b
	9571 getblockchaininfo_statistics-0.14		e0e0e31 last=557c9a6  # RPC: getblockchaininfo returns BIP signaling statistics
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready: 9697 [Qt] simple fee bumper with user verification
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	9740 dumpwallet-friendly-0.14				efc0987 last=164019d  # Add friendly output to dumpwallet
	# not ready: 9745 [RPC] Getting confirmations command
	9749 unique_spk_mempool+sendraw_force		ef7abcb	last=fe4be7b
	# not ready? 9774 Enable host lookups for -proxy and -onion parameters
	# not ready: 9830 - # Add trusted flag to listunspent result
		# check for unnecessary refactoring; orig fe6cbed
	9849 gui_netwatch+knots-0.14				3e30ee6
	8775 multiwallet_prefactor_rpc-0.14			86a70f6 last=d678771
		# TODO: use pairWtx per 104095b^
	8694 multiwallet-0.14						b887294 last=06b431c
m	- multiwallet_rpc-0.14						2425e6f
	- multiwallet_gui-0.14						f692523
	9724 intro_explain							3c5f457
	9890 gui_openconfig-0.14					4dfa671	last=9ab9e7d  # Add a button to open the config file in a text editor
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	10143 rpc_disconnect_node_by_id-0.14+k		3a8ae05	last=d54297f  # [net] Allow disconnectnode RPC to be called with node id
	# Needs review: 10199 morcos:smarterfee
	# needs review: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	10231 qt_freeze-0.14+knots					0e4a1ef	last=4082fb0
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10275 gettx-with-blockhash-0.14						last=8f84e8c6e1
	10282 timebomb
	10290 stopatheight-0.14
		#+10305
	# TODO 10426 if bytes_serialized is left alone
	10512 samechain_rework
	10442 bip148
	n/a  checkpoint_update						87cd92c
# POLICY:
	# maybe? 9527 ryanofsky:pr/walletrbf
	# maybe? change default confirmation target to 25
	7149 bugfix_priority						859dd5c
	-	 bytespersigopstrict+sendraw_force		360652b
	-    spamfilter+sendraw_force				8d9dbc3
	-    rwconf_policy							744429a
		# TODO: final rebase
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								f20c50b
# BRANDING:
	n/a  knots_branding							8b684e5
	n/a  (bump_version=Knots:20170420)			79e8ebd
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=769bdadd2a)				e8ca4e6  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=16eb4950d5)				d3a038f  # translation update (move after relnotes for 0.14?)
# NOTE: use git diff --minimal for patches!
