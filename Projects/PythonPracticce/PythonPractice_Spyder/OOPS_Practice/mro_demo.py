#mro -Method Order Resolotion 

class Parent1():
    def test1 (self):
        print ("Inside the Parent1 method")
        
class Parent2 (Parent1):
    def test2 (self):
        print ("Insid ethe Parent2 Method")
        
class Child1 (Parent1):
    def test1 (self):
        print ("Onside the child1 method")
        
class Child1_1(Parent2):
    def test1(self):
        print ("Inside the child1_1")
        
# class Child2 (Parent1,Parent2):
#     pass

""" 
After inheriting Parent 1 inside the Parent 1
Traceback (most recent call last):
  File "c:\Projects\PythonPracticce\PythonPractice_Spyder\OOPS_Practice\mro_demo.py", line 19, in <module>
    class Child2 (Parent1,Parent2):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases Parent1, Parent2
"""
class Child3 (Child1,Child1_1):
    pass

print (Parent1.__mro__) #(<class '__main__.Parent1'>, <class 'object'>)
print (Child1.__mro__) #(<class '__main__.Child1'>, <class '__main__.Parent1'>, <class 'object'>)
print (Child3.__mro__)
#(<class '__main__.Child3'>, <class '__main__.Child1'>, <class '__main__.Parent1'>,
# <class '__main__.Child1_1'>, <class '__main__.Parent2'>, <class 'object'>)