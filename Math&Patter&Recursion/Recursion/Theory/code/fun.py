#________________________________________________________
#
#   Time Complexity Analysis of Recursive Functions
#________________________________________________________

def fun(n):
    if n<= 1:
        return
    fun(n // 2)
    for i in range(n):
        print("GFG", end=' ')

# Driver code
if __name__ == "__main__":
    n = 4
    fun(n)
    print()