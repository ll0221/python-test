#!/bin/sh

echo "#!/usr/bin/env python" > $1.py 
echo "#-*- coding:utf8 -*-" >> $1.py 
chmod +x $1.py
