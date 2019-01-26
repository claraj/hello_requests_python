## Flask and peewee app

### From the api directory:

To run the API server, set an environment variable 

`FLASK_APP=app.py`

Set another environment variable to configure development mode 

`FLASK_ENV=development`

Install dependencies 

`pip install -r requirements.txt`

Then run with 

`flask run`

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
