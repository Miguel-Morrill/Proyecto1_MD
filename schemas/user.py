from peewee import *

db = SqliteDatabase('proyecto_1.db')


class User(Model):
    rfc = CharField()
    curp = CharField()
    name = CharField()
    address = CharField()
    phone_number = IntegerField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db

