from django.shortcuts import render
from book.models import Book
# Create your views here.


def show_frontpage(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "frontpage.html", context)
