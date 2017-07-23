#!/usr/bin/env python
#-*- coding:utf8 -*-

class MyRange(object):
    def __init__(self,n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

if __name__ == "__main__":
    x = MyRange(7)
    print list(x)
    print "x.next()==>",x.next()
