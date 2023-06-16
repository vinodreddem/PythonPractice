
"""
Random Module :
---------------
1.random --module generates the  random numbers from the 
1. seed(2) ---generates same numbers for multiple runs --by using random() method.

2.choice(self, seq Choose a random element from a non-empty sequence.)
     |     
3.randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
4.randrange(self, start, stop=None, step=1, _int=<class 'int'>)
     |      Choose a random item from range(start, stop[, step]).
      
5.sample(self, population, k)
     |      Chooses k unique random elements from a population sequence or set.



Difference Between random.random and numpy.random :

"""
#help(random)
import random
import numpy as np

np.random.seed(100) #it uses to generate same number if we run multiple times also.
x = np.random.rand(2)
print(type(x)) #numpy.ndarray
print(x)

random.seed(2)
y= random.random() #it does not take an argument as input, So it generates only one number i.e. float type

z= random.randrange(5,20,2) #This also generates single number only between given integers
print(z)
print(type(y))
print(y)