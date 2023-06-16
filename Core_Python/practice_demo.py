class Computer:
    def __init__(self,name ,age):
        self.name =name
        self.age=age

c1 = Computer('lenoa',25)
c2 =Computer('lenoa',25)
print ("Id of c1",id(c1))
print ("Id of c1c2",id(c2))
if c1==c2 :
    print('Two onjects same')
else:
    print('Two objects not same ')