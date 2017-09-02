timestamp 2017-08-29 04:09:24
lastapply no-merge

#.. checked up to PR #11209

checkout v0.15.0rc3
@0.15.x-syslibs
	5872 subdir_incl_compat						cbde6af708
	2241 sys_leveldb							e5befdbe89
	5416 sys_libsecp256k1-0.15					7d26bf48ba	last=37109ccc1d sys_libsecp256k1
	7485 sys_univalue_def						97fc42318e
	5618 separate_utils							cdf705c9c6
	7339 opt_libevent							318935fbac
@0.15.x-knots
# TESTS:
	7142 travis_qt4								52982f061b
	-    travis_nolibevent
# FIXES:
	9524 marco/Mf1701-qaPruning					ac18ebe9fa
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						b356af91e7
	11026 bugfix_acceptnonstd_def
	10731 log_more_uacomment
	10957 -													# Avoid BIP9Stats object w/ uninitialized values
	11169 rm_hide_tabs-0.15									# Make tabs toolbar no longer have a context menu
	11198 -													# [Qt] Fix pkg name on 'open config file' tooltip
	11206 fix_hidetrayicon_accel							# Fix accelerator key for Hide tray icon
	11208 fix_offscreen-0.15								last=6067244698	# Fixing offscreen GUI issue
# FUNCTIONALITY:
	n/a  def_sse4_sha256
	7061 jonas/2015/11/wallet_rescan_rpc		edf97337e6
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs							8a21f38186 last=464827af1e  # multisig sorting
	11089 p2shp2wpkhstuff						e7955d907f  # replacing 8992, 9017; removed sign/verify message stuff
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							3c1f05194e
	9245 ionice									5093c918bf
	-    ionice_win
	8501 old_stats_rpc							028fb4b2da	last=c412d0a66e
		# Held back on old version due to lack of GUI updates
	8550 old_stats_qt							273230b072	last=251ee28
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					234ccb0dd3
	9991 listreceivedbyaddress-filtered			5cb3754370 last=c262be5  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey						3a3bb63b93	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							03a1773aa0
	10615 multiwallet_rpc+opt_libevent			103657281f	last=370d3361e8
	- multiwallet_gui+rm_hide_tabs				5427fe36fd	last=7790bcdbf2 multiwallet_gui
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs review? CONSIDER FOR 0.15.0 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10275 gettx-with-blockhash-0.15				f5910114d6	last=440123fb8c	# [rpc] Allow fetching tx directly from specified block in getrawtransaction
	10554 zmq_wtx											last=d358230d10	# ZMQ: add publishers for wallet transactions.
	10593 relax_invblk_punishment				47b17f1421
	10594 whitelist_outgoing					c4bd7ca174
	10350 codeshark/MFWB_no_bump_2							# Added support for MSG_FILTERED_WITNESS_BLOCK messages
	10729 scriptex
	10730 scriptflag_strings-mini							last=97cae3915f
	n/a   script_debugger-mini								last=8d1ff9f035 script_debugger
	10871 cli_getinfo-0.15									last=e697d546c2 achow101/cli-getinfo
	10997 stdinrpcpass+cli_getinfo-0.15						# Add option -stdinrpcpass to bitcoin-cli
	# Requires new QA stuff? 11125 promag/2017-08-stdinrpcpass-functional-test
	11099 rpc_dumpmempool+mempool_dat_ext-0.15				last=67d307f606
	# TODO: 11117 sipa:201708_nocbitcoinaddress
	# TODO: 11167 sipa:201708_bech32
	# TODO: 11177 rawodb:pr/rpc_getsegwitaddresses
	# TODO: 11178 MeshCollider:201708_rawtx_bool
	# TODO: 11200 achow101:gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	FIXME: 11203 sdaftuar:2017-08-add-wtxid-to-mempool-entry
# Non-upstreamed functionality:
	7107 qtnetworkport							fa87fd57b9	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					4b4d7b379a	last=89e516ffcb sendraw_force
	11082 rwconf-0.15										last=59d78f9fc1 rwconf
	7510 rwconf_gui-0.15+qtnetworkport			6d2afb424d	last=87f7d1f455 rwconf_gui-0.15
	5916 keyorigin								714bf57365
	 559 accept_nonstdtxn						0411d10872
	 929 tbc									7d9ece422b
	 553 bugfix_qt_uri_amount_parser			bdf5e63f09
	-    mining_priority
	5861 gui_restore_addresses					48b98180e6
	5891 qt_console_history_persist				40f1e383fe
	7219 txrepl_fullrbf							67980e9ad0
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots-0.15					57b5104150	last=21f123db98
	n/a  checkpoint_update						4254fd40a2
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	# maybe? 9527 ryanofsky:pr/walletrbf
	# maybe? change default confirmation target to 25+
	-	 bytespersigopstrict+sendraw_force		d332058883
	#dropping? -    spamfilter+sendraw_force				bbbcd274b6
	9749 unique_spk_mempool+sendraw_force		15d37c3210	last=9b75ab5b39
	-    rwconf_policy							28174b4138
		TODO: final rebase
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								b593bdb523
# BRANDING:
	n/a  knots_branding							022e2c04cf
	n/a  (cherrypick=af9c353c0dd6012e91)					# doc/{bips,files}
	n/a  (bump_version=Knots:20170902)			4046352891
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=0333426103)				21fcedf33b  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=438ecc5957)				c00f805f48  # translation update (move after relnotes for 0.14?)
	n/a  (cherrypick=3156567268)				e7a3c1cba8	# update manpages
# NOTE: use git diff --minimal for patches!
