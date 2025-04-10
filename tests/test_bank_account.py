import unittest, os
from unittest.mock import patch
from datetime import datetime
from src.bank_account import BankAccount
from src.exceptions import WithdrawalTimeRestrictionError

class BankAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount(balance=1000, balance_a=200, log_file="transaction_log.txt", ins_balance_message="There is not enough balance", be_positive_balance_message="Amount must be positive")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_positive_amount_increase_balanace(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "The balance is not equal")

    @patch("src.bank_account.datetime")
    def test_withdraw_positive_amount_decrease_balance(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "The balance is not equal")

    @patch("src.bank_account.datetime")
    def test_withdraw_insufficient_amount_value_error(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        with self.assertRaisesRegex(ValueError, self.account.ins_balance_message):
            self.account.withdraw(1100)

    def test_get_balance_return_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transfer_sufficient_amount_decrease_balance(self):
        new_balance, new_balance_a = self.account.transfer(1000)
        assert new_balance == 0
        assert new_balance_a == 1200

    def test_transfer_insufficient_amount_value_error(self):
        with self.assertRaisesRegex(ValueError, self.account.ins_balance_message):
            self.account.transfer(1100)
        with self.assertRaisesRegex(ValueError, self.account.be_positive_balance_message):
            self.account.transfer(-200)

    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_days(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 2, 28, 10, 0)
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    def test_deposit_multiple_ammounts(self):
        test_cases = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])
