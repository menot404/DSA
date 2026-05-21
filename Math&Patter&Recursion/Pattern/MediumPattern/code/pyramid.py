
#_______________________________________________
#
#   Medium Pattern --- Printing Pyramid Patterns
#________________________________________________


"""
#  Time Complexity: O(n2)
# Space complexity: O(1)

"
The idea is to use two nested loops. The outer loop is used to track the rows, while the inner loops are used to print the required spaces and stars for each row.
"
"""

def pyramid(n):

    # Outer loop to handle number of rows
    for i in range(1, n + 1):

        # printing spaces
        print(" "*(n - i), end="")
        # printing stars
        print("*" * ( 2 * i - 1))

# Drive code
if __name__ == '__main__':
    n = 5
    if n > 1:
        pyramid(n=n)