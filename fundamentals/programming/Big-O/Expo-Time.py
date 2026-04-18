# ____________________________________
#
#    Exponential Time Complexity: Big O(2n) Complexity
# _____________________________________

"""
Exponential time complexity means that the running time of an algorithm doubles with each addition to the input data set.
# For example, the problem of generating all subsets of a set is of exponential time complexity:
"""

"""
Generates all subsets of a given set.

Arguments:
----------
arr : list
    The input set for which subsets are to be generated.
n : int
    The size of the input set.

Returns:
--------
list
    A list containing all subsets of the input set.

Complexity:
-----------
Time: O(2^n), because there are 2^n possible subsets for a set of size n.
Space: O(2^n), to store all the subsets generated.
"""
def generate_subsets(arr, n):
    subsets = []
    total_subsets = 1 << n  # This is 2^n, the total number of subsets

    for i in range(total_subsets):
        subset = []
        for j in range(n):
            if i & (1 << j):  # Check if the j-th element is included in the current subset
                subset.append(arr[j])
        subsets.append(subset)

    return subsets

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    result = generate_subsets(arr, n)
    print(f"All subsets of {arr}: {result}")
    for subset in result:
        print(subset)