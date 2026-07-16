"""Utility for summing the even numbers in a list."""


def sum_even_numbers(numbers):
    """Return the sum of only the even numbers in the given list.

    Args:
        numbers: A list (or any iterable) of numbers. Integers and floats
            are accepted; a float counts as even when it is a whole number
            divisible by 2 (e.g. 4.0).

    Returns:
        The sum of the even numbers. Returns 0 if the list is empty or
        contains no even numbers.

    Raises:
        TypeError: If any element is not an int or float (e.g. a string,
            None, or a nested list), or if ``numbers`` itself is not
            iterable. Booleans are rejected too — ``True``/``False`` are
            technically ints in Python, but summing them is almost
            always a bug.

    Examples:
        >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
        12
        >>> sum_even_numbers([1, 3, 5])
        0
        >>> sum_even_numbers([-2, -4, 7])
        -6
        >>> sum_even_numbers([1, 2, "3", 4])
        Traceback (most recent call last):
            ...
        TypeError: sum_even_numbers expects numbers, but element at index 2 is str: '3'
    """
    if not hasattr(numbers, "__iter__"):
        raise TypeError(
            f"sum_even_numbers expects an iterable of numbers, "
            f"got {type(numbers).__name__}"
        )

    total = 0
    for index, value in enumerate(numbers):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"sum_even_numbers expects numbers, but element at "
                f"index {index} is {type(value).__name__}: {value!r}"
            )
        if value % 2 == 0:
            total += value
    return total


if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12
    print(sum_even_numbers([1, 3, 5]))           # 0
    print(sum_even_numbers([-2, -4, 7]))         # -6
    print(sum_even_numbers([]))                  # 0

    for bad_input in ([1, 2, "3"], [1, None], [2, [4]], [True, 2], 42):
        try:
            sum_even_numbers(bad_input)
        except TypeError as error:
            print(f"{bad_input!r} -> TypeError: {error}")
