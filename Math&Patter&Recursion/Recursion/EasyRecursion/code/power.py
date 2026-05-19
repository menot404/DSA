
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


## Method 2: Using Recursion
"""
#  Time Complexity: O(e)
# Space complexity: O(e)

" The idea is to recursively multiply b exactly e times. To do so, define a recursive function that return b, if e > 0 else returns 1."
"""
def powerRecursive(b, e):
    # Base Case: powerRecursive(e, 0)
    if e == 0: 
        return 1
    
    # If e is negative, return the reciprocal of the result of powerRecursive(b, -e)
    if e < 0:
        return 1 / powerRecursive(b, -e)
    
    return b * powerRecursive(b, e - 1) # Recursive call for e - 1 returns the result of b raised to the power of e - 1, which is then multiplied by b to get the final result of b raised to the power of e.

# Driver code
if __name__ == "__main__":
    b = 3.0
    e = 5
    pow1 = powerIterative(b, e)
    print(f"Using Iteration - {b} raised to the power {e} is: {pow1}")
    pow2 = powerRecursive(b, e)
    print(f"Using Recursion - {b} raised to the power {e} is: {pow2}")