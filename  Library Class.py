# Library Class
class Library:

    # Constructor to initialize book details
    def __init__(self, book_name, author, availability=True):
        self.book_name = book_name
        self.author = author
        self.availability = availability

    # Method to check out a book
    def checkout_book(self):
        if self.availability:
            self.availability = False
            print(f'"{self.book_name}" has been checked out.')
        else:
            print(f'Sorry, "{self.book_name}" is currently unavailable.')

    # Method to return a book
    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f'"{self.book_name}" has been returned.')
        else:
            print(f'"{self.book_name}" is already available.')

    # Method to display available books
    def display_status(self):
        status = "Available" if self.availability else "Not Available"
        print(f'Book: {self.book_name} | Author: {self.author} | Status: {status}')


# Creating objects for books
book1 = Library("Harry Potter", "J.K. Rowling")
book2 = Library("The Alchemist", "Paulo Coelho")
book3 = Library("Wings of Fire", "A.P.J. Abdul Kalam")

# Display books
print("Library Books:")
book1.display_status()
book2.display_status()
book3.display_status()

print("\nChecking out a book:")
book1.checkout_book()

print("\nAfter checkout:")
book1.display_status()

print("\nReturning the book:")
book1.return_book()

print("\nFinal Status:")
book1.display_status()