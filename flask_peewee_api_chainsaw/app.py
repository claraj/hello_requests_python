from flask import Flask, g, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict


DATABASE = 'chainsaw.db'
DEBUG = True


app = Flask(__name__)

database = SqliteDatabase(DATABASE)


class Chainsaw(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = database


database.create_tables([Chainsaw])

@app.before_request
def before_request():
    g.db = database
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/api/chainsaw')
def get_all():
    res = Chainsaw.select()
    for c in res:
        print(c)
    return jsonify([model_to_dict(c) for c in res])


@app.route('/api/chainsaw/<id>/')
def get_by_id(id):
    c = Chainsaw.get_by_id(id)
    return jsonify(model_to_dict(c))


@app.route('/api/chainsaw/', methods=['POST'])
def add_new():
    with database.atomic():
        Chainsaw.create(
            name=request.form['name'],
            country=request.form['country'],
            catches=request.form['catches']
        )
        return 'ok', 201


@app.route('/api/chainsaw/<id>/', methods=['PATCH'])
def update_chainsaw(id):
    print(request.form)
    with database.atomic():
        Chainsaw.update(name=request.form['name'],
                        country=request.form['country'],
                        catches=request.form['catches'])\
            .where(Chainsaw.id == id).execute()

        return 'ok', 200


@app.route('/api/chainsaw/', methods=['DELETE'])
def delete_chainsaw(id):
    with database.atomic():
        Chainsaw.delete().where(Chainsaw.id == id)
    return 'ok', 200


if __name__ == '__main__':
    app.run()