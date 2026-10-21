# M03T05: Recursion - Find largest number in a list
# This program finds the largest number using recursion without loops or max()

def largest_number(numbers):
    """
    Find the largest number in a list using recursion.

    Parameters:
        numbers (list): List of integers.

    Returns:
        int: The largest number in the list.
    """
    # Base case: if list has only one element, return it
    if len(numbers) == 1:
        return numbers[0]

    # Recursive case: compare first element with largest of remaining elements
    largest_of_rest = largest_number(numbers[1:])

    if numbers[0] > largest_of_rest:
        return numbers[0]
    else:
        return largest_of_rest


# Test examples
print(largest_number([1, 4, 5, 3]))  # Should output 5
print(largest_number([3, 1, 6, 8, 2, 4, 5]))  # Should output 8
