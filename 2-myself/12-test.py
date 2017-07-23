#!/usr/bin/env python
#-*- coding:utf8 -*-

x = 2

def funcx():
    global x
    x = 9
    print "This x is in the funcx:---->",x

funcx()
print "*" * 40
print "This x is out the funcx:---->",x
