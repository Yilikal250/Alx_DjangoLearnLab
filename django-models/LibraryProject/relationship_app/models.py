from django.db import models

# Create your models here.
# Define Complex Models in relationship_app/models.py:
# Author Model:
# name: CharField.
# Book Model:
# title: CharField.
# author: ForeignKey to Author.
# Library Model:
# name: CharField.
# books: ManyToManyField to Book.
# Librarian Model:
# name: CharField.
# library: OneToOneField to Library.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name='book')  
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE) 