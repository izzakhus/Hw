'''
    Задание 3
'''

class Stadium:
    def __init__(self, name, open_data, country, city, capacity):
        self.name = name
        self.open_data = open_data
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_name(self):
        return f'Название стадиона {self.name}'

    def get_open_data(self):
        return f'Дата открытия {self.open_data}'

    def get_country(self):
        return f'Страна {self.country}'

    def get_city(self):
        return f'Город {self.city}'

    def get_capacity(self):
        return f'Вместимость {self.capacity}'

    def __str__(self):
        return f'{self.get_name()},{self.get_open_data()},{self.get_country()},{self.get_city()},{self.get_capacity()}'

if __name__ == '__main__':
    stadium = Stadium('Wembley Stadium', '23 марта 2007', 'Англия', 'Лондон', 90000)
    print(stadium)