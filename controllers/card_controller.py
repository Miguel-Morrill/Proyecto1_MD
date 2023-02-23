from schemas.card import Card


class CardController:

    @staticmethod
    def create_card(account_ID: int, clabe: int, expiration_date: int, cvv: int, nip: int, credit_limit: int)->Card:
        card = Card(account_ID=account_ID,
                    clabe=clabe,
                    expiration_date=expiration_date,
                    cvv=cvv,
                    nip=nip,
                    credit_limit=credit_limit)
        card.save()
        return card

    @staticmethod
    def get_available_credit(credit_usage: float):
        available_credit = Card.credit_limit - credit_usage
        return available_credit
