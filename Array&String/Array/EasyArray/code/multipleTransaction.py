#____________________________________________________________________
#
#   EASY ARRAY - Stock Buy and Sell - Multiple Transaction Allowed
#____________________________________________________________________

# Method 1: [Naive Approach] By Trying All Possibility
"""
The idea is to use recursion to simulate all choices of buying and selling. For each day, you can either skip it or buy on that day. 
If you buy at day i, then you try all possible selling days j > i where price[j] > price[i].
    # O(2^n) Time
    # O(n) Space
"""

def maxProfitNaive(price, start, end):
    res = 0
    # Try every possible pair of buy (i) and sell (j) days
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            # Valide transaction if selling price is greater than buying price
            if price[j] > price[i]:
                # Calculate current profit
                curr_profit = price[j] - price[i] + maxProfitNaive(price, start, i + 1) + maxProfitNaive(price, j + 1, end)
                # Update result if current profit is greater than the maximum found so far
                res = max(res, curr_profit)
    return res

def maxProfit(price):
    n = len(price)
    return maxProfitNaive(price, 0, n - 1)

# Driver Code
if __name__ == "__main__":
    price = [7, 1, 5, 3, 6, 4]
    print(f"[Naive Approach] By Trying All Possibility --- Profit: {maxProfit(price)}")