import requests

r = requests.get('https://api.github.com/users/aryanjain991')

# print(r.text)

with open("Api_fetch_details.txt", "w") as f:
    f.write(r.text)