
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

import math


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


## Method 3: Modified Euclidean Algorithm using Subtraction by Checking Divisibility
"""
#  Time Complexity: O(min(a, b))
# Space complexity: O(min(a, b))

"
Consider a = 98 and b = 56

a = 98, b = 56:

a > b so put a = a-b and b remains same. So  a = 98-56 = 42  & b= 56. 
a = 42, b = 56:

Since b > a, we check if b%a=0. Since answer is no, we proceed further. 
Now b>a. So b = b-a and a remains same. So b = 56-42 = 14 & a= 42. 
a = 42, b = 14:

Since a>b, we check if a%b=0. Now the answer is yes. 
So we print smaller among a and b as H.C.F . i.e. 42 is  3 times of 14.
So HCF is 14.
"
"""

def gcdSubChDiv(a, b):
    # Everyting divides 0
    if (a == 0 or b == 0):
        return max(a, b)
    
    # Base case
    if b == a :
        return a
    
    # a is greater than b
    if a > b:
        if a % b == 0:
            return b
        return gcdSubChDiv(a - b, b)

    # b is greater than a
    if b > a:
        if b % a == 0:
            return a
        return gcdSubChDiv(a , b - a)


## Method 4: Optimized Euclidean Algorithm by Checking Remainder
"""
#  Time Complexity: O(log(min(a,b)))
# Space complexity: O(log(min(a,b)))

"
Instead of the Euclidean algorithm by subtraction, a better approach can be used. We don't perform subtraction here. 
we continuously divide the bigger number by the smaller number. More can be learned about this efficient solution by using the modulo operator in Euclidean algorithm.

# Time Complexity: O(log(min(a,b)))

Each recursive call reduces the size of the numbers significantly using the modulo operation (a % b), which shrinks the input faster than subtraction.
The worst-case scenario for the number of steps occurs when the inputs are consecutive Fibonacci numbers, like (21, 13), which maximizes the number of recursive calls.
Since Fibonacci numbers grow exponentially, and the number of steps increases linearly with their position, the time complexity becomes logarithmic in terms of the smaller number — O(log(min(a, b))).

# Auxiliary Space: O(log(min(a,b)))
The maximum number of recursive calls is proportional to the number of steps taken to reduce the input to zero, which is O(log(min(a, b))) in the worst case.
"
"""

def gcdOptimized(a, b):
    # Everything divides 0
    if (a == 0 or b == 0):
        return max(a, b)
    
    # Base case
    if a == b:
        return a
    
    # Recursive call for a % b and b % a returns the GCD of a % b and b % a, which is then returned as the GCD of a and b
    if a > b:
        return gcdOptimized(a % b, b)
    return gcdOptimized(a, b % a)

import math

def gcdOptimized1(a, b):
    return math.gcd(a, b)


# Driver code
if __name__ == "__main__":
    a = 0
    b = 12
    print(f"Using Iterative Method - The GCD of {a} and {b} is: {gcdIterative(a, b)}")
    print(f"Euclidean Algorithm using Subtraction - The GCD of 20 and 28 is: {gcdSubstraction(a=20, b=28)}")
    print(f"Modified Euclidean Algorithm using Subtraction by Checking Divisibility - The GCD of 92 and 36 is: {gcdSubChDiv(a=92, b=36)}")
    print(f"Optimized Euclidean Algorithm by Checking Remainder - The GCD of 48 and 18 is: {gcdOptimized(a=20, b=28)}")
    print(f"Optimized Euclidean Algorithm using math.gcd - The GCD of 48 and 18 is: {gcdOptimized1(a=48, b=18)}")