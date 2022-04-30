from django.urls import path

from shelf.views import BookDetailView, BookListView, CreateBookView, DeleteBookView, EditBookView, archive_book

app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('new', CreateBookView.as_view(), name='create'),
    path('book/edit/<int:pk>', EditBookView.as_view(), name='edit'),
    path('book/delete/<int:pk>', DeleteBookView.as_view(), name='delete'),
    path('book/detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('book/archive/<int:pk>', archive_book, name='archive')
]