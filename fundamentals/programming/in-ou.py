# This program takes user input for age, height, grade, and name, and then outputs the values in a formatted manner.
age, height, grade, name = input("Enter your age, height, grade, and name (comma-separated): ").split()

# Convert the input values to appropriate types
age = int(age)
height = float(height)
grade = grade.upper()
name = name.strip()

# Output the values
print(f"Your age: {age}")
print(f"Your height: {height}")
print(f"Your grade: {grade}")
print(f"Your name: {name.capitalize()}")