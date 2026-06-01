#___________________________________________________________
#
#   EASY ARRAY - Replace with Adjacent Multiplication
#____________________________________________________________

# Method 1: Using Auxiliary Array
"""
The idea is to use a temporary array to store the updated values. This avoids losing the original values while computing the product for each element. After processing all elements, copy the temporary array back to the original array.
    # O(n) Time
    # O(n) Space
"""

def updateArrayAuxiliary(arr):
    n = len(arr)

    # Tempory array to shore the updated values
    temp = [0]*n

    for i in range(n):
        # Previous adjacent element
        prev = 1 if i == 0 else arr[i - 1]
        # Next adjacent element
        next = 1 if i == n - 1 else arr[i + 1]
        temp[i] = prev * arr[i] * next

    # Copy the updated values back to the original array
    for i in range(n):
        arr[i] = temp[i]


# Method 2: [Expected Approach] In-Place using Previous Tracking
"""
The idea is to update the array in-place while keeping track of the previous original element using a variable prev.
    # O(n) Time Complexity
    # O(1) Space Complexity
"""

def updateArrayInplace(arr):
    n = len(arr)
    # Stores previous original element
    prev = 1
    for i in range(n):
        # Store the current original value before updating
        curr = arr[i]
        # Get next adjacent element
        next = 1 if i == n - 1 else arr[i + 1]
        # Update current element using previous and next
        arr[i] = prev * curr * next
        # Update prev to current original value for next iteration
        prev = curr

# Driver Code
if __name__ == "__main__":

    #
    arr = [2, 4, 6, 8, 10]
    print("Original Array:", arr)
    updateArrayAuxiliary(arr)
    print("Updated Array:", *arr)

    #
    arr1 = [2, 4, 5]
    print("Original Array:", arr1)
    updateArrayInplace(arr = arr1)
    print("Updated Array:", *arr1)
