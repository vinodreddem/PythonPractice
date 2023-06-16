"""
Python Scope follows LEGB Rule:
    1.  Locals
    2.  Enclosing Function Locals
    3.  Global 
    4.  Built In 

"""     
name = "This is Global Name"

def greet():
    name  = "New Name"
    def hello():
        print ("Hello "+name) #Local Name
    hello()

greet()
print(name)#Global Name

#--------------------------------------
x =100
def func(x):
    print('X inside func',x)
    x =1000
    print('x After changed ',x)

func(x)
print('x outside function',x)

#-----------------------------------------------
def func2(x):
    global x
    x=1000

print('Before calling function',x)
func2()
print('After Calling Function',x)

#Here instead of Global keyword we can return the variable and assign variable to requred variable.
