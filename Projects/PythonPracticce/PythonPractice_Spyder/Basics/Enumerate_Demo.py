import math
"""
A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
Python eases the programmers’ task by providing a built-in function enumerate() for this task.
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

enumerate(iterable, start=0)

Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is 
              to be started, by default it is 0 
              
              
"""

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

set_1 ={2,6,8}
obj3= enumerate(set_1)
print(list(enumerate(set_1)))

lst = [2,4,1,5,3,2]
set_lst = set(lst)

print (set_lst) #Ordered and Unique elements 