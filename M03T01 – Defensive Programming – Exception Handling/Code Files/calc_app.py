# M03T01: Exception Handling - Calculator application
# This program performs and records simple calculations with error handling

def perform_calculation():
    """Perform a calculation and save to equations.txt."""
    try:
        # Get user inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        # Perform calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation! Use +, -, *, or /")
            return

        # Display result
        print(f"Result: {num1} {operation} {num2} = {result}")

        # Save to file
        with open('equations.txt', 'a') as file:
            file.write(f"{num1} {operation} {num2} = {result}\n")

        print("Equation saved to equations.txt")

    except ValueError:
        print("Error: Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


def print_equations():
    """Print all previous equations from equations.txt."""
    try:
        with open('equations.txt', 'r') as file:
            equations = file.read()
            if equations:
                print("\n" + "="*50)
                print("PREVIOUS EQUATIONS")
                print("="*50)
                print(equations)
            else:
                print("No equations found.")
    except FileNotFoundError:
        print("No previous equations found. The file doesn't exist yet.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


# Main program
while True:
    print("\n" + "="*50)
    print("CALCULATOR APPLICATION")
    print("="*50)
    print("1. Perform a calculation")
    print("2. Print previous equations")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        perform_calculation()
    elif choice == "2":
        print_equations()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
