from django.urls import path
from reviewbuku.views import show_review_buku, get_review_json, add_review, tambah_poin, ubah_rating, get_borrow_json, get_bought_json, get_book_json, get_review_json_flutter, create_product_flutter, tambah_poin_flutter

app_name = 'reviewbuku'

urlpatterns = [
    path('', show_review_buku, name='show_review_buku'),
    path('get-review-json/', get_review_json, name='get_review_json'),
    path('get-review-json-flutter/', get_review_json_flutter, name='get_review_json_flutter'),
    path('get-book-json/', get_book_json, name='get_book_json'),
    path('get-borrow-json/', get_borrow_json, name='get_borrow_json'),
    path('get-bought-json/', get_bought_json, name='get_bought_json'),
    path('add_review/', add_review, name='add_review'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),
    path('tambah_poin/', tambah_poin, name='tambah_poin'),
    path('tambah_poin_flutter/', tambah_poin_flutter, name='tambah_poin_flutter'),
    path('ubah_rating/', ubah_rating, name='ubah_rating'),
]
