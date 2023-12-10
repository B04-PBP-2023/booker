from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.core import serializers
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from book.models import BorrowedBook, Book
from datetime import datetime, timedelta, date
from authentication.models import User
# Create your views here.


@login_required(login_url='/authentication/login/')
def show_pinjam_buku(request):
    id = request.GET.get('id')
    book = Book.objects.get(pk=id)
    context = {
        'id': id,
        'book': book,
    }
    return render(request, 'pinjambuku.html', context)


# Fungsi mengembalikan buku
@csrf_exempt
@login_required
@require_http_methods(["GET"])
def pengembalian(request):
    id = request.GET.get('id')
    user = request.user
    book = Book.objects.get(pk=id)
    borrowed_book = BorrowedBook.objects.get(book=book)
    try:
        borrowed_book.delete()
        user.points += 10
        user.save()
    except:
        return HttpResponseBadRequest()
    return HttpResponseRedirect(reverse('bookshelf:show_bookshelf'))


@csrf_exempt
@login_required(login_url='/authentication/login/')
@require_http_methods(["GET"])
def peminjaman(request):
    try:
        id = int(request.GET.get('id'))
        durasi = int(request.GET.get('durasi'))
        book = Book.objects.get(pk=id)
    except:
        return HttpResponseBadRequest()

    if (not (1 <= durasi <= 7)):
        return HttpResponseBadRequest()

    user = request.user
    start_date = date.today()
    end_date = start_date + timedelta(days=durasi)
    new_borrowed_book = BorrowedBook(
        user=user, book=book, start_date=start_date, end_date=end_date)
    new_borrowed_book.save()
    return HttpResponse(b"CREATED", status=201)
