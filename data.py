import string
import random

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def new_name_ingredient():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    name_ingredient = generate_random_string(10)
    return name_ingredient


def new_price_ingredient():
    price_ingredient = random.randint(10, 5000)
    return price_ingredient


def choice_type_ingredient():
    types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    type_ingredient = random.choice(types)
    return type_ingredient
