from peewee import *
from schemas.account import Account

db = SqliteDatabase("proyecto_1.db")


class Card(Model):
    account_ID = ForeignKeyField(Account, backref="cards")
    clabe = IntegerField()
    expiration_date = DateField()
    cvv = IntegerField(3)
    nip = IntegerField(4)
    credit_limit = FloatField()

    class Meta:
        database = db

