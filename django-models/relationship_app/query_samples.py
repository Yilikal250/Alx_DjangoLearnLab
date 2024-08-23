from django.db import models

author_name = "George Orwell"
books_by_author = Book.objects.filter(author__name=author_name)


library_name = "Central Library"
library = Library.objects.get(name=library_name)

# List all books in the library
books_in_library = library.books.all()

# Again, assuming you know the library's name
library_name = "Central Library"
library = Library.objects.get(name=library_name)

# Retrieve the librarian associated with the library
librarian = library.librarian

# This will give you the Librarian instance associated with the specified library