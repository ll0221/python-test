#!/usr/bin/python

import sys
import os

def isNum(s):
    for i in s:
        if i not in '0123456789':
            return False
    return True

for i in os.listdir('/proc'):
    if isNum(i):
        print i
