import math

"""
Set :

1.Unordered (No concept of index)
2.Mutable
3.represented by {} 
4.We cannot access or change an element of set using indexing or slicing.et does not support
5.Unique elements -no repeation of elements

Method	Description
add()	Adds an element to the set
clear()	Removes all elements from the set
copy()	Returns a copy of the set
difference()	Returns the difference of two or more sets as a new set
difference_update()	Removes all elements of another set from this set
discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
pop()	Removes and returns an arbitary set element. Raise KeyError if the set is empty
remove()	Removes an element from the set. If the element is not a member, raise a KeyError
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()	Returns the union of sets in a new set
update()	Updates the set with the union of itself and others
"""

set_1 = {1,3.5,"vinod",1,6}
print(set_1)

"""
Set can not have a mutable list inside this.
"""
# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #23,
# this will cause an error.
# TypeError: unhashable type: 'list'

#my_set = {1, 2, [3, 4]}

"""
Set : creating an empty set is somewhat difficult here.
empty {} braces creates empty dicitionary here , not the set .
set() -method is used to create the empty set.
"""
a={}
b=set()
print(type(a)) #<class 'dict'>
print(type(b)) #<class 'set'>


"""
Sets Methods :
1.Change of Sets : add() -method to add an element to the list.
2.update() -to add mutltiple elements -like adding of other data types like lists ,tuples to the set.

"""
print(len(set_1)) #do not cosinder the repeation of elements
set_2 = {1,3,4,5}
print(set_2)
set_2.add(7)
print(set_2)

list =[3,66,75]
set_2.update(list)
print(set_2)

#set_2.remove(55) --KeyError: 55


"""
Python Set Operations :
1.Union : It is like a mathematical operation union.
    done by | symbol or union() method

2.Intersection :It is like a intersection operation in maths
    done by & symbol or intersection() method.
    
3.Set Difference : A-B is not equal to B-A here.
    deone by - symbol or difference method.
    
4.Set Symmetric Difference -Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
    done by ^ symbol or symmetric_difference
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("The Union of A ,B is ...",A|B) #{1, 2, 3, 4, 5, 6, 7, 8}
print("The Union of A ,B is ...",A.union(B))
print("The Union of A ,B is ...",B.union(A))

print("The intersection of A ,B is ...",A&B) #{1, 2, 3, 4, 5, 6, 7, 8}
print("The intersection of A ,B is ...",A.intersection(B))
print("The intersection of A ,B is ...",B.intersection(A))

print ("The A-B is ",A-B) # {1, 2, 3}
print ("The B-A is ",B-A) # {8, 6, 7}
print((A-B)==(B-A)) #False

print("The A difference B is " ,A.difference(B))
print("The B difference A is " ,B.difference(A))

print ("The A^B is ",A^B)  #it is like union of (A-B) and (B-A)
print ("The B^A is ",B^A)

print("The A difference B is " ,A.symmetric_difference(B))
print("The B difference A is " ,B.symmetric_difference(A))


"""
Enumerate :

"""
enumerate_set = enumerate(set_1)
print("The Enumerate is ",enumerate_set)
for count,ele in enumerate_set :
    print(count,ele)


"""
Frozenset is a new class that has the characteristics of a set, 
but its elements cannot be changed once assigned.
While tuples are immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as dictionary keys. 
On the other hand, frozensets are hashable and can be used as keys to a dictionary.

When you use dictionary as an iterable for a frozen set. It only takes key of the dictionary to create the set.
"""

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)