import aiohttp
import asyncio
import time


async def fetch_url_async(session, url):
    async with session.get(url) as response:
        return await response.text()


async def save_to_file(content, index):
    filename = f'file_{index}.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


async def fetch_all_urls_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        save_tasks = [save_to_file(content, i) for i, content in enumerate(responses)]
        await asyncio.gather(*save_tasks)


if __name__ == '__main__':
    urls = [
        'https://ru.wikipedia.org/wiki/Python',
        'https://example.com'
    ]

    start_time = time.time()
    asyncio.run(fetch_all_urls_async(urls))
    end_time = time.time()
    print(f"Время выполнения сасинхронно \n{time.time() - start_time:.4f} секунд")
