#!/usr/bin/python

x = 100
def fun():
    global x
    x += 1
    print x

fun()
print x
