""" 
When we pass a function as an argument to another function 
and return is assigning again to same function then we use decarators

https://www.geeksforgeeks.org/decorators-in-python/
Decarators : It allows programmers to modify the behaviour of the function or class
It allows us to wrap another function , in order to extend their functionality without modifying it permanently

"""

#Passing the function as an argument
def lower_case (str_inp):
    str_inp = str_inp.lower()
    return str_inp

def upper_case (str_inp):
    str_inp = str_inp.upper()
    return str_inp

def greet (func):
    greeting = func("Hi, I am created by a function passed as an argument")    
    print (greeting)

greet (lower_case)
greet (upper_case)

# Returning Function from another FUnction
def create_adder (x):
    def adder (y):
        return x+y
    return adder

adder_15 = create_adder (15)
print (type(adder_15))
print (adder_15(10))


#Decarator Example
def new_decarator (func):
    def inner (*args,**kwargs):
        x =func(*args,**kwargs)
        x = x +12 #--We can modify the functionality of func_need_decarator her       
        return x
    return inner

@new_decarator       
def func_need_decarator (a,b):
    return a+b
    
print (func_need_decarator(3,5))


""" 
#Decorators - functions that take another function as a parameter and extend its functionality
and behavior without modifying it
def my_decorator(target_function):
 def function_wrapper():
 return "Python is the " + target_function() + " programming language!"
 return function_wrapper
@my_decorator
def target_function():
 return "coolest"

target_function() #returns 'Python is the coolest programming language!'
"""