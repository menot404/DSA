# ____________________________________
#
#    Logarithmic Time Complexity: Big O(log n) Complexity
# _____________________________________

"""
Logarithmic time complexity means that the running time of an algorithm is proportional to the logarithm of the input size.
# For example, a binary search algorithm has a logarithmic time complexity
"""


"""
arr: sorted array of size n
l: left index of the array
r: right index of the array
x: the element we want to find
mid: the middle index of the array
"""
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        return binary_search(arr, mid + 1, r, x)
    else:
        return -1


# Example usage
arr = [2, 4, 6, 8, 10, 20, 19]
x = 8
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"Element found at index: {result}, value: {arr[result]}")
else:
    print("Element not found in the array.")
