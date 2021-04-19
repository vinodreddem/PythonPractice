#  def insertionSort_list (lst):
    
#     for i in range (1, len (lst)):
#         print ('The I value is ',i)
#         j =i
        
#         while j > 0 and lst[j-1] > lst[j]:
#             print ('J value is ' , j)
#             print (' lst[j] is',lst[j])
#             print (' lst[j-1] is',lst[j-1])
            
#             lst [j],lst [j-1] = lst [j-1], lst [j]
#             j -=1
#     return lst

lst = [56,2,56,43,40,35,35,37,42]
print ('lst', lst)
# Start with second element  in insertion start , So 'i' value from 1 to length of the array
#print (insertionSort_list (lst))

def insertionSort_list_method2 (array_inp):
    
    for i in range (1,len(array_inp)):
        
        key_elm = array_inp[i]
        print ('Key ELement is ',key_elm)
        
        #intiate J value to i-1 , The Elements upto 'i-1' are already sorted , So we need to 
        # identify the right place for the ith element.
        j = i-1 
        
        while j >=0 and array_inp [j] > key_elm :
            print ('arr_inp[j] is ',array_inp[j])
            array_inp [j+1] = array_inp [j]
            print ('arr_inp is ',array_inp)
            j -= 1
        array_inp [ j+1 ] = key_elm 
        print ('arr_inp is After Adding ',array_inp)#here J +1 is not equal to i since the value of the J is decreaseing 
        #Do not for get the Key element with the j +1 position.
        
    return array_inp
print (insertionSort_list_method2 (lst))
         


