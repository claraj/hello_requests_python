import requests

data = requests.get('https://catfact.ninja/fact').json()
print(data)   # Just to see what response is returned. Data is a dictionary
fact = data['fact']
print(f'A random cat fact is: {fact}')


