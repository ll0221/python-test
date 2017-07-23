#!/usr/bin/env python
#-*- coding:utf8 -*-

class Person:
    def __init__(self,name,lang="golang",website="opsvr.cn"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "abc@123.com"

laoqi = Person("laoqi")
info = Person("lao",lang="python",website="k8s.com")

print "laoqi.name=",laoqi.name
print "info.name=",info.name
print "-" * 30
print "laoqi.lang=",laoqi.lang
print "info.lang=",info.lang
print "-" * 30
print "laoqi.website=",laoqi.website
print "info.website=",info.website
