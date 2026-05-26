#_____________________________________________
#
#   THEORY OF MATRICES - BASICS OPERATIONS
#_____________________________________________

"""
# Declaration of Matrix Data Structure :
Declaration of a Matrix or two-dimensional array is very much similar to that of a one-dimensional array, given as follows.
"""
# Defining number of rows and columns in matrix
rows = 3
cols = 3

# Declaring a matrix of size 3 X 3, and
# Initializing it with value zero
rows, cols = (3, 3)
arr = [[0]*cols]*rows
print(arr)

"""
# Initializing Matrix Data Structure:
In initialization, we assign some initial value to all the cells of the matrix. Below is the implementation to initialize a matrix in different languages:
"""
# Initializing a 2-D array with values
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
print(len(arr[1]))

"""
# Operations on Matrix Data Structure:
We can perform a variety of operations on the Matrix Data Structure. Some of the most common operations are:

# 1. Access Elements of Matrix
    Like one-dimensional arrays, matrices can be accessed randomly by using their indices to access the individual elements.
    A cell has two indices, one for its row number, and the other for its column number.
    We can use arr[i][j] to access the element which is at the ith row and jth column of the matrix.
"""
# Accessing elements of 2-D array
print(f"First element of first row: {arr[0][0]}")
print(f"Second element of first row: {arr[0][1]}")
print(f"Third element of first row: {arr[0][2]}")
print(f"First element of second row: {arr[1][0]}")
print(f"Second element of second row: {arr[1][1]}")
print(f"Third element of second row: {arr[1][2]}")
print(f"First element of third row: {arr[2][0]}")
print(f"Second element of third row: {arr[2][1]}")
print(f"Third element of third row: {arr[2][2]}")

"""
# 2. Traversal of a Matrix
    We can traverse all the elements of a matrix or two-dimensional array by using two for-loops.
"""
# Initializing a 2-D list with values
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Traversing each row
for row in arr:
    # Traversing each column of current row
    for col in row:
        print(col, end=" ")
    print()
