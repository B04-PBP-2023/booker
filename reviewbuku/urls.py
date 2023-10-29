from django.urls import path
from reviewbuku.views import show_review_buku, review

app_name = 'reviewbuku'

urlpatterns = [
    path('', show_review_buku, name='show_review_buku'),
    path('review/', review, name='review'),
]
