def quicksort(array):
    
    if len(arr < 2):
        return array
    
    low, high, same = [] , [], []
    
    pivot = array([randint(0, len(array - 1)))
    
    for item in array:
        if item < pivot:
            low.append(item) 
        elif item > pivot:
            high.append(item)
        else item == pivot:
            same.append(item)
    return quicksort(low) + same + quicksort (high)
    
            
    