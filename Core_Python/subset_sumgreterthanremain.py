#  input -- [4,5,4,1,3]
#  Subset having sum as greater than remaining elements 
#  sum 5 and 4 s greater than remaining elements -- Ans is 4, 5

def subsetA(arr):
    ori_arr = arr.copy()
    arr.sort(reverse = True)
    sub_arr_B = []   
    out_arr = [] 
    print (arr)
    for i in range (len(arr)):
        if sum(sub_arr_B) > sum(arr[i:]):
            break
        else:
            sub_arr_B.append(arr[i])
            
    for elm in ori_arr:
        if elm in sub_arr_B:
            out_arr.append(elm)
            sub_arr_B.remove(elm)
    
    return out_arr

 
print (subsetA([4,5,4,1,3]))