timestamp 2017-03-07 10:29:56

#.. checked up to PR #9849

# FIXME: undeprecate priority

checkout v0.14.0
@0.14.x-syslibs
	5872 subdir_incl_compat						c5cab7e
	2241 sys_leveldb							18a4863
	5416 sys_libsecp256k1						fa9f42e
	7485 sys_univalue_def						29ef492
	7522 bugfix_gitdir							4343ab1
	5618 separate_utils-0.14.x					bcebcc1	last=6d5b247 separate_utils
	7339 opt_libevent-0.14						49486e0	last=3cc7b69 opt_libevent
@0.14.x-knots
# TESTS:
	-    travis_qt4_nolibevent					1ed6c96
	9359 test_wallet_immature-0.14				a471c48	last=7ed143c	# Add test for CWalletTx::GetImmatureCredit() returning stale values.
# FIXES:
	9495 -										0765be7 #JeremyRubin:checkqueue-control-lock
	9497 -										2c02ce5 #JeremyRubin:checkqueue-tests
	# broken: 9522 achow101/fix-decoderawtx
	9524 marco/Mf1701-qaPruning					023c03b
	9549 -										a5779d5 #practicalswift:avoid-potential-null-pointer-dereference-in-markblockasinflight
	9622 listsinceblock_removedtxs-0.14			9e7ad7b	last=561b2cf
		# Holding back 44be568..d453b37 "allow_partial" ugliness
	9481 jonas/2017/01/fee_warning				4980c9c
# FUNCTIONALITY:
	 559 accept_nonstdtxn						22e9aa5
	 929 tbc									fae1ad4
	 553 bugfix_qt_uri_amount_parser			adcc600
	5861 gui_restore_addresses					6ccb9f0
	5891 qt_console_history_persist				ce204cf
	5916 keyorigin-0.14							630aec0
	7061 jonas_rpc_rescan-0.14					784407e last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							4ec5d79	last=1f37c87 origin-pull/7107/head
	9592 -										f06d849 #ryanofsky:pr/grbf
	9672 rpc_rbf								e97099b	# WAS 7159 with last=b64ebaf
	7219 txrepl_fullrbf							13ff64f
	7533 sendraw_force							d2190cb
	7510 rwconf+knots							fd4a1d0
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 -										9ba797f
	-    trivial_blockmaxsize_mainnet			bde01d5
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 -										5c2eebf  # getblock extraverbose
	8751 sort-multisigs							f0cceca last=7439562  # multisig sorting
	9017 instagibbs_p2shp2wpkhstuff_partial		bc45206	last=6a67000  # replacing 8992; removed sign/verify message stuff
	8952 -										f94be47  # Add query options to listunspent RPC call
	9152 sweepprivkeys+sendraw_force			42828b6
	9245 ionice									7421787
	8501 stats_rpc-0.14							b67bf61
	8550 stats_qt-0.14							2909178	last=251ee28
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	# useless? 9402  # Allow per network configuration file
	9422 mempool_dat_extensible-0.14			c1ca01b
	9500 achow101/help-rpc-autocomplete			ecd7b96
	9503 -										eab5119 #JeremyRubin:listreceivedbyaddress-filtered
	9504 achow101/dumpmasterprivkey				3c14f76
	9571 -										cc3b8bb # RPC: getblockchaininfo returns BIP signaling statistics
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready: 9697 [Qt] simple fee bumper with user verification
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	9740 -										1fa60ba #Add friendly output to dumpwallet
	# not ready: 9745 [RPC] Getting confirmations command
	9749 unique_spk_mempool+sendraw_force		dbabbb1	last=fe4be7b
	# not ready? 9774 Enable host lookups for -proxy and -onion parameters
	# not ready: 9830 - # Add trusted flag to listunspent result
		# check for unnecessary refactoring; orig fe6cbed
	9849 gui_netwatch+knots-0.14				d8809c6
	8775 multiwallet_prefactor_rpc-0.14			14257db last=d678771
	8694 multiwallet-0.14						f080323 last=2147835
	- multiwallet_rpc-0.14						f582ed6
	- multiwallet_gui-0.14						c0f1fbe
	9724 intro_explain							cd9d813
	n/a  checkpoint_update						667e4d6
# POLICY:
	# maybe? 9527 ryanofsky:pr/walletrbf
	# maybe? change default confirmation target to 25
	7149 bugfix_priority						3db795f
	-	 bytespersigopstrict+sendraw_force		aba2a0e
	-    spamfilter+sendraw_force				c27f365
	-    rwconf_policy							38b3fca
		# TODO: final rebase
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								5e8cdae
# BRANDING:
	n/a  knots_branding							711e641
	n/a  (bump_version=Knots:20170307)			5db9c66
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=c7aabb5746)				c5b9a97  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=f3b6d8592d)				46952c8  # translation update (move after relnotes for 0.14?)
# NOTE: use git diff --minimal for patches!
