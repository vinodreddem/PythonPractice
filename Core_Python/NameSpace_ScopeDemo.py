#------------------------------------------------------------------------------------------
"""
NameSpaces are collection of names, It is a mapping of every name with an object.
    1.Built in Name space -available before we start a program.Ex :id(),print(),type() ...etc
    2.Global Name Space  - Every module can create it's global names ,These are isolated with other modules
    3.Local Name Spaces  - Every module has functions and classes - So these all are having local name spaces

Variable Scope :
    Although there are various namespaces availble ,we may not access all of them ,Since scope of variable concept 
    comes into the picture.
    There are we have below scope of the variable.

"""
#-------------------------------------------------------------------------------------------

def outer_function(a):
    a=10# ------------------------------------------------> Local Scope variable for outer most functon
    def inner_function(a):
        a=20 #--------------------------------------------> Local scope for inner function and it is nested scope
        print("a inside the inner_function",a)
    inner_function(a)
    print("a inside the outer_function",a)
a=30 #----------------------------------------------------> Global Variable
outer_function(a)
print("global the value of a is ",a)


"""
In the above program , If we are in inside the inner function then the varaible a is just a local variable 
We can use the variable , but we can not assign the variable , If we assign a new value to 'a' then it is going to  create a
new variable .
"""

#If we need to refer the variable to global , then we need to use global key word
#Here, all reference and assignment are to the global a due to the use of keyword global.
def outer_function():
    global a
    a=10# ------------------------------------------------> Local Scope variable for outer most functon
    def inner_function():
        global a
        a=20 #--------------------------------------------> Local scope for inner function and it is nested scope
        print("a inside the inner_function",a)
    inner_function()
    print("a inside the outer_function",a)
a=30 #----------------------------------------------------> Global Variable
outer_function()
print("global the value of a is ",a)
