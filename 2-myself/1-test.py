#!/usr/bin/env python
#-*- coding:utf8 -*-

import random

i = 0
while i < 4:
    print '*' * 30
    num = input('请输入0到9任一个数：')

    xnum = random.randint(0,9)

    x = 3 - i

    if num == xnum:
        print '运气真好，您猜对了！'
        break
    elif num > xnum:
        print '''您猜大了！\n正确答案是:%s\n,您还有%s次机会！''' %(xnum,x)
    elif num < xnum:
        print '''您猜小了！\n正确答案是:%s\n,您还有%s次机会！''' %(xnum,x)
    print '*' * 30
    i += 1
