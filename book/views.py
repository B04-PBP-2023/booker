from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from book.models import Book
# Create your views here.


def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def search_books(request):
    query = request.GET.get('q', '')
    if (query == ''):
        data = Book.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        data = Book.objects.filter(
            name__contains=query) | Book.objects.filter(author__contains=query) | Book.objects.filter(genre__contains=query)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
