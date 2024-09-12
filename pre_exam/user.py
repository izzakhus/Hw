class User:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Имя {self.get_name()}"
