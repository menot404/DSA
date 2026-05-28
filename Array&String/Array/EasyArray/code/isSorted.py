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
def isSorted(arr):

    # Get the length of the array
    n = len(arr)

    # Iterate over the array and check if
    # every element is greater than or
    # equal to the previous element
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            return False
        return True
    
# Driver Code
if __name__ == "__main__":
    arr = [8, 10, 12, 14, 16]
    if isSorted(arr):
        print("The array is sorted.")
    else:
        print("The array is not sorted.")