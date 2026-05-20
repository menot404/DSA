# Express a Number as Sum of Consecutive Numbers
*Source: GeeksforGeeks — Last Updated: 20 May, 2026*

Given a positive integer `n`, find whether it can be represented as the sum of **two or more consecutive positive integers**.

**Examples:**
- Input: `n = 10` → Output: `true` — `1 + 2 + 3 + 4 = 10`
- Input: `n = 8` → Output: `false` — 8 cannot be expressed as such a sum.
- Input: `n = 24` → Output: `true` — `7 + 8 + 9 = 24`

---

## [Naive Approach] Checking All Consecutive Sums — O(n²) Time and O(1) Space

Start from every number and keep adding consecutive numbers until the sum becomes equal to or greater than `n`. If it equals `n`, return `true`.

The sum of `k` consecutive numbers starting from `x` satisfies:

$$2n = (x + k)(x + k + 1) - x(x + 1)$$

We try all possible values and check whether this condition holds.

```python
def isSumOfConsecutive(n):
    # Try every starting number
    for i in range(1, n):
        sum = 0
        # Generate consecutive sum
        for j in range(i, n):
            sum += j
            # If sum becomes equal to n and at least two numbers are used
            if sum == n and j > i:
                return True
            # If sum exceeds n
            if sum > n:
                break
    return False

# Driver code
if __name__ == "__main__":
    n = 10
    if isSumOfConsecutive(n):
        print("true")
    else:
        print("false")
```

**Output:**
```
true
```

---

## [Expected Approach] Using Power of 2 Property — O(1) Time and O(1) Space

A number can be written as the sum of consecutive positive integers **if and only if it is not a power of 2**. We check this using bit manipulation.

### Why a power of 2 cannot be expressed?

The sum of `k` consecutive numbers satisfies:

$$\frac{k(2a + k - 1)}{2} = n \quad \Rightarrow \quad k(2a + k - 1) = 2n$$

If `k` is even, then `(k - 1)` is odd. Adding `2a` (even) to an odd number gives an odd number — so one factor is always odd and the other even. This means every such sum must have **at least one odd factor greater than 1**, which powers of 2 do not have.

### Why all other numbers can be expressed?

Every odd number `n = 2m + 1` can be written as `m + (m + 1)` — a sum of two consecutive integers.

```python
def isSumOfConsecutive(n):

    # 1 cannot be represented
    if n == 1:
        return False

    # Check if n is a power of 2
    if (n & (n - 1)) == 0:
        return False

    return True

# Driver code
if __name__ == "__main__":
    n = 10
    if isSumOfConsecutive(n):
        print("true")
    else:
        print("false")
```

**Output:**
```
true
```