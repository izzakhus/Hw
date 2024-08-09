import requests
import time


def fetch_url(url):
    response = requests.get(url)
    return response.text


def save_to_file(content, index):
    filename = f'file_{index}.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def fetch_all_urls(urls):
    for i, url in enumerate(urls):
        content = fetch_url(url)
        save_to_file(content, i)


if __name__ == '__main__':
    urls = [
        'https://ru.wikipedia.org/wiki/Python',
        'https://example.com'
    ]
    start_time = time.time()
    fetch_all_urls(urls)
    print(f'Время выполнения c  синхронно \n{time.time() - start_time:.4f} секунд')
