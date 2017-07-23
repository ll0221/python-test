#!/usr/bin/python
#coding:utf8

class People(object):
    color = 'yellow'
    __age = 30

    def think(self):
        self.color = "black"
        print "I am a %s" % self.color
        print "I am a thinker"

ren = People()
ren.color = '白人'
print ren.color
ren.think()
print ren._People__age
print ren.__dict__
print '#' *30
print People.color
print '#' *30
print People.__dict__
