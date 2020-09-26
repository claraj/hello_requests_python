import os 
import requests 

base_url = 'http://127.0.0.1:8000/api/movies/'

key = os.environ.get('MOVIE_API_KEY_LOCAL')  # Set an environment variable

# A user's movies must have unique names. Movie ratings are out of 5

auth_header = {'Authorization': 'Token ' + key }
movie = {'name': 'Wonder Woman', 'rating': 4}

response = requests.post(base_url, data=movie, headers=auth_header)
wonder_woman = response.json()
wonder_woman_id = wonder_woman['id']
print('Added movie', response.status_code, wonder_woman)  # expect 200, movie JSON including ID assigned by server 

movie = {'name': 'Batman', 'rating': 3}
response = requests.post(base_url, data=movie, headers=auth_header)
batman = response.json()
print('Added movie', batman)

# Patch - update Batman 
batman_id = batman['id']
response = requests.patch(f'{base_url}{batman_id}', data={'rating': 4}, headers=auth_header)
print('After update', response.json())

# Get Batman - get one 
response = requests.patch(f'{base_url}{batman_id}', headers=auth_header)
movie = response.json()
print('Get one', movie)

# Get all 
response = requests.get(base_url, headers=auth_header)
movies = response.json()
print('Get all', movies)

# Delete Batman 
response = requests.delete(f'{base_url}{batman_id}', headers=auth_header)
print(response.status_code)  # 204, request processed, no content to send in response 

# Delete Wonderwoman 
response = requests.delete(f'{base_url}{wonder_woman_id}', headers=auth_header)
print(response.status_code)  # 204, request processed, no content to send in response 
