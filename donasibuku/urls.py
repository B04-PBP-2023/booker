from django.urls import path
from donasibuku.views import show_donasi_buku

app_name = 'donasibuku'

urlpatterns = [
    path('', show_donasi_buku, name='show_donasi_buku'),
]
