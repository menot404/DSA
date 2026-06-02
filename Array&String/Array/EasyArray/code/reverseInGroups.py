#___________________________________________
#
#   EASY ARRAY - Reverse an Array in groups
#___________________________________________

"""
# Fixed-Size Group Reversal–Time O(n) and Space O(1)
    Edge Cases:

        ==> When k = 1, the array stays the same
        ==> When k is greater than or equal to the array size
    Approach

        ==> We begin from index 0 and find the size of the current subarray to be reversed. If the number of remaining elements at the end is less than k, reverse all of them.
        ==> Each subarray is reversed using two pointers that start from the two corners of the subarray.
    # O(n) Complexity Time
    # O(1) Complexity Space
"""
def reverseInGroups(arr, K):
    n = len(arr)
    i = 0

    while i < n:
        left = i
        # Find the end index of the current subarray
        right = min(i + K - 1, n - 1)

        # Reverse the sub-array [left, right]
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        i += K

# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    K = 5
    print(f"Original array: {arr}")
    reverseInGroups(arr, K)
    print(f"Reversed array in groups of {K}: ", end="")
    print(" ".join(map(str, arr)))
