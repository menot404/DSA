# __________________________________________________________
#
#    Factorial Time Complexity: Big O(n!) Complexity
# ___________________________________________________________

"""
Factorial time complexity means that the running time of an algorithm grows factorially with the size of the input. This is often seen in algorithms that generate all permutations of a set of data.
# Here’s an example of a factorial time complexity algorithm, which generates all permutations of an array:
"""

"""
Generates all permutations of a given array.

Arguments:
----------
arr : list
    The input array for which permutations are to be generated.
l : int
    The starting index for the permutation.
r : int
    The ending index for the permutation.

returns:
--------
None
    This function prints all permutations of the input array to the console.
    
Complexity:
-----------
Time: O(n!), because there are n! permutations of n distinct elements.
Space: O(n), due to the recursive call stack and the space used for storing the current
"""
def permute(arr, l, r):
    if l==r :
        for i in range(r+1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]  # Swap
            permute(arr, l+1, r)  # Recurse
            arr[l], arr[i] = arr[i], arr[l]  # Backtrack

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3]
    n = len(arr)
    print(f"All permutations of {arr}:")
    permute(arr, 0, n-1)