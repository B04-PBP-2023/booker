from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from bookshelf.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from book.models import BorrowedBook, BoughtBook
from django.contrib.auth.decorators import login_required
# import requests


@login_required
def show_bookshelf(request):
    context = {}
    return render(request, 'bookshelf.html', context)


@login_required
def get_bookshelf_items(request):
    borrow = request.GET.get('borrow')
    if (borrow == '1'):
        books = []
        items = BorrowedBook.objects.filter(user=request.user)
        for item in items:
            books.append(item.book)
    elif (borrow == '0'):
        books = []
        items = BoughtBook.objects.filter(user=request.user)
        for item in items:
            books.append(item.book)

    return HttpResponse(serializers.serialize("json", books), content_type="application/json")
