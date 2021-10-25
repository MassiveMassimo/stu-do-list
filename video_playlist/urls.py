from django.urls import path
from .views import index
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', index, name='index'),
  path('add-video', add_video, name='add'),
  path('admin/login/', auth_views.LoginView.as_view()),
]