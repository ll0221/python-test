#!/usr/bin/python

x = 100
def fun():
    x = 1
    y = 1
    print locals()

fun()
print locals()
