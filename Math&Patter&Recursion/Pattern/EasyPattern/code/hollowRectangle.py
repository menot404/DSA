#__________________________________________________________________
#
#   Easy Pattern --- Print Hollow Rectangle or Square Star Pattern
#__________________________________________________________________

def hollowRectangle(rows, columns):

    # Loop through each row
    for i in range(1, rows + 1):

        # Loop through each column is the current rows
        for j in range(1, columns + 1):
            # Print start if it is the first or last row or column
            if i == 1 or i == rows or j == 1 or j == columns:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()


# Driver code
def main():
    n = 6
    m = 20
    hollowRectangle(rows = n, columns = m)

# Driver code
if __name__ == "__main__":
    main()


# Using Nested Loops – O(n*m) Time and O(1) Space