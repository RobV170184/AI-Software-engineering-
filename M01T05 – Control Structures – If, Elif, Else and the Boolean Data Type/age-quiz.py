# M01T05: Age Quiz Program
# This program takes a user's age and provides different messages based on age ranges

# Get the user's age as input
age = int(input("Enter your age: "))

# Check conditions in order from most specific to most general
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")
