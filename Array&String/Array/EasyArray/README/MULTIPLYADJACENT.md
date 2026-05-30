# Replace with Adjacent Multiplication
*Source: GeeksforGeeks — Last Updated: 10 May, 2026*

Given an array `arr[]`, replace each element with the product of itself and its adjacent elements.

For index `i` :
- `arr[i] = arr[i-1] * arr[i] * arr[i+1]`
- Assume the previous of the first and the next of the last as `1`.

**Examples:**

- Input: `arr[] = [2, 4, 5]` → Output: `[8, 40, 20]`
```
  i = 0 : arr[0] = 1 * 2 * 4 = 8
  i = 1 : arr[1] = 2 * 4 * 5 = 40
  i = 2 : arr[2] = 4 * 5 * 1 = 20
```

- Input: `arr[] = [2, 5, 7, 8, 3]` → Output: `[10, 70, 280, 168, 24]`
```
  i = 0 : arr[0] = 1 * 2 * 5 = 10
  i = 1 : arr[1] = 2 * 5 * 7 = 70
  i = 2 : arr[2] = 5 * 7 * 8 = 280
  i = 3 : arr[3] = 7 * 8 * 3 = 168
  i = 4 : arr[4] = 8 * 3 * 1 = 24
```

---

## [Naive Approach] Using Auxiliary Array — O(n) Time and O(n) Space

Use a temporary array to store the updated values, avoiding loss of original values while computing the product for each element. After processing all elements, copy the temporary array back to the original.

```python
def updateArray(arr):
    n = len(arr)

    # Temporary array to store updated values
    temp = [0] * n

    for i in range(n):

        # Previous adjacent element
        prev = 1 if i == 0 else arr[i - 1]

        # Next adjacent element
        next_ele = 1 if i == n - 1 else arr[i + 1]

        # Store product of previous, current and next element
        temp[i] = prev * arr[i] * next_ele

    # Copy updated values back to original array
    for i in range(n):
        arr[i] = temp[i]


arr = [2, 4, 5]
updateArray(arr)
print(*arr)
```

**Output:**

![Adjacent multiplication naive approach output in terminal](adjacent-multiplication-naive-output.png)

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## [Expected Approach] In-Place using Previous Tracking — O(n) Time and O(1) Space

Update the array in-place while keeping track of the previous original element using a variable `prev`.

**Working of approach:**

- Start with `prev = 1`
- For each index `i`, store the original value before updating it
- Use the next original value directly from the array
- Replace `arr[i]` with `prev * arr[i] * next`
- Update `prev` with the original current value

**Example for `arr[] = [2, 4, 5]` :**
```
Start with prev = 1
i = 0 : arr[0] = 1 * 2 * 4 = 8,  prev = 2
i = 1 : arr[1] = 2 * 4 * 5 = 40, prev = 4
i = 2 : arr[2] = 4 * 5 * 1 = 20, prev = 5
Final array = [8, 40, 20]
```

```python
def updateArray(arr):
    n = len(arr)

    # Stores previous original element
    prev = 1

    for i in range(n):

        # Store current original value before updating
        curr = arr[i]

        # Get next adjacent element
        next_ele = 1 if i == n - 1 else arr[i + 1]

        # Update current element
        arr[i] = prev * curr * next_ele

        # Update prev with original current value
        prev = curr


arr = [2, 4, 5]
updateArray(arr)
print(*arr)
```

**Output:**

![Adjacent multiplication expected approach output in terminal](adjacent-multiplication-expected-output.png)

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)