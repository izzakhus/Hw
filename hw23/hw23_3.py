'''
    Задание 3
'''
class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __add__(self, passengers):
        new_passengers = self.current_passengers + passengers
        if new_passengers <= self.max_passengers:
            self.current_passengers = new_passengers
        else:
            raise ValueError('Превышено максимальное количество пассажиров ')
        return self

    def __sub__(self, passengers):
        new_passengers = self.current_passengers - passengers
        if new_passengers >= 0:
            self.current_passengers = new_passengers
        else:
            self.current_passengers = 0
            print(f'В самолете {self.model} больше нет пассажиров ')
        return self

    def __iadd__(self, passengers):
        return self.__add__(passengers)

    def __isub__(self, passengers):
        return self.__sub__(passengers)

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __str__(self):
        return f"{self.model} - Пассажиры: {self.current_passengers}/{self.max_passengers}"

if __name__ == '__main__':
    airplane = Airplane("Boeing 747", 416)
    airplane1 = Airplane("Airbus A380", 853)

    print(f'Самолеты {airplane.model} и {airplane1.model} одинаковы по модели {airplane == airplane1}')
    print(f'Самолет {airplane.model} имеет меньшую вместимость чем {airplane1.model} {airplane < airplane1}')

    airplane += 200
    print(airplane)

    airplane1 += 700
    print(airplane1)

    airplane -= 50
    print(airplane)

    airplane1 -= 600
    print(airplane1)
