# Program for Sum of N Natural Numbers
*Source: GeeksforGeeks — Last Updated: 9 Apr, 2026*

Given a positive integer `n`, find the sum of the first `n` natural numbers.

**Examples:**
- Input: `n = 3` → Output: `6` — `1 + 2 + 3 = 6`
- Input: `n = 5` → Output: `15` — `1 + 2 + 3 + 4 + 5 = 15`

---

## [Naive Approach] Using Loop — O(n) Time and O(1) Space

- Initialize `sum` as `0`
- Run a loop from `i = 1` to `n`, adding `i` to `sum` at each step.

**Example for `n = 4`:**
```
Initially : sum = 0
i = 1, sum = 0 + 1 = 1
i = 2, sum = 1 + 2 = 3
i = 3, sum = 3 + 3 = 6
i = 4, sum = 6 + 4 = 10
```

```python
def findSum(n):
    sum = 0
    i = 1

    # Iterating over all the numbers between 1 to n
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum

if __name__ == "__main__":
    n = 5
    print(findSum(n))
```

**Output:**
```
15
```

---

## [Alternative Approach] Using Recursion — O(n) Time and O(n) Space

The function calls itself with `(n-1)` until it reaches the base case `n == 1`. Each call adds the current value of `n` to the sum of smaller values, building the result in a top-down manner.

```python
def findSum(n):
    # base condition
    if n == 1:
        return 1
    return n + findSum(n - 1)

if __name__ == "__main__":
    n = 5
    print(findSum(n))
```

**Output:**
```
15
```

---

## [Expected Approach] Formula Based Method — O(1) Time and O(1) Space

$$\text{Sum of first } n \text{ natural numbers} = \frac{n \times (n + 1)}{2}$$

**Example for `n = 5`:**

$$\frac{5 \times (5 + 1)}{2} = \frac{5 \times 6}{2} = \frac{30}{2} = 15$$

### How does this work?

We can prove this formula using **mathematical induction**:

- For `n = 1` : `1 × (1+1) / 2 = 1` ✅
- For `n = 4` : `4 × (4+1) / 2 = 10` ✅

Assume it is true for `k = n - 1`:

$$\text{Sum of } k \text{ numbers} = \frac{k \times (k+1)}{2}$$

Substituting `k = n - 1`:

$$\text{Sum of } (n-1) \text{ numbers} = \frac{(n-1) \times n}{2}$$

Adding `n` to both sides:

$$\text{Sum of } n \text{ numbers} = n + \frac{(n-1) \times n}{2} = \frac{2n + n^2 - n}{2} = \frac{n \times (n+1)}{2}$$

```python
def findSum(n):
    # Using mathematical formula to compute
    # sum of first n natural numbers
    return n * (n + 1) // 2

if __name__ == "__main__":
    n = 5
    print(findSum(n))
```

**Output:**
```
15
```