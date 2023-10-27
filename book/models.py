from django.db import models
from authentication.models import User
# Create your models here.


class Book(models.Model):
    name = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    reviews = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=False, blank=False, default=10)
    points_to_exchange = models.IntegerField(
        null=False, blank=False, default=100)
    for_sale = models.BooleanField(null=False, blank=False, default=True)


class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()


class BoughtBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    bought_date = models.DateField(auto_now_add=True)
