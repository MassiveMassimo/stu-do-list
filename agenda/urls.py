from django.urls import path
from .views import index, add_agenda

urlpatterns = [
    path('', index, name='index'),
    path('add', add_agenda, name='add')
]