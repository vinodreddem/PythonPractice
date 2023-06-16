"""AAAABBBCCDDDD you have to print it as 4A3B2C4D"""
str_in = "AAAABBBCCDDDDabe"
str_in=str_in.upper()
str_in= sorted(str_in)
print (list(str_in))

# Method 1
result = ""
count = 1
for i in range (0,len(str_in)):

    if i == len(str_in)-1:
        result = result + str_in[i]+str(count)
    elif  str_in[i] == str_in[i+1]:
        count = count +1 
    else:
        result = result + str_in[i]+str(count)
        count =1
print (result)

#Method 2
result2 = str_in[0]
count = 1
for i in range (1, len(str_in)):
    if  str_in[i] == str_in[i-1]:
        count = count +1 
    else:
        result2 = result2 + str(count) +  str_in[i]
        count = 1
result2 = result2 + str (count)
    
print ('result2', result2)

"""write a program check if the expression isbalanced or not?
Given a string str of length N, consisting of ‘(‘ and ‘)‘ only, the task is to check whether it is balanced or not.
Input: str = “((()))()()” 
Output: Balanced

Input: str = “())((())” 
Output: Not Balanced 
"""
# flag = True

# st_bal = r'a((()))()())((b'
# print (len(st_bal))
# count_b = 0
# for i in range (len(st_bal)):
#     if st_bal[i]== '(':
#         count_b += 1
#     if st_bal[i]==')':
#         count_b -= 1
# print(count_b)
