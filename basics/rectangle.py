from basics.figure import Figure


class Rectangle(Figure):
    """Класс прямоугольника"""

    def __init__(self, a, b):
        self.a, self.b = a, b
        super().__init__(angles=4, name='Прямоугольник')

    @property
    def get_perimeter(self):
        """Вычисление периметра прямоугольника"""
        return (self.a + self.b) * 2

    def get_area(self):
        """Вычисление площади прямоугольника"""
        return self.a * self.b
