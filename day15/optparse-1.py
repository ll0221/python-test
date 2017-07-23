#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys,os
from optparse import OptionParser

parser = OptionParser()
#parser = OptionParser("Usage:%prog [file1] [file2]...")

parser.add_option("-c",
                  "--chars",
                  dest = "chars",
                  action = "store_true",
                  default = False,
                  help = "only count chars")

parser.add_option("-w",
                  "--words",
                  dest = "words",
                  action = "store_true",
                  default = False,
                  help = "only count words")

parser.add_option("-l",
                  "--lines",
                  dest = "lines",
                  action = "store_true",
                  default = False,
                  help = "only count lines")

options, args = parser.parse_args()
if not (options.lines or options.words or options.chars):
    options.lines,options.words,options.chars = True,True,True
#print options.words, args

data = sys.stdin.read()
chars = len(data)
words = len(data.split())
lines = data.count('\n')

if options.chars:
    print chars,
if options.words:
    print words,
if options.lines:
    print lines,
