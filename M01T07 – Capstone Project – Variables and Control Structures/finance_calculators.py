# This program allows users to calculate investment interest or home loan repayments

import math

# Display the menu to the user
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")
print()

# Get user's choice
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Investment calculator
if user_choice == "investment":
    # Get investment details from user
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    # Convert interest rate to decimal
    r = interest_rate / 100

    # Calculate based on interest type
    if interest == "simple":
        # Simple interest formula: A = P(1 + r*t)
        total_amount = deposit * (1 + r * years)
        print(f"\nYour total amount after {years} years with simple interest: {total_amount:.2f}")

    elif interest == "compound":
        # Compound interest formula: A = P(1 + r)^t
        total_amount = deposit * math.pow((1 + r), years)
        print(f"\nYour total amount after {years} years with compound interest: {total_amount:.2f}")

    else:
        print("Invalid interest type entered.")

# Bond calculator
elif user_choice == "bond":
    # Get bond details from user
    house_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months to repay the bond: "))

    # Calculate monthly interest rate
    i = (annual_interest_rate / 100) / 12

    # Bond repayment formula: repayment = (i * P) / (1 - (1 + i)^(-n))
    repayment = (i * house_value) / (1 - (1 + i) ** (-months))

    print(f"\nYour monthly repayment amount: {repayment:.2f}")

# Invalid input
else:
    print("Error: Invalid input. Please enter either 'investment' or 'bond'.")
