import shop_module


def main_shop():
    print("Welcome to the Shop!!!")
    print("-------------------------")

    products = [
        {"name": "T-shirt", "price": 20.0},
        {"name": "Jeans", "price": 50.0},
        {"name": "Shoes", "price": 80.0},
        {"name": "Hat", "price": 15.0},
    ]

    cart = shop_module.create_cart()
    while True:
        print("\nMenu:")
        print("1. Browse to products")
        print("2. Add product to cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            shop_module.display_products(products)

        elif choice == '2':
            item_index = int(input("Enter the product number to add to cart: ")) - 1
            if shop_module.add_to_cart(cart, products, item_index):
                print("Product added to cart.")
            else:
                print("Invalid product number")

        elif choice == '3':
            shop_module.display_products(cart)

        elif choice == '4':
            shop_module.checkout(cart)
            cart.clear()

        elif choice == '5':
            print("Thank you for shopping")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_shop()
