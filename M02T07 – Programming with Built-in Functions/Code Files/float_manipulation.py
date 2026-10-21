# M02T07: Built-in Functions - Float manipulation with statistics module

import statistics

# Ask user to input 10 floats
numbers = []
for i in range(10):
    num = float(input(f"Enter float number {i + 1}: "))
    numbers.append(num)

# Find the total of all numbers
total = sum(numbers)
print(f"Total: {total}")

# Find the index of the maximum
max_index = numbers.index(max(numbers))
print(f"Index of maximum: {max_index}")

# Find the index of the minimum
min_index = numbers.index(min(numbers))
print(f"Index of minimum: {min_index}")

# Calculate the average (mean) rounded to two decimal places
average = round(statistics.mean(numbers), 2)
print(f"Average (mean): {average}")

# Find the median
median = statistics.median(numbers)
print(f"Median: {median}")
