#!/usr/bin/env python
#-*- coding:utf8 -*-

import random

number = random.randint(1,101)

guess = 0

while True:

    num_input = raw_input("Please input one integer that is in 1 to 100:")
    guess += 1

    if not num_input.isdigit():
        print "Please input interge."
    elif int(num_input) < 0 or int(num_input) >= 100:
        print "The number should be in 1 to 100."
    else:
        if number == int(num_input):
            print "OK,you are good.It is only %d,then you success." % guess
            break
        elif number > int(num_input):
            print "your number is more less."
        elif number < int(num_input):
            print "your number is bigger."
        else:
            print "There is something bad,I will not work."
