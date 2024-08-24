from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
# Create your views here.from django.shortcuts import render
from .models import Book

def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    # Create a simple text list of book titles and authors
    book_list = "\n".join([f"{book.title} by {book.author}" for book in books])

    # Render the response with the list of books
    return render(request, 'book_list.html', {'book_list': book_list})
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the context
        context = super().get_context_data(**kwargs)
        # Add all books related to this library
        context['books'] = self.object.books.all()
        return context