# Step 1: Retrieve the book with the current title "1984"
book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()