# Python3 program to find longest 
# contiguous subsequence 
 
# Returns length of the longest 
# contiguous subsequence 
def findLongestConseqSubseq(arr, n):
     
    ans = 0
    count = 0
 
    # Sort the array 
    arr.sort()
 
    v = []
 
    v.append(arr[0])
 
    # Insert non-repeated elements only 
    # once in the vector 
    for i in range(1, n):
        print ('arr [i] is ',arr[i])
        print ('arr [i] is ',arr[i-1])
        if (arr[i] != arr[i - 1]):
            print (arr[i])
            v.append(arr[i])
 
    # Find the maximum length 
    print (v)
    # by traversing the array 
    for i in range(len(v)):
 
        # Check if the current element is
        # equal to previous element +1 
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
             
        # Reset the count 
        else:
            count = 1
             
        # Update the maximum 
        ans = max(ans, count)
         
    return ans
 
# Driver code 
arr = [ 1,5,7,8,3,1,2,3,4,5,9,4,5,6,8 ]
n = len(arr)
 
print("Length of the Longest contiguous subsequence is",
       findLongestConseqSubseq(arr, n))

#Algorithm
#Step 1: First Sort the Array
#Step 2: Remove duplicated elements so that we will get unique List
#Step 3: Compare current element with previous element + 1
#Step 4: Update Max of the previous count with current count
