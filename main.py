from book import Book
from library import Library
from user import User

def main():
    my_library = Library()

    book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    book3 = Book("Python Crash Course", "Eric Matthews", "978-1593279288")
    book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book5 = Book("Clean Code", "Robert C. Martin", "978-0132350884")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)
    my_library.add_book(book5)

    user = User("Raj", "Alex", "978-0547928227")

    print("--- Current Catalog ---")
    for b in my_library.catalog:
        print(b)
    print("\n")

    my_library.borrow_book(user, '978-0547928227')

    print(f"\n--- {user.first_name}'s Backpack ---")
    for book in user.borrowed_books:
        print(book)


    print("\n--- 1. Raj returns the book ---")
    my_library.return_book(user, "978-0547928227")

    print(f"\n--- 2. {user.first_name}'s Backpack after return ---")
    for book in user.borrowed_books:
        print(book)

    print("\n--- 3. Library Catalog ---")
    for b in my_library.catalog:
        print(b)

if __name__ == "__main__":
    main()

