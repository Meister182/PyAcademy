
class InsufficientAmount(Exception):
    pass

class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def sell_bitcoin(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_bitcoin(self, amount):
        self.balance += amount
