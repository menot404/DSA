
#____________________________________
#
#   CIntroduction to Recursion -- Sum
#_____________________________________

def sum(n):
    # Base condition case : when n is 1, return 1
    if n == 1 :
        return 1
    
    return n + sum(n - 1)

# driver code
if __name__ == "__main__":
    n = 5
    print("Sum of first", n, "natural numbers is", sum(n))
