from abc import ABC, abstractmethod


class Figure(ABC):
    """Базовый класс фигур"""

    def __init__(self, name, angles, *args):
        self.name = name
        self.angles = angles
        self.perimeter = self.get_perimeter
        self.area = self.get_area()

    def get_perimeter(self):
        """Вычисление периметра фигуры"""
        pass

    @abstractmethod
    def get_area(self):
        """Вычисление площади фигуры"""
        pass

    def add_area(self, figure):
        """Вычисление суммы площадей двух фигур"""
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise TypeError("Передан неправильный класс")
