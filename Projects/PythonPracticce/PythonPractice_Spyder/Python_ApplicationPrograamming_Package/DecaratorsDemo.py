
def outer (func) :
    def inner () :
        print("Accessign ", func.__name__)
        return func()
    return inner


def greet():
    return "Hello I am Vinod"

wish =outer(greet) #outer function return inner function

print(wish)
print(type(wish))
#
print(wish()) #wish is same as greet ---->wish() ==greet() ,The inner function is executed only when inner funcvtion is executed
print(greet())