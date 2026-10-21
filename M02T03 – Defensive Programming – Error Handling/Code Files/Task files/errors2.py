# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"  # RUNTIME ERROR: Original was missing quotes around Lion, causing NameError (Lion not defined as a variable)
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  # SYNTAX ERROR: Original missing 'f' prefix for f-string formatting; LOGICAL ERROR: animal_type and number_of_teeth were swapped in wrong order

print(full_spec)  # SYNTAX ERROR: Python 3 requires parentheses for print function
