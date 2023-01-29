EXPECTED_BAKE_TIME = 40
LAYER_PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from
    'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """Calculate the time spent to prepare layers to the lasagna.

    :param layers: int - number of layers to prepare.
    :return: int -  time (in minutes) spent to prepare the layers.

    Function that takes the number of layers of an lasagna and returns how many
    minutes will be spent to prepare these layers based on the
    `LAYER_PREPARATION_TIME`.
    """
    return layers * LAYER_PREPARATION_TIME


def elapsed_time_in_minutes(
    number_of_layers: int,
    elapsed_bake_time: int
) -> int:
    """
    Return elapsed cooking time.

    :param number_of_layers: int - number of layers that were prepared.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - baking + prepare time already elapsed.

    This function takes two numbers representing the number of layers & the
    time already spent baking and calculates the total elapsed minutes spent
    cooking the lasagna.
    """
    layers_preparation_time = preparation_time_in_minutes(number_of_layers)
    return layers_preparation_time + elapsed_bake_time
