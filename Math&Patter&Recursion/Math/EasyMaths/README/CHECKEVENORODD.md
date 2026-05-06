# Check Even or Odd
*Source: GeeksforGeeks — Last Updated: 9 Apr, 2026*

Given a number `n`, check whether it is even or odd. Return `true` for even and `false` for odd.

**Examples:**

- Input: `n = 15` → Output: `false` — `15 % 2 = 1`, so 15 is odd.
- Input: `n = 44` → Output: `true` — `44 % 2 = 0`, so 44 is even.

---

## [Naive Approach] By Finding the Remainder — O(1) Time and O(1) Space

We can check the remainder when divided by 2. If the remainder is 0, the number is even, otherwise it is odd.  
For example, dividing 13 by 2 gives remainder 1, and dividing 14 by 2 gives remainder 0.

```python
def isEven(n):

    # finding remainder of n
    rem = n % 2
    if rem == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")
```

**Output:**
```
false
```

---

## [Efficient Approach] Using Bitwise AND Operator — O(1) Time and O(1) Space

The last bit of all odd numbers is always `1`, while for even numbers it is `0`. So, when performing a bitwise AND with `1`, odd numbers give `1` and even numbers give `0`.

> **Note:** Bitwise operators are extremely fast and efficient because they operate directly at the binary level, making them significantly faster than arithmetic or logical operations.

**Examples:**

```
15  →   1 1 1 1
      & 0 0 0 1
        -------
        0 0 0 1  → odd number

44  →   1 0 1 1 0 0
      & 0 0 0 0 0 1
        -----------
        0 0 0 0 0 0  → even number
```

```python
def isEven(n):
    # taking bitwise and of n with 1
    if (n & 1) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")
```

**Output:**
```
false
```