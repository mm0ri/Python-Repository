import requests

name = input()
url = 'https://www.codewars.com/api/v1/users/' + name
response = requests.get(url)

print(response.json())