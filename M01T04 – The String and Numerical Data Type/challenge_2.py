# Challenge 2: challenge_2.py
# Practice casting between data types

# Get the user's favorite restaurant name (string)
restaurant = input("Enter your favorite restaurant name: ")
print(f"Your favorite restaurant is: {restaurant}")
print(f"Data type: {type(restaurant)}")

# Get the user's favorite number and cast it to an integer
favorite_number = int(input("Enter your favorite number: "))
print(f"Your favorite number is: {favorite_number}")
print(f"Data type: {type(favorite_number)}")

# Demonstrate what happens when trying to cast a string to an integer
print("\n--- Attempting to cast restaurant name to integer ---")
try:
    # This will fail if the restaurant name contains non-numeric characters
    restaurant_as_int = int(restaurant)
    print(f"Restaurant as integer: {restaurant_as_int}")
except ValueError:
    print("Error: Cannot convert the restaurant name to an integer!")
    print("Explanation: The int() function can only convert strings that contain")
    print("numeric characters (like '123'). Since restaurant names typically")
    print("contain letters and special characters, Python raises a ValueError.")
    print(f"'{restaurant}' is not a valid integer representation.")
