#!/usr/bin/env python
#-*- coding:utf8 -*-

def h():
    print 'one'
    yield 1
    print 'two'
    yield 2
    print 'three'
    yield 3
h()
