#!/usr/bin/env python
#-*- coding:utf8 -*-

def hello(fn):
    print "hello,%s" % fn.__name__
    fn()
    print "goodby,%s" % fn.__name__

#@hello
def foo():
    print "i am foo"
foo()
