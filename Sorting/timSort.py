""" 
The Timsort algorithm is considered a 
hybrid sorting algorithm because it employs a best-of-both-worlds combination of insertion sort and merge sort. 

The main characteristic of Timsort is that it takes advantage of already-sorted elements that exist in most real-world datasets. These are called natural runs. 
The algorithm then iterates over the list, collecting the elements into runs and merging them into a single sorted list.

"""