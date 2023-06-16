a= 6
"""
What is Function ? :
Function is a group of related statements that perform a specific task.
Functions help break our program into smaller and modular chunks. 
As our program grows larger and larger, functions make it more organized and manageable.
def function_name(parameters):
	....docstring.....
	statement(s)

def ---Start of the function 
fn name ---uniquely identifies it
Parameters (arguments) through which we pass values to a function. They are optional.
A colon (:) to mark the end of function header.
Optional documentation string (docstring) to describe what the function does.
One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
An optional return statement to return a value from the function.
"""

def print_Name(name):
    """This prints the name of the fn """
    print("Good Mroning ",name )
name ="aay"
print_Name("Ajay")
print(print_Name.__doc__)
print(print_Name.__getattribute__(name))