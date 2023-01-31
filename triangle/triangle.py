"""triangle exercise implementation"""

from typing import Callable

SIDES = list[float]


def is_triangle(func: Callable) -> Callable:
    def inner(sides: SIDES) -> bool:
        sum_ = sum(sides)
        is_valid = not any(x > sum_ - x if x != 0 else True for x in sides)
        return is_valid and func(sides)

    return inner


@is_triangle
def equilateral(sides: SIDES) -> bool:
    return len(set(sides)) == 1


@is_triangle
def isosceles(sides: SIDES) -> bool:
    return len(set(sides)) <= 2


@is_triangle
def scalene(sides: SIDES) -> bool:
    return len(set(sides)) == 3
