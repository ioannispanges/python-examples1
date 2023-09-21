def display_products(products):
    print("Available Products: ")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product['name']} - ${product['price']:.2f}")


def create_cart():
    return []


def add_to_cart(cart, products, item_index):
    if 0 <= item_index < len(products):
        cart.append(products[item_index])
        return True
    return False


def calculate_total(cart):
    total = sum(item['price'] for item in cart)
    return total


def checkout(cart):
    print("Your Cart:")
    for item in cart:
        print(f"{item['name']}- ${item['price']:.2f}")

    total = calculate_total(cart)
    print(f"Total: ${total:.2f}")
