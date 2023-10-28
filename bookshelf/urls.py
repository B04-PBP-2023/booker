from bookshelf.views import show_bookshelf, filter_books, return_book_early, show_xml, show_json, show_xml_by_id, show_json_by_id,get_books_json
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bookshelf'

urlpatterns = [
    path('', show_bookshelf, name='show_bookshelf'),
    path('filter-books/', filter_books, name='filter_books'),
    path('return_book/<int:book_id>/', return_book_early, name='return_book'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('get-books/', get_books_json, name='get_books_json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)