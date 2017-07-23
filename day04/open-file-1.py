#!/usr/bin/python

fd = open('/tmp/tmp.txt')
#for line in fd.readlines():
for line in fd:
    print line,
