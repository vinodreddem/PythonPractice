
"""
Inheritence:

It refers to defining a new class with little or no modification to an existing class. 
The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
IS _A relationship (Dog (DerivedClass) is a Animal(Parent class))

class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class

  Inheritance models what is called an is a relationship. This means that when you have a Derived 
  class that inherits from a Base class, you created a relationship where Derived is a specialized version of Base.



"""
class Animal:
    category = "Mammal"
    def __init__(self):
        print("vinod inside the Animal __init__()")
        self.numberoflegs = 4
        self.tail = True

    def getnumberofLegs(self):
        print("\n vinod insid the number of legs method")
        return self.numberoflegs

    def whoAmI(self):
        print("Animal")

class Dog(Animal):
    def __init__(self,legs):
        print("vinod inside the dog  __init__() method")
        self.numberoflegs =legs
        self.sound ='Bark'

    def __str__(self):
        return "This is Animal Object"
    #Needs to check how we use python __str__ method.

dog = Dog(6)
print(dog)
print(dog.__str__()) #How this
print(dog.getnumberofLegs()) #This will call parent method and send child instance and return legs of created object

animal =Animal()
print(animal)
print(animal.getnumberofLegs())

""" #is it possible to have a child class object with parent class instance like in java?? """

##sPECIAL Methods --
class Book():
    def __new__(self):


    def __init__(self,title,author,pages):
        self.title =title
        self.author = author
        self.pages =pages

    def __str__(self):
        return "Title Of Book {} , Author {},Pages {}".format(self.title,self.author,self.pages)
    """
    __new__() method
    Languages such as Java and C# use the new operator to create a new instance of a class. 
    In Python the __new__() magic method is implicitly called before the __init__() method. 
    The __new__() method returns a new object, which is then initialized by __init__().

    """
    def __class__(self):

b =Book("The Last Ship","James","1506")

print(b) #<__main__.Book object at 0x0000018D687B8438>
#In order to print like title , author and pages (toString) formati in java , we can use special methods.
#Title Of Book The Last Ship , Author James,Pages 1506 -After __str__ function



