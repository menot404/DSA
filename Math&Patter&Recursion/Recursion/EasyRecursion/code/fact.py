
#______________________________________________
#
#   Easy Recursion:  --- Factorial of a Number
#______________________________________________

## Method 1: Iterative Solution - O(n) Time and O(1) Space
def fact(n):
    ans = 1
    i = 2
    if n == 0 or n == 1:
        return ans
    while i <= n:
        ans *= i
        i += 1
    return ans
"""
    # Time Complexity: O(n)
    # Space Complexity: O(1)
"""

## Method 1: Recursive Solution - O(n) Time and O(n) Space
def factRecursive(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive call for n - 1 returns the fact of n - 1, which is then multiplied by n to get the fact of n
    return n * factRecursive(n-1)
"""
    # Time Complexity: O(n)
    # Space Complexity: O(n)
"""


# Driver code
if __name__ == "__main__":
    n = 5
    print(f"The factorial of {n} is: {fact(n)}")
    print(f"The factorial of {n} is: {factRecursive(n)}")
    print()
