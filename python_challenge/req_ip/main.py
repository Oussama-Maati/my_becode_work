import requests, json


req = requests.get('https://api.ipify.org?format=json')

print(req.status_code)
print(req.content)
print(req.text)

print(json.loads(req.text)["ip"])