#!/usr/bin/env python
#-*- coding:utf8 -*-

"""
    solving a quadratic equation.
"""

from __future__ import division
import math

def quadratic_equation(a,b,c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return False
    elif delta == 0:
        return -(b / (2 * a))
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return x1,x2

if __name__ = "__main__":
    print "a quadratic equation:x^2 +2x +1 =0"
    coeficients = (1,2,1)
    roots = quadratic_equation(*coeficients)
    if roots:
        print "the reuslt is:",roots
    else:
        print "this equiation has no solution."
