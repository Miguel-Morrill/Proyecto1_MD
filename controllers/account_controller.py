from schemas.account import Account


class AccountController:

    @staticmethod
    def create_account(balance: float) -> Account:
        account = Account(balance=balance)
        account.save()

        return account
