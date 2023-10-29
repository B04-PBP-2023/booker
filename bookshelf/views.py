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

from book.models import BorrowedBookSerializer, BoughtBookSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# import requests


@login_required(login_url='/authentication/login/')
def show_bookshelf(request):
    context = {}
    return render(request, 'bookshelf.html', context)


@login_required(login_url='/authentication/login/')
def get_bookshelf_items(request):
    borrow = request.GET.get('borrow')
    if (borrow == '1'):
        books = BorrowedBook.objects.filter(user=request.user)
        serialized_books = BorrowedBookSerializer(books, many=True)
    elif (borrow == '0'):
        books = BoughtBook.objects.filter(user=request.user)
        serialized_books = BoughtBookSerializer(books, many=True)
    return HttpResponse(JSONRenderer().render(serialized_books.data), content_type="application/json")


@login_required(login_url='/authentication/login/')
def search_bookshelf_items(request):
    borrow = request.GET.get('borrow')
    q = request.GET.get('q')
    if (borrow == '1'):
        if (q == ''):
            books = BorrowedBook.objects.filter(user=request.user)
            serialized_books = BorrowedBookSerializer(books, many=True)
            return HttpResponse(JSONRenderer().render(serialized_books.data), content_type="application/json")
        books = BorrowedBook.objects.filter(
            user=request.user, book__name__contains=q) | BorrowedBook.objects.filter(
            user=request.user, book__author__contains=q) | BorrowedBook.objects.filter(
            user=request.user, book__genre__contains=q)
        serialized_books = BorrowedBookSerializer(books, many=True)
    elif (borrow == '0'):
        if (q == ''):
            books = BoughtBook.objects.filter(user=request.user)
            serialized_books = BoughtBookSerializer(books, many=True)
            return HttpResponse(JSONRenderer().render(serialized_books.data), content_type="application/json")
        books = BoughtBook.objects.filter(
            user=request.user, book__name__contains=q) | BoughtBook.objects.filter(
            user=request.user, book__author__contains=q) | BoughtBook.objects.filter(
            user=request.user, book__genre__contains=q)
        serialized_books = BoughtBookSerializer(books, many=True)
    return HttpResponse(JSONRenderer().render(serialized_books.data), content_type="application/json")
