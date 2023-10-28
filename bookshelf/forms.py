from django.forms import ModelForm
from bookshelf.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'books', 'selected_category', 'sort_by']