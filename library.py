import csv

# File where the book data will be stored
library_file = "library_books.csv"

# Function to load books from CSV file
def load_books():
    library = {}
    try:
        with open(library_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                library[row['id']] = {'title': row['title'], 'author': row['author'], 'year': row['year']}
    except FileNotFoundError:
        # File does not exist, return an empty dictionary
        print(f"No existing file found. Starting a new library.")
    return library

# Function to save books to CSV file
def save_books():
    with open(library_file, 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'author', 'year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book_id, details in library.items():
            writer.writerow({'id': book_id, 'title': details['title'], 'author': details['author'], 'year': details['year']})

# Library is loaded from file at the start
library = load_books()

# Function to create/add a new book
def add_book(book_id, title, author, year):
    if book_id in library:
        print("Book ID already exists. Please use a unique ID.")
    else:
        library[book_id] = {"title": title, "author": author, "year": year}
        save_books()  # Save the library after adding a book
        print(f"Book '{title}' added successfully.")

# Function to retrieve or read book details
def view_book(book_id):
    if book_id in library:
        book = library[book_id]
        print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print("Book not found.")

# Function to update an existing book
def update_book(book_id, title=None, author=None, year=None):
    if book_id in library:
        if title:
            library[book_id]['title'] = title
        if author:
            library[book_id]['author'] = author
        if year:
            library[book_id]['year'] = year
        save_books()  # Save the library after updating a book
        print(f"Book with ID {book_id} updated successfully.")
    else:
        print("Book not found.")

# Function to delete a book
def delete_book(book_id):
    if book_id in library:
        deleted_book = library.pop(book_id)
        save_books()  # Save the library after deleting a book
        print(f"Book '{deleted_book['title']}' deleted successfully.")
    else:
        print("Book not found.")

# Function to list all books in the library
def list_books():
    if library:
        for book_id, book in library.items():
            print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print("No books in the library.")

# Main program to test CRUD operations
if __name__ == "__main__":
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. List All Books")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = input("Enter Year of Publication: ")
            add_book(book_id, title, author, year)
        
        elif choice == '2':
            book_id = input("Enter Book ID: ")
            view_book(book_id)
        
        elif choice == '3':
            book_id = input("Enter Book ID: ")
            print("Leave blank if you don't want to update a field.")
            title = input("Enter new title (or leave blank): ")
            author = input("Enter new author (or leave blank): ")
            year = input("Enter new year (or leave blank): ")
            update_book(book_id, title, author, year)
        
        elif choice == '4':
            book_id = input("Enter Book ID: ")
            delete_book(book_id)
        
        elif choice == '5':
            list_books()
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")