timestamp 2017-11-05 11:05:21

#.. checked up to PR #11209

checkout v0.15.1rc1
@0.15.x-syslibs
	5872 subdir_incl_compat						f45c042844
	2241 sys_leveldb							1640e1c33d
	5416 sys_libsecp256k1-0.15					2aa4352aa0	last=37109ccc1d sys_libsecp256k1
	7485 sys_univalue_def						49018af089
	5618 separate_utils							92f93108dd
	7339 opt_libevent							c151287c2f
@0.15.x-knots
# TESTS:
	7142 travis_qt4								2aa48dfe11
	-    travis_nolibevent						f7502f2cba
# FIXES:
	9524 marco/Mf1701-qaPruning					f3cbbc60c6
	#10529? systemd stuff
	10595 gbt_nosegwit_fix						6af558251f
	11026 bugfix_acceptnonstd_def				a5ebe4f877
	10731 log_more_uacomment					b3e0e3f170
	10957 -										28c612d087	# Avoid BIP9Stats object w/ uninitialized values
	11169 rm_hide_tabs-0.15						93f5ee585e	# Make tabs toolbar no longer have a context menu
	11198 -										2bb0ac1cb9	# [Qt] Fix pkg name on 'open config file' tooltip
	11206 fix_hidetrayicon_accel				eed9a49c41	# Fix accelerator key for Hide tray icon
	11208 fix_offscreen-0.15					518d05399e	last=6067244698	# Fixing offscreen GUI issue
	11332 bugfix_customfeeradio-0.15			10e3cd04b2	last=cdaf3a1f9e
# FUNCTIONALITY:
	-     restore_blockmaxsize
	n/a  def_sse4_sha256						bf9540b1f4
	7061 wallet_rescan_rpc-0.15					a2a32be9a9	last=bf6f25373a
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonas/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	8751 sort-multisigs							95cf8a9936	last=222cfb940d  # multisig sorting
	11089 p2shp2wpkhstuff						eaceeb3ec0  # replacing 8992, 9017; removed sign/verify message stuff
	# NOWHERE NEAR READY: 9806 UTXO index stuff
	9152 sweepprivkeys							9bf4a397ff
	9245 ionice									6a8229f3b6
	-    ionice_win								c590dfa43d
	8501 old_stats_rpc							86b9b56a46	last=c412d0a66e
		# Held back on old version due to lack of GUI updates
	8550 old_stats_qt							961efb8653	last=251ee28
	# needs review: 9332 Let wallet importmulti RPC accept labels for standard scriptPubKeys
	9422 mempool_dat_extensible					f84754560e
	9991 listreceivedbyaddress-filtered			4cae0a2cd0	last=c262be5  # listreceivedbyaddress Filter Address; was #9503
	9504 dumpmasterprivkey						50d85ee436	last=07fc81109a
	# not ready yet: SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready: 9662 Add `-disablehot` mode: a sane mode for watchonly-wallets
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# ehhhhh?? 9728 Can create Watch Only HD wallet with -hdwatchonly
	# not ready: 9745 [RPC] Getting confirmations command
	9849 gui_netwatch							57541053e3
	10615 multiwallet_rpc+opt_libevent			a1db2f517d	last=370d3361e8
	11383 multiwallet_gui+rm_hide_tabs			eb8203dbb3	last=7790bcdbf2 multiwallet_gui
	# needs review: 10040 - #wallet: use headers chain for anti fee sniping
	# needs review? CONSIDER FOR 0.15.0 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# needs review/concept ack: 10233 and/or 10386
	# TODO 10267 (conflicts with rwconf?)
	10275 gettx-with-blockhash-0.15				8f338e0578	last=300a5f15d5	# [rpc] Allow fetching tx directly from specified block in getrawtransaction
	10554 zmq_wtx								e700ad2d22	last=d358230d10	# ZMQ: add publishers for wallet transactions.
	10593 relax_invblk_punishment				b8f7d06a62
	10594 whitelist_outgoing					82b021688b
	10350 codeshark/MFWB_no_bump_2				a493278023	# Added support for MSG_FILTERED_WITNESS_BLOCK messages
	10729 scriptex								8e6403dde7
	10730 scriptflag_strings-mini				1e4295e36e	last=97cae3915f
	n/a   script_debugger-mini					0afed0460e	last=8d1ff9f035 script_debugger
	10871 cli_getinfo-0.15						977d461711	last=f2fde56bc6 achow101/cli-getinfo
		# test not backported, since it relies on very new frameworks
	10997 stdinrpcpass+cli_getinfo-0.15			d6f667ebb8	# Add option -stdinrpcpass to bitcoin-cli
	# Requires new QA stuff? 11125 promag/2017-08-stdinrpcpass-functional-test
	11099 rpc_savemempool+mempool_dat_ext-0.15	941c2f6363	last=1aa97ee088
	# TODO: 11117 sipa:201708_nocbitcoinaddress
	# TODO: 11167 sipa:201708_bech32
	# TODO: 11177 rawodb:pr/rpc_getsegwitaddresses
	# TODO: 11178 MeshCollider:201708_rawtx_bool
	# TODO: 11200 achow101:gui-recan-abort
	# Needs work: 11201 justicz:maxj_add_verify_tx_rpc
	11203 rpc_mempoolentry_txhash				e731a14670	last=617c459c6c
# Non-upstreamed functionality:
	7107 qtnetworkport							7f9a041b82	last=1f37c87 origin-pull/7107/head
	7533 sendraw_force+knots					2e39a01eba	last=89e516ffcb sendraw_force
	11082 rwconf-0.15							ed1db5c2ff	last=59d78f9fc1 rwconf
	7510 rwconf_gui-0.15+qtnetworkport			8cd547a79b	last=87f7d1f455 rwconf_gui-0.15
	5916 keyorigin								1538fa0865
	 559 accept_nonstdtxn						b4dacf415a
	 929 tbc									01bb601248
	 553 bugfix_qt_uri_amount_parser			d88519dc6d
	-    mining_priority						481d33d4da
	5861 gui_restore_addresses					4863c923d4
	5891 qt_console_history_persist				243acc6420
	7219 txrepl_fullrbf							f834138fa4
	# TODO: some way to add UA comments via rwconf
	10282 timebomb_knots-0.15					b71f948865	last=21f123db98
	n/a  checkpoint_update						f2da8e0471
# POLICY:
	# TODO: 10823 greenaddress/replace-by-fee-old-transactions
	# maybe? 9527 ryanofsky:pr/walletrbf
	# maybe? change default confirmation target to 25+
	-	 bytespersigopstrict+sendraw_force		84a4b57ff6
	#dropping? -    spamfilter+sendraw_force				bbbcd274b6
	9749 unique_spk_mempool+sendraw_force		34c0aaacee	last=9b75ab5b39
	-    rwconf_policy							087352a73a
		TODO: final rebase (fix blockmax{size,weight})
# Pre-BRANDING: (needs to be part of F patch to eliminate binary files)
	7483 svg_icon								9769b4d222
# BRANDING:
	n/a  knots_branding							11cd47d0c4
	n/a  (cherrypick=af9c353c0dd6012e91)		2ddc6eb90e	# doc/{bips,files}
	n/a  (bump_version=Knots:20170914)			046850d23d
#	n/a  knots_historical_relnotes				61100a2
	n/a  (cherrypick=32f41a825e)				10c01d90e4  # release notes: write/update, including change log and credits
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
	n/a  (cherrypick=703daed7c9)				431cf19a91  # translation update
	n/a  (cherrypick=e6478ff3f4)				3ae5fe9a5b	# update manpages
# NOTE: use git diff --minimal for patches!
