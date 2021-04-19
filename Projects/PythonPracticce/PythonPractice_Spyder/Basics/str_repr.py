""" 
Both are the DUnder methods of a class
__str__ : This method is generally is used for an Easy to Read and Human Consumption
Called when we use print function to print an Object.

__repr__: Used to print an Object directly on shell
"""

class Car():
    def __init__(self,color,milage):
        self.color = color
        self.milage = milage
    
#With out __str__ and __repr__ functions
myCar = Car ('Red',150)
print (myCar) #<__main__.Car object at 0x00000216B2D5DFD0>
myCar # Same result will come when we use Python Shell for myCar --<__main__.Car object at 0x00000216B2D5DFD0>Check in Python IDLE

class Car1():
    def __init__(self,color,milage):
        self.color = color
        self.milage = milage
        
    def __str__ (self):
        return "Inside the __str__ methof"
    
    def __repr__ (seld):
        return " Inside the __repr__ method"
    

mycar1 = Car1 ('Green',134)
print (mycar1) #Inside the __str__ methof
'{}'.format(mycar1) #Inside the __str__ methof
str(mycar1) #Inside the __str__ methof
mycar1 #Inside the __repr__ method
    
    

class Car2():
    def __init__(self,color,milage):
        self.color = color
        self.milage = milage
    
    def __repr__ (self):
        return '{self.__class__.__name__} ({self.color}),({self.milage})'.format (self = self)

myCar2 = Car2 ('Yello',167)
print (myCar2) # Car2 (Yello),(167) , __str__ internally calls __repr__ method.
myCar2 #Car2 (Yello),(167)
    