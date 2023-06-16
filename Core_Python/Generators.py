# # list_a = [i**2 for i in range(20)] # List comprehension is used a [ ] square brackets.
# # print(list_a)
# #
# # generator_a = (i*2 for i in range(20))
# # print(generator_a) # It will generates elements one at a time , iterator wise . It uses ( ) open brackets to generates generator.
# #
# # print(next(generator_a))
# # print(next(generator_a))
# # https://www.programiz.com/python-programming/generator

def fib ():
    a,b =0,1

    while 1:
        yield a
        a,b =b,a+b

fs =fib()
print ('Fib one element is', fs.__next__())

print ('Fib one element is', fs.__next__())

print ('Fib one element is', fs.__next__())

print ('Fib one element is', fs.__next__())
# a = int(input('Give amount: '))
#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# print(list(fib(a)))

def factoria_number (n):
    n = abs(n)
    if n < 1 :
        return 1
    else :
        return ( n * factoria_number(n-1))

def factorial_generator (numbersinseries):
    i=0
    while i<=numbersinseries:
        yield factoria_number(i)
        i+=1

fs = factorial_generator(5)

print(fs)

print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())
print(fs.__next__())



"""

When to use yield instead of return in Python?
Difficulty Level : Easy
 Last Updated : 06 Dec, 2019
The yield statement suspends function’s execution and sends a value back to the caller, 
but retains enough state to enable function to resume where it is left off.
When resumed, the function continues execution immediately after the last yield run.
This allows its code to produce a series of values over time, 
rather than computing them at once and sending them back like a list.

Let’s see with an example:

filter_none
edit
play_arrow

brightness_4
# A Simple Python program to demonstrate working 
# of yield 
  
# A generator function that yields 1 for the first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 
Output:

1
2
3
Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

Yield are used in Python generators. 
A generator function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword rather than return.
If the body of a def contains yield, the function automatically becomes a generator function.
"""