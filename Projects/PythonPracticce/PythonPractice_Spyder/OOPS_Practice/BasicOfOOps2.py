# Q. Do we have multiple init methods inside a clsas?
#Ans:  We can define but the last defined one is going to be considered while creating the opbject 
#Previous records are going to be overide.

class Book1():
    def __init__(self):
        pass

    def __init__(self,pages):
        self.pages =pages
        
#here If we use below command we will get error 
b =Book1(20)
"""
b= Book1()
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/BasicOfOOps2.py", line 11, in <module>
    b =Book1()
TypeError: __init__() missing 1 required positional argument: 'pages'

Below code will work for above instance since the last init method does not have any instance atttribute.
class Book1():
    def __init__(self,pages):
        self.pages =pages
    def __init__(self):
        pass

Sollution: In order to pass one argument or Zero Argument we need to have default argument values or *args (WHich accepts n number of inputs)  in method intialization.

Like : 
def__init__(self, pages=100):
    pass

then we can use both instances leke 
b -=Book1()
b2 =Book1(20) at a time.

"""
class Demo2():
    def __init__():
        pass

#d =Demo2() #below error will come
"""
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/BasicOfOOps2.py", line 33, in <module>
    d =Demo2()
TypeError: __init__() takes 0 positional arguments but 1 was given
"""

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()

"""
ob = MyClass() --This will create a new instance object named ob. 
We can access attributes of objects using the object name prefix.

Attributes may be data or method. Method of an object are corresponding functions of that class.
 Any function object that is a class attribute defines a method for objects of that class.

This means to say, since MyClass.func is a function object (attribute of class), ob.func will be a method object.


You may have noticed the self parameter in function definition inside the class but, we called the method simply as ob.func() without any arguments. It still worked.

This is because, whenever an object calls its method, the object itself is passed as the first argument. So, ob.func() translates into MyClass.func(ob).
"""
lst = [3,4,56,3]
max(lst)


"""
Constructors in Python:
__init__() -Thifunction will call whenever the object is created (oject of class is instantiated)
in Python this type of function is called constructor.
"""
class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
#c1.attr

"""
Deleting Attributes and Objects
Any attribute of an object can be deleted anytime, using the del statement. Try the following on the Python shell to see the output.
"""

c3 = ComplexNumber(5,6)
print(c3.getData())

del c3.imag
#print(c3.getData()) #AttributeError: 'ComplexNumber' object has no attribute 'imag'

del c1

print (c1) #NameError: name 'c1' is not defined
"""
Actually, it is more complicated than that. When we do c1 = ComplexNumber(1,3), 
a new instance object is created in memory and the name c1 binds with it.

On the command del c1, this binding is removed and the name c1 is deleted from the corresponding namespace. 
The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.

This automatic destruction of unreferenced objects in Python is also called garbage collection.
"""