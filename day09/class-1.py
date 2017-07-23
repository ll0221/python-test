#!/usr/bin/python

class People(object): #def class
    color = 'yellow'
    
    def think(self): #def fangfa
        self.color = "black"
        print "I am a %s" % self.color
        print "I am a thinker"

ren = People()
print ren.color
ren.think()
