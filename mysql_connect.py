#!/usr/local/bin/python

import mysql.connector

conn = mysql.connector.connect(host='114.115.213.217',user='leo',password='1a2s3dqwe',database='mytest',use_unicode=True)
cursor = conn.curson()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id,name) values (%s,%s)',['1','Michael'])
cursor.rowcount
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values
cursor.close()
conn.close()
