import pytest
from src.wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_bitcoin():
    wallet = Wallet(10)
    wallet.add_bitcoin(90)
    assert wallet.balance == 100

def test_wallet_spend_bitcoin():
    wallet = Wallet(20)
    wallet.sell_bitcoin(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.sell_bitcoin(100)
