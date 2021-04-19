# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:22:01 2019

@author: Sanvi
"""

import math
print(math.pi)
print(round(math.pi))
[str(round(math.pi)) for i in range(6)]

#Round is used to round the float value to previous integer

#Program to print minimum number from a list inside the list
x = [[2,3,9,3,5,6],[4,2,7]]
min = x[0][0]
for el in x:
    for val in el:
        if val<min:
            min = val
        
print(min)

#deep copy , if we do any changes in parent list will not reflected in child.
#copy or assignment will change the value later on also.
import copy
parent_list  = [4,6,8,[78,76]]
child_list =  copy.deepcopy(parent_list)
child_list2 =copy.copy(parent_list)
child_list3 =parent_list
print(type(parent_list[3][0]))
parent_list[3][0] =0
print(parent_list)
print(child_list)
print(child_list2)
print(child_list3)

l1= [2,4,6]
l2=[1,7,3]
z =[x*y for x in l1 for y in l2 if x>2 & y >2]
print(z)

#in list comprehention each value of l1 (first mentioned value in for ) with second for loop mentioned second

#The above expression is like l2 is inner loop and l1 is outer loop , i.e. we apply value of l1 every time on entire l2
for el1 in l1:
    for el2 in l2:
        print(el1*el2,end=' ')


