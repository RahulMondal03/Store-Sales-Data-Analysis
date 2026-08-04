def sum_even_numbers(numbers):
    """
    Calculate the sum of even numbers in a list.

    Args:
        numbers: A list of integers

    Returns:
        int: The sum of all even numbers in the list

    Raises:
        TypeError: If numbers is not a list or contains non-integer values
        ValueError: If the list contains boolean values
    """
    # Validate that input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__}")

    # Validate that all elements are integers (excluding booleans)
    for i, num in enumerate(numbers):
        if isinstance(num, bool):
            raise ValueError(f"Element at index {i} is a boolean, expected an integer")
        if not isinstance(num, int):
            raise TypeError(f"Element at index {i} is {type(num).__name__}, expected an integer")

    # Calculate and return sum of even numbers
    return sum(num for num in numbers if num % 2 == 0)


if __name__ == "__main__":
    # Test cases
    print("Valid cases:")
    print(f"sum_even_numbers([1, 2, 3, 4, 5, 6]) = {sum_even_numbers([1, 2, 3, 4, 5, 6])}")
    print(f"sum_even_numbers([2, 4, 6, 8]) = {sum_even_numbers([2, 4, 6, 8])}")
    print(f"sum_even_numbers([1, 3, 5, 7]) = {sum_even_numbers([1, 3, 5, 7])}")
    print(f"sum_even_numbers([]) = {sum_even_numbers([])}")

    print("\nInvalid cases:")
    # Test with non-list input
    try:
        sum_even_numbers("not a list")
    except TypeError as e:
        print(f"String input: {e}")

    # Test with float values
    try:
        sum_even_numbers([1, 2.5, 3])
    except TypeError as e:
        print(f"Float in list: {e}")

    # Test with boolean values
    try:
        sum_even_numbers([1, 2, True])
    except ValueError as e:
        print(f"Boolean in list: {e}")

    # Test with mixed invalid types
    try:
        sum_even_numbers([1, 2, "3"])
    except TypeError as e:
        print(f"String element in list: {e}")
