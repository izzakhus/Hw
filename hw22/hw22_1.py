'''
    Задание 1
'''
class Device:
    '''
        Device
    '''

    def __init__(self, brand, model, weight):
        self.brand = brand
        self.model = model
        self.weight = weight

    def __str__(self):
        return f"Бренд {self.brand} Модель {self.model} Вес {self.weight} кг"

class Coffe(Device):
    '''
        Coffe
    '''
    def __init__(self, brand, model, weight, water):
        super().__init__(brand, model, weight)
        self.water = water

    def __str__(self):
        return f"{super().__str__()} Емкость для воды {self.water} л"

class Blender(Device):
    '''
        Blender
    '''
    def __init__(self, brand, model, weight, speed):
        super().__init__(brand, model, weight)
        self.speed = speed

    def __str__(self):
        return f"{super().__str__()} Скоростей {self.speed}"

class MeatGrinder(Device):
    '''
        Grinder
    '''
    def __init__(self, brand, model, weight, material):
        super().__init__(brand, model, weight)
        self.material = material

    def __str__(self):
        return f"{super().__str__()} Лезвие из {self.material}"

if __name__ == '__main__':
    coffe = Coffe('DeLonghi', 'Magnifica', 9.5, 1.8)
    print(coffe)

    blender = Blender('Philips', 'HR3652', 4.2, 5)
    print(blender)

    grinder = MeatGrinder('Bosch', 'MFW67440', 6.3, 'Нержавеющая сталь')
    print(grinder)
