def reverse_string(s):
    """
    Reverses a string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]


original_string = "ILoveCoding"
reversed_string = reverse_string(original_string)
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")

#Output
#Original string: ILoveCoding
#Reversed string: gnidoCevoLI
