'''BookShelf app Models'''

from django.db import models

# Setting the book Categories i.e specifying chhoices
BOOK_CATEGORIES = (
    ("Comic", "Comic"),
    ("Fantasy", "Fantasy"),
    ("Action", "Action"),
    ("Thriller", "Thriller"),
    ("Contemporary", "Contemporary")
)

# Create your models here.
class Book(models.Model):
    
    title = models.CharField(max_length=100)
    
    author = models.CharField(max_length=250) 

    description = models.TextField(max_length=1000)

    publication_date = models.DateTimeField(auto_now_add=True)

    book_cover = models.ImageField(upload_to='photos/')

    categories = models.CharField(max_length=20, choices=BOOK_CATEGORIES)

    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['archived']

