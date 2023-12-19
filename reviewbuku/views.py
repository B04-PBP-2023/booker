import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from rest_framework.renderers import JSONRenderer
from book.models import Book, BorrowedBook, BoughtBook, BorrowedBookSerializer, BoughtBookSerializer, BookSerializer, BookReview, BookReviewSerializer


@login_required(login_url='/authentication/login/')
def show_review_buku(request):
    global id
    id = request.GET.get('id')
    book = Book.objects.get(pk=id)
    books_review = BookReview.objects.filter(id=1)
    user = request.user

    context = {
        'books_review': books_review,
        'book': book,
        'user': user,
    }
    return render(request, "reviewbuku.html", context)


@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rate')
        review_text = request.POST.get('review_text')
        book_id = request.POST.get('quantity')
        user_id = request.POST.get('user_id')

        book_review = BookReview(
            rating=rating, review_text=review_text, book_id=book_id, user=request.user)
        book_review.save()

        return HttpResponse(b"CREATED", status=201)


@csrf_exempt
def tambah_poin(request):
    user = request.user
    user.points += 10
    user.save()
    return redirect('reviewbuku:add_review')


@csrf_exempt
def tambah_poin_flutter(request):
    if request.method == 'POST':

        book_review = BookReview.objects.filter(
            book_id=request.POST.get("book_id"))
        juml = 0
        for item in book_review:
            juml += item.rating
        if len(book_review) != 0:
            total_rating = juml / len(book_review)
            total_rating_round = round(total_rating, 1)
            book = Book.objects.get(pk=request.POST.get("book_id"))
            book.rating = total_rating_round
            book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def ubah_rating(request):
    book_review = BookReview.objects.filter(book_id=id)
    juml = 0
    for item in book_review:
        juml += item.rating
    if len(book_review) != 0:
        total_rating = juml / len(book_review)
        total_rating_round = round(total_rating, 1)
        book = Book.objects.get(pk=id)
        book.rating = total_rating_round
        book.save()
    return HttpResponse(b"CREATED", status=201)


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        new_product = BookReview.objects.create(
            user=request.user,
            book_id=int(request.POST.get("book_id")),
            rating=int(request.POST.get("rating")),
            review_text=request.POST.get("review_text"),
        )
        new_product.save()
        user = request.user
        user.points += 10
        user.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


def get_review_json(request):
    review_item = BookReview.objects.filter(book_id=id)
    serializer_books = BookReviewSerializer(review_item, many=True)
    return HttpResponse(JSONRenderer().render(serializer_books.data), content_type='application/json')


def get_review_json_flutter(request):
    review_item = BookReview.objects.all()
    serializer_books = BookReviewSerializer(review_item, many=True)
    return HttpResponse(JSONRenderer().render(serializer_books.data), content_type='application/json')


def get_book_json(request):
    books = Book.objects.filter(id=id)
    serialized_books = BookSerializer(books, many=True)
    return HttpResponse(JSONRenderer().render(serialized_books.data), content_type="application/json")


def get_borrow_json(request):
    books = BorrowedBook.objects.filter(user=request.user)
    serialized_books = BorrowedBookSerializer(books, many=True)
    return HttpResponse(JSONRenderer().render(serialized_books.data), content_type="application/json")


def get_bought_json(request):
    books = BoughtBook.objects.filter(user=request.user)
    serialized_books = BoughtBookSerializer(books, many=True)
    return HttpResponse(JSONRenderer().render(serialized_books.data), content_type="application/json")
