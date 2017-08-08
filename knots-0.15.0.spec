timestamp 2017-06-18 17:25:52

#.. checked up to PR #10495

checkout v0.14.2
@0.14.x-syslibs
	5872 subdir_incl_compat						cbde6af708
	2241 sys_leveldb							e5befdbe89
	5416 sys_libsecp256k1						7d26bf48ba
	7485 sys_univalue_def						97fc42318e
	7522 bugfix_gitdir							b8321a2832
	5618 separate_utils-0.14.x					cdf705c9c6	last=6d5b247 separate_utils
	7339 opt_libevent-0.14						318935fbac	last=3cc7b69 opt_libevent
@0.14.x-knots
# TESTS:
	-    travis_qt4_nolibevent					52982f061b
m	9359 test_wallet_immature-0.14				49b24492a4	last=7ed143c	# Add test for CWalletTx::GetImmatureCredit() returning stale values.
# FIXES:
	9495 -										c1ad5981cb #JeremyRubin:checkqueue-control-lock
	9497 -										172c99c008 #JeremyRubin:checkqueue-tests
	# broken: 9522 achow101/fix-decoderawtx
	9524 marco/Mf1701-qaPruning					ac18ebe9fa
	9549 -										927435d1c3 #practicalswift:avoid-potential-null-pointer-dereference-in-markblockasinflight
	9622 listsinceblock_removedtxs-0.14			d848d666f0	last=5d352044ca
		# Hold back (eg 44be568..d453b37) any new "allow_partial" ugliness
	9481 fee_warning-0.14						beddb821c9
		#+10008
	10156 bugfix_restore_onscreen-0.14			b3ef873f99	last=b0c302b
	10196 prioritisetx_gbtcache-0.14			95e5e7ae57	last=6c2e25caf6
	9853  fixerrorcodes-0.14					0d148f6a60
	10376 disconnect_ban_fixes-0.14				0777533cd6
		#+10234+10143p+9853
NM	10234 list_banned_correctly-0.14			8b790db953
		# Now included in 10376+etc
	10328 debianppa-0.14						b333f12822
	# Misc fixes:
	10250 0.14.2_fixes_subst^^^					85475ecb9a
	10265 0.14.2_fixes_subst^^					995f3b22cd
	10308 0.14.2_fixes_subst^					96b092ecba
	10445 0.14.2_fixes_subst					b0b7ea09a9
	10595 gbt_nosegwit_fix-0.14					b356af91e7	last=4292a752c7
	-    undeprecate_prioritymining				b943c70880
# FUNCTIONALITY:
	 559 accept_nonstdtxn						0411d10872
	 929 tbc									7d9ece422b
	 553 bugfix_qt_uri_amount_parser			bdf5e63f09
	5861 gui_restore_addresses					48b98180e6
	5891 qt_console_history_persist				40f1e383fe
	5916 keyorigin-0.14							714bf57365
	7061 jonas_rpc_rescan-0.14					edf97337e6 last=0092c0662c jonas/2015/11/wallet_rescan_rpc
		# Skipping 0092c0662c which removes -rescan functionality
	7107 qtnetworkport							fa87fd57b9	last=1f37c87 origin-pull/7107/head
	9592 gui_rbf_checkbox-0.14					8dcd58fb79
		#+10242
m	9672 rpc_rbf-0.14+k							5809aa2f1c	last=9a5a1d7d45  # WAS 7159 with last=b64ebaf
	7219 txrepl_fullrbf							67980e9ad0
	7533 sendraw_force							4b4d7b379a
	7510 rwconf+knots							6d2afb424d
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	8384 txinerr_witness-0.14+k					91c64d21d7
	-    trivial_blockmaxsize_mainnet			0d80ba743d
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8704 getblock-extraverbose-0.14				3ee9a9401f	last=e3c9f2ddb1  # getblock extraverbose
	8751 sort-multisigs-0.14+knots				8a21f38186 last=69a90ec573  # multisig sorting
	9017 instagibbs_p2shp2wpkhstuff_partial		e7955d907f	last=6a67000  # replacing 8992; removed sign/verify message stuff
	8952 listunspent_query_options-0.14+knots	bfa2964259	last=11ee5ec  # Add query options to listunspent RPC call
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys+sendraw_force			3c1f05194e
	9245 ionice									5093c918bf
	8501 stats_rpc-0.14							028fb4b2da
m	8550 stats_qt-0.14							273230b072	last=251ee28
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	# useless? 9402  # Allow per network configuration file
	9422 mempool_dat_extensible-0.14			234ccb0dd3
	9500 achow101/help-rpc-autocomplete			ac34d0620e
	9991 listreceivedbyaddress-filtered-0.14+k	5cb3754370 last=c262be5  # listreceivedbyaddress Filter Address; was #9503
	9504 achow101/dumpmasterprivkey				3a3bb63b93
	9571 getblockchaininfo_statistics-0.14		6b365cbf20 last=557c9a6  # RPC: getblockchaininfo returns BIP signaling statistics
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready: 9697 [Qt] simple fee bumper with user verification
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	9740 dumpwallet-friendly-0.14				15df875b0c last=164019d  # Add friendly output to dumpwallet
	# not ready: 9745 [RPC] Getting confirmations command
	9749 unique_spk_mempool+sendraw_force		15d37c3210	last=fe4be7b
	# not ready? 9774 Enable host lookups for -proxy and -onion parameters
	# not ready: 9830 - # Add trusted flag to listunspent result
		# check for unnecessary refactoring; orig fe6cbed
	9849 gui_netwatch+knots-0.14				03a1773aa0
m	8775 multiwallet_prefactor_rpc-0.14			848ca2fe1c last=d678771
		# TODO: use pairWtx per 104095b^
	8694 multiwallet-0.14						0b5d79a530 last=c237bd750e
		# TODO: postponed 06b431cf11..8284a27b9a waiting for translations
	10615 multiwallet_rpc-0.14					103657281f last=dbbdef9942
	- multiwallet_gui-0.14						5427fe36fd
	9724 intro_explain							285fe2eb3e
	9890 gui_openconfig-0.14					4d829b692a	last=9ab9e7d  # Add a button to open the config file in a text editor
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
NM	10143 rpc_disconnect_node_by_id-0.14+k		7a79534eb1
	10143 rpc_disconnect_node_by_id-0.14		74e37424dd	last=d54297f1a8
	# Needs review: 10199 morcos:smarterfee
	# needs review: 10200 sdaftuar:2017-04-dont-mine-recent-tx
TM	10231 qt_freeze-0.14+knots					ee956e18a9
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10275 gettx-with-blockhash-0.14				f5910114d6	last=8f2ce52c92
	10282 timebomb_knots-0.14					57b5104150	last=21f123db98
	10290 stopatheight-0.14						26dac5841a
		#+10305+10569
	# TODO 10426 if bytes_serialized is left alone
	10593 relax_invblk_punishment-0.14			47b17f1421	last=ba51652610
	10594 whitelist_outgoing					c4bd7ca174
	10532 bip148-0.14+knots						b7496c800c	last=1115b02c67
	n/a  checkpoint_update						4254fd40a2
# POLICY:
	# maybe? 9527 ryanofsky:pr/walletrbf
	# maybe? change default confirmation target to 25
	7149 bugfix_priority						96b8318528
	-	 bytespersigopstrict+sendraw_force		d332058883
	-    spamfilter+sendraw_force				bbbcd274b6
	-    rwconf_policy							28174b4138
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								b593bdb523
# BRANDING:
	n/a  knots_branding							022e2c04cf
	n/a  (bump_version=Knots:20170618)			4046352891
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=72645b3f33)				21fcedf33b  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# UPDATE doc/files.md versions! and 9263 in 0.14
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=438ecc5957)				c00f805f48  # translation update (move after relnotes for 0.14?)
	n/a  (cherrypick=3156567268)				e7a3c1cba8	# update manpages
# NOTE: use git diff --minimal for patches!
