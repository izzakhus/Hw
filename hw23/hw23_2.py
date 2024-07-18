'''
    Задание 2
'''
class Complex:
    def __init__(self, number, number1):
        self.number = number
        self.number1 = number1

    def __str__(self):
        return f'({self.number}, {self.number1})'

    def __add__(self, other):
        return Complex(self.number + other.number, self.number1 + other.number1)

    def __sub__(self, other):
        return Complex(self.number - other.number, self.number1 - other.number1)

    def __mul__(self, other):
        return Complex(self.number * other.number - self.number1 * other.number1,
                       self.number * other.number1 + self.number1 * other.number)

    def __truediv__(self, other):
        denominator = other.number ** 2 + other.number1 ** 2
        number_part = (self.number * other.number + self.number1 * other.number1) / denominator
        number1_part = (self.number1 * other.number - self.number * other.number1) / denominator
        return Complex(number_part, number1_part)

if __name__ == '__main__':
    c1 = Complex(3, 2)
    c2 = Complex(1, -1)

    print(f'c1 = {c1}')
    print(f'c2 = {c2}')

    print(f'c1 + c2 = {c1 + c2}')
    print(f'c1 - c2 = {c1 - c2}')
    print(f'c1 * c2 = {c1 * c2}')
    print(f'c1 / c2 = {c1 / c2}')
