#!/usr/bin/python
#-*- coding:utf8 -*-

with open('/etc/hosts') as f:
    while True:
        data = f.readline()
        if not data:
            break
        print data,
