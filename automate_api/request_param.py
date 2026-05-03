import requests


url = "https://icanhazdadjoke.com/search"

request_params ={
    'term':'pizza'
}

response = requests.get(url, headers={'Accept': 'application/json'}, params=request_params)

response_json = response.json()

data = response_json['results']

for joke in data:
    print(joke['joke'])
