
#____________________________________
#
#   For loop in Programming
#_____________________________________


#1. Basic For Loop

"""
    2 (start): The loop begins at 2.
    11 (stop): The loop stops before it reaches 11.
    3 (step): The loop increments (counts up) by 3 at each step.
    end=" ": This prevents the default newline and adds a space between the numbers instead.
    Final Output:
    2 5 8
"""

for i in range(2, 11, 3):
    print(i, end=" ")

# 2. For Each Loop
# The for-each loop is used to iterate directly over elements of a collection such as arrays or lists without using an index.

numbers = [1,12,23,34,45]

print("\n")
for num in numbers:
    print(num, end=" ")

print("\n")

#3. For Loop with Multiple Variables
# Some languages like C, C++, and Java allow multiple loop control variables in a for loop.

i, j = 0, 10
while i < 5 and j > 0:
    print(f"i={i}, j={j}")
    i += 2
    j -= 1

# 4. Infinite For Loop
# An infinite for loop runs indefinitely because it has no terminating condition.
"""
    syntax c, c++, java, c#, javaScript
for (;;) {
    // Infinite loop
}
"""

# 5. Nested For Loop
# A nested for loop is a loop inside another loop. It is used for multidimensional data or when multiple levels of iteration are needed.
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
