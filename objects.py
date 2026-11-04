'''
OBJECTS
 What is object
 Iterable objects & RANGE
 DICTIONARY
 Error handling system
'''


import array  # package/module
import math  # package
from math import ceil
print(" ==== What is object ==== ")
# An object has state and method properties.
# Everything is object in Python!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & 00P
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritence
result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)
