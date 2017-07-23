#!/usr/bin/env python
#-*- coding:utf8 -*-

__metaclass__ = type

class Person:
    def __init__(self,name):
        self.name = name
        self.email = "opsvr@opsvr.cn"

info = Person("leo")
print "info.name=",info.name
print "info.email=",info.email
