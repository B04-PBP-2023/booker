from django.forms import ModelForm
from bookshelf.models import Bookshelf
from django import forms

class BookshelfForm(ModelForm):
    class Meta:
        model = Bookshelf
        fields = ['user', 'book']