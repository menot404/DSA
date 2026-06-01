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
    # O(n) Complexity Space
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


# Method 2: Using Two Pointers
"""
The idea is to maintain two pointers: left and right, such that left points at the beginning of the array and right points to the end of the array.
While left pointer is less than the right pointer, swap the elements at these two positions. After each swap, increment the left pointer and decrement the right pointer to move towards the center of array. This will swap all the elements in the first half with their corresponding element in the second half.
    # O(n) Complexity Time
    # O(1) Complexity Space
"""
def reverseArray2Pointers(arr):
    n = len(arr)

    # Initialize left to the beginning
    # and right to the end of the array
    left = 0
    right = n - 1

    # Iterate till left is less than right
    while left < right :

        # Swap the elements at left
        # and right position
        arr[left], arr[right] = arr[right], arr[left]

        # Increment left pointer
        left += 1
        # Decrement right pointer
        right -= 1



# Method 3: Using Single Pointer
"""
The idea is to iterate over the first half of the array and swap each element with its corresponding element from the end. 
So, while iterating over the first half, any element at index i is swapped with the element at index (n - i - 1).

    # O(n) Complexity Time
    # O(1) Complexity Space
"""
def reverseArraySinglePointer(arr3):
    # Size Array
    n = len(arr3)
    
    # Iterate over the first half
    # and for every index i, swap
    # arr[i] with arr[n - i - 1]
    for i in range(n // 2):
        temp = arr3[i]
        arr3[i] = arr3[n - i - 1]
        arr3[n - i - 1] = temp

# Driver Code
if __name__ == "__main__":

    # Method 1: Using a temporary array
    arr1 = [1, 4, 3, 2, 6, 5]
    print(f"Original array: {arr1}")
    reverseArrayTemp(arr1)
    print("[Naive Approach] Using a temporary array - Array Reverse: ", end="")
    for i in range(len(arr1)):
        print(arr1[i], end=" ")
    print("\n")

    # Method 2: Using Two Pointers
    arr2 = [8, 2, 12, 6, 24, 4, 14]
    print(f"Original array: {arr2}")
    reverseArray2Pointers(arr2)
    print("[Expected Approach - 1] Using Two Pointers - Array Reverse: ", end="")
    for i in range(len(arr2)):
        print(arr2[i], end=" ")
    print()

    # Method 3: Using Single Pointer
    arr3 = [16, 4, 24, 12, 48, 8, 28]
    print(f"Original array: {arr3}")
    reverseArraySinglePointer(arr3)
    print("[Expected Approach - 1] Using Single Pointers - Array Reverse: ", end="")
    for i in range(len(arr3)):
        print(arr3[i], end=" ")
    print()