# M02T06: Lists and Dictionaries - Calculate total stock worth in a café
# This program calculates the total value of stock in a café

# Create a list of menu items
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Create a dictionary of stock quantities
stock = {
    "Coffee": 50,
    "Tea": 100,
    "Sandwich": 20,
    "Cake": 15
}

# Create a dictionary of prices
price = {
    "Coffee": 3.50,
    "Tea": 2.50,
    "Sandwich": 5.00,
    "Cake": 4.00
}

# Calculate total worth of stock
total_stock = 0

for item in menu:
    # Calculate value for each item: stock * price
    item_value = stock[item] * price[item]
    total_stock += item_value

# Print the result
print(f"Total stock worth: ${total_stock:.2f}")
