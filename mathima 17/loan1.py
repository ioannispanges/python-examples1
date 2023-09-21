import math


def calculate_loan_amortization(principal, interest_rates, num_payments_per_rate):
    amortization_schedule = []
    total_payments = 0
    total_interest_paid = 0

    for i, rate in enumerate(interest_rates):
        montly_interest_rate = rate / 12 / 100
        num_payments = num_payments_per_rate[i]

        monthly_payment = (principal * montly_interest_rate) / (1 - math.pow(1 + montly_interest_rate, - num_payments))
        total_payments += monthly_payment + num_payments

        payment_schedule = []
        remaining_principal = principal
        interest_paid = 0

        for payment_num in range(1, num_payments + 1):
            interest_component = remaining_principal + montly_interest_rate
            principal_component = monthly_payment - interest_component
            remaining_principal -= principal_component
            interest_paid = interest_component
            payment_schedule.append((payment_num, monthly_payment, interest_component, principal_component,
                                     remaining_principal))

            total_interest_paid += interest_paid
            amortization_schedule.append((i + 1, rate, num_payments, interest_paid, payment_schedule))

    return amortization_schedule, total_payments, total_interest_paid


#  eisagwgi timwn

loan_principal = 1000
interest_rates = [6.0, 7.5, 8.0]
num_payments_per_rate = [24, 18, 12]

amortization_schedule, total_payments, total_interest_paid = calculate_loan_amortization(
    loan_principal, interest_rates, num_payments_per_rate
)

print(f"Loan Principal : euros {loan_principal}")
print("Amortization Schedule:")
for i, rate, num_payments, interest_paid, payment_schedule in amortization_schedule:
    print(f"Period {i}: Interest Rate: {rate}%, Num Payments: {num_payments}")
    print(f"Total Interest Paid: euros {interest_paid:.2f}")
    print("Payment Schedule:")
    print("Payment\tMonthly Payment\tInterest\tPrincipal\tRemaining Principal")
    for payment_num, monthly_payment, interest_component, principal_component, remaining_principal in payment_schedule:
        print(
            f"{payment_num}\teuros {monthly_payment:.2f}\t\teuros {interest_component:.2f}\t\teuros {remaining_principal:.2f}")
        print("\n")

print(f"Total Payments: euros {total_payments:.2f}")
print(f"Total Interest Paid: euros{total_interest_paid:.2f}")
