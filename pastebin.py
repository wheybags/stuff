#!/usr/bin/env python
import mechanize
import sys

br = mechanize.Browser()
br.open("http://pastebin.com/")

br.select_form("myform")

br["paste_code"] = str(open(sys.argv[1]).read())

print br.submit().geturl() 
