# Print n to 1 using Recursion
*Source: GeeksforGeeks — Last Updated: 27 Sep, 2025*

Given an integer `n`, print numbers from `n` to `1` using recursion.

**Examples:**
- Input: `n = 3` → Output: `[3, 2, 1]`
- Input: `n = 10` → Output: `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`

---

## Approach

We first check the base case: if `n == 0`, stop further recursive calls. Otherwise, we **print first**, then make the recursive call with `n - 1`. This way the function keeps reducing the problem size until it reaches the base case, printing numbers in decreasing order.

```python
def printNos(n):
    # base case
    if n == 0:
        return
    print(n, end=' ')

    # recursive call
    printNos(n - 1)

if __name__ == "__main__":
    n = 3
    printNos(n)
```

**Output:**
```
3 2 1
```

- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n) — Recursive Stack Space