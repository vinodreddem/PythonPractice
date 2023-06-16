"""
Tuple -Immutable
List  -Mutable

"""
tup1 = ()
tup2 = 15,25,36,44

print(type(tup1))
print(type(tup2))
#tup2 [3]= 15 # TypeError: 'tuple' object does not support item assignment

lst = [3,5,(4,5,6)]
lst[2][1] = 4
print (lst)
""" 
Traceback (most recent call last):
  File "c:\Projects\PythonPracticce\PythonPractice_Spyder\Basics\TupleDemo.py", line 15, in <module>
    lst[2][1] = 4
TypeError: 'tuple' object does not support item assignment
(Django_Level3) PS C:\Projects\PythonPracticce\PythonPractice_Spyder> 
"""