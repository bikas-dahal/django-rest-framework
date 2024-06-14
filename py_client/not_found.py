import requests

endpoint = 'http://localhost:8000/api/products/13434/'

get_response = requests.get(
    endpoint,
    # json = {
    #     'name': 'test',
    #     'price': 10000,
    # }
)

print(get_response.json())