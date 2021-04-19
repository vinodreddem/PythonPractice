int_a =7
"""
Numbers in Python :
int, float, complex

type() function to know the type of the variable.
isinstance() function to know the /check the variable is belongs to particular class or not.

"""

a = 5

# Output: <class 'int'>
print(type(a))

# Output: <class 'float'>
print(type(5.0))

# Output: (8+3j)
c = 5 + 3j
print(c + 3)

# Output: True
print(isinstance(c, complex))

"""
Type COnversion :

We can convert one type of number into another. This is also known as coercion.
built in functions to convert a string  :
int() ,float() , complex() --these funtions converts from string as well.

"""
print(int(5.8))
print(float(567))
print(complex('6+5j'))
"""
We might ask, why not implement
Decimal every time, instead of float? The main reason is efficiency. 
Floating point operations are carried out must faster than Decimal operations.
"""

import decimal as D
print(1.1+2.2)  #3.3000000000000003
print(D.Decimal(1.1) +D.Decimal(2.2)) #3.300000000000000266453525910

#If we use string then , we will get that.
print(D.Decimal('1.1')+D.Decimal('2.2'))



"""
Python Fractions:
----------------
Python provides operations involving fractional numbers through its fractions module.
A fraction has a numerator and a denominator, both of which are integers. This module has support for rational number arithmetic.
While creating Fraction from float, we might get some unusual results.
This is due to the imperfect binary floating point number representation as discussed in the previous section.
"""
import fractions
print(fractions.Fraction(1.5)) #converts decimal into fractions
print(fractions.Decimal(17/2)) #converts fraction into decimal
print(fractions.Fraction(6,5)) #6 --Nr , 5 --Dr.
print(fractions.Fraction(1.1)) #2476979795053773/2251799813685248  -Unusual result -creating from float only
#if we use string then we will get normal
print(fractions.Fraction('1.1'))

