# from django.contrib import admin
# from django.urls import include, path
# from . import views

# urlpatterns = [
#     path('', views.sign_in),
# ]

from django.urls import path
from . import views
from main.views import home

# app_name = "main"   

urlpatterns = [
  # path("register", views.register_request, name="register"),
  # path("", views.login_request, name="login"),
  # path("logout", views.logout_request, name= "logout"),  
]