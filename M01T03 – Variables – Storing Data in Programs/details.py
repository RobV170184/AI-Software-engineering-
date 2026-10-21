# M01T03: Variables Task 1 - User Details
# This program collects user information and displays it in a sentence

# Get user information
name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")

# Print all details in a single sentence using f-string
print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}.")
