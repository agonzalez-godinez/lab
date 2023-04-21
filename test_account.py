from account import Account
import pytest


class TestClass:

    def setup_method(self):
        self.acc = Account('John')

    def teardown_method(self):
        del self.acc

    def test_init(self):
        assert self.acc.get_name() == 'John'
        assert self.acc.get_balance() == 0

    def test_deposit(self):
        assert self.acc.deposit(5) is True
        assert self.acc.get_balance() == 5.0

        assert self.acc.deposit(5.0) is True
        assert self.acc.get_balance() == 10.0

        assert self.acc.deposit(-5) is False
        assert self.acc.get_balance() == 10.0

        assert self.acc.deposit(-5.0) is False
        assert self.acc.get_balance() == 10.0

        assert self.acc.deposit(0) is False
        assert self.acc.get_balance() == 10.0

    def test_withdraw(self):
        assert self.acc.deposit(5) is True
        assert self.acc.get_balance() == 5.0

        assert self.acc.withdraw(5) is True
        assert self.acc.get_balance() == 0

        assert self.acc.withdraw(5.0) is False
        assert self.acc.get_balance() == 0

        assert self.acc.withdraw(-5) is False
        assert self.acc.get_balance() == 0

        assert self.acc.withdraw(-5.0) is False
        assert self.acc.get_balance() == 0

        assert self.acc.withdraw(0) is False
        assert self.acc.get_balance() == 0
