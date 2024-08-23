from django.contrib import admin
from .models import Book

# Custom admin class to customize the display and functionality
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication year in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for author and publication year
    list_filter = ('author', 'published_date')

    # Enable search by title and author
    search_fields = ('title', 'author')

    # Method to extract and display the publication year
    def publication_year(self, obj):
        return obj.published_date.year
    
    # Add short description for the custom method
    publication_year.short_description = 'Publication Year'
