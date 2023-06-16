# lst = [1,1,0,0,0,1,1,0]

# def sort_elm (lst):
#     left = 0
#     right = len (lst) -1
    
#     while (left > right):
#         if (lst[left] > lst [right]):
#             lst [left], lst [right ] == lst [right] ,lst [left]
#             right -= 1
#         else :
#             left += 1
#     return lst

# print(sort_elm(lst))

# Find all Common elements in a given 3 sorted arrays 
lst1 = []
lst2 = []
lst3 = []

i ,j, k =0,0,0
out = []
while (i< len (lst1) and j < len (lst2) and k < len(lst3)):
    
    if (lst1[i]==lst2[j] and lst1[i]==lst3[k]):
        out.append(lsst[i])
    elif (lst1[i] > lst2[j] and lst1[i]==lst3[k]):
        j += 1
    elif (lst1[i]==lst2[j] and lst1[i] > lst3[k]):
        k += 1
    elif (lst1[i] > lst2[j] and lst1[i] > lst3[k]):
        j += 1 
        k += 1
        
    elif ( lst2[j] > lst1[i] and lst2[j]==lst3[k] ):
        i += 1
    
    elif ( lst2[j] > lst1[i] and lst2[j] > lst3[k] ):
        i += 1
        k += 1
        
    elif ( lst2[j] > lst1[i] and lst2[j]==lst3[k] ):
        i += 1
    elif ( lst3[k] > lst1[i] and lst2[j] < lst3[k] ):
        i += 1
        j += 1
    
#Given a number n find the number of 
#pairs (x,y) where both x and y are less than n and highest common factor (hcf) of x and y is 1

def hcf_numbers (x,y):
    
    if x >y:
        smaller = y
    else :
        smaller = x
    for i in range (1, smaller + 1) :
    
        if (x % i == 0 and y % i == 0):
            hcf = i

    return hcf

number = 10

pair = []
for  j in range (4, number+1):
    
    for k in range (4, number+1):
        
        hcf = hcf_numbers (j,k)
        
        if hcf == 1:
            tup = (j,k)    
            pair.append(tup)

print (pair)

