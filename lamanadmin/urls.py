from django.urls import path
from lamanadmin.views import page_admin, get_items_json
app_name = 'lamanadmin'

urlpatterns = [
    path('page_admin/', page_admin, name='page_admin'),
    path('get_items_json/', get_items_json, name='get_items_json'),
]
