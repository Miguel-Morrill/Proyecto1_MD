from schemas.account import Account


class TransactionController:

    @staticmethod
    def deposit(account: Account, amount: float):
        account.balance += amount
        account.save()

    @staticmethod
    def withdraw(account: Account, amount: float):
        if account.balance < amount:
            print("Insufficient funds")
        else:
            account.balance -= amount

    @staticmethod
    def transaction(account: Account , amount: float, transaction_type):
        if transaction_type == "deposit":
            TransactionController.deposit(amount)
            print(f"{amount} deposited into account {account}. New balance is {account.balance}")
        elif transaction_type == "withdraw":
            TransactionController.withdraw(amount)
            print(f"{amount} withdrawn from account {account}. New balance is {account.balance}")
        else:
            print("Invalid transaction type")
