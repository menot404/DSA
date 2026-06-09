#_____________________________________________
#
#   EASY ARRAY - Rearrange Array by Sign
#_____________________________________________


"""
The idea is to separate the numbers into positive and negative arrays. Then, alternately place numbers from each array back into the original array. Also place any remaining positive or negative numbers at the end.
    # O(n) Time
    # O(n) Space
"""
def rearrange(arr):
    pos = []
    neg = []

    # Separate positive and negative numbers
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    posIdx = 0
    negIdx = 0
    i = 0

    # Place positive and negative numbers alternately
    # in the original array
    while posIdx < len(pos) and negIdx < len(neg):
        if i % 2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        i += 1

    # Append remaining positive numbers (if any)
    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1
    # Append remaining negative numbers (if any)
    while negIdx < len(pos):
            arr[i] = neg[negIdx]
            negIdx += 1
            i += 1


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]
    rearrange(arr=arr)
    print(' '.join(map(str, arr)))