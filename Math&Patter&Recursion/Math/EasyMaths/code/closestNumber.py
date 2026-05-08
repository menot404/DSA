
#____________________________________
#
#   Easy Maths --- Closest Number
#_____________________________________


### Method 1: [Naive Approach] Iterative Checking - O(m) Time and O(1) Space
def closestNumber1(n, m):
    # find Quotient
    closest = 0
    min_diff = float('inf')

    # Check numbers arround n
    for i in range(n -abs(m), n + abs(m) + 1):
        if i % m == 0:
            diff = abs(n - i)
            if diff < min_diff or (diff == min_diff and abs(i) < abs(closest)):
                closest = i
                min_diff = diff
    return closest

### Method 2:


# Driver code

if __name__ == "__main__":
    n = 10
    m = 6
    print(f"The closest number to {n} that is divisible by {m} is: {closestNumber1(n = n, m = m)}")