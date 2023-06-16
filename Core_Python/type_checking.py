
# """
# pip install mypy

#     and run this with mypy type_checking.py
    
#     Similarly to check violation or standards of code (Like PMD reports in QPP)
    
#     pip install flake8 --- to beatyfy your code in python
#     flake8 example.py
# """
# def add_this (a ,b) ->int :
#     return a + b

# print (add_this('Hello','World'))
def add_two (a: int, b: int) -> int:
    return a+b

print (add_two ('Hello' ,'world'))

"""
 mypy type_checking.py
 
type_checking.py:19: error: Argument 1 to "add_two" has incompatible type "str"; expected "int"
type_checking.py:19: error: Argument 2 to "add_two" has incompatible type "str"; expected "int"
Found 2 errors in 1 file (checked 1 source file)
"""