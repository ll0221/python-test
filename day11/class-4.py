#!/usr/bin/python
#-*- coding:utf8 -*-

class MyClass(object):
    name = 'Test'

    def __init__(self):
        print '*' * 50
        self.func1()
        self.__func2()
        self.classFun()
        self.staticFun()
        print '*' * 50

    def func1(self):
        print self.name,
        print "公有方法"
        self.__func2()

    def __func2(self):
        print self.name,
        print "私有方法"

    @classmethod
    def classFun(self):
        print self.name,
        print "类方法"

    @staticmethod
    def staticFun():
        print MyClass.name,
        print "静态方法"

mc = MyClass()
print '*' * 50
mc.func1()
print '*' * 50
MyClass.classFun()
print '*' * 50
MyClass.staticFun()
print '*' * 50
