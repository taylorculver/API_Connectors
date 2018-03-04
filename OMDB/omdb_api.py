'''GET DATA FROM OMDB API'''
import requests
url = 'http://www.omdbapi.com/'
payload = {'i': 'tt3861987', 't': 'hackers', 'APIKEY': 'b07a08fc'}
r = requests.get(url, params=payload)
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)
