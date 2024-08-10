import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
data = response.json()

for i, item in enumerate(data):
    file_name = f"jsonplaceholder_{i+1}.json"
    with open(file_name, 'w') as f:
        json.dump(item, f, indent=4)

