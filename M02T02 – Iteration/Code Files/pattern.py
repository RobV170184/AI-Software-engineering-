# M02T02: Pattern - Print an arrow pattern using for loops
# This program prints an arrow pattern using if-else and for loops

# Loop through rows 1 to 9
for row in range(1, 10):
    # If row is 1 to 5, print increasing asterisks
    if row <= 5:
        print("*" * row)
    # If row is 6 to 9, print decreasing asterisks
    else:
        print("*" * (10 - row))
