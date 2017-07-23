#!/usr/bin/env python
#-*- coding:utf8 -*-

__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = "leo"
        self.__name = "opsvr"

    def __python(self):
        print "I love python."

    def code(self):
        print "Which language do you like?"
        self.__python()

if __name__ == "__main__":
    p = ProtectMe()
    print p.me
    p.code()
p.__python()
