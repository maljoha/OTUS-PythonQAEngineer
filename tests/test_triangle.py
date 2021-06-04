import random

import pytest

from basics.circle import Circle
from basics.rectangle import Rectangle
from basics.square import Square
from basics.triangle import Triangle


class TestTriangle():

    def test_triangle_name(self):
        tr = Triangle(random.random(), random.random(), random.random())
        assert tr.name == "Треугольник", f"Ожидаемое название 'Треугольник', фактическое '{tr.name}'"

    def test_triangle_angles(self):
        tr = Triangle(random.random(), random.random(), random.random())
        assert tr.angles == 3, f"Ожидаемое количество углов: 3, фактическое: '{tr.angles}'"

    @pytest.mark.parametrize("a, b, c, exp_perim", [
        (32767, 32767, 32767, 98301),
        (0.123456789, 1.23456789, 1.23456789, 2.592592569), ], ids=[
        ("integer values"),
        ("float values")])
    def test_triangle_perimeter(self, a, b, c, exp_perim):
        fact_perim = Triangle(a, b, c).perimeter
        assert fact_perim == exp_perim, f"Ожидаемая площадь треугольника {exp_perim}, фактическая {fact_perim}"

    @pytest.mark.parametrize("a, b, c, expected_area", [
        (12, 9, 15, 54),
        (2, 1, 2.23606797749979, 1),
        (3, 3, 3, 3.897114317029974),
        (1, 2, 3, 0), ], ids=[
        ("all integer values"),
        ("float side"),
        ("float area"),
        ("zero area")])
    def test_triangle_area(self, a, b, c, expected_area):
        fact_area = Triangle(a, b, c).area
        assert fact_area == expected_area, f"Ожидаемая площадь треугольника {expected_area}, фактическая {fact_area}"

    @pytest.mark.parametrize("a, b, c, figure, expected_area", [
        (12, 9, 15, Rectangle(23, 2), 100),
        (12, 9, 15, Square(3), 63),
        (12, 9, 15, Circle(3.826519928662906), 100),
        (12, 9, 15, "Non_figure", "Передан неправильный класс"),
    ], ids=[
        ("+ Rectangle"),
        ("+ Square"),
        ("+ Circle"),
        ("Check error")
    ])
    def test_triangle_add_area(self, a, b, c, figure, expected_area):
        try:
            fact_area = Triangle(a, b, c).add_area(figure)
            assert fact_area == expected_area, f"Ожидаемая площадь: {expected_area}, фактическая: {fact_area}"
        except TypeError as err:
            assert err.__str__() == expected_area, f"Некорректное сообщение об ошибке: {err.__str__()}"
