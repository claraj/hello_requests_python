""" Very basic API server.
Error handling and validation omitted for clarity.
"""

from flask import Flask, g, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict


# Configuration - database file name
DATABASE = 'chainsaw.db'


# Create a Flask web app
app = Flask(__name__)

# Connect to the database
database = SqliteDatabase(DATABASE)

# Model class, fields will map to columns in the database
class Chainsaw(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = database


# Create table for model - just one table in this example
database.create_tables([Chainsaw])


# Before every request is handled, connect to the database
# g is the application context for the lifetime of one request
# app.before_request decorated functions are automatically called
# before a request-handling function runs
@app.before_request
def before_request():
    g.db = database
    g.db.connect()


# And close the DB connection after the request. This function
# is passed the response and can modify it if needed. Here the
# response is returned as-is.
@app.after_request
def after_request(response):
    g.db.close()
    return response


# GET all the records
@app.route('/api/chainsaw')
def get_all():
    # Get all the records from the database.
    res = Chainsaw.select()
    # Convert each record to a dictionary
    # Convert this list of dictionaries to JSON
    return jsonify([model_to_dict(c) for c in res])


# GET one record by ID
@app.route('/api/chainsaw/<catcher_id>')
def get_by_id(catcher_id):
    try:
        c = Chainsaw.get_by_id(catcher_id)
        # Convert object into dictionary of fields and values;
        # then convert the dictionary to JSON
        return jsonify(model_to_dict(c))
    except DoesNotExist:
        return 'Not found', 404


# POST to create a new record
@app.route('/api/chainsaw', methods=['POST'])
def add_new():
    with database.atomic():
        c = Chainsaw.create(**request.form.to_dict())
        return jsonify(model_to_dict(c)), 201  # 201 status means 'resource created'


# PATCH to modify an existing record
@app.route('/api/chainsaw/<catcher_id>', methods=['PATCH'])
def update_chainsaw(catcher_id):
    with database.atomic():
        Chainsaw.update(**request.form.to_dict())\
            .where(Chainsaw.id == catcher_id)\
            .execute()
        return 'ok', 200  # 200 status means 'ok', request successful


# DELETE to delete an existing record
@app.route('/api/chainsaw/<catcher_id>', methods=['DELETE'])
def delete_chainsaw(catcher_id):
    with database.atomic():
        Chainsaw.delete().where(Chainsaw.id == catcher_id).execute()
    return 'ok', 200  # 200 status means 'ok', request successful


# Start the web app running. By default, port 5000
if __name__ == '__main__':
    app.run()
