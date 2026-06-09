#_________________________________________________________________
#
#   EASY ARRAY - Stock Buy and Sell - Max one Transaction Allowed
#__________________________________________________________________

# Method 1: [Naive Approach] By exploring all possible pairs
"""
The idea is to use two nested loops to explore all the possible ways to buy and sell stock. 
The outer loop decides the day to buy the stock and the inner loop decides the day to sell the stock. 
The maximum difference between the selling price and buying price between every pair of days will be our answer. 
    # O(n^2) Time
    # O(1) Space
"""
def maxProfit(prices):
    n = len(prices)
    res = 0
    # Explore all possible ways to buy and sell stock
    for i in range(n - 1):
        for j in range(i +1 , n):
            res = max(res, prices[j] - prices[i])
    return res

# Driver Code
if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices=prices))