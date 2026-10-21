# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # SYNTAX ERROR: Python 3 requires parentheses for print function
print("\n")  # SYNTAX ERROR: Python 3 requires parentheses for print function, also had incorrect indentation

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"  # SYNTAX ERROR: Was using '==' (comparison) instead of '=' (assignment); RUNTIME ERROR: Original value "24 years old" couldn't be converted to int
age = int(age_Str)  # Also had incorrect indentation (SYNTAX ERROR)
print("I'm " + str(age) + " years old.")  # RUNTIME ERROR: Had to add str() to convert age to string for concatenation, also added missing spaces

# Variables declaring additional years and printing the total years of age
years_from_now = "3"  # Also had incorrect indentation (SYNTAX ERROR)
total_years = age + int(years_from_now)  # RUNTIME ERROR: Had to convert years_from_now to int before adding to age (can't add int + str)

print("The total number of years: " + str(total_years))  # SYNTAX ERROR: Original missing parentheses; LOGICAL ERROR: Was printing "answer_years" instead of actual total_years variable

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 + 6  # RUNTIME ERROR: Variable was named 'total' instead of 'total_years'; LOGICAL ERROR: Need to add 6 months for "3 years and 6 months"
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")  # SYNTAX ERROR: Original missing parentheses; RUNTIME ERROR: Had to add str() to convert total_months for concatenation

# 330 months is the correct answer
