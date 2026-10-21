# M02T06: Lists and Dictionaries - Store incorrect names until "John" is entered
# This program stores all incorrectly entered names in a list

# List to store incorrect names
incorrect_names = []

# Keep asking for names until "John" is entered
while True:
    name = input("Enter your name: ")

    # Check if the name is "John" (case-insensitive)
    if name.lower() == "john":
        break

    # Add incorrect name to list
    incorrect_names.append(name)

# Print out the list of incorrect names
print("Incorrect names:", incorrect_names)
