#!/bin/bash
last_checked=1744511465
exec ./check-pr-updates.pl $last_checked <knots-next.spec 3<github_auth | sort -k 3
