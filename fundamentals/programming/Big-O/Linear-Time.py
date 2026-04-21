
#____________________________________
#
#   Linear Time Complexity: Big O(n) Complexity
#_____________________________________

"""
Linear time complexity means that the running time of an algorithm grows linearly with the size of the input.
For example, consider an algorithm that traverses through an array to find a specific element:
"""

"""
Searches for a specific key in an array.
Arguments:
----------
arr : list
    The input array in which to search for the key.
n : int
    The size of the input array.
key : int
    The element to search for in the array.
Returns:
--------
tuple
    A tuple containing the index and value of the found element, or -1 if the element
"""
def find_element(arr, n, key):
    for i in range(0, n):
        if(arr[i] == key):
            return i, arr[i]
    return -1

# Example usage
arr = [1, 2, 3, 4, 5]
key = 3
n = len(arr)
result = find_element(arr, n, key)
if result != -1:
    print(f"Element found at index: {result[0]}, value: {result[1]}")
else:    print("Element not found in the array.")




