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


# Method 2: [Expected Approach] Using Suffix Maximum
"""
The idea is to scan all the elements from right to left in an array and keep track of the maximum till now. 
When the maximum changes its value, add it to the result. 
Finally reverse the result  
    # O(n) Time
    # O(1) Space
"""
def leadersSuffixMax(arr):
    result = []
    n = len(arr)

    ## Start with the rightmost element
    maxRight = arr[-1]

    # Rightmost element is always a leader
    result.append(maxRight)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            result.append(maxRight)

    # Reverse the result list to maintain
    # original order
    result.reverse()
    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leadersLoop(arr=arr)
    print(" [Naive Approach] Using Nested Loops: ", end='')
    print(' '.join(map(str, result))) 

    arr  = [1, 8, 18, 8, 26, 0, 12, 1]
    result = leadersSuffixMax(arr=arr) ## Update Result 
    print("[Expected Approach] Using Suffix Maximum: ", end='')
    print(' '.join(map(str, result))) 