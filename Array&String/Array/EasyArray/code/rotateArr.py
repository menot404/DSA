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


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print(f"Original array: {arr}")
    rotateArrOneByOne(arr, d)
    print(f"Array after rotating by {d} positions: ", end="")
    print(" ".join(map(str, arr)))