class Book:
    def __init__(self, author: str, title: str):
        self.__author = author
        self.__title = title

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def __str__(self):
        return f'Автор {self.get_author()}, название книги {self.get_title()}'
