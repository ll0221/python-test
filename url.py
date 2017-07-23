#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
status=urllib.urlopen("http://www.opsvr.cn").code
print status
