#----------------------------------------------------------------------------------
""""
This File explains about input an doutput patterns
Input :
    1. To read the data from user , we are using input function
    2. By default it is a string data
    To allow flexibility we might want to take the input from the user.
    In Python, we have the input() function to allow this. The syntax for input() is

    input([prompt])

Output :
    1. to display the output to user in the console , we are using the "print" function.
    2. output formats explained below.
    The actual syntax of the print() function is
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

    sep ----> used to separate the different objects and The sep separator is used between the values.
    It defaults into a space character.

    end --->After all values are printed, end is printed. It defaults into a new line.

    Here, objects is the value(s) to be printed.

Output Formatting:
    Sometimes we would like to format our output to make it look attractive.
    This can be done by using the str.format() method. This method is visible to any string object.


"""
#----------------------------------------------------------------------------------

#output :

str_example = "this is a string"
print("The String Exmple is ",str_example) #here we have a space between the string and varianle str_example


a,b,c= 4,"vijay",3+7j

print(a,b,c,sep=" && ",end="\n")

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&


#output formatting
x,y =3,5
print("The  value of the X is {} and Y is {} is ".format(x,y))
#Here the {} are used as place holders to display the values.
#We can use the index of tuple also ,by defining the values in the tuple
#Here the curly braces {} are used as placeholders. We can specify the order in which it is printed by using numbers (tuple index).

print("The  value of the z is {1} and a is {0} is ".format("undefined","infinity"))
#here ("undefined","infinity") --is taking as tuple with index of 0 and 1

# We can use dict as also , like keyword arguments to format the string.
print("Hello {name} ,{greetings}".format(name ="Vijay",greetings="Good Mornig" ))

#We can even format strings like the old sprintf() style used in C programming language. We use the % operator to accomplish this.

x = 12.3456789
print('The value of x is %3.2f' %x)
#The value of x is 12.35
print('The value of x is %3.4f' %x)
#The value of x is 12.3457


#Input Function
_str =input("Enter the name ")
# by default value is string ---to get the data into int , flowat or desired format ,
#we need to use the type conversion methods.
type(_str)
num = int(input("Enter the values "))
type(num)

#To-DO
#needs to learn about eval() function

add=int(input ())

"""
If we enter an exptression we are getting the below error , we can implement this by eval() function
5+6
Traceback (most recent call last):
  File "C:/Users/Sanvi/PycharmProjects/PracticePython/Basics/Python_ApplicationPrograamming_Package/Input_OutputDemo.py", line 79, in <module>
    add=int(input ())
ValueError: invalid literal for int() with base 10: '5+6'
"""
sum =eval(input())
print(sum)