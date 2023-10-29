from audioop import avg
import json
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from bookshelf.forms import BookshelfForm
from bookshelf.models import Book, Bookmark, Bookshelf
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_bookshelf(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'bookshelf.html', context)

# def add_to_bookshelf(request):
#     form = BookshelfForm(request.POST or None)
#     if form.is_valid() and request.method == "POST":
#         book = form.save(commit=False)
#         book.user = request.user
#         book.save()
#     context = {'form': form}
#     return HttpResponseRedirect(reverse('bookshelf:show_bookshelf'))

@login_required
def show_bookshelf_json(request):
    user = request.user
    data = Bookshelf.objects.filter(user=user)
    serialized_data = []

    for item in data:
        modeldata = {
            'fields' : {
                'name' : item.book.name,
                'author' : item.book.author,
                'year' : item.book.year,
                'genre' : item.book.genre,
                'price' : item.book.price,
                'rating' : item.book.rating
            },
            'pk' : item.book.pk
        }
        serialized_data.append(modeldata)
    json_data = json.dumps(serialized_data)
    return HttpResponse(json_data, content_type="application/json")

def get_recommendations(request):
    data = Book.objects.order_by('-rating')[:10]
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_bookmarks(request):
    user = request.user
    bookmarked_books = Bookmark.objects.filter(user=user)
    return render(request, 'bookmarked.html', bookmarked_books)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@login_required
def add_to_bookshelf_ajax(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookshelfForm({
        'book' : book, 
        'user' : request.user,
    })
    print(form.errors)
    if form.is_valid() and request.method == "POST":
        bookshelf = form.save(commit=False)
        bookshelf.user = request.user
        bookshelf.save()
        return HttpResponse(b"CREATED", status=201)