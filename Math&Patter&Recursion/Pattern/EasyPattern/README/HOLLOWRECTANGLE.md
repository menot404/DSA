# Print Hollow Rectangle or Square Star Pattern
*Source: GeeksforGeeks — Last Updated: 2 May, 2026*

Given two integers `n` and `m`, print a hollow rectangle star pattern of `n` rows and `m` columns. Stars (`*`) are printed on the **boundary** of the rectangle, while the inner area contains spaces.

**Example:**

- Input: `n = 6, m = 20`
```
********************
*                  *
*                  *
*                  *
*                  *
********************
```

---

## Using Nested Loops — O(m×n) Time and O(1) Space

The pattern is printed using two nested loops. The outer loop iterates through the rows and the inner loop through the columns. A star `*` is printed when the current position is on the **first row**, **last row**, **first column**, or **last column** — otherwise a space is printed.

```python
def print_rectangle(rows, columns):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):

            # Print star at boundary positions
            if i == 1 or i == rows or j == 1 or j == columns:
                print("*", end="")
            else:
                print(" ", end="")

        # Move to the next line
        print()

def main():
    rows = 6
    columns = 20
    print_rectangle(rows, columns)


if __name__ == "__main__":
    main()

```