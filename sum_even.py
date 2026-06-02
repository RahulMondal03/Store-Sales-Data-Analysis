def sum_even_numbers(numbers):
    """Return the sum of only the even numbers in a list.

    Args:
        numbers: A list of numbers (ints or floats).

    Returns:
        The sum of all even numbers in the list. Returns 0 if there are none.
    """
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6]
    print(f"Sum of even numbers in {sample}: {sum_even_numbers(sample)}")
