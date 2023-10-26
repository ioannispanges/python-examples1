class BankAccount:
    bank_name = "XYZ Bank"

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount{amount} deposited. Current balance :{self.balance}")
        else:
            print("Invalid amount for Deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount{amount} withdraw. Current balance :{self.balance}")
        else:
            print("Invalid")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")

account1 = BankAccount("123456789", "John Doe", 1000)


account1.deposit(100)
account1.withdraw(200)
account1.check_balance()

print(f"Bank name: {BankAccount.bank_name}")
