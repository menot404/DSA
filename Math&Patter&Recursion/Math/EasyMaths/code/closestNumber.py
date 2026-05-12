
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

### Method 2: [Expected Approach] By finding Quotient - O(1) Time and O(1) Space
def closestNumber2(n, m):
    # find Quotient
    q = int (n / m)

    # 1st possible closest number
    n1 = m * q

    # 2nd possible closest number
    if ((n*m) > 0):
        n2 = (m * (q + 1))
    else: 
        n2 = (m * (q - 1))

    # if true, then n1 is the required closest number
    if (abs(n - n1) < abs(n - n2)):
        return n1
    
    # else n2 is the required closest number
    return n2

# Driver code

if __name__ == "__main__":
    n = 10
    m = 6
    print(f"Method 1 - The closest number to {n} that is divisible by {m} is: {closestNumber1(n = n, m = m)}")
    print(f"Method 2 - The closest number to {-15} that is divisible by {m} is: {closestNumber2(n = -15, m = m)}")