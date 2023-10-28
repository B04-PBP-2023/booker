from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

class Bookshelf(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     bought_date = models.DateField()
#     borrowed_date = models.DateField(null=True, blank=True)
#     due_date = models.DateField(null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
#     def __str__(self):
#         return self.title

# class User(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bookshelf = models.ManyToManyField(Book)