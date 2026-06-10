#____________________________________
#   EASY ARRAY - Leaders in an array
#____________________________________

# Method 1: [Naive Approach] Using Nested Loops
"""
Use two loops. The outer loop runs from 0 to size - 1 and one by one pick all elements from left to right. 
The inner loop compares the picked element to all the elements on its right side. 
If the picked element is greater than all the elements to its right side, then the picked element is the leader. 
    # O(n^2) Time
    # O(1) Space
"""
def leadersLoop(arr):
    result = []
    n = len(arr) # Size Array

    for i in range(n):
        #Check elements to the right
        for j in range(i + 1, n):
            # If a larger element is found
            if arr[i] < arr[j]:
                break
        else:
            # If no larger element was found
            result.append(arr[i])
    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leadersLoop(arr=arr)
    print(' '.join(map(str, result))) 