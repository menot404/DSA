#______________________________
#
#   EASY ARRAY - Array Reverse
#______________________________

# Method 1: Using a temporary array
"""
The idea is to use a temporary array to store the reverse of the array.

Create a temporary array of same size as the original array. 
Now, copy all elements from original array to the temporary array in reverse order.
Finally, copy all the elements from temporary array back to the original array.

    # O(n) Complexity Time
    # O(1) Complexity Space
"""

def reverseArrayTemp(arr):
    n = len(arr)
    # Temporary array to store elements
    # in reversed order
    temp = [0]*n
    
    # Copy elements from original array
    # To temp in reverse order
    for i in range(n):
        temp[i] = arr[n - i - 1]
    
    for i in range(n):
        arr[i] = temp[i]


# Driver Code
if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    print(f"Original array: {arr}")
    reverseArrayTemp(arr)
    print("[Naive Approach] Using a temporary array - Array Reverse: ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()