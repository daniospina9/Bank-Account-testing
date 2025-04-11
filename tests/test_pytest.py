import pytest
from src.bank_account import BankAccount

@pytest.mark.parametrize("ammount, expected", [
     (100, 1100),
     (3000, 4000),
     (4500, 5500),
])
def test_deposit_multiple_ammounts(ammount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected

def test_deposit_negative_amount():
    account = BankAccount(balance=1000, log_file="transactions.txt")
    with pytest.raises(ValueError):
        account.deposit(-100)

@pytest.mark.parametrize("amount,should_raise", [
    (-100, True),   # Negative amount → should raise ValueError
    (200, False),   # Positive amount → should succeed
])
def test_deposit_parametrized(amount, should_raise):
    account = BankAccount(
        balance=1000,
        log_file="transactions.txt",
        be_positive_balance_message="Amount must be positive"
    )

    if should_raise:
        with pytest.raises(ValueError, match="Amount must be positive"):
            account.deposit(amount)
    else:
        new_balance = account.deposit(amount)
        assert new_balance == 1000 + amount