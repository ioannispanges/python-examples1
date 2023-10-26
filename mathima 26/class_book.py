class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.pubilcation_year = publication_year
        self.is_read = False

    def display_info(self):
        read_status = "read" if self.is_read else "not read"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.pubilcation_year}")
        print(f"Status: {read_status}")

    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} marked as read")


book1 = Book("To Kill a MockingBird", "Harper Lee", 1960)
book2 = Book("1984", "George Drwell", 1984)

book1.display_info()
book2.display_info()

book1.mark_as_read()

book1.display_info()
