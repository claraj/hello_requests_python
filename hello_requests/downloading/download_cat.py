import requests 

# Kitten pictures from https://placekitten.com/

cat_url = 'http://placekitten.com/200/300'

response = requests.get(cat_url)

with open('kitten.jpg', 'wb') as file:
    for chunk in response.iter_content():
        file.write(chunk)


        