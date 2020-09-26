import os 
import requests 

key = os.environ.get('MOVIE_KEY')  # Ask Clara if you'd like a key to try this code 
key = '528036ee90344d71485d8a0491414fe91ba5f953'
base_url = 'https://movies-2417.herokuapp.com/api/movies/'  

headers = {'Authorization' : 'Token ' + key}

# Add movies with POST.

movie = {'name': 'Frozsdfdfen', 'rating': 2}
response = requests.post(base_url, headers=headers, data=movie)
print(response.json())  # the movie object, or maybe an error message

movie = {'name': 'Black Panther', 'rating': 5}
response = requests.post(base_url, headers=headers, data=movie)
print(response.json())

# Get all the movies 
movies = requests.get(base_url, headers=headers)
for movie in movies.json():
    print(movie)

movie_id = input('Enter movie to change rating: ')
new_rating = int(input('New rating: '))    # obvious todo - validation 

# Modify a movie 
# Need the movie's ID 
update_movie = {'rating': new_rating}
response = requests.patch(base_url + movie_id + '/', headers=headers, data=update_movie)
print(response.status_code, response.text)
 
# Delete a movie 

movie_id = input('Enter movie to delete: ')

response = requests.delete(base_url + movie_id + '/', headers=headers)
print(response.text)

