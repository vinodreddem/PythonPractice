import math
"""
Define the class Point that represents x, y, and z coordinates of 3D coordinate system.

Hint : Define the initializer method, __init__ that takes three values and assigns them to attributes x, y and z respectively.
Now create an object p1 = Point(4, 2, 9) and print it using the statement print(p1).

"""

class point():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return 'Point is ( x ='+str(self.x)+', y='+str(self.y)+',z='+str(self.z)+')'

    # in Str we have only string data type , here x,y,z is of int type so we need to convert them into str , before appending to it.
    def __repr__(self):
        return {'x': self.x, 'y': self.y ,"z":self.z}

    def distance(self,point1):
        distance  = math.sqrt(((self.x -point1.x) ** 2 )+ ((self.y-point1.y)**2) +((self.z-point1.z)**2) )
        return distance
    # Here we are going to update self values as well further flow
    # def __add__(self, other):
    #     self.x += other.x
    #     self.y += other.y
    #     self.z += other.z
    #     return self

    #here we are not going to update self values in the caling 
    def __add__(self, other):
        p4 =point(0,0,0)
        p4.x = self.x+ other.x
        p4.y = self.y+other.y
        p4.z = self.z+other.z
        return p4


p1=point(4,5,6)
print(p1)   # <__main__.point object at 0x010DAEB0> -It would n't give the values , to give this values we need toString() method like java ,
#here toString() is off __str__()

# After __str__() method the output is ,Point is ( x =4, y=5,z=6)

print(p1.__repr__()) #__repr__ method returns an expresiion instead of string , mostly uses as dictionary.

"""
Difference between __str__ and __repr__ functions
__str__ must return string object whereas __repr__ can return any python expression.
If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.
"""
print(type(p1.__repr__()))

# Distance calculation :
p2 = point(-2,-1,4)

p3 =point(4,5,6)

add =p2.__add__(p3)
print(add)

print(p2)
dist =p2.distance(p3)
print(dist)