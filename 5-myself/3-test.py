#!/usr/bin/env python
#-*- coding:utf8 -*-

__mateclass__ = type

class Person:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def breast(self,n):
        self.breast = n

    def color(self,color):
        print "%s is %s" % (self.name,color)

    def how(self):
        print "%s breast is %s" % (self.name,self.breast)


girl = Person("canglaoshi")
girl.breast(90)

girl.color("white")
girl.how()
