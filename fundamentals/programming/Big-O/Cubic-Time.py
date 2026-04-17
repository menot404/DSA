# ____________________________________
#
#   Cubic Time Complexity: Big O(n3) Complexity
# _____________________________________

"""
Cubic time complexity means that the running time of an algorithm is proportional to the cube of the input size.
# For example, a naive matrix multiplication algorithm has a cubic time complexity:
"""


"""
Performs the multiplication of two square matrices.

Arguments:
----------
mat1 : list[list[int/float]]
    The first matrix (left matrix) of size n x n.
mat2 : list[list[int/float]]
    The second matrix (right matrix) of size n x n.
result : list[list[int/float]]
    The destination matrix of size n x n, pre-initialized, 
    which will store the final result.
n : int
    The dimension of the matrices (number of rows or columns).

Complexity:
-----------
Time: O(n³), due to three nested loops each iterating n times.
Space: O(n²), to store the n*n elements of the resulting matrix.
"""

def multiply(mat1, mat2, result, n):
    for i in range(n):
        for j in range(n):
            result[i][j] = 0
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]


# Example usage

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
n = 2
result = [[0 for _ in range(n)] for _ in range(n)]
multiply(mat1, mat2, result, n)
print(result)
