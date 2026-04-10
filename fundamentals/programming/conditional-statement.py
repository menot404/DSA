
#____________________________________
#
#   If Conditional Statement
#_____________________________________

#The if statement checks a condition and executes a block of code only when the condition is true.
x = 10

if x > 0 :
    print(f"x: {x} is positive")



#____________________________________
#
#   If-Else Conditional Statement
#_____________________________________

#The if-else statement checks a condition and runs one block of code if the condition is true, and another block of code if the condition is false.

x = -5
if x > 0 :
    print(f"x: {x} is positive")
else :
    print(f"x: {x} is not positive")




#____________________________________
#
#   if-Else if Conditional Statement
#_____________________________________

#The if-else if statement is used to check multiple conditions. The program evaluates each condition one by one and executes the block of code for the first condition that is true.

x = 0

if x > 0 :
    print(f"x: {x} is positive")
elif x < 0 :
    print(f"x: {x} is negative")
else :
    print(f"x: {x} is zero")



#____________________________________
#
#   iSwitch Conditional Statement
#_____________________________________

# The switch statement checks a variable against multiple possible values. Each option is written as a case, and the program executes the matching case. A break statement is usually used to stop execution after a case runs.
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day!")


#____________________________________
#
#   Key Considerations for Switch Case Statements
#_____________________________________

#  Constant Expression: A switch expression must evaluate to a constant value. This can include constants or arithmetic operations.

x = 10
y = 5

match x + y:
    case 15:
        print("The sum is 15")
    case 20: 
        print("The sum is 20")
    case _ :
        print("The sum is neither 15 nor 20")

# 2. Limited to Certain Types: Switch statements are mainly designed for int, char, or string values depending on the language.

grade = 'A'

match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case _:
        print("Not specified")


#____________________________________
#
#   Ternary Expression Conditional Statement
#_____________________________________

"""The ternary operator is a short way to write an if-else statement. It evaluates a condition and returns one value if the condition is true, and another value if the condition is false.

It is called a ternary operator because each ternary expression uses three parts.
Multiple ternary expressions can also be nested to check more conditions."""

x = 20
resultat = "x is positive" if x > 0 else "x is not positive"
print(resultat)

#Nested Ternary Condition: A nested ternary condition is a ternary operator placed inside another ternary operator. It is used when you need to check multiple conditions in a single line. The inner ternary executes only if required by the outer condition.

x = 0

result = "x is positive" if x > 0 else ( "x is not positive" if x < 0 else "x is zero")
print(result)