class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total_price = 0

    def add_item(self, item, quantity, price_per_unit):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        self.total_price += quantity * price_per_unit
        print(f"Added {quantity} {item} (s) to the cart")

    def remove_item(self, item, quantity, price_per_unit):
        if item in self.items and quantity <= self.items[item]:
            self.items[item] -= quantity
            self.total_price -= quantity * price_per_unit
            print(f"Removed {quantity}{item}(s) to the cart")
        else:
            print("Item not found or insufficient quantity")

    def checkout(self):
        print(f"Total Price: Euros {self.total_price: .2f}")


cart = ShoppingCart()
cart.add_item("Laptop", 2, 800)
cart.add_item("mouse", 1, 20)
cart.remove_item("Laptop", 2, 800)

cart.checkout()
