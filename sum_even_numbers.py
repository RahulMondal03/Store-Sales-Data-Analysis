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

    Examples:
        >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
        12
        >>> sum_even_numbers([1, 3, 5])
        0
        >>> sum_even_numbers([-2, -4, 7])
        -6
    """
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12
    print(sum_even_numbers([1, 3, 5]))           # 0
    print(sum_even_numbers([-2, -4, 7]))         # -6
    print(sum_even_numbers([]))                  # 0
