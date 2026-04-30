#___________________________________________
#
#   Introduction to Recursion -- Factorial
#___________________________________________

def fact(n):
    # Base condition case: when n is 0, return 1

    if n == 0:
        return 1
    
    return n*fact(n - 1)

# driver code
if __name__ == "__main__":
    n = 5
    print("Factorial of", n, "is", fact(n))