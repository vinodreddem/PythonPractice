"""
we have defined two product method, but we can only use the second product method, 
as python does not support method overloading. We may define many methods of the same name and different arguments,
 but we can only use the latest defined method. Calling the other method will produce an error. Like here calling product(4, 5)    
will produce an error as the latest defined product method takes three arguments.

"""
class Product():
    def product (self,a,b):
        return a*b
    def product (self,a,b,c):
        return a*b*c

p =Product()
#p.product (3,4)
"""
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Method_Overloadinig_MathOperators.py", line 15, in <module>
    p.product (3,4)
TypeError: product() missing 1 required positional argument: 'c'
"""

#------------------------------------------------------------------------------------------
#Python Operator Overloading
#Operator   	    Expression      	Internally
#---------      ----------------    -----------------
# Addition	        p1 + p2	        p1.__add__(p2)
# Subtraction	    p1 - p2	        p1.__sub__(p2)
# Multiplication	p1 * p2	        p1.__mul__(p2)
# Power	            p1 ** p2    	p1.__pow__(p2)
# Division      	p1 / p2	        p1.__truediv__(p2)
# Floor Division	p1 // p2	    p1.__floordiv__(p2)
# Remainder (modulo)	p1 % p2 	p1.__mod__(p2)
# Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
# Bitwise AND	        p1 & p2	    p1.__and__(p2)
# Bitwise OR	        p1 | p2	    p1.__or__(p2)
# Bitwise XOR	        p1 ^ p2	    p1.__xor__(p2)
# Bitwise NOT	        ~p1	        p1.__invert__()
# Overloading Comparison Operators
# # Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.
# Less than	             p1 < p2	p1.__lt__(p2)
# Less than or equal to	 p1 <= p2	p1.__le__(p2)
# Equal to	             p1 == p2	p1.__eq__(p2)
# Not equal to           p1 != p2	p1.__ne__(p2)
# Greater than	        p1 > p2	    p1.__gt__(p2)
# Greater than      	p1 >= p2	p1.__ge__(p2)
# equal to
#---------------------------------------------------------------------------------------
import math
class Circle():
    
    def __init__(self,radious):
        self.__radious=radious

    def ger_radious (self):
        return self.__radious

    def set_radious (self,re):
        self.__radious = re
    
    def area (self):
        return math.pi*self.__radious**2

    def __add__(self, Other_object):
        return Circle(self.__radious + Other_object.__radious)
    
c1 = Circle(21)
c2 = Circle(22)
# c1.set_radious(22)
# c2.set_radious(12)

c3 =c1+c2
"""
PS C:\PythonPracticce> & C:/Users/Sanvi/Anaconda3/python.exe c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Method_Overloadinig_MathOperators.py
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Method_Overloadinig_MathOperators.py", line 42, in <module>
    c3 =c1+c2
TypeError: unsupported operand type(s) for +: 'Circle' and 'Circle'
PS C:\PythonPracticce> 

Before Implementing the __add__ method inside the class.
"""
print (c3)
#<__main__.Circle object at 0x00000245D8A78358> --It creats a Circle Object whose radious is sum of both radious
print (c3.ger_radious()) #43
#return Circle(self.__radious + Other_object.__radious) --If we remove Circle then we will return only radious