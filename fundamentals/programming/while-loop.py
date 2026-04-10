
#____________________________________
#
#   While loop in Programming
#_____________________________________

"""
    A while loop is a control structure that repeatedly executes a block of code as long as a specified condition remains true.

        ==> The condition is checked before each iteration, and the loop stops once the condition becomes false.
        ==> It is useful when the number of iterations is not known beforehand.
"""

def print_numbers():
    # Function that prints numbers using while loop
    count = 0

    # while loop runs while the condition is true
    while count < 5 :
        print(count)
        count += 1

# Calling the function
print_numbers()


"""
    Use Cases of While Loop:
        -Input Validation: Repeatedly ask for input until the user provides a valid value.
        -Processing Data: Traverse arrays, lists, or collections until a condition is met.
        -Event Handling: Continuously monitor events like sensor data or network requests.
        -Implementing Algorithms: Used in algorithms such as searching, sorting, and mathematical computations.
        -State Machines: Execute logic repeatedly until a state change occurs.
        -Games and Simulations: Run the main game loop to update state, process input, and render output.
        -Batch Processing: Process multiple tasks (files, records, etc.) until all items are handled.
"""