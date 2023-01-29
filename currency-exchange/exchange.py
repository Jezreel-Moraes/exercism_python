"""Functions for implementing the rules of Currency Exchange."""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Exchange budget to a new value based in the exchange_rate.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    exchanged_budget = budget / exchange_rate
    return exchanged_budget


def get_change(budget: float, exchanging_value: float) -> float:
    """Return the remaining budget after exchanging.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange
    now.
    :return: float - amount left of your starting currency after exchanging.
    """

    left_budget = budget - exchanging_value
    return left_budget


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Return total value of bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    bills_total_value = denomination * number_of_bills
    return bills_total_value


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Return the number of bills that can be received after exchanging
    the budget.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    number_of_bills = int(budget // denomination)
    return number_of_bills


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Return the remaining budget that cannot be exchanged given
    the current denomination.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the
    current denomination.
    """
    remaining_budget = budget % denomination
    return remaining_budget


def exchangeable_value(
    budget: float,
    exchange_rate: float,
    spread: int,
    denomination: int
) -> int:
    """Return the maximum value that can be exchanged given the current
    denomination.

    :param budget: float - the amount of your money you are planning to
    exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_to_percent = spread / 100
    spread_rate = spread_to_percent + 1
    exchange_rate_with_spread = exchange_rate * spread_rate
    exchanged_budget = exchange_money(budget, exchange_rate_with_spread)
    number_of_bills = get_number_of_bills(exchanged_budget, denomination)
    maximum_value = number_of_bills * denomination
    return maximum_value
