from django import forms

from .models import UserListBooks, ListAuthors


class BooksForm(forms.ModelForm):
    class Meta:
        model = UserListBooks
        fields = ['title', 'description', 'status']


class BooksAuthorsForm(forms.ModelForm):
    class Meta:
        model = ListAuthors
        fields = ['name', 'surname', 'books']
