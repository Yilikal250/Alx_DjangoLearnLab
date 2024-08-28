from django.urls import path
from .views import list_books, BookDetailView, LibraryDetailView  # Import the views you need

urlpatterns = [
    path('books/', list_books, name='book_list'),  # Add the URL pattern for listing books
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # URL pattern for book details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for library details
]