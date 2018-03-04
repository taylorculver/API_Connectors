import requests

url = 'http://www.zillow.com/webservice/GetZestimate.htm'
payload = {'zws-id': 'X1-ZWz18ti2spowsr_77v70', 'zpid': '2560520'}
r = requests.get(url, params=payload)
print(r)
json_data = r.json()
# for key, value in json_data.items():
#     print(key + ':', value)
#
