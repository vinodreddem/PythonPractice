# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 02:40:52 2019

@author: Sanvi
"""

"""1. Tilde Opderator  - ~
        It performs 2's compliment operation
        2's compliment is used to store  negitive numbers
        generally negitive numbers can store directly in the computer , we will store them in the form of 
        2's complement 
    
    Bitwise and (&) ,Bitwise (|) ,bitwise xor (^),rightshift , left shif(<<) operators
    
"""

x = ~12
print(x)

z =~14
print(z)

a =12
b=13

print(a&b)
print(a|b)
print(a<<2)
print(b<<2)


"""
Mathematic Functions"""

print(sqrt(25))
 
"""
Traceback (most recent call last):


  File "<ipython-input-16-edbbb0b36cd5>", line 1, in <module>
    print(sqrt(25))

NameError: name 'sqrt' is not defined

We need to import maths function
"""
import math

print(math.sqrt(25))






















