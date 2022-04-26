import requests

name = 'mm0ri'
url = 'https://www.codewars.com/api/v1/users/' + name
response = requests.get(url)

print(response.json())