import requests 

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api'

get_response = requests.get(endpoint, params={'abc': 123}, json={'query': "Hyalo"})
# print(dir(get_response))
# print(get_response.url)
# print(get_response.raw)
print(get_response.json())