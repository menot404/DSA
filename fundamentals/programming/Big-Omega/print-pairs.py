#____________________________________
#
#   Example of Big-Omega Ω Notation
#_____________________________________

"""
Consider an example to print all the possible pairs of an array. The idea is to run two nested loops to generate all the possible pairs of the given array:

# The time complexity of this algorithm is O(n^2) because we have two nested loops, each running n times. However, we can also say that the time complexity is Ω(n^2) because in the worst case, we will have to print all the pairs, which takes n^2 time.
"""

"""
Prints all pairs of an array.
Arguments:
----------
arr : list
    The input array for which to print pairs.
n : int
    The size of the input array.
Returns:
--------
None
    This function does not return anything. It prints all pairs of the input array to the console
"""

def printPairs(arr, n):
    for i in range(n):
        for j in range(n):
            if i != j:
                print(arr[i], arr[j])

# Example usage

if __name__ == "__main__":
    arr = [2, 6, 1]
    n = len(arr)
    printPairs(arr, n)