import math
"""
If Condition in python
Decision making is required when we want to execute a code only if a certain condition is satisfied.
The if…elif…else statement is used in Python for decision making.
"""

if True:
    print("Inside If")

# If -Else Condition.
x = int(input("Enter the Number"))
r = x % 2
if (r == 0):
    print("Inside inside If -it is even ")
else:
    print("Inside Else")

# If -elif -else Statements
inp = int(input("Enter your values "))
if (inp == 1):
    print("inside if inp is 1")
elif (inp == 2):
    print("inside if inp is 2")
elif inp == 3:
    print("inside if inp is 3")
else:
    print("other values")
"""
While Loop :
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

"""
x = 3
while x <= 7:
    print("the values of x is ", x)
    x = x + 1



"""
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
Iterating over a sequence is called traversal.
for val in sequence:
	Body of for
	
Loop continues until we reach the last item in the sequence. 
The body of for loop is separated from the rest of the code using indentation.
	# for loops is used for the iterate the values in a list like sequences
"""

y = [14, 65.66, 'vinod']
for i in y:
    print("insidde for", i)

list_1=[1,2,5,3,6,88,9,4,]
sum =0
print(id(sum))
for num in list_1 :
    sum = sum+num
    print(id(sum)) #Every time it creates a new object , which allocates a new memory
print(id(sum))#It refers to the latest memory location , not the intial one
print(sum)

# WE can iterate through the string by using the for loop
str = "ITERATOR"
for j in str:
    print(j, end="       ")  # end is used to keep the prints in the same line,by default end is a new line.

"""
In Python, break and continue statements can alter the flow of a normal loop
Loops iterate over a block of code until test expression is false, but sometimes we wish to
 terminate the current iteration or even the whole loop without checking test expression.

The break and continue statements are used in these cases.



"""
#Continue and Break the Statements
x = 1
while x <= 11:
    x = x + 1
    if x==5:
        continue
    if x==9:
        break
    if x==8:
        pass #If we don't know the logic here we can keep the pass command
    print("the values of x is ", x)

"""
Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. 
They cannot have an empty body.
The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.
The interpreter would complain. So, we use the pass statement to construct a body that does nothing.
We generally use it as a placeholder."""
def funq():
    pass

"""
Range Funtion :
It will generate a sequence of numbers 
We have a start,stop and step size in the range functions.
range is used in for loops to iterate through the sequence of the numbers.
the len() used to iterate through indexing.
"""
range (10)
print(range(10)) #output is :range(0, 10)
print(list(range (10))) #output is :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range (2,6)))#output is :[2, 3, 4, 5]
print(list(range (2,16,3)))#output is :[2, 5, 8, 11, 14]
for r in range (10) :
    if(r%2==0) :
        print("Even Number" ,r)
    else :
        print("The number {} is odd ".format(r))

"""
For with Optional Else :
    1.A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
    2.break statement can be used to stop a for loop. In such case, the else part is ignored.
    3.Hence, a for loop's else part runs if no break occurs.
    4.But inncase of continue , we will execute the optional else part.
"""

list_ex2 = [3,6,7,7,5]
for l in list_ex2 :
    print("the value in list is ",l)
else:
    print("The all elemnts are iterated ")


"""
IF , IF -ELSE . IF -ELIF -ELSE  Statements :
Decision making statements 
"""

num =2
if (num %2==0):
    print("even number")
elif (num ==2):
    print("Even prime number")
else :
    print("odd number")

"""
FOR Loop:
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
Iterating over a sequence is called traversal.

for val in sequence:
	Body of for
"""

