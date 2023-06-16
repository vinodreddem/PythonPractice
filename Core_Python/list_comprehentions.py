# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:22:01 2019

@author: Sanvi
"""

# List comprehention Examples

#1. Simple List Comprehention
#   Get the Square of Numbers
lst_before = [1,2,3,4,5,6]
lst_square = [x**2 for x in lst_before]
print("vinod example of simple list comprehenion ", lst_square)


#2. If condition List comprehention
# Get Odd numbers from the given list
lst_odd = [elm for elm in lst_before if elm%2 == 1]
print("vinod if condition of list comprehention example ", lst_odd)

#3. If and Else list comprehention 
lst_if_else = [x**2 if x%2 == 0 else x**3 for x in lst_before]
print("vinod if and else condtions of list comprehentions ", lst_if_else)

#4. Nested List list comprehention
l1= [2,4,6]
l2=[1,7,3]
z =[x*y for x in l1 for y in l2 if x>2 & y >2]
print(z)
#in list comprehention each value of l1 (first mentioned value in for ) with second for loop mentioned second

#The above expression is like l2 is inner loop and l1 is outer loop , i.e. we apply value of l1 every time on entire l2
for el1 in l1:
    for el2 in l2:
        print(el1*el2,end=' ')
        


#Program to print minimum number from a list inside the list
x = [[2,3,9,3,5,6],[4,2,7]]
min = x[0][0]
for el in x:
    for val in el:
        if val<min:
            min = val
        
print(min)

# write above program through the list comprehention.
flatten_lst = min([val for sub_lst in x for val in sub_lst])










