from peewee import *

from schemas.user import User
from schemas.account import Account
from schemas.card import Card
from schemas.payment import Payment
from schemas.transaction import Transaction


db = SqliteDatabase('proyecto_1.db')
db.create_tables([User, Account, Card, Payment, Transaction])

