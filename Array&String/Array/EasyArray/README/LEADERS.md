# Leaders in an Array
*Source: GeeksforGeeks — Last Updated: 22 Jan, 2026*

Given an array `arr[]` of size `n`, find all the **leaders** in the array. An element is a leader if it is **greater than or equal to all elements to its right**.

> **Note:** The rightmost element is always a leader.

**Examples:**
- Input: `arr[] = [16, 17, 4, 3, 5, 2]` → Output: `[17, 5, 2]`
  - `17 > [4, 3, 5, 2]` ✅, `5 > [2]` ✅, `2` has no right element ✅
- Input: `arr[] = [1, 2, 3, 4, 5, 2]` → Output: `[5, 2]`
  - `5 > [2]` ✅, `2` has no right element ✅

---

## [Naive Approach] Using Nested Loops — O(n²) Time and O(1) Space

Use two loops. The outer loop picks each element from left to right. The inner loop compares it to all elements on its right. If no larger element is found, the picked element is a leader.

```python
# Function to find the leaders in an array
def leaders(arr):
    result = []
    n = len(arr)

    for i in range(n):

        # Check elements to the right
        for j in range(i + 1, n):

            # If a larger element is found
            if arr[i] < arr[j]:
                break
        else:
            # If no larger element was found
            result.append(arr[i])

    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))
```

**Output:**
```
17 5 2
```

---

## [Expected Approach] Using Suffix Maximum — O(n) Time and O(1) Space

Scan all elements from **right to left**, keeping track of the maximum seen so far. Whenever the maximum changes, add it to the result. Finally, reverse the result to restore the original order.

```python
# Function to find the leaders in an array
def leaders(arr):
    result = []
    n = len(arr)

    # Start with the rightmost element
    maxRight = arr[-1]

    # Rightmost element is always a leader
    result.append(maxRight)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            result.append(maxRight)

    # Reverse the result list to maintain original order
    result.reverse()

    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))
```

**Output:**
```
17 5 2
```

**Illustration for `arr[] = [16, 17, 4, 3, 5, 2]` :**
```
Initially : maxRight = 2,  res[] = [2]
i = 4    : maxRight = 5,  res[] = [2, 5]
i = 3    : maxRight = 5,  res[] = [2, 5]
i = 2    : maxRight = 5,  res[] = [2, 5]
i = 1    : maxRight = 17, res[] = [2, 5, 17]
i = 0    : maxRight = 17, res[] = [2, 5, 17]
Reverse  : res[] = [17, 5, 2]  ✅
```