import math


def calculate_loan_payment(principal, interest_rate, num_payments):
    monthly_interest_rate = interest_rate / 12 / 100
    monthly_payment = (principal * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -num_payments))
    return monthly_payment


loan_principal = 1000
annual_interest_rate = 5.0
loan_term_years = 3

monthly_payment = calculate_loan_payment(loan_principal, annual_interest_rate, loan_term_years * 12)

print(f"Loan Principal: Euros {loan_principal}")
print(f"Annual Interest Rate: {annual_interest_rate}%")
print(f"Loan Term: {loan_term_years} years")
print(f"Monthly Payment: Euros {monthly_payment:.2f}")
