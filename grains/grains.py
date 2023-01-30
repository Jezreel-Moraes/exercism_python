"""Implementation of grains exercise"""
MIN_SQUARE = 1
MAX_SQUARE = 64


def square(number: int) -> int:
    if not MIN_SQUARE <= number <= MAX_SQUARE:
        raise ValueError("square must be between 1 and 64")

    return 1 << (number - 1)


def total() -> int:
    return (1 << MAX_SQUARE) - 1
