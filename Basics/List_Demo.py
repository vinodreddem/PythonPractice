import math
"""

Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

"""


"""
List Comprehension: Elegant way to create new List
List comprehension is an elegant and concise way to create new list from an existing list in Python.

List comprehension consists of an expression followed by for statement inside square brackets.

"""
mylist =[2,8,7,56]
mul = [10 * x for x in mylist]
print(mul)
pow2 = [2 **x for x in range (10) if x%2==0] # Wecan have an if condition as well
print(pow2)

for m in mylist :
    print(m)