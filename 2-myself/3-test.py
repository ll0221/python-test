#!/usr/bin/env python
#-*- coding:utf8 -*-

a = 9

while a:
    if a % 2 == 0:
        break
    else:
        print "%d is odd number." % a
        a = 0
print "%d is even number." % a
