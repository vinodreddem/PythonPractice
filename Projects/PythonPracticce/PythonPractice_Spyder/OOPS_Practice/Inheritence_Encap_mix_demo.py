class Polygon():
    __height=None
    __width =None

    pi = 3.14

    def set_values(self,h,w):
        self.__height=h
        self.__width =w 
    def get_width(self):
        return self.__width
    
    def get_height (self):
        return self.__height
        
    def __privateMethod(self):
        pass

    #Inorder to invoke a private Method we need to call this only inside this class.

class Rectangular(Polygon):

    def Area(self):
        print (self.pi)
        #print (self.__height) 
        # We can not fetch the private variables in the derived classes also ,
        # It is only applicable to that class alone
        """
           Traceback (most recent call last):
           File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Inheritence_Encap_mix_demo.py", line 29, in <module>
            r.Area()
            File "c:/PythonPracticce/PythonPractice_Spyder/OOPS_Practice/Inheritence_Encap_mix_demo.py", line 16, in Area
            print (self.__height)
            AttributeError: 'Rectangular' object has no attribute '_Rectangular__height'
       
        """
       #Q . How can we access private variables of parent class in child class?
       #Ans : We need to use getters of the parent method
        return self.get_width() *self.get_height()

class Triangle ( Polygon ):
    def Area (self):
        return self.get_height() *self.get_width() *1/2

t =Triangle()
r = Rectangular()
r.set_values(34,56)
r.Area()


#Multiple Ineheritence - Inpython we can inherit mmore than one class.
# Q.  Are we going to call init() method of parent class from init() method of the child class by default ?
# Ans: No , We need to call explicitly by using super.__init__()

class Parent():
    def __init__(self):
        print (" Inside the Parent Init method")

class Child ():
    def __init__(self):
        print ("Inside the Child Init Method")
        super().__init__()

    # def __new__(self):
    #     print ("Inside the New Method")
    #<class 'NoneType'> --It will give above value.
c =Child() 
print(type(c))


#-----------------------------------------------------------------------------------------------------------------
class Shape ():
    __shape=None

    def set_shape(self,shape):
        self.__shape =shape
    def get_shape(self):
        retrun self.__shape


class Rhombos(Polygon,Shape):
