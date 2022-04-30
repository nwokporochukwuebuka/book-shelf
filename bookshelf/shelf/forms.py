from django import forms
from .models import Book

""" add book form """
class AddBook(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddBook, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control input-lg'
        }
        self.fields['author'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['categories'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'categories', 'book_cover')


""" edit book form"""
class EditBook(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditBook, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control input-lg'
        }
        self.fields['author'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['categories'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'categories', 'book_cover')