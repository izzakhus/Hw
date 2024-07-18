'''
    Задание 1
'''
def plus_two():
    try:
        number = int(input('Введите число '))
        result = number + 2
        print(result)
    except ValueError:
        print('«Ожидаемый тип данных — число!')
if __name__ == '__main__':
    plus_two()
