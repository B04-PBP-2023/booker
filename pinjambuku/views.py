from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, JsonResponse
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
@require_http_methods(["GET", "POST"])
def pengembalian(request):
    if (request.method == "GET"):
        id = request.GET.get('id')
    else:
        id = request.POST.get('id')
    user = request.user
    book = Book.objects.get(pk=id)
    try:
        borrowed_book = BorrowedBook.objects.get(user=user, book=book)
        borrowed_book.delete()
        # borrowed_book = BorrowedBook.objects.filter(user=user, book=book)
        # for b in borrowed_book:
        #     b.delete()
        user.points += 10
        user.save()
    except Exception as e:
        print(e)
        if (request.method == "GET"):
            return HttpResponseBadRequest()
        else:
            return JsonResponse({
                "success": False,
                "message": "Gagal mengembalikan buku."
            }, status=301)
    if (request.method == "GET"):
        return HttpResponseRedirect(reverse('bookshelf:show_bookshelf'))
    else:
        return JsonResponse({
            "success": True,
            "message": "Berhasil mengembalikan buku."
        }, status=201)


@csrf_exempt
@login_required(login_url='/authentication/login/')
@require_http_methods(["GET", "POST"])
def peminjaman(request):
    user = request.user
    try:
        if (request.method == "GET"):
            id = int(request.GET.get('id'))
            durasi = int(request.GET.get('durasi'))
            book = Book.objects.get(pk=id)
        else:
            id = int(request.POST.get('id'))
            durasi = int(request.POST.get('durasi'))
            book = Book.objects.get(pk=id)

        try:
            borrowed_book = BorrowedBook.objects.get(user=user, book=book)
        except:
            borrowed_book = None

        if (borrowed_book != None):
            if (request.method == "GET"):
                return HttpResponseBadRequest()
            else:
                return JsonResponse({
                    "created": False,
                    "message": "Buku tersebut sedang anda pinjam."
                }, status=301)

    except Exception as e:
        if (request.method == "GET"):
            return HttpResponseBadRequest()
        else:
            return JsonResponse({
                "created": False,
                "message": "Gagal meminjam buku."
            }, status=301)

    if (not (1 <= durasi <= 7)):
        if (request.method == "GET"):
            return HttpResponseBadRequest()
        else:
            return JsonResponse({
                "created": False,
                "message": "Gagal meminjam buku."
            }, status=301)

    user = request.user
    start_date = date.today()
    end_date = start_date + timedelta(days=durasi)
    new_borrowed_book = BorrowedBook(
        user=user, book=book, start_date=start_date, end_date=end_date)
    new_borrowed_book.save()
    if (request.method == "GET"):
        return HttpResponse(b"CREATED", status=201)
    else:
        return JsonResponse({
            "created": True,
            "message": "Berhasil meminjam buku."
        }, status=201)
