
""" NOT COMPLETE OR WORKING.
Flask_peewee """


from flask import Flask
from peewee import *
from flask_potion import Api, ModelResource, fields
from flask_potion.contrib.peewee import PeeweeManager
from playhouse.flask_utils import FlaskDB

# db = SqliteDatabase('chainsaw.sqlite')


class DB(FlaskDB):
    def connect_db(self):
        super(DB, self).connect_db()
        if not Chainsaw.table_exists():
            Chainsaw.create_table()

app = Flask(__name__)
app.debug = True
app.config['DATABASE'] = 'sqlite://chainsaw.sqlite'

db = DB(app)


class Chainsaw(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db


class ChainsawResource(db.Model):
    class Meta:
        model = Chainsaw

api = Api(app, default_manager=PeeweeManager)
api.add_resource(ChainsawResource)

if __name__ == '__main__':
    app.run()

