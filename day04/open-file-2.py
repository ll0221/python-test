#!/usr/bin/python

fd = open('/tmp/tmp.txt')
while True:
    line = fd.readline()
    if not line:
        break
    print line,
fd.close()
