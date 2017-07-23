#!/usr/bin/python
#coding:utf8

class People(object):  #定义类
    color = 'yellow'
    __age = 30

    def think(self):
        self.color = "black"
        print "I am a %s." % self.color
        print "I am a thinker."
        print self.__age

    def __talk(self):
        print "I am talking with Tom"

    def test(self):
        print 'Testing...'

    cm = classmethod(test)

jack = People()
People.cm()
