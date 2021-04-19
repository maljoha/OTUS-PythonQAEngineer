import random

import pytest

from basics.circle import Circle
from basics.rectangle import Rectangle
from basics.square import Square
from basics.triangle import Triangle


class TestSquare():

    def test_square_name(self):
        kv = Square(random.random())
        assert kv.name == "Квадрат", f"Ожидаемое название: 'Квадрат', фактическое: '{kv.name}'"

    def test_square_angles(self):
        kv = Square(random.random())
        assert kv.angles == 4, f"Ожидаемое количество углов квадрата: 4, фактическое: '{kv.angles}'"

    @pytest.mark.parametrize("a, exp_perim", [
        (32767, 131068),
        (0.123456789, 0.493827156), ], ids=[
        ("integer values"),
        ("float values")])
    def test_square_perimeter(self, a, exp_perim):
        fact_perim = Square(a).perimeter
        assert fact_perim == exp_perim, f"Ожидаемая площадь квадрата: {exp_perim}, фактическая: {fact_perim}"

    @pytest.mark.parametrize("a, expected_area", [
        (32767, 1073676289),
        (0.123456789, 0.01524157875019052),
        (0, 0), ], ids=[
        ("integer values"),
        ("float values"),
        ("zero area")])
    def test_square_area(self, a, expected_area):
        fact_area = Square(a).area
        assert fact_area == expected_area, f"Ожидаемая площадь квадрата {expected_area}, фактическая {fact_area}"

    @pytest.mark.parametrize("a, figure, expected_area", [
        (6, Triangle(12, 9, 15), 90),
        (8, Rectangle(3, 12), 100),
        (2, Circle(3.826519928662906), 50),
        (12, "Non_figure", "Передан неправильный класс"),
    ], ids=[
        ("+ Triangle"),
        ("+ Rectangle"),
        ("+ Circle"),
        ("Check error")
    ])
    def test_square_add_area(self, a, figure, expected_area):
        try:
            fact_area = Square(a).add_area(figure)
            assert fact_area == expected_area, f"Ожидаемая площадь: {expected_area}, фактическая: {fact_area}"
        except TypeError as err:
            assert err.__str__() == expected_area, f"Некорректное сообщение об ошибке: {err.__str__()}"
