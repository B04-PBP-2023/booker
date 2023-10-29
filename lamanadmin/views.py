from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from book.models import Book
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def page_admin(request):
    books = Book.objects.all() 
    return render(request, 'page_admin.html', {'books': books})

def get_items_json(request):
    book_products = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_products), content_type="application/json")