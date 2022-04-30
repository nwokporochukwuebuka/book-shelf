from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import AddBook, EditBook


# Create your views here
class BookListView(ListView):
    """To display the list of teh whole book"""
    model = Book
    context_object_name = 'books'
    template_name='shelf/book_list.html'
    paginate_by = 3

# To add a new book
class CreateBookView(LoginRequiredMixin, CreateView):
    context_object_name = 'form'
    form_class = AddBook
    success_url = reverse_lazy('book:list')
    template_name = 'shelf/add_book.html'
    model = Book


# Edit Book
class EditBookView(LoginRequiredMixin, UpdateView):
    context_object_name = 'form'
    form_class = EditBook
    model = Book
    success_url = reverse_lazy("book:list")
    template_name = "shelf/add_book.html"

# Delete Book
class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "shelf/book_confirm_delete.html"
    context_object_name = "object"
    success_url = reverse_lazy("book:list")

class BookDetailView(DetailView):
    context_object_name = 'book_detail'
    model = Book
    template_name = "shelf/book_detail.html"

# archive - intended for 'retired or lost books' 
@login_required
def archive_book(request, pk):
    books = Book.objects.all().order_by("title")
    book = get_object_or_404(Book, pk=pk) if pk else None
    if book.archived is False:
        book.archived = True
    else:
        book.archived = False
    book.save()
    return render(request, "shelf/book_list.html", {"books" : books})