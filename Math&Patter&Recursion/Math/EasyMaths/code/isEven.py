
#____________________________________
#
#   Easy Maths --- Check Even or Odd
#_____________________________________


def isEvenNaive(n):

    # finding remainder of n
    rem = n%2
    if rem == 0:
        return True
    else:
        return False

def isEvenBitwise(m):
    # taking bitwise and of n with 1 to check if the last bit is 0 or 1
    # if the last bit is 0, then n is even, otherwise it is odd
    # return (n & 1) == 0
    if (m & 1) == 0:
        return True
    else:
        return False
    


#Driver code

if __name__ == "__main__":
    n = 15
    m = 10
    if isEvenNaive(n = n):
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")

    if isEvenBitwise(m = m):
        print(f"{m} is an even number.")
    else:
        print(f"{m} is an odd number.")