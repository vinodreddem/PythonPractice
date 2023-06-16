import heapq
from functools import reduce
arr = [12,45,3,4,67,89]
#Method 1 Use MAx Function 

print (max(arr))

#Method 2 : Use For Loop

def max_number_from_list(arr):
    max_number = arr[0]
    for num in arr[1:]:
        if num > max_number :
            max_number = num 
    return max_number

#Method 3: Use Reduce method

max_number_two = reduce(lambda x, y: x if x > y else y,arr)

#Heapq - nth largest element
print (heapq.nlargest (2,arr))


