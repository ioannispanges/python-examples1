books = []


def add_book(book):
    global books
    books.append(book)


def remove_book(book):
    global books
    if book in books:
        books.remove(book)
    else:
        print(f"{books} is not in the list")


def list_books():
    
    global books
    return books



add_book("The Great Gatsby")
add_book("To Kill a Mockingbird")
add_book("1984")
# remove_book("1984")

print(f"List of Book: {list_books()}")
book_to_delete = input("Choose a book to delete:")

remove_book(book_to_delete)

print({f"List od Books after deletions:{list_books()}"})

print(f"List of Books after additions: {list_books()}")
