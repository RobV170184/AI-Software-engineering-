# This program calculates the final price of items after applying a discount
# However, it contains a LOGICAL ERROR - can you spot it?

print("Welcome to the Discount Calculator!")
print("=" * 40)

# Original prices of items
laptop_price = 1000
phone_price = 500
tablet_price = 300

# Calculate total before discount
total_before_discount = laptop_price + phone_price + tablet_price
print(f"Total before discount: ${total_before_discount}")

# Apply 20% discount
discount_percentage = 20
discount_amount = total_before_discount * discount_percentage  # LOGICAL ERROR: Should divide by 100!

print(f"Discount amount ({discount_percentage}%): ${discount_amount}")

# Calculate final price
final_price = total_before_discount - discount_amount
print(f"Final price after discount: ${final_price}")

# The program runs without errors, but the output is completely wrong!
# A 20% discount on $1800 should be $360, making the final price $1440
# Instead, it shows a discount of $36000, resulting in a negative price!
