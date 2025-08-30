import requests

r = requests.get('https://api.github.com/users/aryanjain991')

print(r.text)