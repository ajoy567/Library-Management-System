class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):

        status = "Available" if self.is_available else "Borrowed"
        return f"{status} : {self.title} by {self.author}"

