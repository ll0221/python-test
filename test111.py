#!/usr/bin/python

a = open('/tmp/tmp.txt','r')
b = a.readlines()
a.close()
print b,
