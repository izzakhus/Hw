import aiohttp
import asyncio
import json


async def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/users'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def save_data(data):
    for i, item in enumerate(data):
        file_name = f'jsonplaceholder_{i+1}.json'
        with open(file_name, 'w') as f:
            json.dump(item, f, indent=4)


if __name__ == '__main__':
    data = asyncio.run(fetch_data())
    asyncio.run(save_data(data))
