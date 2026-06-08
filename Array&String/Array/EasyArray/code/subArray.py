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
"""
def subArrayIterative(arr):
    n = len(arr)

    # Pick starting point
    for i in range(n):
        # Pick ending point
        for j in range(i, n):
            # Print subarray between current starting and ending points
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print() # New line after each subarray

# Drive Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("All Non-empty Subarray: ")
    subArrayIterative(arr)