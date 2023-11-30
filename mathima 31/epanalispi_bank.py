class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Euros {amount}. New balance : Euros {self.__balance}")

        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw Euros {amount}. New Balance: Euros {self.__balance}")
        else:
            print("Invalid withdrawal amount")

    def check_balance(self):
        print(f"Account Holder: {self.__account_holder}, Account Number :{self.__account_number}")
        print(f"Current Balance: Euros {self.__balance}")


account1 = BankAccount("Bob", "123456", 1000)
account1.check_balance()
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
