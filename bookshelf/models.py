from django.db import models
from authentication.models import User

from book.models import Book

class Category(models.Model):
    name = models.CharField(max_length=50)

class Bookshelf(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)