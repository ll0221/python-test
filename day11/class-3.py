#!/usr/bin/python
#-*- coding:utf8 -*-

var5 = "全局变量 var5"
class MyClass(object):
    var1 = '类属性，类的公有属性 var1'
    __var2 = '类的私有属性 __var2'

    def func1(self):
        self.var3 = '对象的公有属性 var3'
        self.__var4 = '对象的私有属性 __var4'
        var5 = '函数的局部变量'
        print self.__var4
        print var5

    def func2(self):
        print self.var1
        print self.__var2
        print self.var3
        print self.__var4
        print var5

mc = MyClass()
mc.func1()
print '*' * 50
mc.func2()
print '*' * 50
print mc.__dict__
print '*' * 50
print MyClass.__dict__
