import numpy as np

# arr = np.random.randn(5,4)
arr = np.arange(20).reshape(5,4)
print(arr)

#Slicing of arr 

#Getting Rows 
first_row = arr[0]
second_row = arr[1]
print ('first Row ',first_row)
print ('second_row ',second_row)

first_two_rows = arr[:2]
print ('first_two_rows',first_two_rows)

from_first_row = arr[1:] #[ 0  4  8 12 16]
print ('from_first_row is',from_first_row)

#getting COlumns 
first_column = arr[:,0]
print (first_column)

few_columns = arr[:,1:3]
print ('few_columns ',few_columns)


#axis = 0 ----> Column wise operations and axis = 1 -----> Row wise operations
print (arr.mean(axis =0)) # [ 8.  9. 10. 11.]

# [[ 0  1  2  3] ---1.5
#  [ 4  5  6  7] ---5.5
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]]

print (arr.mean(axis = 1)) #[ 1.5  5.5  9.5 13.5 17.5]