from user import User
from book import Book


class Library:
    def __init__(self, user: User, book: Book):
        self.__user = user
        self.__book = book

    def __str__(self):
        return f"Книга {self.__book.get_title()} автора {self.__book.get_author()}  взял {self.__user.get_name()}"
