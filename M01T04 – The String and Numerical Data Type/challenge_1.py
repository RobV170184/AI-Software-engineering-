# Challenge 1: challenge_1.py
# Calculate triangle area using Heron's formula

import math

# Get the three side lengths from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Calculate the semi-perimeter (s)
s = (side1 + side2 + side3) / 2

# Calculate the area 
# area = √(s(s-a)(s-b)(s-c))
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Print the area
print(f"The area of the triangle is: {area}")
