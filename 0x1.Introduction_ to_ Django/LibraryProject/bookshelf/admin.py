from django.contrib import admin
from .models import Book

# Custom admin class to customize the display and functionality
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication year in the admin list view
    list_display = ('title', 'author', 'published_date')
    
    # Add filters for author and publication year
    list_filter = ('author', 'published_date')
    
    # Enable search by title and author
    search_fields = ('title', 'author')

