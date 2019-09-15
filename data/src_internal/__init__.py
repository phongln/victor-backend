import requests

url = 'http://localhost:8090/api/v1/backend/user'

res = requests.get(url)

print(res.json())