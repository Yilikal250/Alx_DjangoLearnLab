from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
def book_list(request):
    """View to list all books with their titles and authors."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'books': books}  # Create a context dictionary to pass the books to the template
    return render(request, 'relationship_app/list_books.html', context)
class LibraryDetailView(DetailView):
    model = Library  # The model that this view will display
    template_name = 'relationship_app/library_detail.html'  # Specify the template name

    def get_context_data(self, **kwargs):
        # Get the default context data from the DetailView
        context = super().get_context_data(**kwargs)
        
        # Get the specific library instance
        library = self.get_object()
        
        # Add the list of books related to this library to the context
        context['books'] = library.books.all()  # This uses the related_name 'books' to access related books
        
        return context