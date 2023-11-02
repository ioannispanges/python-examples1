class BankAccount:
    interest_rate = 0.02

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def calculate_interest(self):
        return self.balance * self.interest_rate


account1 = BankAccount("12345", 10000)
account2 = BankAccount("567890", 5000)

print("Rate", BankAccount.interest_rate)

print("Account 1 - Account Number", account1.account_number)
print("Account 1 - Balance", account1.balance)
print("Account 1 - Interest:", account1.calculate_interest())

print("Account 1 - Account Number", account2.account_number)
print("Account 1 - Balance", account2.balance)
print("Account 1 - Interest:", account2.calculate_interest())
