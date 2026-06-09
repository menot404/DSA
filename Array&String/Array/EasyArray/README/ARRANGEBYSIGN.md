# Rearrange Array by Sign
*Source: GeeksforGeeks — Last Updated: 3 Apr, 2026*

Given an array `arr[]` of size `n`, rearrange it in **alternate positive and negative** manner without changing the relative order of positive and negative numbers. Extra positive/negative numbers appear at the end.

> **Note:** The rearranged array should start with a positive number. `0` (zero) is considered a positive number.

**Examples:**
- Input: `arr[] = [1, 2, 3, -4, -1, 4]` → Output: `arr[] = [1, -4, 2, -1, 3, 4]`
- Input: `arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]` → Output: `arr[] = [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]`

---

## Approach

Separate the numbers into positive and negative arrays, then alternately place numbers from each array back into the original array. Place any remaining elements at the end.

**Working example for `arr = [1, 2, 3, -4, -1, 4]` :**

1. Separate into: `pos[] = [1, 2, 3, 4]`, `neg[] = [-4, -1]`
2. Alternately fill back into `arr[]`:
```
   i = 0 (even) → pick from pos : arr = [1,  _,  _,  _,  _, _]
   i = 1 (odd)  → pick from neg : arr = [1, -4,  _,  _,  _, _]
   i = 2 (even) → pick from pos : arr = [1, -4,  2,  _,  _, _]
   i = 3 (odd)  → pick from neg : arr = [1, -4,  2, -1,  _, _]
```
3. `neg[]` exhausted — append remaining `pos[] = [3, 4]`:
```
   Final arr[] = [1, -4, 2, -1, 3, 4]
```

---

```python
# Rearrange positive and negative numbers alternately

def rearrange(arr):
    pos = []
    neg = []

    # Separate positive and negative numbers
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    posIdx = 0
    negIdx = 0
    i = 0

    # Place positive and negative numbers alternately
    while posIdx < len(pos) and negIdx < len(neg):
        if i % 2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        i += 1

    # Append remaining positive numbers (if any)
    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1

    # Append remaining negative numbers (if any)
    while negIdx < len(neg):
        arr[i] = neg[negIdx]
        negIdx += 1
        i += 1

if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]
    rearrange(arr)
    print(' '.join(map(str, arr)))
```

**Output:**
```
1 -4 2 -1 3 4
```

- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)