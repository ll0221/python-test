#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = '120.25.192.149'
#host = socket.gethostname()
port = 1989
s.bind((host,port))

s.listen(5)
while True:
	c, addr = s.accept()
	print '连接地址：', addr
	c.send('Socket 测试！')
	c.close()
