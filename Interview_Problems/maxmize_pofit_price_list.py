# You want to maximize your profit by choosing a single day to buy 
# one stock and choosing a different day in the future to sell that stock. 
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# Note: That buying on day 2 and selling on day 1 
# is not allowed because you must buy before 
# you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are 
# done and the max profit = 0.

# prices = [7,1,5,3,6,4]

# find max-diff betwen the given numbers
def maximize_profit(price_lst):
    max_profit = 0
    i = 0
    j = 1
    while j < len(price_lst):
        if price_lst[i] < price_lst[j]:
            profit = price_lst[j] - price_lst[i]
            max_profit = max(max_profit, profit)
        else:
            i = j
        j += 1
        
    return max_profit
prices = [7,6,4,3,1]

# left pointer -- first index
# right pointer -- last index. -- 

print(maximize_profit(prices))