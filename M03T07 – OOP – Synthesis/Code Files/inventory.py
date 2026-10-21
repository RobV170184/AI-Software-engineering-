"""
Shoe Inventory Management System

This program manages a shoe inventory using OOP concepts.
It allows reading from file, adding shoes, viewing inventory,
restocking, searching, and calculating values.
"""

#========The beginning of the class==========
class Shoe:
    """Class representing a shoe product."""

    def __init__(self, country, code, product, cost, quantity):
        """
        Initialize a Shoe object with all attributes.

        Parameters:
            country (str): Country of origin
            code (str): Product code (SKU)
            product (str): Product name
            cost (int): Cost of the shoe
            quantity (int): Quantity in stock
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoes."""
        return self.quantity

    def __str__(self):
        """Return a string representation of the Shoe object."""
        return f"{self.code} - {self.product} from {self.country}, Cost: {self.cost}, Qty: {self.quantity}"


#=============Shoe list===========
# List to store shoe objects
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    """
    Read shoe data from inventory.txt file and create Shoe objects.
    Uses try-except for error handling and skips the header line.
    """
    try:
        with open('inventory.txt', 'r') as file:
            lines = file.readlines()
            # Skip the first line (header)
            for i in range(1, len(lines)):
                line = lines[i].strip()
                if line:  # Skip empty lines
                    data = line.split(',')
                    country = data[0]
                    code = data[1]
                    product = data[2]
                    cost = int(data[3])
                    quantity = int(data[4])
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
        print("Shoe data loaded successfully!")
    except FileNotFoundError:
        print("Error: inventory.txt file not found!")
    except Exception as e:
        print(f"Error reading file: {e}")
def capture_shoes():
    """
    Capture data about a shoe from user input and add to shoe_list.
    """
    print("\n--- Add New Shoe ---")
    country = input("Enter country: ")
    code = input("Enter product code (e.g., SKU12345): ")
    product = input("Enter product name: ")
    cost = int(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully!")

def view_all():
    """
    Display all shoes in the inventory in a table format.
    """
    print("\n" + "="*80)
    print("SHOE INVENTORY")
    print("="*80)
    print(f"{'Code':<12} {'Product':<20} {'Country':<15} {'Cost':<8} {'Quantity':<8}")
    print("-"*80)
    for shoe in shoe_list:
        print(f"{shoe.code:<12} {shoe.product:<20} {shoe.country:<15} {shoe.cost:<8} {shoe.quantity:<8}")
    print("="*80)

def re_stock():
    """
    Find the shoe with the lowest quantity and offer to restock it.
    """
    if not shoe_list:
        print("No shoes in inventory!")
        return

    # Find shoe with lowest quantity
    lowest_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_shoe.get_quantity():
            lowest_shoe = shoe

    print(f"\nLowest stock: {lowest_shoe}")
    choice = input("Do you want to restock this shoe? (yes/no): ").lower()

    if choice == "yes":
        add_qty = int(input("Enter quantity to add: "))
        lowest_shoe.quantity += add_qty
        print(f"Updated! New quantity: {lowest_shoe.quantity}")

        # Update the file
        try:
            with open('inventory.txt', 'w') as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            print("Inventory file updated!")
        except Exception as e:
            print(f"Error updating file: {e}")

def search_shoe():
    """
    Search for a shoe by product code and display it.
    """
    code = input("\nEnter shoe code to search: ")
    found = False

    for shoe in shoe_list:
        if shoe.code == code:
            print(f"\nShoe found: {shoe}")
            found = True
            break

    if not found:
        print("Shoe not found!")

def value_per_item():
    """
    Calculate and display the total value for each item.
    Value = cost * quantity
    """
    print("\n" + "="*70)
    print("VALUE PER ITEM")
    print("="*70)
    print(f"{'Code':<12} {'Product':<20} {'Value':<15}")
    print("-"*70)

    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.code:<12} {shoe.product:<20} {value:<15}")
    print("="*70)

def highest_qty():
    """
    Find and display the shoe with the highest quantity as being on sale.
    """
    if not shoe_list:
        print("No shoes in inventory!")
        return

    # Find shoe with highest quantity
    highest_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.get_quantity() > highest_shoe.get_quantity():
            highest_shoe = shoe

    print(f"\n*** ON SALE! ***")
    print(f"{highest_shoe.product} ({highest_shoe.code})")
    print(f"Available quantity: {highest_shoe.quantity}")
    print(f"Price: {highest_shoe.cost}")


#==========Main Menu=============
def main():
    """Main menu for the shoe inventory system."""

    # Load data at start
    read_shoes_data()

    while True:
        print("\n" + "="*50)
        print("SHOE INVENTORY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. View all shoes")
        print("2. Add new shoe")
        print("3. Search for shoe")
        print("4. Restock shoes")
        print("5. View value per item")
        print("6. View highest quantity (on sale)")
        print("7. Exit")
        print("="*50)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            search_shoe()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Thank you for using the Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


# Run the main program
if __name__ == "__main__":
    main()
