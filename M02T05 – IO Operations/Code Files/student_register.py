# M02T05: IO Operations - Student registration for exam venue

# Ask user how many students are registering
num_students = int(input("How many students are registering? "))

# Open file for writing
with open('reg_form.txt', 'w') as file:
    # Loop for each student
    for i in range(num_students):
        # Ask for student ID
        student_id = input(f"Enter student ID number {i + 1}: ")

        # Write ID to file
        file.write(student_id + "\n")

        # Write dotted line for signature
        file.write("." * 50 + "\n")

print(f"\nRegistration form created successfully with {num_students} students.")



