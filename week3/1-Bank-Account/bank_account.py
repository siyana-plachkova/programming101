class BankAccount:

    def __init__(self, name, balance, currency):
        if balance <= 0:
            raise ValueError

        if not isinstance(name, str):
            raise TypeError

        if not isinstance(currency, str):
            raise TypeError

        self.story = []

        self.name = name
        self.balance = balance
        self.currency = currency

        self.story.append("Account was created")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError

        self.balance += amount

        self.story.append("Deposited " + str(amount) + "$")

    def acc_balance(self):
        self.story.append("Balance check -> " + str(self.balance) + "$")

        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError

        self.balance -= amount

        self.story.append(str(amount) + "$" + " was withdrawed")

    def __str__(self):
        return "Bank account for " + self.name + " with balance of " + str(self.balance) + str(self.currency)

    def __int__(self):

        self.story.append("__int__ check -> " + str(self.balance) + "$")

        return self.balance

    def transfer_to(self, account, amount):
        if account.currency != self.currency:
            raise ValueError

        account.balance += amount

        self.story.append("Transfer to " + account.name + " for " + str(amount) + self.currency)

        return True

    def history(self):
        return self.story
