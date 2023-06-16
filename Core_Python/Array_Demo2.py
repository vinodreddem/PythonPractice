from array import *
"""
1.This module explains taking user input and built an array from user elements
2.Search an user inpt in the array
"""


x = int(input(' Tell me How many numbers need in Array'))

arr = array('i',[])

for i in range(x):
    y = int (input('Please enter you number '))
    arr.append(y)

print (arr)

"""
Search an element in the array nd print an index
"""

search = int(input ("Please enter the value to search "))

for i in range(len(arr)):
    if arr[i]== search:
        print("the values is prenet in the loop and index is ",i)
        break
else :
    print("the value is not in the array")

#second method
print("the value of index is " ,arr.index(search))

"""
Traceback (most recent call last):
  File "C:/Users/Sanvi/PycharmProjects/PracticePython/Basics/Array_Demo2.py", line 25, in <module>
    print("the value of index is " ,arr.index(search))
ValueError: array.index(x): x not in array

Throw an error if it is not present in the array
"""