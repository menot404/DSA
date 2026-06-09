# Stock Buy and Sell — Max One Transaction Allowed
*Source: GeeksforGeeks — Last Updated: 31 Jan, 2026*

Given an array `prices[]` of non-negative integers representing stock prices on different days, find the **maximum profit** possible by buying and selling stocks when **at most one transaction** is allowed (1 buy + 1 sell). Return `0` if no profit is possible.

> **Note:** Stock must be bought before being sold.

**Examples:**
- Input: `prices[] = [7, 10, 1, 3, 6, 9, 2]` → Output: `8` — buy at `1`, sell at `9`.
- Input: `prices[] = [7, 6, 4, 3, 1]` → Output: `0` — array is decreasing, no profit possible.
- Input: `prices[] = [1, 3, 6, 9, 11]` → Output: `10` — buy at `prices[0]`, sell at `prices[n-1]`.

---

## [Naive Approach] Exploring All Possible Pairs — O(n²) Time and O(1) Space

Use two nested loops to explore all possible buy/sell combinations. The outer loop picks the buy day, the inner loop picks the sell day. The maximum difference between selling and buying price across all pairs is the answer.

```python
def max_profit(prices):
    n = len(prices)
    res = 0

    # Explore all possible ways to buy and sell stock
    for i in range(n - 1):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])

    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(max_profit(prices))
```

**Output:**
```
8
```

---

## [Expected Approach] One Traversal Solution — O(n) Time and O(1) Space

To maximize profit, we need to **minimize the buy price** and **maximize the sell price**. At every step, we track the minimum price seen so far. For every price, we compute the profit by subtracting the minimum so far, and update the result if we get a higher profit.

```python
def maxProfit(prices):
    minSoFar = prices[0]
    res = 0

    for i in range(1, len(prices)):

        # Update the minimum value seen so far
        minSoFar = min(minSoFar, prices[i])

        # Update result if we get more profit
        res = max(res, prices[i] - minSoFar)

    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))
```

**Output:**
```
8
```