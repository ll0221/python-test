#!/usr/bin/python

#print [i+2 for i in range(1,11) if i % 2 == 0 ]
for i in [i**2 for i in range(1,11) if i % 2 != 0]:
    print i,
