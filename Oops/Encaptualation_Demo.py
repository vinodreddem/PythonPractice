"""
Say suppose we have a Car class and we need to replace speed with string variable after instance created
It is possible to overide 
So when we give our data to others --then encapulation plays a big role

Q. How to make attribute Private in you class?

We can use double underscore before an attribute, then it becomes private. So whenever we use double underscore --it makes our dagta private.

"""

class ENcp():

    def __init__(self):
        self.a =10
        self._b=20 # it is partially private variable it's only convention still we can acces the values.
        self.__c =30

e =ENcp() #created an Object

print(dir(e)) #_ENcp__c--->pvt ariable
"""
['_ENcp__c', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', '_b', 'a']['_ENcp__c', '__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_b', 'a']

"""
print("Printinf a",e.a)
print("Printinf b",e._b)
#print("Printinf a",e.__c) # Here we will get an error,since we have used __ 
# before c that means it is a private variable with variable name as c
"""
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Encaptualation_Demo.py", line 22, in <module>
    print("Printinf a",e.__c) # Here we will get an error,since we have used __ before c that means it is a private variable with variable name as c
AttributeError: 'ENcp' object has no attribute '__c'
"""
#print("Variable c is ",e.c)
"""
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Encaptualation_Demo.py", line 30, in <module>
    print("Variable c is ",e.c)
AttributeError: 'ENcp' object has no attribute 'c'
PS C:\PythonPracticce>"""

#So how can we access the private data ?
#Ans:  For  this purpose we need to create setters and getters to take control over data is called Encapulation.

class Car():
    def __init__(self,name,speed):
        self.__name =name #Now name is a private variable.
        self.__speed = speed 
    
    def set_speed(self,value):
        self.__speed =value

    def get_speed (self):
        return self.__speed

    def __privateMethod(self):
        pass
#Same way we can define private methods indide a class
ford = Car('Ford',200)
ford.__name ="MGT"
ford.set_speed(455)

#WE can not inherit private members of super class into a subclass.

print(ford.__name)
print(ford.get_speed())

#Needs to check above problem

class Cat ():
    def __init__(self,legs):
        self.__legs =legs

c =Cat(4)
"""
print(c.__legs)
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Encaptualation_Demo.py", line 72, in <module>
    print(c.__legs)
AttributeError: 'Cat' object has no attribute '__legs'
"""