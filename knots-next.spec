timestamp 2017-04-20 20:24:22

#.. checked up to PR #10234

checkout v0.14.1
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
	9481 jonas/2017/01/fee_warning				be69a9d
	10156 bugfix_restore_onscreen-0.14			6757870	last=b0c302b
	10196 prioritisetx_gbtcache-0.14			fa6493e	last=6a61424
	10234 list_banned_correctly-0.14			b9e0057	last=ea2c925
	-    undeprecate_prioritymining				84b7070
# FUNCTIONALITY:
	 559 accept_nonstdtxn						95e1f89
	 929 tbc									de68c47
	 553 bugfix_qt_uri_amount_parser			8783e76
	5861 gui_restore_addresses					8946951
	5891 qt_console_history_persist				13260e7
	5916 keyorigin-0.14							fc7ea56
	7061 jonas_rpc_rescan-0.14					6c1c307 last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							2817012	last=1f37c87 origin-pull/7107/head
	9592 -										9dbf552 #ryanofsky:pr/grbf
	9672 rpc_rbf								5a31ddf	# WAS 7159 with last=b64ebaf
	7219 txrepl_fullrbf							a005587
	7533 sendraw_force							28a3711
	7510 rwconf+knots							8c46465
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 -										5b62039
	-    trivial_blockmaxsize_mainnet			8d807b3
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 getblock-extraverbose-0.14				2eeae53	last=b779f30  # getblock extraverbose
	8751 sort-multisigs							ab63831 last=30f2ac9  # multisig sorting
	9017 instagibbs_p2shp2wpkhstuff_partial		4048b9b	last=6a67000  # replacing 8992; removed sign/verify message stuff
m	8952 listunspent_query_options-0.14+knots	5ab1b2d	last=11ee5ec  # Add query options to listunspent RPC call
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sendraw_force			af5ae0a
	9245 ionice									a8fa82d
	8501 stats_rpc-0.14							89cac9f
	8550 stats_qt-0.14							e33de43	last=251ee28
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	# useless? 9402  # Allow per network configuration file
	9422 mempool_dat_extensible-0.14			4d9dc41
	9500 achow101/help-rpc-autocomplete			a7e3028
m	9991 listreceivedbyaddress-filtered-0.14+k	5f08944 last=c262be5  # listreceivedbyaddress Filter Address; was #9503
	9504 achow101/dumpmasterprivkey				8928ae5
	9571 getblockchaininfo_statistics-0.14		9de2c14 last=557c9a6  # RPC: getblockchaininfo returns BIP signaling statistics
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready: 9697 [Qt] simple fee bumper with user verification
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	9740 dumpwallet-friendly-0.14				fcf51ef last=164019d  # Add friendly output to dumpwallet
	# not ready: 9745 [RPC] Getting confirmations command
	9749 unique_spk_mempool+sendraw_force		603297e	last=fe4be7b
	# not ready? 9774 Enable host lookups for -proxy and -onion parameters
	# not ready: 9830 - # Add trusted flag to listunspent result
		# check for unnecessary refactoring; orig fe6cbed
	9849 gui_netwatch+knots-0.14				3fac2c8
	8775 multiwallet_prefactor_rpc-0.14			da24c20 last=d678771
		# TODO: use pairWtx per 104095b^
	8694 multiwallet-0.14						b62cde6 last=06b431c
m	- multiwallet_rpc-0.14						3d05f3e
	- multiwallet_gui-0.14						32422f8
	9724 intro_explain							b020076
	9890 gui_openconfig-0.14					8ab9046	last=9ab9e7d  # Add a button to open the config file in a text editor
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	10143 rpc_disconnect_node_by_id-0.14+k		e446e4f	last=d54297f  # [net] Allow disconnectnode RPC to be called with node id
	# Needs review: 10199 morcos:smarterfee
	# needs review: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	10231 qt_freeze-0.14+knots					193f113	last=4082fb0
	# needs review/concept ack: 10233
	n/a  checkpoint_update						8e39a37
# POLICY:
	# maybe? 9527 ryanofsky:pr/walletrbf
	# maybe? change default confirmation target to 25
	7149 bugfix_priority						814743d
	-	 bytespersigopstrict+sendraw_force		8ba3f83
	-    spamfilter+sendraw_force				0c1dc58
	-    rwconf_policy							f9b60f1
		# TODO: final rebase
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								13211e0
# BRANDING:
	n/a  knots_branding							a971267
	n/a  (bump_version=Knots:20170420)			7fed345
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=4fa4b0e078)				9f08a43  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=16eb4950d5)				79f3fb3  # translation update (move after relnotes for 0.14?)
# NOTE: use git diff --minimal for patches!
