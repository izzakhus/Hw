'''
    Задание 2
'''
class Ship:
    '''
        Ship
    '''
    def __init__(self, name, displacement, speed):
        self.name = name
        self.displacement = displacement
        self.speed = speed

    def __str__(self):
        return f'Название {self.name} Водоизмещение {self.displacement} тонн Скорость {self.speed} узлов'

class Frigate(Ship):
    '''
        Frigate
    '''
    def __init__(self, name, displacement, speed, weapon):
        super().__init__(name, displacement, speed)
        self.weapon = weapon

    def __str__(self):
        return f'{super().__str__()} Оружейные системы {self.weapon}'

class Destroyer(Ship):
    '''
    Destroyer
    '''
    def __init__(self, name, displacement, speed, missile):
        super().__init__(name, displacement, speed)
        self.missile = missile

    def __str__(self):
        return f'{super().__str__()} Количество ракет {self.missile}'

class Cruiser(Ship):
    '''
    Cruiser
    '''
    def __init__(self, name, displacement, speed, aircraft):
        super().__init__(name, displacement, speed)
        self.aircraft = aircraft

    def __str__(self):
        return f'{super().__str__()} Вместимость самолётов {self.aircraft}'


frigate = Frigate('Фрегат', 4000, 30, 'Зенитные ракеты, Торпеды')
print(frigate)

destroyer = Destroyer('Эсминец', 8000, 35, 80)
print(destroyer)

cruiser = Cruiser('Крейсер', 10000, 32, 20)
print(cruiser)
