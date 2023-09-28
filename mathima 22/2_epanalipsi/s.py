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


add_book("The Great Gatsby")
add_book("To Kill a Mockingbird")
add_book("1984")
# remove_book("1984")

print(f"List of Books:{books}")
# for i, book in enumerate(list_books(), 1):
#     print(f"{i}. {book}")
print(f"choose a book to delete:" (book = str(input())

# print("choose a book:", input(book))
# if book in books:
#     remove_book(books)
# else:
#     print(f"{book} is not in list")

