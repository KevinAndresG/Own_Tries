#!/usr/bin/python3
import functools
f = 3
j = 2
g = 5
c  =  [[ 3],[4]]
x = list(functools.reduce(lambda c, b: c + b, c))
print(x)
