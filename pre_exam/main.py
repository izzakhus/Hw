from book import Book
from user import User
from library import Library

if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    book2 = Book("Brave New World", "Aldous Huxley")

    user1 = User("Alice")
    user2 = User("Bob")

    library1 = Library(user1, book1)
    library2 = Library(user2, book2)

    print(library1)
    print(library2)
