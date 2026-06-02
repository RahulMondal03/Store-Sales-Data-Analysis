from numbers import Integral


def sum_even_numbers(numbers):
    """Return the sum of only the even numbers in a list.

    Args:
        numbers: A list (or other iterable) of integers.

    Returns:
        The sum of all even numbers. Returns 0 if there are none.

    Raises:
        TypeError: If ``numbers`` is not iterable, or if any element is not
            an integer (booleans are also rejected, since ``True``/``False``
            are not meaningful numbers to sum).
    """
    try:
        iterator = iter(numbers)
    except TypeError:
        raise TypeError(
            f"Expected an iterable of integers, got {type(numbers).__name__!r}"
        )

    total = 0
    for index, value in enumerate(iterator):
        # bool is a subclass of int, so exclude it explicitly.
        if isinstance(value, bool) or not isinstance(value, Integral):
            raise TypeError(
                f"Element at index {index} is not an integer: "
                f"{value!r} ({type(value).__name__})"
            )
        if value % 2 == 0:
            total += value
    return total


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6]
    print(f"Sum of even numbers in {sample}: {sum_even_numbers(sample)}")

    # Demonstrate validation of non-integer values.
    try:
        sum_even_numbers([2, 4, "6", 8])
    except TypeError as err:
        print(f"Rejected invalid input: {err}")
