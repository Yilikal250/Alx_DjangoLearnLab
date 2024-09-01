from django.urls import path
from .views import book_list, LibraryDetailView  # Import the views you need
from django.urls import path
from .views import LoginView, LogoutView, RegisterView
urlpatterns = [
    path('books/', book_list, name='book_list'),  # Add the URL pattern for listing books
    # path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # URL pattern for book details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for library details
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]