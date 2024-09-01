from relationship_app.models import Author, Book, Library, Librarian

# Query to get all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Fetch the author by name
        books = Book.objects.filter(author=author)  # Get all books by the author
        return books
    except Author.DoesNotExist:
        return None

# Query to list all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Fetch the library by name
        books = library.books.all()  # Get all books in the library
        return books
    except Library.DoesNotExist:
        return None

# Query to retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Fetch the library by name
        librarian = Librarian.objects.get(library=library)  # Get the librarian for the library
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None