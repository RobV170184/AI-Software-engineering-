# Optional Challenge: Telecommunications Billing System


print("=" * 50)
print("Welcome to TelecomMax Billing Calculator")
print("=" * 50)

# Customer details
customer_name = "John Smith"
account_number = 12345
print(f"Customer: {customer_name}")
print(f"Account Number: {account_number}")

# Monthly plan details
monthly_base_fee = 50
included_minutes = 500
call_minutes_used = 650
cost_per_extra_minute = 0.15

# COMPILATION ERROR #1: Missing closing parenthesis
# This is a SYNTAX ERROR because Python requires balanced parentheses
# The Python compiler will immediately detect this and refuse to run the program
print(f"Base Monthly Fee: ${monthly_base_fee}"
print(f"Included Minutes: {included_minutes}")

# Calculate extra minutes
extra_minutes = call_minutes_used - included_minutes

# COMPILATION ERROR #2: Incorrect indentation (unexpected indent)
# This is a SYNTAX ERROR because Python uses indentation to define code blocks
# This line has unexpected indentation without a preceding statement requiring it
    extra_minutes_charge = extra_minutes * cost_per_extra_minute

# LOGICAL ERROR: Wrong calculation for total bill
# Should be monthly_base_fee + extra_minutes_charge, but uses subtraction instead
# This is a LOGICAL ERROR because the syntax is correct and it runs without crashing,
# but the business logic is wrong - we should ADD charges, not SUBTRACT them
# This results in customers getting money back instead of being charged!
total_bill = monthly_base_fee - extra_minutes_charge

print(f"\nCall minutes used: {call_minutes_used}")
print(f"Extra minutes: {extra_minutes}")
print(f"Extra minutes charge: ${extra_minutes_charge}")

# RUNTIME ERROR: Attempting to concatenate string with float without conversion
# This is a RUNTIME ERROR because Python cannot concatenate incompatible data types
# The program will compile successfully but crash with TypeError when this line executes
print("Your total bill is: $" + total_bill)

print("\nThank you for choosing TelecomMax!")

# Summary of errors in this program:
# 1. SYNTAX ERROR (Line 20): Missing closing parenthesis in print statement
# 2. SYNTAX ERROR (Line 27): Unexpected indentation without preceding block statement
# 3. RUNTIME ERROR (Line 44): Cannot concatenate string with float (needs str() conversion)
# 4. LOGICAL ERROR (Line 33): Using subtraction instead of addition for total bill calculation
