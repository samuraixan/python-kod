import requests
import json
app_id = "62fc0762"
app_key = "0da558ad627580c876890a65f8ab6a60"
language = "en-gb"
word_id = "python"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id":app_id, "app_key": app_key})
print(r.status_code)
res = r.json()
print(res)
# print(res.keys())
# print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
# print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])