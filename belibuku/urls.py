from django.urls import path
from belibuku.views import show_beli_buku, pembelian, pembelian_dengan_poin

app_name = 'belibuku'

urlpatterns = [
    path('', show_beli_buku, name='show_beli_buku'),
    path('pembelian/', pembelian, name='pembelian'),
    path('pembelian-dengan-poin/', pembelian_dengan_poin,
         name='pembelian_dengan_poin'),
]
