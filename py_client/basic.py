import requests 

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

# get_response = requests.get(endpoint, params={'abc': 123}, json={'query': "Hyalo"})
get_response = requests.post(endpoint, json={'title': 'Hyalo', 'content':'check'})
# print(dir(get_response))
# print(get_response.url)
# print(get_response.raw)
print(get_response.json())