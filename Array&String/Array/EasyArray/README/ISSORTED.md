# Check if an Array is Sorted
*Source: GeeksforGeeks — Last Updated: 28 Mar, 2026*

Given an array `arr[]`, check if it is sorted in **ascending order** or not. Equal values are allowed — two consecutive equal values are considered sorted.

**Examples:**
- Input: `arr[] = [10, 20, 30, 40, 50]` → Output: `true` — the array is sorted.
- Input: `arr[] = [90, 80, 100, 70, 40, 30]` → Output: `false` — the array is not sorted.

---

## Iterative Approach — O(n) Time and O(1) Space

Traverse from the second element. For every element, check if it is smaller than the previous one. If so, return `false`.

**Example for `arr[] = [10, 20, 30, 5, 6]` :**
```
i = 1 : (10 <= 20), continue
i = 2 : (20 <= 30), continue
i = 3 : (30 > 5),   return false
```

```python
def isSorted(arr):
    n = len(arr)

    # Iterate over the array and check if every element
    # is greater than or equal to the previous element
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False

    return True

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    if isSorted(arr):
        print("true")
    else:
        print("false")
```

**Output:**
```
true
```

---

## Recursive Approach — O(n) Time and O(n) Space

Check if the last two elements are in order, then recursively check the rest of the array. The base case is when the array has zero or one element — always considered sorted.

**Step-by-step approach:**

1. If the size of the array is zero or one, return `true`.
2. Check the last two elements — if sorted, make a recursive call with `n - 1`, else return `false`.

```python
def isSortedhelper(arr, n):

    # Base case
    if n == 0 or n == 1:
        return True

    # Check if current and previous elements are in order
    # and recursively check the rest of the array
    return arr[n - 1] >= arr[n - 2] and isSortedhelper(arr, n - 1)

def isSorted(arr):
    n = len(arr)
    return isSortedhelper(arr, n)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    if isSorted(arr):
        print("true")
    else:
        print("false")
```

**Output:**
```
true
```

---

## Using Built-in Methods (Python only) — O(n) Time and O(1) Space

We use Python's built-in `sorted()` method to check if an array is sorted.

```python
def is_sorted(arr):

    # sorted() is a built-in method for Python
    return arr == sorted(arr)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    if is_sorted(arr):
        print("true")
    else:
        print("false")
```

**Output:**
```
true
```