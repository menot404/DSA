# Program to Print Floyd's Triangle
*Source: GeeksforGeeks — Last Updated: 11 Mar, 2026*

Given an integer `n`, print Floyd's Triangle with `n` rows. Floyd's Triangle is a right-angled triangular pattern formed using **consecutive natural numbers** starting from 1.

**Example:**

- Input: `6`
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
```

---

## Using Nested Loops — O(n²) Time and O(1) Space

The pattern is printed using two nested loops. The outer loop controls the number of rows, while the inner loop prints the numbers in each row. A variable `val` keeps track of the current number, incremented after each print so that numbers appear in increasing order across the triangle.

**Step-wise approach:**

1. Initialize `val = 1` to store the current number to print.
2. Run an outer loop from `1` to `n` to iterate through the rows.
3. For each row `i`, run an inner loop from `1` to `i`.
4. Print the current value of `val`.
5. Increment `val` after printing each number.
6. After completing each row, move to the next line.

```python
def printfloydtriangle(n):
    val = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(val, end=" ")
            val += 1
        print()
```

**Output:**
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
```