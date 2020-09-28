import requests 
 
""" To get the image, need to make two requests - one to get 
JSON with the image location, and then a second request to download 
the image """

dog_json = requests.get('https://dog.ceo/api/breeds/image/random').json()

img_url = dog_json['message']

image_response = requests.get(img_url)

with open('dog.jpg', 'wb') as file:
    for chunk in image_response.iter_content():
        file.write(chunk)