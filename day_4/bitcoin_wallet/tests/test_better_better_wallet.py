
import pytest
from src.wallet import Wallet, InsufficientAmount

# Parametrized Test Functions
@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])

def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_bitcoin(earned)
    my_wallet.sell_bitcoin(spent)
    assert my_wallet.balance == expected
