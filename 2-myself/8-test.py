#!/usr/bin/env python
#-*- coding:utf8 -*-

f = open("/xdfapp/learn/python/2-myself/read.md")

while True:
    line = f.readline()
    if not line:
        break
    print line,
f.close()
