#User input data
import sys
import os
x= input()
y=input()
z=x+y # by default it is taking as String , So if we need other data type we need mention 
#
print(z)#if x=6,y=55 then z =655 not 61 because it is concatinating instead of addition

a= int(input("ENter the First digit"))
b= int(input("ENter the second digit"))
y =a+b;
print(y)

#iF WE WANT TAKE INPUT FROM THE COMMAND LINE THEN WE HAVE TO USE THE argv (0argument value )
#This is in sys package 

input1 = int(sys.argv[1])
input2=int(sys.argv[2])
