#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
import os

if len(sys.argv) == 1:
    data = sys.stdin.read()
else:
    try:
        fn = sys.argv[1]
    except IndexError:
        print "Please follow a argument at %s" % __file__
        sys.exit()
    if not os.path.exists(fn):
        print "%s is not exists" % fn
        sys.exit()
    fd = open(sys.argv[1])
    data = fd.read()
    fd.close()

chars = len(data)
words = len(data.split())
lines = data.count('\n')

print "%(lines)s %(words)s %(chars)s" % locals()

