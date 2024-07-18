'''
    Задание 1
'''

class Car:
    def __init__(self, model, year, brand, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
    def get_model(self):
        return f'Модель машины {self.model}'

    def get_year(self):
        return f'Год выпуска {self.year}'

    def get_brand(self):
        return f'Брэнд {self.brand}'

    def get_engine_capacity(self):
        return f'Объем двигателя {self.engine_capacity}'

    def get_color(self):
        return f'Цвет {self.color}'

    def get_price(self):
        return f'Цена {self.price}'

    def __str__(self):
        return f'{self.get_model()},{self.get_year()},{self.get_brand()},{self.get_engine_capacity()},{self.get_engine_capacity()},{self.get_color()},{self.get_price()}'


if __name__ == '__main__':
    car = Car('Toyota Camry',2020, 'Toyota',2.5, 'красный', 250000)
    print(car)
