from praktikum.ingredient import Ingredient
from data import new_name_ingredient, new_price_ingredient, choice_type_ingredient


class TestIngredient:

    def test_type_of_ingredient_true(self):
        type_ingredient = choice_type_ingredient()
        name = new_name_ingredient()
        price = new_price_ingredient()
        ingredient = Ingredient(type_ingredient, name, price)

        assert ingredient.type == type_ingredient

    def test_name_of_ingredient_true(self):
        type_ingredient = choice_type_ingredient()
        name = new_name_ingredient()
        price = new_price_ingredient()
        ingredient = Ingredient(type_ingredient, name, price)

        assert ingredient.name == name

    def test_price_of_ingredient_true(self):
        type_ingredient = choice_type_ingredient()
        name = new_name_ingredient()
        price = new_price_ingredient()
        ingredient = Ingredient(type_ingredient, name, price)

        assert ingredient.price == price

    def test_get_price_of_ingredient_true(self):
        type_ingredient = choice_type_ingredient()
        name = new_name_ingredient()
        price = new_price_ingredient()
        ingredient = Ingredient(type_ingredient, name, price)

        assert ingredient.get_price() == ingredient.price

    def test_get_name_of_ingredient_true(self):
        type_ingredient = choice_type_ingredient()
        name = new_name_ingredient()
        price = new_price_ingredient()
        ingredient = Ingredient(type_ingredient, name, price)

        assert ingredient.get_name() == ingredient.name

    def test_get_type_of_ingredient_true(self):
        type_ingredient = choice_type_ingredient()
        name = new_name_ingredient()
        price = new_price_ingredient()
        ingredient = Ingredient(type_ingredient, name, price)

        assert ingredient.get_type() == ingredient.type
