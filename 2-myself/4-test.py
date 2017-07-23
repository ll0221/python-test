#!/usr/bin/env python
#-*- coding:utf8 -*-

a = 28

while a:
    if a % 2 == 0:
        a -= 1
        continue
    else:
        print "%d is odd number." % a
        a -= 1
