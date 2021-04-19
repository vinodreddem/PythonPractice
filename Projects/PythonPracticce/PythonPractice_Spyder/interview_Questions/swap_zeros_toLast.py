
# lst --- contains only zeros and ones 
# Shift all zeroes to left and all ones to right 
lst = [1,0,1,0,0,1,1,0]

def is_shift_zeros(lst):
    j = len(lst)
    for i in range (len(lst)):
        if lst[i] == 1: 
            for j in range(len(lst)-1,i,-1):
                print (j)
                if lst[j] == 0:
                    lst[i],lst[j] = lst[j],lst[i]
                    break
    return lst

print ('lst is ',is_shift_zeros(lst))