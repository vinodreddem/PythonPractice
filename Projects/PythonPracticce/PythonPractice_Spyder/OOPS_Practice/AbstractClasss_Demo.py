from abc import ABC ,abstractmethod

"""
abc --Anstract Base classes
Abstract Class: A class contains a abstract methods without implementation.
Implementation is done on derived classes.
Abstract class is created by deriving a class from abc Module (ABC -Abstract Bse Classs)

"""
class A(ABC):
    @abstractmethod
    def m1(self):
        print("inside the Abstract class")

# a=A()
# a.m1()

"""
Traceback (most recent call last):
  File "C:/Users/Sanvi/PycharmProjects/PracticePython/Basics/OOPS_Practice/AbstractClasss_Demo.py", line 14, in <module>
    a=A()
TypeError: Can't instantiate abstract class A with abstract methods m1
"""

class B(A):
    def m1(self):
        print("Inside class B ,method m1")

class C(B):
    def m2(self):
        print("Inside class C , mehod m2")

c =C()
c.m1()
c.m2()
#-------------------------------------------------------------------------------------------------------
# class Shape():
#     def area (self):pass
#     def perimeter(self):pass

# class Square(Shape):
#     def __init__(self,side):
#         self.__side =side
# We have a built in module called Abstract that will used to create abstract classes.

# Q. Here Shape class is just an template , So we don't want to create an instance for that How can we achieve that?
# Ans: After making class as abstract by using ABC and abstractmethods.

# Q. Here area()& perimeter() methods are abstract methods and we make sure to implement them in the inheritence class.
# How can we achieve that?
# Ans: We have a built in module named 'abc' from this we need to import ABC and abstractmethod
# and we need to extend the shape class from ABC class --so that we can make shape class as abstract class
# and we can use @abstractmethod annotation before metho to make method as abstract method.

class Shape(ABC):
    @abstractmethod
    def area (self):pass

    @abstractmethod
    def perimeter(self):pass

class Square(Shape):
    def __init__(self,side):
        self.__side =side

    def area(self):pass
    def perimeter(self):pass


"""
sqr = Square() -----Without implementing the abstract methods inside the class,we will get below error.

Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/AbstractClasss_Demo.py", line 67, in <module>
    sqr = Square()
TypeError: Can't instantiate abstract class Square with abstract methods area, perimeter
"""
"""

s =Shape()

Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/AbstractClasss_Demo.py", line 76, in <module>
    s =Shape()
TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
"""
# #Example 3:

# class A2(ABC):
#     @classmethod
#     @abstractmethod
#     def m1(self):
#         print("Inside class A2 ,method m1")

# class B2(A2):
#     @staticmethod
#     def m1(self):
#         print("Inside class B2, method m1")
# b2 =B2()
# B2.m1(b2)

# # b2.m1()
# # B2.m1()
# # A2.m1()