from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from bookshelf.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date

# import requests

def show_bookshelf(request):
    selected_category = request.GET.get('category')
    sort_by = request.GET.get('sort_by', 'default')
    books = Book.objects.all()

    if selected_category:
        books = books.filter(category=selected_category)

    if sort_by == 'borrowed_date':
        books = books.order_by('borrowed_date')
    elif sort_by == 'bought_date':
        books = books.order_by('bought_date')
    else:
        books = books.order_by('borrowed_date', 'bought_date')

    context = {
        'books': books,
        'selected_category': selected_category,
        'sort_by': sort_by,
    }

    return render(request, 'bookshelf.html', context)

def filter_books(request):
    genre = request.GET.get('genre')
    is_borrowed = request.GET.get('borrowed')
    is_purchased = request.GET.get('purchased')

    books = Book.objects.all()

    if genre:
        books = books.filter(genre=genre)

    if is_borrowed:
        books = books.filter(is_borrowed=True)

    if is_purchased:
        books = books.filter(is_purchased=True)

    return render(request, 'books/filter_books.html', {'books': books})

def return_book_early(request, id):
    try:
        book = Book.objects.get(pk=id)
        
        if book.due_date is None:
            return HttpResponse("Buku ini telah dibeli")
        
        if book.due_date >= date.today():
            book.borrowed_date = date.today()
            book.save()
            return redirect(reverse('bookshelf:show_bookshelf'))
        else:
            book.delete()
            return HttpResponse("Buku ini telah dikembalikan.")
    except Book.DoesNotExist:
        return HttpResponse("Buku tidak ditemukan.")

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_books_json(request):
    books = Book.objects.filter().order_by('borrowed_date', 'bought_date')
    return HttpResponse(serializers.serialize('json', books))