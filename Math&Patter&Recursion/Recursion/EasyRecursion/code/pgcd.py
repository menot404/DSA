
#___________________________________________________________________
#
#   Easy Recursion:  --- Program to Find GCD or HCF of Two Numbers
#___________________________________________________________________

## Method 1: Using Loop
"""
#  Time Complexity: O(min(a, b))
# Space complexity: O(1)

" The idea is to find the minimum of the two numbers and find its highest factor which is also a factor of the other number. "
"""

def gcdIterative(a, b):

    # Everything divides O
    if(a == 0 or b == 0):
        return max(a, b)

    # Fing Minimum of  a and b
    min_num = min(a, b)

    while min_num > 0:
        if(a % min_num == 0 and b % min_num == 0):
            break
        min_num -= 1

    return min_num

## Method 2: Euclidean Algorithm using Subtraction
"""
#  Time Complexity: O(min(a, b))
# Space complexity: O(min(a, b))

" The idea of this algorithm is, the GCD of two numbers doesn't change if the smaller number is subtracted from the bigger number.
  This is the Euclidean algorithm by subtraction. It is a process of repeat subtraction, carrying the result forward each time until the result is equal to any one number being subtracted.
"
"""

def gcdSubstraction(a, b):

    # Everything divides 0
    if(a == 0 or b == 0):
        return max(a, b)
    
    # Base case
    if a == b:
        return a
    
    # Recursive call for a - b and b - a returns the GCD of a - b and b - a, which is then returned as the GCD of a and b
    if a > b:
        return gcdSubstraction(a - b, b)
    return gcdSubstraction(a, b - a)



# Driver code
if __name__ == "__main__":
    a = 0
    b = 12
    print(f"Using Iterative Method - The GCD of {a} and {b} is: {gcdIterative(a, b)}")
    print(f"Euclidean Algorithm using Subtraction - The GCD of {a} and {b} is: {gcdSubstraction(a=20, b=28)}")