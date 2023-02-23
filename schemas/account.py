from peewee import *
from schemas.user import User

db = SqliteDatabase("proyecto_1.db")


class Account(Model):
    user_ID = ForeignKeyField(User, backref='users')
    balance = IntegerField()

    class Meta:
        database = db

