from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_req, name="register"),
    path('login/', views.login_req, name="login"),
    path('logout/', views.logout_req, name="logout"),
    path('login_flutter/', views.login_flutter, name="login_flutter"),
]
