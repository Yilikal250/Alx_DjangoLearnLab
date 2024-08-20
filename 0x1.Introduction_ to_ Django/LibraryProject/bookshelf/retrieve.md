# Retrieving the book with the title "1984" using the get() method
book = Book.objects.get(title='1984')

# Displaying all attributes of the retrieved book
print(book.title, book.author, book.published_date)