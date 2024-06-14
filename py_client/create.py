import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'test',
    'content': 'test',
    'price': 10000,
}

get_response = requests.post(
    endpoint,
    data
    # json = {
    #     'name': 'test',
    #     'price': 10000,
    # }
)

print(get_response.json())