# Importing the Book model
from bookshelf.models import Book
# Step 1: Retrieve the book with the title "Nineteen Eighty-Four"
book = Book.objects.get(title='Nineteen Eighty-Four')

# Step 2: Delete the retrieved book from the database
book.delete()

# Step 3: Confirm deletion by trying to retrieve all books
books = Book.objects.all()
print(books)  # The output should not include the deleted book.