#!/usr/bin/python

key = ''
while key != 'q':
    print 'Hello'
    key = raw_input("Please input something,q for quit:")
    if key == '':
        break
    if key == 'quit':
        continue
    print 'aaaa'
else:
    print 'World'
print "End"
