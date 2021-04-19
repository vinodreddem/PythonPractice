
"""
Inheritence:

It refers to defining a new class with little or no modification to an existing class. 
The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class

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

    def __init__(self,title,author,pages):
        self.title =title
        self.author = author
        self.pages =pages

    def __str__(self):
        return "Title Of Book {} , Author {},Pages {}".format(self.title,self.author,self.pages)
    
b =Book("The Last Ship","James","1506")

print(b) #<__main__.Book object at 0x0000018D687B8438>
#In order to print like title , author and pages (toString) formati in java , we can use special methods.


