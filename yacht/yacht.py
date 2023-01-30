YACHT = (lambda d: 50 if len(set(d)) == 1 else 0)
ONES = (lambda d: digits(d, 1))
TWOS = (lambda d: digits(d, 2))
THREES = (lambda d: digits(d, 3))
FOURS = (lambda d: digits(d, 4))
FIVES = (lambda d: digits(d, 5))
SIXES = (lambda d: digits(d, 6))
FULL_HOUSE = (lambda d: sum(d) if len(set(d)) == 2 and any(
    d.count(x) == 3 for x in set(d)) else 0)
FOUR_OF_A_KIND = (lambda d: sum(x * 4 for x in set(d) if d.count(x) >= 4))
LITTLE_STRAIGHT = (lambda d: 30 if len(set(d)) == 5 and 6 not in d else 0)
BIG_STRAIGHT = (lambda d: 30 if len(set(d)) == 5 and 1 not in d else 0)
CHOICE = sum


def digits(dice, digit):
    return dice.count(digit) * digit


def score(dice, category):
    return category(dice)
