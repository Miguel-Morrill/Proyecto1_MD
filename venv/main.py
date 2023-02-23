from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.transaction_controller import TransactionController
from controllers.user_controller import UserController

from schemas.account import Account
from schemas.card import Card
from schemas.transaction import Transaction
from schemas.user import User
from schemas.payment import Payment

from db import migrations

user = UserController.create_user(
    rfc='MOMM991110BQ3',
    curp='MOMM991110',
    name='Miguel Moreno',
    address='Contadores 597',
    phone_number=3334882893,
    email='if722133@iteso.mx',
    password='contrasena')
user.save()

print(user)

for u in User.select():
    print(u.id, u.rfc, u.curp, u.name, u.address)