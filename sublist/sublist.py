"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one: list[int], list_two: list[int]) -> str:

    if list_one == list_two:
        return EQUAL

    str_list_one = ','.join([f'{c} ' for c in list_one])
    str_list_two = ','.join([f'{c} ' for c in list_two])

    if str_list_one in str_list_two:
        return SUBLIST

    if str_list_two in str_list_one:
        return SUPERLIST

    return UNEQUAL
