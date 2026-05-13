# Print Solid Rectangle Star Pattern
*Source: GeeksforGeeks — Last Updated: 13 Mar, 2026*

Given two integers `n` and `m`, print a solid rectangle pattern of stars with `n` rows and `m` columns. Each row has exactly `m` stars.

**Examples:**

- Input: `n = 3, m = 5`
```
* * * * *
* * * * *
* * * * *
```

- Input: `n = 4, m = 2`
```
* *
* *
* *
* *
```

---

## Using Nested Loops — O(n×m) Time and O(1) Space

The pattern is printed using two nested loops. The outer loop runs once for each row, while the inner loop runs for each column in that row, printing a star. After printing all stars in a row, a newline is added to move to the next row.

```python
def main():
    # Number of rows and columns
    n, m = 3, 5

    # Loop through each row
    for i in range(1, n + 1):

        # Loop through each column in the current row
        for j in range(1, m + 1):
            # Print a star
            print("*", end=" ")

        # Move to the next row
        print()

if __name__ == "__main__":
    main()
```

**Output:**
```
* * * * * 
* * * * * 
* * * * * 
```