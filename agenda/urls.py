from django.urls import path
from .views import *

app_name = "agenda"

urlpatterns = [
    path('', index, name='index'),
    path('add', add_agenda, name='add'),
    path('get', get_agenda, name='get'),
    # path('get/<str:user_id>', get_agenda, name='get'),
    path('delete/<str:agenda_id>', delete_agenda, name='delete'),
]