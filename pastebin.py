#!/usr/bin/env python

# Usage: ./pastebin.py filename
# use - as filename for stdin
# Requires http://wwwsearch.sourceforge.net/mechanize/

import mechanize
import sys
import os

br = mechanize.Browser()
br.open("http://pastebin.com/")

br.select_form("myform")

if sys.argv[1] == "-":
	file = sys.stdin
else:
	file = open(sys.argv[1])
	br["paste_name"] = os.path.basename(sys.argv[1])

br["paste_code"] = str(file.read())

print br.submit().geturl() 
