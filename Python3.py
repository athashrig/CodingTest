def count_occurrences(lst, elem):
    """
    Counts the occurrences of a specific element in a list.

    Args:
        lst (list): The list to search.
        elem: The element to count.

    Returns:
        int: The number of occurrences of the element.
    """
    return lst.count(elem)


my_list = [1, 2, 3, 2, 3, 5, 4, 3, 2, 8, 6, 1, 2, 3, 4, 5, 8, 9, 0, 3, 1, 2, 4, 5, 4, 2, 5, 2]
target_element = 3
count = count_occurrences(my_list, target_element)
print(f"The element {target_element} occurs {count} times in the list.")

#Output
#The element 3 occurs 5 times in the list.
