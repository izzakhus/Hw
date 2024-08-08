import random
import threading
import time


def random_number(filename):
    time.sleep(1)
    random_num = random.randint(1, 100)
    with open(filename, 'w') as f:
        f.write(str(random_num))


def random_numer1000():
    start_time = time.time()

    for i in range(10):
        random_number(f'file{i}.txt')

    print(f'Время выполнения без многопоточности \n{time.time() - start_time:.4f}  секунд')


def multithreaded():
    threads = []

    start_time = time.time()

    for i in range(20):
        thread = threading.Thread(target=random_number, args=(f"file{i}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Время выполнения с многопоточностью: \n{time.time() - start_time:.4f} секунд')


if __name__ == '__main__':
    random_number('file.txt')
    random_numer1000()
    multithreaded()
