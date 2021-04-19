#----------------------------------------------------------------------------------------- 
# Your previous Plain Text content is preserved below:
# 
# Belzabar is 18 years old. On this occasion, we formulated the Belzabar Number. A positive integer is a Belzabar number if it can be represented either as (n  (n + 18)) OR (n  (n - 18)), where n is a prime number.
# 
# Write a function named 'is_belzabar_number' which accepts a number as input and determines if it is a Belzabar Number (or not). Input to the function will be a number and the output will be boolean.
# 
# For bonus points,
# 1. Write a function that calculates and prints the count of Belzabar numbers less than or equal to 1 million.
# 2. Write a function that calculates and prints the count of Belzabar numbers from bonus question #1 above that are prime.
# 
# There are additional bonus points for elegance, adequate code comments describing the algorithm(s) used, focus on coding conventions, optimal speed and time complexity and readability.
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
#  Method to CHeck the Prime Number
# ----------------------------------------------------------------------------------------

def is_primeNumber(num):
    """ This method returns True If given Number is Prime Else False """
    if num <= 1:
        return False
    for i in range (2,num-1):
        if (num%i==0):
            return False
    return True


belzabar_Number = int (input ("Please Enter your Number"))
""" determine given Number is belzabar Number or Not """
def is_belzabar_number(number):    
    
    belzabar_Year = 18
    flag = True
    inc = 2
    #------------------------------------------------------------------------------------
    # Even Prime Number :For Even Prime Numbers - There is only one Possible positive 
    # Belzabar Number Exists  i.e.40  ( n= 2 -- (2 * (2+18)) 
    # 
    # Odd Prime Numbers : We will Loop until we found given Belzabar number or greater 
    # number by using  equation (n * (n+18) ) 
    #------------------------------------------------------------------------------------
    
    if number % 2 == 0:
        
        belzabar_Number_EvenPrime = 2
        
        if (number == (belzabar_Number_EvenPrime * (belzabar_Number_EvenPrime + belzabar_Year))):
            return True
        else :
            return False
    else:
        temp = 1

    while flag:
        x = temp * (temp + belzabar_Year)
        if x >= number:
            break 
        
        temp = temp + inc
    # ------------------------------------------------------------------------------------
    # Case 1: If number matches with the given input Number: 
    #     Sub Case 1: Check for Member is Prime or Not , If yes Return True Else Execute 
    #                 below code (This is sollution for (n * (n +18)))
    #     Sub case 2: Needs to determine sollution for (n * (n - 18))) i.e. ( temp +18) for 
    #                 positive integers. (difference is 18)
    #                Number         (n * (n +18)) Sollution     (n * (n - 18)) Sollution
    #               ---------------------------------------------------------------------
    #                 19                1                            19 
    #                 40                2                            20
    #                 63                3                            21
    # Case 2: If number does not match then return False as Both equeations does not have 
    # sollution
    #-----------------------------------------------------------------------------------
    if x == number:
        if(is_primeNumber (temp)):
            return True
        else :
            if(is_primeNumber (temp + belzabar_Year)):
                return True
            
    return False

print ('given Number is belzabar Number or Nor ...', is_belzabar_number(belzabar_Number))

#----------------------------------------------------------------------------------------
# 1. Write a function that calculates and prints the count of Belzabar numbers less than 
# or equal to 1 million.
# Function to Calculate Belzabar Numbers under Million
#----------------------------------------------------------------------------------------

ONE_MILLION = 1000000
def belzabar_Numbers_Under_Million(input_Number ):  
    """ Determine the Count of Belzabar Numbers Under Million"""
    temp = 1
    belzabar_Year = 18
    flag = True
 
    while flag:
        x = temp * (temp + belzabar_Year)
        if x >= input_Number  :
            break 
        temp = temp + 1
    
    if x == input_Number:
        return temp
    
    else:
        return temp - 1
    



print ('belzabar Numbers Under one Million', belzabar_Numbers_Under_Million(ONE_MILLION))


# --------------------------------------------------------------------------------------    # 2. Write a function that calculates and prints the count of Belzabar numbers from bonus 
# question #1 above that are prime.
# We can use the count of numbers to determine prime numbers from that
# -------------------------------------------------------------------------------------

def count_BelzabarNumbers_underMillion_WhichArePrime( number ):
    """ Belzabar Numbers which are prime"""
    
    count_Of_BelzaBar_Nmbrs = belzabar_Numbers_Under_Million(number)
    
    prime_numbers = filter (is_primeNumber, list (range (2, count_Of_BelzaBar_Nmbrs +1) ))

    return len (list (prime_numbers))

print (' belzabar Numbers Under one Million Which are Prime' , count_BelzabarNumbers_underMillion_WhichArePrime(ONE_MILLION))