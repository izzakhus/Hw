'''
    Задание 2
'''
def treatment(array, index):
    try:
        element = array[index]
        print(f'Элемент с индексом {index}: {element}')
    except IndexError:
        print(f'Индекс {index} выходит за предел {len(array)}')

if __name__ == "__main__":
    input_array = input('Введите элементы через пробел ')
    user_array = list(map(int, input_array.split()))
    user_index = int(input('Введите индекс элемента '))

    treatment(user_array, user_index)
