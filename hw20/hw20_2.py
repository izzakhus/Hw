'''
    Задание 1
'''

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_name(self):
        return f'Название книги {self.name}'

    def get_year(self):
        return f'Год выпуска {self.year}'

    def get_publisher(self):
        return f'Издатель {self.publisher}'

    def get_genre(self):
        return f'Жанр {self.genre}'

    def get_author(self):
        return f'Автор {self.author}'

    def get_price(self):
        return f'Цена {self.price}'

    def __str__(self):
        return f'{self.get_name()},{self.get_year()},{self.get_publisher()},{self.get_genre()},{self.get_author()},{self.get_price()}'

if __name__ == '__main__':
    book = Book('1984', 1949, 'Secker & Warburg', "Дистопия", 'Джордж Оруэлл', 300)
    print(book)