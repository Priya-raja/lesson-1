import requests

response = requests.get('https://icanhazdadjoke.com/',headers={'Accept':'application/json'})

if response.ok:
    # print(response.status_code)
    # print(response.text[:1000])
    response_json = response.json()
    print(response_json['joke'])
    print(type(response_json))
else:
    print('Error:', response.status_code)