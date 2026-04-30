#___________________________________________
#
#   Introduction to Recursion
#___________________________________________

#How memory is allocated to different function calls in recursion? 

def printFun(test):
    if test < 1 :
        return
    else:
        print(test, end = ' ')
        printFun(test - 1)
        print(test, end = ' ')


# Driver code

if __name__ == "__main__":
    test = 3
    printFun(test=test)
    print()

