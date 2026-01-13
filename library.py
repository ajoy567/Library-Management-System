class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def borrow_book(self, user, isbn):

        found_book = None

        for book in self.catalog:
            if book.isbn == isbn:
                found_book = book
                break

        if found_book is not None:
            if found_book.is_available:
                found_book.is_available = False
                user.borrowed_books.append(found_book)
                print(f"Success! {user.first_name} borrowed {found_book.title}")
            else:
                print(f"Sorry, {found_book.title} is already borrowed!")

        else:
            print("The Book is not available in this library.")


