# Print 1 to n using Recursion
*Source: GeeksforGeeks — Last Updated: 30 Sep, 2025*

Given an integer `n`, print numbers from 1 to `n` using recursion.

**Examples:**
- Input: `n = 3` → Output: `[1, 2, 3]`
- Input: `n = 10` → Output: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

---

## Approach

We define a recursive function that takes `n` as argument:

1. **Base case:** if `n == 0`, stop the recursion.
2. **Recursive call:** call `printNos(n - 1)` first, so smaller numbers are handled before the current one.
3. **Print:** after the recursive call returns, print the current value of `n`.

This ensures numbers are printed in ascending order from 1 to `n`.

```python
def printNos(n):
    if n == 0:
        # base condition
        return

    # recursive call first
    printNos(n - 1)

    # print after recursion
    print(n, end=' ')

if __name__ == "__main__":
    n = 3
    printNos(n)
```

**Output:**
```
1 2 3
```

- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)