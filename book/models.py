from django.db import models
from authentication.models import User
from rest_framework import serializers as rest_serializers
# Create your models here.


class Book(models.Model):
    name = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True, default=5)
    reviews = models.IntegerField(null=True, blank=True, default=1)
    price = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True, default=10)
    points_to_exchange = models.IntegerField(
        null=True, blank=True, default=100)
    for_sale = models.BooleanField(null=True, blank=True, default=True)


class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()


class BoughtBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    bought_date = models.DateField(auto_now_add=True)

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()

class BookSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowedBookSerializer(rest_serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BorrowedBook
        fields = ('user', 'book', 'start_date', 'end_date')


class BoughtBookSerializer(rest_serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BoughtBook
        fields = ('user', 'book', 'bought_date')

class BookReviewSerializer(rest_serializers.ModelSerializer):
    user_name = rest_serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BookReview
        fields = ['id', 'user', 'user_name', 'book', 'rating', 'review_text']
