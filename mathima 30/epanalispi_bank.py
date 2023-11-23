class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit Euro {amount}. New balance : euro {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw Euro {amount}. New balance : euro {self.balance}")
        else:
            print("Invalid withdrawal amount")

    def display_balance(self):
        print(f"Current balance: Euro {self.balance}")


account = BankAccount(1000)
account.display_balance()
account.deposit(300)
account.withdraw(600)
account.display_balance()
