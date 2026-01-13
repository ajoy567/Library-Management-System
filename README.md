# 📚 Library Management System

A modular, object-oriented Python application that simulates a real-world library system. This project demonstrates core OOP principles including **Association**, **State Management**, and **Encapsulation**.

## 🚀 Features

* **Book Management:** Create books with metadata (Title, Author, ISBN) and track their availability status.
* **User Management:** Create users who can maintain a personal collection of borrowed items.
* **The Librarian (Logic):** A central `Library` class that handles the rules of the system:
    * Prevents borrowing of already taken books.
    * Validates ISBNs against the catalog.
    * Dynamically updates the state of Book objects.

## 📂 Project Structure

The architecture is split into single-responsibility modules:

* `book.py`: Defines the `Book` class (The Item).
* `user.py`: Defines the `User` class (The Actor).
* `library.py`: Defines the `Library` class (The Controller/Manager).
* `main.py`: The entry point that ties all modules together and runs the simulation.

## 🛠️ Usage

1.  Clone the repository.
2.  Run the simulation:
    ```bash
    python main.py
    ```

## 📝 Example Output

```text
--- Current Catalog ---
[Available] The Hobbit by J.R.R. Tolkien
[Available] 1984 by George Orwell

Success! Raj borrowed The Hobbit

--- Raj's Backpack ---
[Borrowed] The Hobbit by J.R.R. Tolkien