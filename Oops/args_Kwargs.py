
def foo (required, *args, **Kwargs):
    print (required)
    if args:
        print (args) #(1, 2, 4)
        print(type (args)) #<class 'tuple'>
    if Kwargs:
        print  (Kwargs) # {'key1': 'hey', 'key2': 'how are you'}
        print (type(Kwargs)) #<class 'dict'>

"""
required : This mandatory inputs while calling the function
args : This is positional arguments (We can have 0 or more elements , those will represents in args) (Not Mandatory)  --Type is Tuple all elements present in tuple 
        Single Star we have used for Args 
kwargs: Kyword arguments (Not Mandatory) -- These varaibles we can represent with name and value while calling method
        Type is Dictionary
        Double ** used for kwargs
"""

foo ('hello',1,2,4,key1 ='hey',key2= 'how are you')


class Car():
    def __init__(self,color, milegae):
        self.color = color 
        self.milage = milegae
        print ('color is ',color)
        print ('milage is ',milegae)


class AlwaysBlueCar (Car):
    def __init__ (self, *args,**kwargs):
        super().__init__(*args,*kwargs)
        self.color = 'Blue'

