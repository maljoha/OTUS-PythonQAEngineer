from basics.figure import Figure


class Square(Figure):
    """Класс квадрата"""

    def __init__(self, a):
        self.a = a
        super().__init__(angles=4, name='Квадрат')

    @property
    def get_perimeter(self):
        """Вычисление периметра квадрата"""
        return self.a * 4

    def get_area(self):
        """Вычисление площади квадрата"""
        return self.a ** 2
