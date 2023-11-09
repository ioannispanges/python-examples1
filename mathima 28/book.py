class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"'{self.title}','{self.author}'"

book1 = Book("The Catcher", "Salinger")
book2 = Book("Kill a mockingbird", "Lee")

print(book1)
print(repr(book2))
