DIGITS = list[int]


def to_decimal(digits: DIGITS, input_base: int) -> int:
    # credits
    # https://exercism.org/tracks/python/exercises/all-your-base/solutions/glennj
    decimal = 0
    for digit in digits:
        if digit >= input_base or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")

        decimal = decimal * input_base + digit

    return decimal


def to_new_base(div_: int, output_base: int) -> DIGITS:
    if div_ < output_base:
        return [div_]

    div_, mod_ = divmod(div_, output_base)
    return [*to_new_base(div_, output_base), mod_]


def rebase(input_base: int, digits: DIGITS, output_base: int) -> DIGITS:
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    decimal = to_decimal(digits, input_base)
    new_digits = to_new_base(decimal, output_base)

    return new_digits
