# M02T05: IO Operations - Read and separate names and birthdays from DOB.txt
# This program reads DOB.txt and prints names and birthdays in separate sections

# Open and read the file
with open('DOB.txt', 'r') as file:
    lines = file.readlines()

# Lists to store names and birthday
names = []
birthdates = []

# Process each line
for line in lines:
    line = line.strip()
    if line:  # Skip empty lines
        parts = line.split()
        # First two parts are the name
        name = parts[0] + " " + parts[1]
        # Remaining parts are the birthdate
        birthdate = " ".join(parts[2:])

        names.append(name)
        birthdates.append(birthdate)

# Print names section
print("Name")
for name in names:
    print(name)

print()

# Print birthday section
print("Birthdate")
for birthdate in birthdates:
    print(birthdate)
