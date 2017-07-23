#!/usr/bin/env python
#-*- coding:utf8 -*-
myinfo={"name":"leo","site":"opsvr.cn","lang":"python"}
infor={}
for k,v in myinfo.items():
    #print k,v
    #print "*" * 30
    infor[v]=k
    print infor
