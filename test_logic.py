from logic import add, is_even, BankAccount
import pytest

def test_add():
    assert add(1, 2) == 3

def test_is_even():
    assert is_even(0) is True
    assert is_even(4) is True
    assert is_even(3) is False

def test_bank_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150

def test_bank_withdraw_error():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Not enough funds"):
        account.withdraw(200)

def test_bank_withdraw_success():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.balance == 70

def test_is_even_edge_cases():
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-1) is False
    assert is_even(10**18) is True
    assert is_even(10**18 + 1) is False

def test_is_even_non_numeric():
    with pytest.raises(TypeError, match="Input must be a number"):
        is_even("hi")

def test_is_even_none():
    with pytest.raises(TypeError, match="Input must be a number"):
        is_even(None)

def test_bank_transfer():
    acc1 = BankAccount(100)
    acc2 = BankAccount(50)
    acc1.transfer(acc2, 30)
    assert acc1.balance == 70
    assert acc2.balance == 80

def test_bank_transfer_not_enough_funds():
    acc1 = BankAccount(20)
    acc2 = BankAccount(50)
    with pytest.raises(ValueError, match="Not enough funds"):
        acc1.transfer(acc2, 100)