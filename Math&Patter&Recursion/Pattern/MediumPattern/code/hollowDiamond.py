#_____________________________________________
#
#   Medium Pattern --- Hollow Diamond Pattern
#_____________________________________________


"""
#  Time Complexity: O(n2)
# Space complexity: O(1)

"

==> Iterate through 2 × n − 1 rows to form the upper and lower parts of the pattern, and compute a variable (comp) to control the spacing for each row.
==> Print leading spaces using an inner loop so that the stars shift toward the center and form the desired shape.
==> Use another inner loop to print stars at the first and last positions of the row and spaces in between, creating a hollow pattern.

"
"""

def hollowDiamond(n):

    # Outer loop for rows
    for i in range(2 * n - 1):
        comp = 2 * (n - i) - 1 if i < n else 2 * (i - n + 1) + 1

        # Print leading spaces
        for j in range(comp):
            print(" ", end="")

        # Print stars and inner spaces
        for k in range(2 * n - comp):
            if k == 0 or k == 2 * n - comp - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


# Driver Code
if __name__ == "__main__":
    n = 5
    hollowDiamond(n)