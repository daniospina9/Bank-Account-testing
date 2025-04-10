from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError, WithdrawalDayRestrictionError

class BankAccount:
    def __init__(self, balance=0, balance_a=0, log_file=None, ins_balance_message=None, be_positive_balance_message=None):
        self.balance = balance
        self.balance_a = balance_a
        self.log_file = log_file
        self._log_transaction('cuenta creada')
        self.ins_balance_message = ins_balance_message
        self.be_positive_balance_message = be_positive_balance_message

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.weekday() == 5 or now.weekday() == 6:
            raise WithdrawalDayRestrictionError("Withdrawals are only allowed saturdays an sundays")
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8am to 5pm")
        if amount > self.balance:
            self._log_transaction(self.ins_balance_message)
            raise ValueError(self.ins_balance_message) 
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance

    def transfer(self, amount):
        if amount > self.balance:
            self._log_transaction(self.ins_balance_message)
            raise ValueError(self.ins_balance_message)
        if amount <= 0:
            self._log_transaction(self.be_positive_balance_message)
            raise ValueError(self.be_positive_balance_message)
        self.balance -= amount
        self.balance_a += amount
        self._log_transaction(f"Successful transfer. Transferred: {amount}. New balance: {self.balance}")
        return self.balance, self.balance_a