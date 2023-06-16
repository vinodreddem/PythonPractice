s = "greekforks"
c ='k'
emp= [ch for ch in s if ch!=c]
print (emp)
emp_str ="".join(emp) 
print (emp_str)

# Program to FInd the Nth prime Number


def isPrime (num):
    if num > 1:
        
        for i in range (2, num):
            if num%2 == 0:
                return False 
        return True
    else :
        return False 
    

nth_prime = 8
num_prime = 2
count = 0
while (count < nth_prime ) :
    
    if (isPrime (num_prime)):
        count += 1
    num_prime += 1

print ( num_prime -1)
    
    
