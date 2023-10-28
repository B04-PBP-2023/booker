from bookshelf.views import show_bookshelf, get_bookshelf_items
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bookshelf'

urlpatterns = [
    path('', show_bookshelf, name='show_bookshelf'),
    path('get-bookshelf/', get_bookshelf_items, name='get_bookshelf_items'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
