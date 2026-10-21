# M03T06: Sorting and Searching - Linear search and insertion sort
# This program demonstrates searching and sorting algorithms

# Given list
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Linear search for 9 on unsorted list
# Linear search is appropriate here because the list is unsorted.
# It checks each element sequentially until the target is found.
def linear_search(arr, target):
    """Search for target using linear search."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

index = linear_search(numbers, 9)
print(f"Linear search: Found 9 at index {index}")
print("Linear search is a good choice for unsorted lists because it works")
print("regardless of the list order and is simple to implement.\n")

# Insertion sort implementation
def insertion_sort(arr):
    """Sort array using insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sorted_numbers = insertion_sort(numbers.copy())
print(f"Sorted list: {sorted_numbers}\n")

# Binary search for 9 on sorted list
# Binary search is efficient for sorted lists as it divides the search space in half each time.
def binary_search(arr, target):
    """Search for target using binary search on a sorted list."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

index = binary_search(sorted_numbers, 9)
print(f"Binary search: Found 9 at index {index}")
print("Binary search is useful in real-world applications like:")
print("- Searching in phone directories")
print("- Finding words in dictionaries")
print("- Database indexing and queries")
print("- Any situation with pre-sorted large datasets")
