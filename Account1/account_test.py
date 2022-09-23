import unittest

from .account_test import Account


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.acc = Account("Elder Jega")

    def test_account_can_be_created(self):
        # acc = Account()
        self.assertIsNotNone(self.acc)

    def test_that_account_has_zero_balance_on_creation(self):
        # acc = Account()
        self.assertEqual(0, self.acc.balance)

    def test_that_account_has_a_name(self):
        # acc = Account("Elder Jega")

        self.assertEqual("Elder Jega", self.acc.name)

    def test_that_we_can_deposit_money(self):
        self.acc.deposit(1000)
        self.assertEqual(1000, self.acc.get_balance())

    def test_that_we_can_withdraw_money(self):
        self.acc.deposit(2000)
        self.acc.withdraw(1000)
        self.assertEqual(1000, self.acc.get_balance())


if __name__ == '__main__':
    unittest.main()


class Account :
    pass