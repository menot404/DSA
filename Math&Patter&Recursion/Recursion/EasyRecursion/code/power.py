
#___________________________________________________________________
#
#   Easy Recursion:  --- Power Function Implementation
#___________________________________________________________________

## Method 1: Using Iteration
"""
#  Time Complexity: O(e)
# Space complexity: O(1)

" The idea is to simply multiply b exactly e times using a iterative loop. "
"""
def powerIterative(b, e):

    # Initialize result to 1
    pow = 1

    # Multiply b for e times and store the result
    for i in range(abs(e)):
        pow *= b
    
    # If e is negative, return the reciprocal of the resultat
    if e < 0:
        return 1 / pow
    return pow



# Driver code
if __name__ == "__main__":
    b = 3.0
    e = 5
    pow = powerIterative(b, e)
    print(f"Using Iteration - {b} raised to the power {e} is: {pow}")