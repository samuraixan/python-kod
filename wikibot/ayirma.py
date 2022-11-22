import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/0a6e8a06d0b248fae507d599/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
