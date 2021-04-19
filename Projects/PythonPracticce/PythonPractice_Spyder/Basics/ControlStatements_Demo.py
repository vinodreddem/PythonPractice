#If Condition in python
import math
if True:
    print("Inside If")

# If -Else Condition.
x = int(input("Enter the Number"))
r = x % 2
if(r == 0):
    print("Inside inside If -it is even ")
else:
    print("Inside Else")

    
#If -elif -else Statements
inp = int(input("Enter your values "))
if(inp ==1):
    print("inside if inp is 1")
elif(inp == 2):
    print("inside if inp is 2")
elif(inp == 3):
    print("inside if inp is 3")
else:
    print("other values")

#whle loops , is used to print the values for iteratios with conditions 
x = 3
while(x <= 7):
    print("the values of x is ", x)
    x = x + 1
#for loops is used for the iterate the values in a list like sequences
y = [14, 65.66, 'vinod']

for i in y:
    print("insidde for", i)

#WE can iterate through the string by using the for loop
str = "ITERATOR"
for j in str:
    print(j, end="     ")   # end is used to keep the prints in the same line
