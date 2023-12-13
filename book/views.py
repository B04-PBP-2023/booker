from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from book.models import Book, BorrowedBook, BoughtBook

# Create your views here.


def get_borrowed(request):
    data = BorrowedBook.objects.all().order_by('pk')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def get_bought(request):
    data = BoughtBook.objects.all().order_by('pk')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def get_books(request):
    data = Book.objects.all().order_by('pk')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def search_books(request):
    query = request.GET.get('q', '')
    if (query == ''):
        data = Book.objects.all().order_by('pk')
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        data = Book.objects.filter(
            name__contains=query).order_by('pk') | Book.objects.filter(author__contains=query).order_by('pk') | Book.objects.filter(genre__contains=query).order_by('pk')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
