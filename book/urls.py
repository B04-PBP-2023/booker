from django.urls import path
from book.views import get_books, search_books

app_name = "book"

urlpatterns = [
    path('', get_books, name='get_books'),
    path('search/', search_books, name='search_books'),
]
