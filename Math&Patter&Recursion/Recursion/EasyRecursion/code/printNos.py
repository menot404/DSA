
#____________________________________
#
#   Easy Recursion:  --- Print 1 to N
#_____________________________________

def printNos(n):
    # Base case
    if n == 0:
        return
    
    # Recursive call with n-1
    printNos(n - 1)

    # Print the current number after the recursive call
    print(n, end=" ")
    nosArr.append(n)

# Driver code
if __name__ == "__main__":
    nosArr = []
    n = 5
    print(f"The numbers from 1 to {n} are: ", end="")
    printNos(n)
    print(f"\nThe numbers stored in the array are: {nosArr}")
    print()


"""
# Time Complexity: O(n)
# Auxiliary Space: O(n)
"""