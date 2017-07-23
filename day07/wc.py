#!/usr/bin/python

def wordCount(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print lines,words,chars

if __name__ == '__main__':
    s = open('/etc/passwd').read()
    wordCount(s)

#s = open('/etc/passwd').read()
#wordCount(s)
