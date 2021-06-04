import random

import pytest

from basics.circle import Circle
from basics.rectangle import Rectangle
from basics.square import Square
from basics.triangle import Triangle


class TestRectangle():

    def test_rectangle_name(self):
        pr = Rectangle(random.random(), random.random())
        assert pr.name == "Прямоугольник", f"Ожидаемое название 'Прямоугольник', фактическое '{pr.name}'"

    def test_rectangle_angles(self):
        pr = Rectangle(random.random(), random.random())
        assert pr.angles == 4, f"Ожидаемое количество углов прямоугольника: 4, фактическое: '{pr.angles}'"

    @pytest.mark.parametrize("a, b, exp_perim", [
        (32767, 32766, 131066),
        (0.123456789, 1.23456789, 2.716049358), ], ids=[
        ("integer values"),
        ("float values")])
    def test_rectangle_perimeter(self, a, b, exp_perim):
        fact_perim = Rectangle(a, b).perimeter
        assert fact_perim == exp_perim, f"Ожидаемая площадь прямоугольника: {exp_perim}, фактическая: {fact_perim}"

    @pytest.mark.parametrize("a, b, expected_area", [
        (32767, 32766, 1073643522),
        (32767, 0.123456789, 4045.308605163),
        (0, 0, 0), ], ids=[
        ("all integer values"),
        ("float area"),
        ("zero area")])
    def test_rectangle_area(self, a, b, expected_area):
        fact_area = Rectangle(a, b).area
        assert fact_area == expected_area, f"Ожидаемая площадь прямоугольника {expected_area}, фактическая {fact_area}"

    @pytest.mark.parametrize("a, b, figure, expected_area", [
        (2, 23, Triangle(12, 9, 15), 100),
        (12, 15, Square(3), 189),
        (13.5, 4, Circle(3.826519928662906), 100),
        (12, 9, "Non_figure", "Передан неправильный класс"),
    ], ids=[
        ("+ Triangle"),
        ("+ Square"),
        ("+ Circle"),
        ("Check error")
    ])
    def test_rectangle_add_area(self, a, b, figure, expected_area):
        try:
            fact_area = Rectangle(a, b).add_area(figure)
            assert fact_area == expected_area, f"Ожидаемая площадь: {expected_area}, фактическая: {fact_area}"
        except TypeError as err:
            assert err.__str__() == expected_area, f"Некорректное сообщение об ошибке: {err.__str__()}"
