#!/usr/bin/python

def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    print sum
    return sum

print factorial(100)
