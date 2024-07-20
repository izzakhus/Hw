'''
    Задание
'''

import threading
import time


def create_file(filename):
    time.sleep(1)
    open(filename, 'w')


def create_files():
    start_time = time.time()

    for i in range(101):
        create_file(f"test_file_{i}.txt")

    print(f'Время выполнения без многопоточности \n{time.time() - start_time:.4f}  секунд')


'''
    Многопоточное
'''


def multithreaded():
    threads = []

    start_time = time.time()

    for i in range(100):
        thread = threading.Thread(target=create_file, args=(f"test_file_{i}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Время выполнения с многопоточностью: \n{time.time() - start_time:.4f} секунд")


if __name__ == '__main__':
    create_file('file.txt')
    create_files()
    multithreaded()
