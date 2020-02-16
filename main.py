import requests
import json

url = 'https://www.ozon.ru/?utm_content=link'
response = requests.get(url)
data = json.loads(response.text)
print(data)