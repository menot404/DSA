# Factorial of a Number
*Source: GeeksforGeeks — Last Updated: 9 Apr, 2026*

Given a non-negative integer `n`, compute its factorial. Factorial of `n` is defined as:

$$n! = n \times (n-1) \times (n-2) \times \dots \times 1$$

For `n = 0`, the factorial is defined as `1`.

**Examples:**
- Input: `n = 5` → Output: `120` — `5! = 5 × 4 × 3 × 2 × 1 = 120`
- Input: `n = 4` → Output: `24` — `4! = 4 × 3 × 2 × 1 = 24`
- Input: `n = 0` → Output: `1`
- Input: `n = 1` → Output: `1`

---

## Iterative Solution — O(n) Time and O(1) Space

Factorial is computed by multiplying all integers from `1` to `n` using a loop. We initialize `ans = 1` and update it at each iteration by multiplying with the current number. This approach avoids recursion and uses constant extra space.

**Step-by-step execution for `n = 4` :**
```
Initialize : ans = 1
i = 1, ans = 1 * 1 = 1
i = 2, ans = 1 * 2 = 2
i = 3, ans = 2 * 3 = 6
i = 4, ans = 6 * 4 = 24
Final factorial = 24
```

```python
def factorial(n):
    ans = 1
    i = 2

    # Calculating factorial of number
    while i <= n:
        ans *= i
        i += 1
    return ans

if __name__ == "__main__":
    num = 5
    print(factorial(num))
```

**Output:**
```
120
```

---

## Recursive Solution — O(n) Time and O(n) Space

Factorial is defined recursively as `n! = n × (n-1)!`. The base case returns `1` when `n == 0` or `n == 1`. Otherwise, the function calls itself with `n - 1`, breaking the problem into smaller subproblems until reaching the base case.

```python
def factorial(n):
    # Base case
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = 5
    print(factorial(num))
```

**Output:**
```
120
```