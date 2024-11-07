# data name, phone,gender
# Account
# deposit / withdrawal / check balance
# oop --object -- bank account holds data and some operations can be done.

class Account:
    def __init__(self, full_name, acc_number, phone_number,
                 balance):  # constructor -- used to  set up something. the 1st item
        self.full_name = full_name
        self.acc_number = acc_number
        self.phone_number = phone_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} has been deposited successfully to account {self.acc_number}.")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds.balance is {self.balance}")
        else:
            self.balance -= amount
            print(f" Amount {amount} has been deposited successfully to account {self.acc_number}.")

    def check_balance(self):
        print(f"Balance for account {self.acc_number} is: {self.balance}")


Mzangulu_account = Account("Mzangulu Allan", "001", "07236573746", 1000)
Eng_Gitonga_account = Account("Gitonga Engineer", "002", "0716736362", 1500)
Pesh_account = Account("Muthaiga Penina", "003", "07188276672", 1800)


Pesh_account.deposit(2000)
Pesh_account.check_balance()

Mzangulu_account.deposit(3000)
Mzangulu_account.check_balance()
Mzangulu_account.withdraw(500)
Mzangulu_account.check_balance()
