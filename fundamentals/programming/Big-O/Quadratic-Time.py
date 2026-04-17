
#____________________________________
#
#   Quadratic Time Complexity: Big O(n2) Complexity
#_____________________________________

"""
Quadratic time complexity means that the running time of an algorithm is proportional to the square of the input size.
# For example, a simple bubble sort algorithm has a quadratic time complexity:
"""

"""
arr: array of size n
n: the size of the array
"""
def bubble_sort(arr, n):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
bubble_sort(arr, n)
print("Sorted array is:", arr)