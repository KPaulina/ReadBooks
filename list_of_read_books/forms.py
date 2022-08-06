from django import forms

from .models import UserListBooks


class BooksForm(forms.ModelForm):
    class Meta:
        model = UserListBooks
        fields = ['title', 'description', 'status']


