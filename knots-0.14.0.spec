timestamp 2017-03-07 10:29:56
lastapply no-merge

#.. checked up to PR #9849

checkout v0.14.0
@0.14.x-syslibs
	5872 subdir_incl_compat						1ac82ae
	2241 sys_leveldb							4e19700
	5416 sys_libsecp256k1						411cb7d
	7485 sys_univalue_def						3432902
	7522 bugfix_gitdir							5960300
	5618 separate_utils-0.14.x					4a38db7	last=6d5b247 separate_utils
	7339 opt_libevent-0.14						a4b3d8a	last=3cc7b69 opt_libevent
@0.14.x-knots
# TESTS:
	-    travis_qt4_nolibevent					dc5d245
	9359 test_wallet_immature-0.14						last=7ed143c	# Add test for CWalletTx::GetImmatureCredit() returning stale values.
# FIXES:
	9495 - #JeremyRubin:checkqueue-control-lock
	9497 - #JeremyRubin:checkqueue-tests
	# broken: 9522 achow101/fix-decoderawtx
	9524 marco/Mf1701-qaPruning
	9549 - #practicalswift:avoid-potential-null-pointer-dereference-in-markblockasinflight
	9622 listsinceblock_removedtxs-0.14					last=561b2cf
		# Holding back 44be568..d453b37 "allow_partial" ugliness
	9481 jonas/2017/01/fee_warning
# FUNCTIONALITY:
	 559 accept_nonstdtxn						ef78424
	 929 tbc									71afd77
	 553 bugfix_qt_uri_amount_parser			9372089
	5861 gui_restore_addresses					beb0845
	5891 qt_console_history_persist				4c61f10
	5916 keyorigin-0.14							96b7b0c
	7061 jonas_rpc_rescan-0.14					7d87b7b last=d1aa8a9 jonas/2015/11/wallet_rescan_rpc
	7107 qtnetworkport							92af35b	last=1f37c87 origin-pull/7107/head
	9592 - #ryanofsky:pr/grbf
	9672 rpc_rbf								0cafb83	# WAS 7159 with last=b64ebaf
	7219 txrepl_fullrbf							c63acf8
	7533 sendraw_force							b6519dd
	7510 rwconf+knots							b3bcfbc
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 -										9f0194a
	-    trivial_blockmaxsize_mainnet			4079db4
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 -										27fe8d3  # getblock extraverbose
	8751 sort-multisigs							4554fe2 last=7439562  # multisig sorting
	9017 instagibbs_p2shp2wpkhstuff_partial		        last=6a67000  # replacing 8992; removed sign/verify message stuff
	8952 -										291f4f5  # Add query options to listunspent RPC call
	9152 sweepprivkeys+sendraw_force			55f1168
	9245 ionice									30fefc9
	8501 stats_rpc-0.14							81634f7
	8550 stats_qt-0.14							d060966	last=251ee28
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	# useless? 9402  # Allow per network configuration file
	9422 mempool_dat_extensible-0.14
	9500 achow101/help-rpc-autocomplete
	9503 - #JeremyRubin:listreceivedbyaddress-filtered
	9504 achow101/dumpmasterprivkey
	9571 - # RPC: getblockchaininfo returns BIP signaling statistics
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready: 9697 [Qt] simple fee bumper with user verification
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	9740 - #Add friendly output to dumpwallet
	# not ready: 9745 [RPC] Getting confirmations command
	9749 unique_spk_mempool+sendraw_force				last=fe4be7b
	# not ready? 9774 Enable host lookups for -proxy and -onion parameters
	# not ready: 9830 - # Add trusted flag to listunspent result
		# check for unnecessary refactoring; orig fe6cbed
	9849 gui_netwatch+knots-0.14
	8775 multiwallet_prefactor_rpc-0.14			436abe5 last=d678771
	8694 multiwallet-0.14						9c10f29 last=2147835
	- multiwallet_rpc-0.14
	- multiwallet_gui-0.14
	9724 intro_explain
	n/a  checkpoint_update						219ac9b
# POLICY:
	# maybe? 9527 ryanofsky:pr/walletrbf
	# maybe? change default confirmation target to 25
	7149 bugfix_priority						9883962
	-	 bytespersigopstrict+sendraw_force		b11e706
	-    spamfilter+sendraw_force				c5d3284
	-    rwconf_policy							8e2cfb0
		# TODO: final rebase
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								ac19e0b
# BRANDING:
	n/a  knots_branding							c30e154
	n/a  (bump_version=Knots:20170307)			5ad6763
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=276d134961)				ef9c66d  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=f3b6d8592d)				dd33592  # translation update (move after relnotes for 0.14?)
# NOTE: use git diff --minimal for patches!
