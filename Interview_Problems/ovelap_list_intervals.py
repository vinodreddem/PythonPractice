# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.

# Example 1: 

# Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

# Output: [[1,6],[8,10],[15,18]]

# Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
#  intervals.

# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]

# Explanation: Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].



intervals=[[1,3],[2,6],[15,18], [8,20]]
def merge_all_intervals(lst_intervals):
    lst_intervals.sort(key = lambda x:x[0])
    print("sorted lst_intervals", lst_intervals)
    out_put = []
    first_elm = lst_intervals[0]
    for ran in lst_intervals[1:]:
        if first_elm[-1] >= ran[0]:
            if first_elm[-1] < ran[1]:
                first_elm[-1] = ran[1]
        else:
            out_put.append(first_elm)
            first_elm = ran
    out_put.append(first_elm)
    print(out_put)

merge_all_intervals(intervals)

