from django.urls import path
from donasibuku.views import show_donasi_buku, donasi_buku_mobile

app_name = 'donasibuku'

urlpatterns = [
    path('', show_donasi_buku, name='show_donasi_buku'),
    path('donasi-mobile/', donasi_buku_mobile, name='donasi_buku_mobile'),
]
