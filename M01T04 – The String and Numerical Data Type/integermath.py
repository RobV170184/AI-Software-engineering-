# Task 3: integermath.py
# Basic arithmetic operations with user input

# Ask the user to enter three integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate and print the sum of all three numbers
sum_all = num1 + num2 + num3
print(f"Sum of all numbers: {sum_all}")

# Calculate and print the first number minus the second number
difference = num1 - num2
print(f"First number minus second number: {difference}")

# Calculate and print the third number multiplied by the first number
product = num3 * num1
print(f"Third number times first number: {product}")

# Calculate and print the sum of all three numbers divided by the third number
division = sum_all / num3
print(f"Sum divided by third number: {division}")
