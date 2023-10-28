from django.urls import path
from frontpage.views import show_frontpage

app_name = 'frontpage'

urlpatterns = [
    path('', show_frontpage, name='show_frontpage'),
]
