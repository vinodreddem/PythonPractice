class Computer:
    def __init__(self,name ,age):
        self.name =name
        self.age=age

    def comapare(self,other):
        if self.age ==other.age :
            return True

c1 = Computer('lenoa',25)
c2 =Computer('lenoa',25)

if c1==c2 :
    print('Two onjects same')

else:
    print('Two objects not same ')


"""
So to compare the two objects based on one attribute or two attributes
here compare is not an inbuilt function , So we need to manually defined in the class

Cmpare() method will take two objects as an input ,one is self i.e c1 and another object i.e. c2
"""
x =c1.comapare(c2)
print('x is ',x)
if c1.comapare(c2):
    print('Two onjects same')
else:
    print('Two objects not same ')



class Apple :

    def __init__(self,name,place):
        self.name =name ;
        self.place =place
# c= Apple() #TypeError: __init__() missing 2 required positional arguments: 'name' and 'pla