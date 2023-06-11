#Library Management System Python Golden Projects task2
class Book:
    def __init__(self, book_id, title, author, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available: {book.available}")

    def search_book(self, title):
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        if len(found_books) == 0:
            print("No matching books found.")
            return
        print("Matching books:")
        for book in found_books:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available: {book.available}")


def menu():
    print("========= Library Management System =========")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Search Book")
    print("0. Exit")
    print("============================================")

library = Library()

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        available = input("Enter Availability (Yes/No): ")
        book = Book(book_id, title, author, available)
        library.add_book(book)
    elif choice == '2':
        book_id = input("Enter Book ID: ")
        library.remove_book(book_id)
    elif choice == '3':
        library.display_books()
    elif choice == '4':
        title = input("Enter Title to search: ")
        library.search_book(title)
    elif choice == '0':
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
