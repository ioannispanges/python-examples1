books = []


def add_book(book):
    global books
    books.append(book)


def remove_book(book):
    global books
    books.remove(book)


def list_books():
    global books
    return books


add_book("The great Gatsby")
add_book("To kill a Mockingbird")
add_book("1984")
remove_book("1984")


print("List of Books", list_books())
