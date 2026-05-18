
#___________________________________________________________________
#
#   Easy Recursion:  --- Program to Find GCD or HCF of Two Numbers
#___________________________________________________________________

## Method 1: Utilisation d'une boucle:
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




# Driver code
if __name__ == "__main__":
    a = 15
    b = 12
    print(f"The GCD of {a} and {b} is: {gcdIterative(a, b)}")