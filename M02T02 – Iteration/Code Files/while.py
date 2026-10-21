# M02T02: While Loop - Calculate average of numbers
# This program continually asks for numbers and calculates their average

# Initialize variables
total = 0
count = 0

# Continually ask user to enter a number
while True:
    number = int(input("Enter a number (-1 to stop): "))

    # Exit loop if -1 is entered
    if number == -1:
        break

    # Skip if 0 is entered (not valid)
    if number == 0:
        continue

    # Add valid number to total
    total += number
    count += 1

# Calculate and print average
if count > 0:
    average = total / count
    print(f"The average of the valid numbers is: {average:.2f}")
else:
    print("No valid numbers were entered.")
