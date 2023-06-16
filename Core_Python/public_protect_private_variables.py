"""
+ 
"""

class public_members():
    school = "XYZ"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

#We can access public variables through instance of the class
print (public_members.school)
pub= public_members('vija',38)
print ('pub Object ', pub.name)
pub.age = 42 #We can modify the data
print ('pub age ',pub.age)

# Protected Variables
class protected_members():
    
    def __init__(self, name , add):
        self._name = name 
        self._add = name 
        
    
prt = protected_members("Hello", "Madanapalli")

print (prt._name)
prt._add = "Chittoor"
print (prt._add)        

# We can able to modify the value even thogh the variable is protected 
#As a programmer we need to aware of this and we should not perform these operatoios 

#method 2 : Using property decarator 

        
class Student():
    def __init__(self, name):
        self._name = name
    
    @property
    def name (self):
        print (" Inside the Get Name")
        return self._name
    
    @name.setter
    def name(self, newName):
        print ('Inside the setterName ')
        self._name = newName
        
        
        
    

    
    
    
    
    
    