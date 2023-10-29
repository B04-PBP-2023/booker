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
from book.models import BorrowedBook, Book, BoughtBook
from datetime import datetime, timedelta, date
# Create your views here.


@login_required(login_url='/authentication/login/')
def show_review_buku(request):
    id = request.GET.get('id')
    book = Book.objects.get(pk=id)
    context = {
        'id': id,
        'book': book,
    }
    return render(request, 'reviewbuku.html', context)


@csrf_exempt
@login_required(login_url='/authentication/login/')
@require_http_methods(["GET"])
def review(request):
    user = request.user
    try:
        id = int(request.GET.get('id'))
        rating = int(request.GET.get('rating'))
        book = Book.objects.get(pk=id)
    except Exception:
        return HttpResponseBadRequest()

    if (not (BorrowedBook.objects.filter(user=user, book=book).exists() or BoughtBook.objects.filter(user=user, book=book).exists)):
        return HttpResponseBadRequest()

    if (not (1 <= rating <= 5)):
        return HttpResponseBadRequest()

    review_count = book.reviews
    rating_before = book.rating
    rating_after = ((rating_before * review_count) + rating)/(review_count + 1)
    book.reviews += 1
    book.rating = round(rating_after, 2)
    book.save()

    user.points += 10
    user.save()

    return HttpResponse(b"CREATED", status=201)
