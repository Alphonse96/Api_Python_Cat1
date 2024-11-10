# LIBRARY MANAGEMENT SYSTEM
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        """Marks the book as borrowed if available."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        """Marks the book as returned."""
        self.is_borrowed = False

# Define the LibraryMember class
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Allows the member to borrow a book if it is available."""
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")

    def return_book(self, book):
        """Allows the member to return a borrowed book."""
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def list_borrowed_books(self):
        """Lists all books borrowed by the member."""
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f" - {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")

# Interactive code to manage borrowing and returning of books
def main():
    # Sample books in the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    # Create a library member
    member = LibraryMember("Alice", "LM001")
    member = LibraryMember("Mike","LM002")
    # Interactive loop
    while True:
        print("\nLibrary Management System")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAvailable books:")
            for i, book in enumerate([book1, book2, book3], 1):
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{i}. {book.title} by {book.author} - {status}")

            book_choice = int(input("Select a book to borrow (1-3): ")) - 1
            book_to_borrow = [book1, book2, book3][book_choice]
            member.borrow_book(book_to_borrow)

        elif choice == "2":
            if member.borrowed_books:
                print("\nYour borrowed books:")
                for i, book in enumerate(member.borrowed_books, 1):
                    print(f"{i}. {book.title} by {book.author}")

                book_choice = int(input("Select a book to return (1-{}): ".format(len(member.borrowed_books)))) - 1
                book_to_return = member.borrowed_books[book_choice]
                member.return_book(book_to_return)
            else:
                print("You have no borrowed books to return.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

