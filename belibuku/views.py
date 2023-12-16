from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
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
@require_http_methods(["GET", "POST"])
def pembelian(request):
    try:
        if (request.method == "GET"):
            id = int(request.GET.get('id'))
            book = Book.objects.get(pk=id)
        else:
            id = int(request.GET.get('id'))
            book = Book.objects.get(pk=id)
    except:
        if (request.method == "GET"):
            return HttpResponseBadRequest()
        else:
            return JsonResponse({
                "created": False,
                "message": "Gagal membeli buku."
            }, status=301)

    if (not book.for_sale):
        if (request.method == "GET"):
            return HttpResponseBadRequest()
        else:
            return JsonResponse({
                "created": False,
                "message": "Gagal membeli buku."
            }, status=301)

    user = request.user
    new_bought_book = BoughtBook(user=user, book=book)
    new_bought_book.save()
    if (request.method == "GET"):
        return HttpResponse(b"CREATED", status=201)
    else:
        return JsonResponse({
            "created": True,
            "message": "Berhasil membeli buku."
        }, status=201)


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
