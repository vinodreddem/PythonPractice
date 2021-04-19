"""
Belzabar is 18 years old. On this occasion, we formulated the Belzabar Number. A positive integer is a Belzabar number if it
can be represented either as (n  (n + 18)) OR (n  (n - 18)), where n is a prime number.

Write a function named 'is_belzabar_number' which accepts a number as input and determines if it is a Belzabar Number (or not). 
Input to the function will be a number and the output will be boolean.

For bonus points,
1. Write a function that calculates and prints the count of Belzabar numbers less than or equal to 1 million.
2. Write a function that calculates and prints the count of Belzabar numbers from bonus question #1 above that are prime.

There are additional bonus points for elegance, adequate code comments describing the algorithm(s) used, focus on coding conventions, 
optimal speed and time complexity and readability.

"""
def is_primeNumber(num):
    if num <= 1:
        return False
    for i in range (2,num-1):
        if (num%i==0):
            return False
    return True

def is_belzabar_number(number):    
    
    flag = True
    inc = 2
    if number % 2 == 0:
        temp = 0
    else:
        temp = 1

    while flag:
        x = temp * (temp + 18)
        temp = temp + inc
        if x >= number:
            flag = False








print (is_primeNumber(4))