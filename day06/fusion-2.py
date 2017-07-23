#!/usr/bin/python

import os
def print_files(path):
    isdir,isfile,join = os.path.isdir,os.path.isfile,os.path.join
    isdir = os.listdir(path)
    dirs = [i for i in isdir if isdir(join(path,i))]
    files = [i for i in isdir if isfile(join(path,i))]
    if dirs:
        for d in dirs:
            print_files(join(path.d))
        if files:
            for f in files:
                print join(path,f)
print_files(sys.argv[1])
