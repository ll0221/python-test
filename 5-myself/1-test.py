#!/usr/bin/env python
#-*- coding:utf8 -*-

__mateclass__ = type

class Person:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def color(self,color):
        print "%s is %s" % (self.name,color)

girl = Person("canglaoshi")
name = girl.getName()
print "the person's name is:",name
girl.color("yellow")

print "--" * 30
print girl.name
