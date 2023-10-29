from django.urls import path
from pinjambuku.views import show_pinjam_buku, peminjaman

app_name = 'pinjambuku'

urlpatterns = [
    path('', show_pinjam_buku, name='show_pinjam_buku'),
    path('peminjaman/', peminjaman, name='peminjaman'),
]
