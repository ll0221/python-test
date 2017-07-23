#!/usr/bin/env python
#-*- coding:utf8 -*-

from sys import stdin

data = stdin.read()

chars = len(data)
words = len(data.split())
lines = data.count('\n')

print "%(lines)s %(words)s %(chars)s" % locals()
print chars,words,lines
