# Compare one element with the other and Place the largest element at the end of the Array
# Then compare upto n-1 elemnts and place second largest element in the last but one position

def buble_sort (arr_inp):
    
    for i in range (len(arr_inp)):
        
        isarray_sorted = True
        
        for j in range ( len (arr_inp ) - i -1) :
            print ('J value is ',j)
            if arr_inp[j] > arr_inp [j+1] :
                arr_inp[j] , arr_inp [j+1] = arr_inp[j+1] ,  arr_inp [j]
                isarray_sorted = False
                print ('List is ',arr_inp)
    
        if isarray_sorted:
            break    
#isarray_sorted -- We will get O(n) as time complexity in case of sorted array as input.

lst = [ 23,45,66,2,5,90,22, 107,109,113]
print (buble_sort (lst))

#Here we will check in each iteration , say like If Iteration is already sorted , then we will not loop further
