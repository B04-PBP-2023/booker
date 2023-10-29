from bookshelf.views import show_bookshelf, add_to_bookshelf_ajax, get_recommendations, view_bookmarks, show_bookshelf_json, show_xml, show_xml_by_id, show_json_by_id
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bookshelf'

urlpatterns = [
    path('', show_bookshelf, name='show_bookshelf'),
    path('add/<int:book_id>/', add_to_bookshelf_ajax, name='add_to_bookshelf_ajax'),
    path('rated/', get_recommendations, name='get_recommendations'),
    path('view/', view_bookmarks, name='view_bookmarks'),
    path('json/', show_bookshelf_json, name="show_bookshelf_json"),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)