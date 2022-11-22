#   exchangerate-api.com
import requests
from pprint import pprint as print

API_KEY = '0a6e8a06d0b248fae507d599'

currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
print(response.status_code)
# print(response.text)
# print(response.json())
kurs = response.json()['conversion_rate']

print(f"Bugungi kursa: 1 AQSH dollari = {kurs}")# res = r.json()
# print(res)
# print(res['conversion_rate'])