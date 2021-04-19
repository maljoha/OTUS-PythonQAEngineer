from basics.figure import Figure


class Circle(Figure):
    """Класс круга"""

    def __init__(self, r):
        self.r = r
        super().__init__(angles=0, name='Круг')

    @property
    def get_perimeter(self):
        """Вычисление длины окружности"""
        return 2 * 3.141592653589793 * self.r

    def get_area(self):
        """Вычисление площади круга"""
        return 3.141592653589793 * self.r ** 2
