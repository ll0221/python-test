#!/usr/bin/python

def fun():
    sth = raw_input("Please input a number:")
    try:
        if type(int(sth)) == type(1):
            print "%s is a number." % sth
    except:
        print "%s is not number." % sth
fun()
