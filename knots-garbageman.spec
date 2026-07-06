timestamp 2026-07-06 00:00:00
#lastapply no-merge

# Sub-Knots example: start from an official Knots 29.3 release and layer the
# garbageman feature set on top. Unlike the release specs (which checkout Core
# and rebuild Knots), a sub-Knots spec checks out the finished Knots release, so
# it only assembles YOUR additions.

checkout v29.3.knots20260508
	n/a	chrisguida/garbageman-29.3	last=ccc7097e24 chrisguida/garbageman-29.3
