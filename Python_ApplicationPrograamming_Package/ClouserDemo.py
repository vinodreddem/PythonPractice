#Clouser is a function , which is returned from the higher order function

def multiply_of(x) :
    def multipleby(y):
        return x*y;
    return  multipleby;


c1= multiply_of(5) # this is going to return function as multiple , which is storing the value of x , i.e
#hold the data passed to enclosing function, multiple_of, during their creation.

print(type(c1))
print(c1)

print(c1(6))


