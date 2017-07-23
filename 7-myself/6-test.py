#!/usr/bin/env python
#-*- coding:utf8 -*-

__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = "leo"
        self.__name = "opsvr"

    @property
    def name(self):
        return self.__name

if __name__ == "__main__":
    p = ProtectMe()
    print p.name
