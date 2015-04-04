from bank_account import BankAccount
import unittest

class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Siyana", 50, "$")

    def test_init(self):
        with self.assertRaises(ValueError):
            w_account = BankAccount("Rado", -100, "$")

        self.assertTrue(isinstance(self.account, BankAccount))
        self.assertEqual(self.account.name, "Siyana")
        self.assertEqual(self.account.balance, 50)
        self.assertEqual(self.account.currency, "$")

    def test_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

        self.account.deposit(50)

        self.assertEqual(self.account.balance, 100)

    def test_acc_balance(self):
        self.assertEqual(self.account.acc_balance(), 50)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-20)

        self.account.withdraw(20)

        self.assertEqual(self.account.balance, 30)

    def test_str(self):
        self.assertEqual(str(self.account), "Bank account for Siyana with balance of 50$")

    def test_int(self):
        self.assertTrue(int(self.account), 50)

    def test_transfer_to(self):
        transf_acc = BankAccount("Alex", 50, "$")
        transf_acc_different_currency = BankAccount("Alex", 50, "#")

        self.account.transfer_to(transf_acc, 30)

        with self.assertRaises(ValueError):
            self.account.transfer_to(transf_acc_different_currency, 30)

        self.assertEqual(transf_acc.balance, 80)

    def test_history(self):
        self.assertEqual(self.account.history(), ["Account was created"])
        self.account.deposit(1000)
        self.assertIn("Deposited 1000$", self.account.history())
        int(self.account)
        self.assertIn("__int__ check -> 1050$", self.account.history())
        self.account.withdraw(500)
        self.assertIn("500$ was withdrawed", self.account.history())
        self.account.acc_balance()
        self.assertIn("Balance check -> 550$", self.account.history())
        self.assertEqual(["Account was created", "Deposited 1000$",
                          "__int__ check -> 1050$", "500$ was withdrawed",
                          "Balance check -> 550$"], self.account.history())

if __name__ == '__main__':
    unittest.main()
