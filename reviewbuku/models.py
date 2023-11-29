from django.db import models
from authentication.models import User
from book.models import Book

# Create your models here.

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