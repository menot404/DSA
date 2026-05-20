
#_________________________________________________________________
#
#   Easy Maths --- Express a number as sum of consecutive numbers
#__________________________________________________________________


## Method 1 [Naive Approach]: Checking All Consecutive Sums
"""
#  Time Complexity: O(n2)
# Space complexity: O(1)

"
The idea is to start from every number and keep adding consecutive numbers until the sum becomes equal to or greater than n. If the sum becomes equal to n, return "true".
"
"""
def isSumOfConsecutive1(n):

    # Try every starting number
    for i in range(1, n):
        sum = 0

        # Generate consecutive sum
        for j in range(i, n):
            sum += j
            # If sum is equal to n, return true
            # and at least two numbers are used
            if sum == n and j > i:
                return True
            # If sum exceeds n, break the inner loop
            if sum > n:
                break
        return False




# Driver Code
if __name__ == "__main__":
    n = 8
    if isSumOfConsecutive1(n = n):
        print(f"{n} can be expressed as the sum of two or more consecutive numbers.")
    else:
        print(f"{n} cannot be expressed as the sum of two or more consecutive numbers.")