#_____________________________________________
#
#   THEORY OF MATRICES - SEARCH IN MATRIX
#_____________________________________________

"""
# 3. Searching in a Matrix
    We can search an element in a matrix by traversing all the elements of the matrix.
    Below is the implementation to search an element in a matrix:
"""
def search_in_matrix(arr, x):
    rows, cols = len(arr), len(arr[0])

    # Traversing each row and column
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == x:
                return True

# Driver Code
if __name__ == "__main__":
    x = 8
    arr = [
        [0, 6, 8, 9, 11],
        [20, 22, 28, 29, 31],
        [36, 38, 50, 61, 67],
        [69, 87, 100, 122, 129]
    ]
    if search_in_matrix(arr, x):
        print("YES!!")
    else:
        print("NO!!")