import random

import pytest

from basics.circle import Circle
from basics.rectangle import Rectangle
from basics.square import Square
from basics.triangle import Triangle


class TestCircle():

    def test_circle_name(self):
        pr = Circle(random.random())
        assert pr.name == "Круг", f"Ожидаемое название: 'Круг', фактическое: '{pr.name}'"

    def test_circle_angles(self):
        pr = Circle(random.random())
        assert pr.angles == 0, f"Ожидаемое количество углов круга: 0, фактическое: '{pr.angles}'"

    @pytest.mark.parametrize("r, exp_perim", [
        (10, 62.83185307179586),
        (0, 0), ], ids=[
        ("nozero values"),
        ("zero values")])
    def test_circle_perimeter(self, r, exp_perim):
        fact_perim = Circle(r).perimeter
        assert fact_perim == exp_perim, f"Ожидаемая площадь круга: {exp_perim}, фактическая: {fact_perim}"

    @pytest.mark.parametrize("r, expected_area", [
        (10, 314.1592653589793),
        (0, 0), ], ids=[
        ("nozero values"),
        ("zero values")])
    def test_circle_area(self, r, expected_area):
        fact_area = Circle(r).area
        assert fact_area == expected_area, f"Ожидаемая площадь круга {expected_area}, фактическая {fact_area}"

    @pytest.mark.parametrize("r, figure, expected_area", [
        (6, Triangle(12, 9, 15), 167.09733552923257),
        (4.51351666838205, Rectangle(3, 12), 100),
        (3.826519928662906, Square(2), 50),
        (12, "Non_figure", "Передан неправильный класс"),
    ], ids=[
        ("+ Triangle"),
        ("+ Rectangle"),
        ("+ Square"),
        ("Check error")
    ])
    def test_circle_add_area(self, r, figure, expected_area):
        try:
            fact_area = Circle(r).add_area(figure)
            assert fact_area == expected_area, f"Ожидаемая площадь: {expected_area}, фактическая: {fact_area}"
        except TypeError as err:
            assert err.__str__() == expected_area, f"Некорректное сообщение об ошибке: {err.__str__()}"
