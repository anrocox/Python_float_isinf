#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to determine if a float is infinite in Python?

¿Cómo determinar si un float es Infinito en Python?
'''
#
#review IEEE 754 Floating Point Special Values in
#http://legacy.python.org/dev/peps/pep-0754/
#
import math

#create a positive infinity
f = float('inf')
print(f)

#the isinf() method verify if 'f' is a positive or negative infinity.
#Return True or False.
print(math.isinf(f))

#create a positive infinity
f = 1e309
print(f)

#return True because 'f' is positive infinity
print(math.isinf(f))

#create a negative infinity
f = -1e309
print(f)

#return True because 'f' is negative infinity
print(math.isinf(f))

#create a float number
f = 1.23
print(f)

#return True because 'f' isn't infinity value
print(math.isinf(f))
