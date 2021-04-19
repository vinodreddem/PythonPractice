import math 

num = int(input('Enter the Number'))

flag = True
inc = 2
if num % 2 == 0:
    temp = 0
else:
    temp = 1

while flag:
    x = temp * (temp + 18)
    # y = temp * (temp - 18)
    temp = temp + inc
    if x >= num:
        flag = False

print(x)
print(temp)

if x == num:
    if(is_primeNumber (temp)):
        return True
    else:
        
        


def is_primeNumber(num):
    if num <= 1:
        return False
    for i in range (2,num-1):
        if (num%i==0):
            return False
    return True

print (2)

# print(x)
# print(temp)
# print("")
     
     
# def is_Match_Exists_Positive(num , temp,inc):
#     while flag:
#     x = temp * (temp + 18)
#     temp = temp + inc
#     if x >= num:
#         flag = False

# def is_Match_Exists_Negaitive(num , temp):
#     while flag:
#         y = temp * (temp - 18)
#         temp += inc
#         if x >= num:
#             flag = False
#     return x, temp
