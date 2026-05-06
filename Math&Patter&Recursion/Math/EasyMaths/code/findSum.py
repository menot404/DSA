
#_________________________________________________________
#
#   Easy Maths --- Program for sum of n natural numbers
#__________________________________________________________


### Method 1: [Naive Approach] Using Loop - O(n) Time and O(1) Space
def findSum1(n):
    sum = 0
    i = 1

    # Iterating over all the numbers between 1 to n
    while i <= n:
        sum += i
        i += 1

    return sum


### Method 2: [Alternative Approach] Using Recursion -O(n) and O(n) Space
def findSum2(n):
    # Base case
    if n == 1:
        return 1
    
    # Recursive case
    return n + findSum2(n - 1)


if __name__ == "__main__":
    n = 10
    print(f"The sum of first {n} natural numbers is: {findSum1(n = n)}")
    print(f"The sum of first {n} natural numbers is: {findSum2(n = 5)}")