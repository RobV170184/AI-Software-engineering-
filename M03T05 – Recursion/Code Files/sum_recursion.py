# M03T05: Recursion - Sum list elements up to an index
# This program sums elements recursively up to a given index

def adding_up_to(numbers, index):
    """
    Sum all numbers in the list up to and including the given index using recursion.

    Parameters:
        numbers (list): List of integers.
        index (int): Index point up to which to sum.

    Returns:
        int: Sum of numbers from index 0 to the given index.
    """
    # Base case: if index is 0, return the first element
    if index == 0:
        return numbers[0]
    # Recursive case: add current element and recurse with index-1
    else:
        return numbers[index] + adding_up_to(numbers, index - 1)


# Test examples
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Should output 25
print(adding_up_to([4, 3, 1, 5], 1))  # Should output 7
