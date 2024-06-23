import pytest

from praktikum.bun import Bun
from data import new_name_ingredient, new_price_ingredient


class TestBun:

    def test_name_of_bun_true(self):
        name = new_name_ingredient()
        price = new_price_ingredient()
        bun = Bun(name, price)

        assert bun.name == name

    def test_price_of_bun_true(self):
        name = new_name_ingredient()
        price = new_price_ingredient()
        bun = Bun(name, price)

        assert bun.price == price

    @pytest.mark.parametrize('incorrect_price', ['300', ['price', 300], -600])
    def test_price_of_bun_negative(self, incorrect_price):
        name = new_name_ingredient()
        bun = Bun(name, incorrect_price)

        assert type(bun.price) is not float

    def test_get_name_of_bun_true(self):
        name = new_name_ingredient()
        price = new_price_ingredient()
        bun = Bun(name, price)

        assert bun.get_name() == bun.name

    def test_get_price_of_bun_true(self):
        name = new_name_ingredient()
        price = new_price_ingredient()
        bun = Bun(name, price)

        assert bun.get_price() == bun.price
