## Flask and peewee app

### From the api directory:

Create a virtual environment and activate it 

Install dependencies 

`pip install -r requirements.txt`

To run the API server, set an environment variable to configure development mode 

`FLASK_ENV=development`

Then run with 

`python app.py`

App will be running on port 5000. 

Can view the GET requests in your browser e.g.

`http://127.0.0.1:5000/api/chainsaw`

or, catcher with ID = 1 with 

`http://127.0.0.1:5000/api/chainsaw/1`

Leave the API server running. 

### From the client directory 

Install dependencies 

`pip install -r requirements.txt`

Run with 

`python client.py`

Edit client.py to add, change, work with the different types of API calls.

Examples 

```
HTTP POST http://127.0.0.1:5000/api/chainsaw 
Create a new record, must provide new data in JSON form in the body 
HTTP PATCH http://127.0.0.1:5000/api/chainsaw/1  Edit record with ID 1, must provide new data in JSON form in the body  
HTTP DELETE http://127.0.0.1:5000/api/chainsaw/1 Delete record with ID = 1 
``` 