# Generating All Subarrays
*Source: GeeksforGeeks — Last Updated: 7 Feb, 2025*

Given an array `arr[]`, generate all possible subarrays.

**Examples:**
- Input: `arr[] = [1, 2, 3]` → Output: `[ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]`
- Input: `arr[] = [1, 2]` → Output: `[ [1], [1, 2], [2] ]`

---

## Iterative Approach

To generate a subarray, we need a starting index. For each starting index `i` (from `0` to `n-1`), we select an ending index from `[i to n-1]`. An innermost loop then prints the elements of each subarray.

- **Outermost loop:** picks the starting index of the current subarray.
- **Middle loop:** picks the ending index of the current subarray.
- **Innermost loop:** prints the subarray from starting to ending index.

```python
# Prints all subarrays in arr[0..n-1]
def sub_array(arr):
    n = len(arr)

    # Pick starting point
    for i in range(n):
        # Pick ending point
        for j in range(i, n):
            # Print subarray between current starting and ending points
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()  # New line after each subarray

# Driver code
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
sub_array(arr)
```

**Output:**
```
All Non-empty Subarrays:
1
1 2
1 2 3
1 2 3 4
2
2 3
2 3 4
3
3 4
4
```

---

## Recursive Approach

We use two pointers `start` and `end` to maintain the starting and ending point of the array:

1. Stop if we have reached the end of the array.
2. Increment the end index if `start` has become greater than `end`.
3. Print the subarray from index `start` to `end` and increment the starting index.

```python
# Recursive function to print all possible subarrays for given array
def printSubArrays(arr, start, end):

    # Stop if we have reached the end of the array
    if end == len(arr):
        return

    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)

    # Print the subarray and increment the starting point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)

# Driver code
arr = [1, 2, 3]
printSubArrays(arr, 0, 0)
```

**Output:**
```
[1]
[1, 2]
[2]
[1, 2, 3]
[2, 3]
[3]
```