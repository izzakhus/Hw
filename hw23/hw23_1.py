'''
    Задание 1
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius


    def __eq__(self, other):
        if isinstance(other, Circle):
            if self.radius == other.radius:
                return f'Радиусы окружностей равны: {self.radius} = {other.radius}'
            else:
                return f'Радиусы окружностей не равны {self.radius} != {other.radius}'
        return 'Сравнение невозможно'

    def __gt__(self, other):
        if isinstance(other, Circle):
            if self.circumference() > other.circumference():
                return (f'Длина окружности с радиусом {self.radius} больше длины окружности '
                        f'с радиусом {other.radius}')
            else:
                return (f'Длина окружности с радиусом {self.radius} меньше или равна длине окружности'
                        f' с радиусом {other.radius}')
        return 'Сравнение невозможно'

    def __lt__(self, other):
        if isinstance(other, Circle):
            if self.circumference() < other.circumference():
                return (f'Длина окружности с радиусом {self.radius} меньше длины окружности'
                        f' с радиусом {other.radius}')
            else:
                return (f'Длина окружности с радиусом {self.radius} больше или равна длине окружности'
                        f' с радиусом {other.radius}')
        return 'Сравнение  невозможно'

    def __ge__(self, other):
        if isinstance(other, Circle):
            if self.circumference() >= other.circumference():
                return (f'Длина окружности с радиусом {self.radius} больше или равна длине окружности'
                        f' с радиусом {other.radius}')
            else:
                return (f'Длина окружности с радиусом {self.radius} меньше длины окружности'
                        f' с радиусом {other.radius}')
        return "Невозможно выполнить сравнение: объект не является экземпляром класса Circle"

    def __le__(self, other):
        if isinstance(other, Circle):
            if self.circumference() <= other.circumference():
                return (f'Длина окружности с радиусом {self.radius} меньше или равна длине окружности'
                        f' с радиусом {other.radius}')
            else:
                return (f'Длина окружности с радиусом {self.radius} больше длины окружности'
                        f' с радиусом {other.radius}')
        return 'Сравнение невозможно'

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def __str__(self):
        return f'Круг с радиусом {self.radius}'

if __name__ == '__main__':
    circle1 = Circle(8)
    circle2 = Circle(7)

    print(circle1 == circle2)
    print(circle1 < circle2)
    print(circle1 > circle2)

    circle1 += 3
    print(circle1)

    circle2 += 5
    print(circle2)
