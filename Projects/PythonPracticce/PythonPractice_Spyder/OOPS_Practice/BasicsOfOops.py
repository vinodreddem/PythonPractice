import math
"""
OOPS:
1. In Python OOPS is used for reusable of the code.
2. everything in python is used as Objects to solve the problem.
3. Object has attributes and behaviour(methods).
In Python, the concept of OOP follows some basic principles:

Inheritance	    A process of using details from a new class without modifying existing class.
Encapsulation	Hiding the private details of a class from other objects.
Polymorphism	A concept of using common operation in different ways for different data input. 

Class : Class is a blue print for the object.
We can think class is a sketch of the parrot.
class parrot: ---syntax of the class defination.

INstance ---specific object creation for a particular class.

An object (instance) is an instantiation of a class. 
When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

obj = parrot()
"""

class parrot:
    pass

obj =parrot();
print(type(obj))

"""
Creating Object and Class

Here Student is a class containing one class attribute called college , and two instance attributes 
named Id , Name of the student.
"""

class Student:
    """ This is My First Class Creation"""
    #Class Attribute
    college ="SVCET"
    address ="CHittor"
    #Instance Attributes
    def __init__(self,id,name):
        print("inside init")
        self.id=id
        self.name=name

#As soon as creation of class , we can access the variables of the class.
print(Student.college)
print('Doc is',Student.__doc__)
#print(Student.name) #AttributeError: type object 'Student' has no attribute 'name'
"""
Creation of instance objects 

An object is also called an instance of a class and the process of creating this object is called instantiation.    

Python automatically detects the type of the variable and operations 
that can be performed on it based on the type of the value it contains. 
In programming jargon, this behavior is known as Dynamic Typing.
"""

std1 = Student(101,"Ajay")
std2 =Student(102,"Aravind")
std3=Student("Arun",103) 
#Here we are not defined data types , implicitly taken , So however we are passing in that way it will take

"""
Accessing of Class Attributes.
"""
print("class Attribute is",std1.__class__.college)
print("Class Attribute Address is ",std2.__class__.address)
print(std3.address)

"""
Accessing of the instance attributes
"""
print("the Std1 of id is {} and name is {}".format(std1.id,std1.name))
print("The Std3 of id is {} and name is {} ".format(std3.id,std3.name))

"""
A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.
We have a special attributes those are begins with double under score.
Named __doc__,__class__etc.

The procedure to create an object is similar to a function call.
"""


std4 = Student(105,"Ajith ")

#Add new attributes to the class after intantiation as well in python
std4.classs = "Intermediate"
#here class attributed added only for std4 object not for std3 and others If we try to retrieve that class variable we will get error.
"""print(std2.classs)
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/BasicsOfOops.py", line 94, in <module>
    print(std2.classs)
AttributeError: 'Student' object has no attribute 'classs'
PS C:\PythonPracticce> 

"""
print (std4.classs)