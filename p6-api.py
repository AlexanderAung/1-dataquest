import requests

endpoint = 'https://api.exchangerate-api.com/v4/latest/usd'
response = requests.get(endpoint)
print(response)
