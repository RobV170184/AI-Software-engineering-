# M03T06: Sorting and Searching - Merge sort for strings by length
# This program sorts strings by length from longest to shortest

def merge_sort(arr):
    """
    Sort a list of strings by length from longest to shortest using merge sort.

    Parameters:
        arr (list): List of strings to sort.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Split the array
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists by string length (longest to shortest).

    Parameters:
        left (list): First sorted list.
        right (list): Second sorted list.

    Returns:
        list: Merged sorted list.
    """
    result = []
    i = j = 0

    # Merge by comparing string lengths (longest first)
    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Test with 3 string lists (each with at least 10 elements)
list1 = ["python", "programming", "computer", "algorithm", "data", "structure", "recursion", "function", "variable", "loop", "condition"]
list2 = ["artificial", "intelligence", "machine", "learning", "neural", "network", "database", "software", "hardware", "development", "application"]
list3 = ["elephant", "cat", "dog", "butterfly", "hippopotamus", "ant", "giraffe", "tiger", "lion", "mosquito", "crocodile"]

print("List 1 sorted by length:")
print(merge_sort(list1))

print("\nList 2 sorted by length:")
print(merge_sort(list2))

print("\nList 3 sorted by length:")
print(merge_sort(list3))
