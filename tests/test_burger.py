from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_bun_in_burger_is_none(self):
        burger = Burger()

        assert burger.bun is None

    def test_ingredients_in_burger_is_empty_list(self):
        burger = Burger()

        assert burger.ingredients == []

    def test_set_buns_true(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        burger.set_buns(buns[1])

        assert burger.bun == buns[1]

    def test_add_ingredient_true(self):
        database: Database = Database()
        burger: Burger = Burger()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.add_ingredient(ingredients[2])

        assert ingredients[2] in burger.ingredients

    def test_remove_ingredient_true(self):
        database: Database = Database()
        burger: Burger = Burger()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.add_ingredient(ingredients[2])
        burger.add_ingredient(ingredients[3])
        burger.remove_ingredient(0)

        assert ingredients[2] is not burger.ingredients

    def test_move_ingredient_true(self):
        database: Database = Database()
        burger: Burger = Burger()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.add_ingredient(ingredients[2])
        burger.add_ingredient(ingredients[3])
        burger.move_ingredient(0, 1)

        assert ingredients[2] == burger.ingredients[1]

    def test_get_price_true(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[3])

        assert burger.get_price() == 400

    def test_get_receipt_true(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[3])

        receipt = (f'(==== {buns[0].name} ====)\n'
                   f'= sauce {ingredients[0].name} =\n'
                   f'= filling {ingredients[3].name} =\n'
                   f'(==== {buns[0].name} ====)\n\n'
                   f'Price: 400')

        assert burger.get_receipt() == receipt
