
#_________________________________________________________
#
#   Easy Pattern --- Program to Print Floyd's Triangle
#__________________________________________________________

def printfloydstriangle(n):
    num = 1

    # Loop through each row
    for i in range(1, n + 1):

        # Loop through each column in current row
        for j in range(1, i + 1):
            print(num, end = " ")
            num += 1
        print()

def main():
    printfloydstriangle(6)

# Driver code

if __name__ == "__main__":
    main()

# Using Nested Loops - O(n²) Time and O(1) Space