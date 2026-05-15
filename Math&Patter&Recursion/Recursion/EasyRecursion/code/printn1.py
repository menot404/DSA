
#_____________________________________
#
#   Easy Recursion:  --- Print N to 1
#_____________________________________

def printn1(n):
    # Base case
    if n == 0:
        return
    
    # Print the current number before the recursive call
    print(n, end=" ")
    printn1(n - 1)

# Driver code
if __name__ == "__main__":
    n = 5
    print(f"The numbers from {n} to 1 are: ", end="")
    printn1(n)
    print()


"""
# Time Complexity: O(n)
# Auxiliary Space: O(n), Recursive Stack Space
"""