#_____________________________________________________
#
#   EASY ARRAY - Rotate an Array - Clockwise or Right
#_____________________________________________________

# Method 1: Rotate one by one
"""
At each iteration, shift the elements by one position to the right in a circular fashion (the last element becomes the first). Perform this operation d times to rotate the elements to the right by d positions.
    # O(n*d) Complexity Time
    # O(n) Complexity Space
"""
def rotateArrOneByOne(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d is greater than n
    for _ in range(d):
        # Store the last element
        last = arr[-1]
        # Shift all elements to the right by one position
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        # Place the last element at the beginning
        arr[0] = last


# Method 2:  Using Temporary Array

"""
The idea is to use a temporary array of size n, where n is the length of the original array. If we right rotate the array by d positions, the last d elements will be in the beginning and the first (n - d) elements will be at the end. 
    ==>Copy the last d elements of the original array into the first d positions of the temporary array
    ==>Then copy the first n - d elements of the original array to the end of temporary array. 
    ==>Finally, copy all the elements of temporary array back into the original array.

    # O(n) Complexity Time
    # O(n) Complexity Space
"""
def rotateArrTempArray(arr, d):
    n = len(arr)
    d = d%n # Handle cases where d is greater than n
    # Sorting rotated version of the array
    temp = [0]*n

    # Copy the last d elements to the beginning of temp
    for i in range(d):
        temp[i] = arr[n - d + i]
    # Copy the first n - d elements to the end of temp
    for i in range(n - d):
        temp[d + i] = arr[i]

    # Copy the temp array back to original array
    for i in range(n):
        arr[i] = temp[i]

# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print(f"Original array: {arr}")

    ########## Method 1: Rotate one by one ##################
    rotateArrOneByOne(arr, d)
    print(f"Array after rotating by {d} positions (otate one by one): ", end="")
    print(" ".join(map(str, arr)))

    ########## Method 2: Using Temporary Array ##################
    arr = [1, 2, 3, 4, 5, 6, 7]  # Reset the array
    rotateArrTempArray(arr, d)
    print(f"Array after rotating by {d} positions (using temp array): ", end="")
    print(" ".join(map(str, arr)))