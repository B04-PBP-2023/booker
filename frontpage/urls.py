from django.urls import path
from frontpage.views import show_frontpage, bookshelf_view

app_name = 'main'

urlpatterns = [
    path('', show_frontpage, name='show_frontpage'),
]
