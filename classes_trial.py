
class Account:
    def __init__(self, name, balance,id_number):
        self.name = name
        self.balance = balance
        self.id = id_number

    def deposit(self, amount):
        self.balance += amount
        print(f"shillings {amount} has been deposited to  this account")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"shillings {amount} has been withdrawn from this account")

    def check_balance(self):
        print(f"The balance to Account {self.id} is: {self.balance}")


John_account = Account("John", 5000, 1234)
John_account.deposit(2000)
John_account.check_balance()
John_account.deposit(1000)
John_account.check_balance()
John_account.withdraw(2000)
John_account.check_balance()