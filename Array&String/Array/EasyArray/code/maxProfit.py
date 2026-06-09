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
def maxProfitNaive(prices):
    n = len(prices)
    res = 0
    # Explore all possible ways to buy and sell stock
    for i in range(n - 1):
        for j in range(i +1 , n):
            res = max(res, prices[j] - prices[i])
    return res


# Method 2: [Expected Approach] One Traversal Solution
"""
In order to maximize the profit, we need to minimize the cost price and maximize the selling price. 
So at every step, we keep track of the minimum buy price of stock encountered so far. 
For every price, we subtract with the minimum so far and if we get more profit than the current result, we update the result.
    # O(n) Complexity Time
    # O(1) Complexity Space
"""
def maxProfitExpected(prices):
    n = len(prices)
    minSofar = prices[0]
    res = 0

    for i in range(1, n):
        # Update the minimum value seen so far
        minSofar = min(minSofar, prices[i])
        # Update result if we get more profit
        res = max(res, prices[i] - minSofar)
    return res

# Driver Code
if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(f"[Naive Approach] By exploring all possible pairs --- Profit: {maxProfitNaive(prices=prices)}")

    prices = [18, 9, 6, 8, 12, 23, 1]
    print(f"[Expected Approach] One Traversal Solution --- Profit: {maxProfitExpected(prices)}")