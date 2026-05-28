#_____________________________________________
#
#   EASY ARRAY - Check if an Array is Sorted
#_____________________________________________

# Method 1: Iterative approach
"""
    We traverse from the second element. For every element we check if it is smaller than or equal to previous element or not. At any point if we find previous element greater, we return false.
    # O(n) Time
    # O(1) Space
"""
def isSortedIterative(arr):

    # Get the length of the array
    n = len(arr)

    # Iterate over the array and check if
    # every element is greater than or
    # equal to the previous element
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            return False
        return True


# Method 2: Recursive approach
"""
The idea is to check if the last two elements are in order, then recursively check the rest of the array. The base case is when the array has zero or one element, which is always considered sorted.
    # O(n) Time
    # O(n) Space
"""
def isSortedHelper(arr, n):

    # Base case: An array of size 0 or 1 is always sorted
    if n == 0 or n == 1:
        return True
    
    # Check if current and previous elements are in order
    # and recursively check the rest of the array
    return arr[n - 1] >= arr[n - 2] and isSortedHelper(arr, n - 1)

def isSortedRecursive(arr):
    n = len(arr)
    return isSortedHelper(arr, n)


# Driver Code
if __name__ == "__main__":
    arr = [8, 10, 12, 14, 16]

    # Check if the array is sorted using iterative approach
    if isSortedIterative(arr):
        print("Method 1: Iterative approach - The array is sorted.")
    else:
        print("Method 1: Iterative approach - The array is not sorted.")

    # Check if the array is sorted using recursive approach
    if isSortedRecursive(arr):
        print("Method 2: Recursive approach - The array is sorted.")
    else:
        print("Method 2: Recursive approach - The array is not sorted.")