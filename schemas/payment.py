from peewee import *
from schemas.card import Card

db = SqliteDatabase("proyecto_1.db")


class Payment(Model):
    payment_ID = IntegerField(unique=True, primary_key=True)
    card_ID = ForeignKeyField(Card, backref="payments")
    amount = IntegerField()
    concept = CharField(40)
    payment_date = DateTimeField()

    class Meta:
        database = db

