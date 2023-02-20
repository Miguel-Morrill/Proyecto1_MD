from peewee import *
from peewee import SqliteDatabase

db = SqliteDatabase("proyecto_1.db")
db.connect()


class User(Model):
    user_ID = IntegerField(unique=True, primary_key=True)
    RFC = CharField(13)
    CURP = CharField(18)
    name = CharField()
    address = CharField(200)
    phone = IntegerField()
    email = CharField()
    password = CharField(100)

    class Meta:
        database = db


db.create_tables([User])


class Account(Model):
    account_ID = IntegerField(unique=True, primary_key=True)
    user_ID = ForeignKeyField(User)
    balance = IntegerField()
    credit_line = IntegerField()

    class Meta:
        database = db


db.create_tables([Account])


class Card(Model):
    card_ID = IntegerField(unique=True, primary_key=True)
    account_ID = ForeignKeyField(Account)
    CLABE = IntegerField()
    expiration_date = DateField()
    CVV = IntegerField(3)
    NIP = IntegerField(4)
    Type = BooleanField()

    class Meta:
        database = db


db.create_tables([Card])


class Transaction(Model):
    transaction_ID = IntegerField(unique=True, primary_key=True)
    card_ID = ForeignKeyField(Card)
    reference = IntegerField(7)
    concept = CharField(40)
    amount = IntegerField()
    transaction_date = DateTimeField()

    class Meta:
        database = db


db.create_tables([Transaction])


class Payments(Model):
    payment_ID = IntegerField(unique=True, primary_key=True)
    card_ID = ForeignKeyField(Card)
    amount = IntegerField()
    concept = CharField(40)
    payment_date = DateTimeField()

    class Meta:
        database = db


db.create_tables([Payments])
