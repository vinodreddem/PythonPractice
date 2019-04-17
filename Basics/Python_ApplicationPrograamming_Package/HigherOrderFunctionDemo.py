#Function as an Argument
def add (x,y) :
    return x+y
def sub(x,y) :
    return x-y
def mul(x,y) :
    return x*y

def do(fun,x ,y) :
    return fun(x,y)

print(do(add, 12, 4))  # 'add' as arg

print(do(sub, 12, 4))  # 'sub' as arg

print(do(mul, 12, 4))  # 'prod' as arg

#here we are not sending the arg in the quotes as a string


#2 .Function as a Data

def greet():
    return "Welcome hero!!!"

wish =greet #Assignning the function to a variable
print(type(wish))

print(wish())

#3. Returning the function
def outer ():
    def inner():
        return "i am in inner function"

    return inner()

print(outer())


def outer1():
    def inner1():
        return "I am in inner2 function"

    return inner1 #removing of the parenthesis

var =outer1()
print(type(var))
print(outer1())

#to call teh inner function we need to call like below'
print(var())