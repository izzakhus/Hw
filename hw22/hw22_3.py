'''
    Задание 3
'''

class Door:
    '''
        Door
    '''
    def __init__(self, door_count):
        self.door_count = door_count

    def __str__(self):
        return f'Количество дверей {self.door_count}'

class Engine:
    '''
        Engine
    '''
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def __str__(self):
        return f'Мощность двигателя {self.horsepower} л.с'

class Wheels:
    '''
        Wheels
    '''
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def __str__(self):
        return f'Количество колес {self.wheel_count}'


class Car(Wheels, Engine, Door):
    '''
        Car
    '''
    def __init__(self, brand, model, wheel_count, horsepower, door_count):
        Wheels.__init__(self, wheel_count)
        Engine.__init__(self, horsepower)
        Door.__init__(self, door_count)
        self.brand = brand
        self.model = model

    def __str__(self):
        return (f'Бренд {self.brand} '
                f'Модель {self.model},'
                f'{Door.__str__(self)},'
                f'{Engine.__str__(self)},'
                f'{Wheels.__str__(self)}')
if __name__ == '__main__':
    car = Car('Toyota', 'Camry', 4, 150, 4)
    print(car)
