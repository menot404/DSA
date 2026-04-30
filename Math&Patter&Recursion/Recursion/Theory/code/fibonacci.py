#___________________________________________
#
#   Introduction to Recursion -- Fibonacci
#___________________________________________

"""
The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0, and 1.

arguments : n : the position in the Fibonacci sequence to return
return : the value of the Fibonacci sequence at position n

# Mathematical Equation:  

n if n == 0, n == 1;      
fib(n) = fib(n-1) + fib(n-2) otherwise;

# Recurrence Relation: 

T(n) = T(n-1) + T(n-2) + O(1)
"""

def fib(n):
    # Stop condition
    if n == 0:
        return 0
    # Stop condition
    if n == 1:
        return 1
    # Recursion function call
    else:
        return (fib(n-1) + fib(n-2))
    
#Driver code

if __name__ == "__main__":
    n = 5
    print("Fibonacci number at position", n, "is", fib(n))

    #for loop to print Fibonacci sequence up to n
    print("Fibonacci sequence up to position", n, "is: ", end = '')
    for i in range(0, n):
        print(fib(i), end = ' ')
    print()
