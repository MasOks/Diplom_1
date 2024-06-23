from unittest.mock import Mock

from praktikum.database import Database


class TestDatabase:

    def test_available_buns_true(self):
        db_buns = Database()

        assert len(db_buns.available_buns()) == 3

    def test_available_ingredients_true(self):
        db_ingredients = Database()

        assert len(db_ingredients.available_ingredients()) == 6

    def test_available_buns_with_mock(self):
        bun_mock = Mock()
        bun_mock.available_buns.return_value = [("white bun", 200), ("red bun", 100)]

        assert len(bun_mock.available_buns()) == 2
