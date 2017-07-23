#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys,os
from optparse import OptionParser

def opt():
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
    return options,args
    if not (options.lines or options.words or options.chars):
        options.lines,options.words,options.chars = True,True,True

if args:
    fn = args[0]
    with open(args[0]) as fd:
        data = fd.read()
else:
    data = sys.stdin.read()
    fn = ''

def get_count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines,word,chars

def print_wc(options,lines,words,chars,fn):
    if options.chars:
        print chars,
    if options.words:
        print words,
    if options.lines:
        print lines,
    print fn

def main():
    options,args = opt()
    if not (options.lines or options.words or options.chars):
        options.lines,options.words,options.chars = True,True,True
    if args:
        fn = args[0]
        with open(args[0]) as fd:
            data = fd.read()
        lines,words,chars = get_count(data)
        print_wc(options,lines,words,chars)
    else:
        data = sys.stdin.read()
        fn = ''
        lines,words,chars = get_count(data)
        print_wc(options,lines,words,chars,fn)

main()
