class Account:
    balance = 0

    def _init_(self, name):
        self.name = name

    def deposit(self, amount: float):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount: float):
        self.balance -= amount