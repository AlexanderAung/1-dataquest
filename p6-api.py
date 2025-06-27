import requests

endpoint = "https://api.exchangerate-api.com/v4/latest/"
# response = requests.get(endpoint)
# response_json = response.json()
currencies = ["MMK", "SGD", "TBH"]

for currency in currencies:
    url = endpoint + currency
    response = requests.get(url).json()
    print(response["rates"]["USD"])
