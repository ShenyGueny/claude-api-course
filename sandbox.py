"""Utilities for classifying integers by parity."""


def parity(number: int) -> str:
    """Return whether ``number`` is odd or even.

    Args:
        number: The integer to classify.

    Returns:
        ``"even"`` if ``number`` is divisible by 2, otherwise ``"odd"``.

    Raises:
        TypeError: If ``number`` is not an integer.
    """
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError(f"expected an int, got {type(number).__name__}")

    return "even" if number % 2 == 0 else "odd"


if __name__ == "__main__":
    for value in (0, 1, 2, -3, 100, -7):
        print(f"{value} is {parity(value)}")
