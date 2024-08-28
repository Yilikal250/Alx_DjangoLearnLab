from django.urls import path
from .views import LibraryDetailView  # Import the class-based view

urlpatterns = [
    # Add a URL pattern for the LibraryDetailView
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
# Map the URL to the BookDetailView  
]