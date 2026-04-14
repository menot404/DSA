#____________________________________
#
#   Functions in programming
#_____________________________________

"""
A function is a block of code that performs a specific task and can be reused whenever needed.

    ==> Avoids writing the same code again and again.
    ==> Makes programs simple and easy to understand by breaking into smaller parts.
    ===> Accepts input (parameters) and gives output.
    ==> Finding and fixing errors become easier.
"""

"""
# Built-in functions
    # ===> These predefined functions provided by programming languages or libraries to perform common tasks such as mathematical calculations, input/output, or string operations.

"""
s = "math"
m = __import__(s)

print(m.sqrt(16))  # Output: 4.0

# Also
from math import sqrt
resultat = sqrt(32) # Output 5.656854249492381
print(f"Square Root: {resultat}")


"""
# User-defined
    # ===> These functions are functions written by programmers to perform specific tasks required in a program.
    # ===> They help organize code and allow reuse of logic whenever needed.
"""

def greet():
    print("Hello, world!")

greet() # calling user-defined function

def add(a, b):
    result = a + b
    return result

print(f"Sum a + b: {add(16, 19)}")

###################################################
## Where are Functions Used in DSA?
###################################################

"""
# In DSA, functions are used to implement algorithms and solve problems in a structured and reusable way.

    # ===> Implement algorithms like searching and sorting.
    # ===> Handle recursion (like factorial, tree traversal).
    # ===> Break problems into smaller subproblems.
    # ===> Operate on data structures like arrays, linked lists, trees, and graphs.
    # ===> Make code clean and easy to understand.

"""