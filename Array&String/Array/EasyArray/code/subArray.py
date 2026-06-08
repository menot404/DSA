#_____________________________________________
#
#   EASY ARRAY - Generating All Subarrays
#_____________________________________________

# Method 1: Iterative Approach
"""
To generate a subarray, we need a starting index from the original array. For choosing the starting index, we can run a loop from [0 to n-1] and consider each i as the starting index. 
For each starting index i, we can select an ending index from the range [i to n-1]. 
A nested loop from [i to n-1] will help in selecting the ending index. 
Once we have the starting and ending indices, we need an innermost loop to print the elements in this subarray.

    ==> Outermost Loop: Picks starting index of current subarray
    ==> Middle Loop: Picks ending index of current subarray
    ==> Innermost Loop: Prints the subarray from the starting index to the ending index
    # O(n²) Time
    # O(n) Space
"""
def subArrayIterative(arr):
    n = len(arr)

    # Pick starting point
    for i in range(n):
        # Pick ending point
        for j in range(i, n):
            # Print subarray between current starting and ending points
            print(arr[i:j+1], end=" ")
            print() # New line after each subarray

# Method 2: Recursive Approach
"""
We use two pointers start and end to maintain the starting and ending point of the array and follow the steps given below: 

    ==> Stop if we have reached the end of the array
    ==> Increment the end index if start has become greater than end
    ==> Print the subarray from index start to end and increment the starting index.
    # O(n^2) Time
    # O(n) Space
"""
def subArrayRecursive(arr, start, end):
    #Stop if we have end point and start from 0
    if end == len(arr):
        return

    # Increment the end point and end of the array
    elif start > end:
        return subArrayRecursive(arr, 0, end=end+1)

    # Print the subarray and increment starting point
    else:
        print(arr[start:end+1])
        return subArrayRecursive(arr, start=start+1, end=end)


# Drive Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("Iterative Approach -- All Non-empty Subarray: ")
    subArrayIterative(arr)
    print()
    arr = [1, 2, 3] # Update Array
    print("Recursive Approach -- All Non-empty Subarray: ")
    subArrayRecursive(arr, 0, 0)