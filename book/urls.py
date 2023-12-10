from django.urls import path
from book.views import get_books, search_books, get_borrowed, get_bought

app_name = "book"

urlpatterns = [
    path('', get_books, name='get_books'),
    path('borrowed', get_borrowed, name='get_borrowed'),
    path('bought', get_bought, name='get_bought'),
    path('search/', search_books, name='search_books'),
]
