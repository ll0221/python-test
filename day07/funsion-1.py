#!/usr/bin/python

def fun():
    sth = raw_input("Please input something:")
    try:
        if type(int(sth)) == type(1):
            print "%s is a number" % sth
    except ValueError:
        print "%s is not number" %sth

fun()
