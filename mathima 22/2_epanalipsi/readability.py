def calculate_total_price(quantity, price):
    return quantity * price


quantity = 5
price_per_item = 20
total = calculate_total_price(quantity, price_per_item)

print(f"The total price for {quantity} items at euros {price_per_item} per item is: euros {total}")
