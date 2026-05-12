
#_________________________________________________________
#
#   Easy Pattern --- Print Solid Rectangle Star Pattern
#__________________________________________________________

def solidRectangle(n, m):

    # Loop through each row
    for i in range(1, n + 1):

        # Loop through each column in the current row
        for j in range(1, m + 1):
            print("*", end = " ")
        print()

# Driver code
if __name__ == "__main__":
    # Number of rows and columns
    n = 4
    m = 5
    print(f"Solid Rectangle Star Pattern of {n} rows and {m} columns:")
    solidRectangle(n = n, m = m)


# Using Nested Loops – O(n*m) Time and O(1) Space