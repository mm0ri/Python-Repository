import requests

name = 'mm0ri'
url = 'https://github.com/' + name
response = requests.get(url)

print(response.json())