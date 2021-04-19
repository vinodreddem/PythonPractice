class Parent1 ():
    clas_var = 10
    def __init__(self):
        print ("Inside Parent_one Init Method")

    def add(self , a ,b):
        print ("Inside Parent_one Add Method")
        return a+b

    def mul(self , a ,b,c):
        print ("Inside Parent_one mul Method")
        return a*b*c

    def common(seld):
        print ("Inside Parent_one Common Method")
    
class Parent2 ():
    clas_var = 20
    def __init__(self):
        print ("Inside Parent_two Init Method")

    def add(self , a ,b):
        print ("Inside Parent_one Add Method")
        return a+b

    def mul(self , a ,b):
        print ("Inside Parent_one Add Method")
        return a*b

    def common(self):
        print ("Inside Parent_Two Common Method")
    
class Child(Parent1,Parent2):
    def __init__ (self):
        print ("Inside Child Init Method")

c =Child()
print(Child.__mro__) #Child --Class name we need to give not the Object name 
#Method Resolution Order (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)
#Method resollution order will tell you , which classs method will executed first and which one is next.
sum1= c.add(12,25)

# mul =c.mul(10,20)
"""
Traceback (most recent call last):
  File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Multiple_InheretinceDemo.py", line 43, in <module>
    mul =c.mul(10,20)
TypeError: mul() missing 1 required positional argument: 'c'
"""
mul2 = c.mul(10,20,30)