# Library Management System

books = []

def add_book(book_name):
    """Add a book to the library"""
    books.append(book_name)
    print(f"Book '{book_name}' added successfully.")

def remove_book(book_name):
    """Remove a book from the library"""
    if book_name in books:
        books.remove(book_name)
        print(f"Book '{book_name}' removed successfully.")
    else:
        print("Book not found.")

def display_books():
    """Display all books in the library"""
    if not books:
        print("No books available in the library.")
    else:
        print("Available books:")
        for book in books:
            print
