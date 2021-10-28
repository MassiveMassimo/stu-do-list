from django.urls import path
from .views import index, add_agenda, remove_agenda

urlpatterns = [
    path('', index, name='index'),
    path('add', add_agenda, name='addagenda'),
    path('remove/<str:pk>/', remove_agenda, name = 'removeagenda'),
]