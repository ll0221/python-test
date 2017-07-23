#!/usr/bin/python

import sys
import time

for i in xrange(10):
    if i == 3:
        continue
    elif i == 5:
        continue
        #break
    elif i == 6:
        pass
    elif i == 7:
        sys.exit()
    print i
else:
    print "END"
