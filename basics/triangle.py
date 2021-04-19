from basics.figure import Figure


class Triangle(Figure):
    """Класс треугольника"""

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        super().__init__(angles=3, name='Треугольник')

    @property
    def get_perimeter(self):
        """Вычисление периметра треугольника"""
        return self.a + self.b + self.c

    def get_area(self):
        """Вычисление площади треугольника"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** .5
