#!/usr/bin/python

macaddr = '00:16:3e:02:56:79'
prefix_mac = macaddr[:-3]
last_two = macaddr[-2:]
plus_one = int(last_two,16) + 1
if plus_one in range(10):
    new_last_two = hex(plus_one)[2:]
    new_last_two = '0' + new_last_two
new_mac = prefix_mac + ':' + new_last_two
print new_mac.upper()
