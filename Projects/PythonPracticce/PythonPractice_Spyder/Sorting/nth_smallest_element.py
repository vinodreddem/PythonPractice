# # This function returns k'th smallest element
# # in arr[l..r] using QuickSort based method.
# # ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
# import sys
 
# def kthSmallest(arr, l, r, k):
#     print ('r value is ',r)
#     # If k is smaller than number of
#     # elements in array
#     print ('k value is ',k)
#     print ('l value is ',l)
#     if (k > 0 and k <= r - l + 1):
        
#         # Partition the array around last
#         # element and get position of pivot
#         # element in sorted array
#         pos = partition(arr, l, r)
#         print ('l value is ',l)
#         print ('pos is ',pos)
#         print ('arr is ',arr)
#         # If position is same as k
#         if (pos - l == k - 1):
#             return arr[pos]
#         if (pos - l > k - 1): # If position is more,
#                               # recur for left subarray
#             return kthSmallest(arr, l, pos - 1, k)
 
#         # Else recur for right subarray
#         return kthSmallest(arr, pos + 1, r,
#                             k - pos + l - 1)
 
#     # If k is more than number of
#     # elements in array
#     return sys.maxsize
 
# # Standard partition process of QuickSort().
# # It considers the last element as pivot and
# # moves all smaller element to left of it
# # and greater elements to right
# def partition(arr, l, r):
 
#     x = arr[r]
#     i = l
#     for j in range(l, r):
#         if (arr[j] <= x):
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#     arr[i], arr[r] = arr[r], arr[i]
#     return i
 
# # Driver Code
# if __name__ == "__main__":
     
#     arr = [12, 3, 5, 7, 4, 19, 26]
#     n = len(arr)
#     nth_element  = 3;
#     print("K'th smallest element is",
#            kthSmallest(arr, 0, n - 1, nth_element))
 
# # This code is contributed by ita_c


arr = [12,45,78,21,32,7,45,2] #[2, 7, 12, 21, 32, 45, 45, 78]
nth_small = 4

def find_nth_smallest_number (arr,nth_element):
    
    get_position = sort_some_part(arr)

def sort_some_part(arr):
    print('input arr is ',arr)
    
    sort_base_element = arr[-1]
    small = []
    high = []
    same = []
    
    for i in len(arr):
        if arr[i] > sort_base_element:
            high.append(i)
            


    












