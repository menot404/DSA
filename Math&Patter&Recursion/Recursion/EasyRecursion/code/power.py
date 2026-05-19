
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



## Method 3: Using Divide and Conquer
"""
#  Time Complexity: O(log e)
# Space complexity: O(log e)

"
The idea is to use Divide and Conquer and recursively bisect e in two equal parts. There are two possible cases:

    ==> If e is even: power(b, e) = power(b, e / 2) * power(b, e / 2); 
    ==> If e is odd: power(b, e) = b * power(b, e / 2) * power(b, e / 2); 
"
"""
def powerDivideAndConquer(b, e):

    # Base Case: powerDivideAndConquer(e, 0)
    if e == 0:
        return 1
    
    # If e is negative, return the reciprocal of the result rule: b^(-e) = 1 / b^e
    if e < 0:
        return 1 / powerDivideAndConquer(b, -e)
    
    # Recursively calculate power for half the exponent
    temp = powerDivideAndConquer(b, e // 2)

    # If exponent is even: b^e = (b^(e/2))^2
    if e % 2 == 0:
        return temp * temp
    else:
        # If exponent is odd: b^e = b * (b^(e/2))^2
        return b * temp * temp

# Driver code
if __name__ == "__main__":
    b = 3.0
    e = 5
    pow1 = powerIterative(b, e)
    print(f"Using Iteration - {b} raised to the power {e} is: {pow1}")
    pow2 = powerRecursive(b, e)
    print(f"Using Recursion - {b} raised to the power {e} is: {pow2}")
    pow3 = powerDivideAndConquer(b, e)
    print(f"Using Divide and Conquer - {b} raised to the power {e} is: {pow3}")