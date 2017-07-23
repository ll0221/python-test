#!/usr/bin/env python
#-*- coding:utf8 -*-

class Plus():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def get_result(self):
        return self.a+self.b 

c1=Plus(1,2)
result1=c1.get_result()
print result1
