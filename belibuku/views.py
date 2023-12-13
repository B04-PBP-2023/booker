from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core import serializers
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from book.models import BoughtBook, Book
from authentication.models import User
from datetime import datetime, timedelta, date

# Create your views here.


@login_required(login_url='/authentication/login/')
def show_beli_buku(request):
    id = request.GET.get('id')
    book = Book.objects.get(pk=id)
    context = {
        'id': id,
        'book': book,
    }
    return render(request, 'belibuku.html', context)


@csrf_exempt
@login_required(login_url='/authentication/login/')
@require_http_methods(["GET"])
def pembelian(request):
    try:
        id = int(request.GET.get('id'))
        book = Book.objects.get(pk=id)
    except:
        return HttpResponseBadRequest()

    if ((not book.for_sale) or (book.price is None)):
        if (book.price is None):
            book.for_sale = False
            book.save()
        return HttpResponseBadRequest()

    user = request.user
    new_bought_book = BoughtBook(user=user, book=book)
    new_bought_book.save()
    return HttpResponse(b"CREATED", status=201)


@csrf_exempt
@login_required(login_url='/authentication/login/')
@require_http_methods(["GET"])
def pembelian_dengan_poin(request):
    user = request.user
    if (user.points >= 100):
        try:
            id = int(request.GET.get('id'))
            book = Book.objects.get(pk=id)
        except:
            return HttpResponseBadRequest()
        new_bought_book = BoughtBook(user=user, book=book)
        new_bought_book.save()
        user.points -= 100
        user.save()
        return HttpResponse(b"CREATED", status=201)
    else:
        return HttpResponse(b"Unprocessable", status=422)
