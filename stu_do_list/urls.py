"""stu_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sign-in/', include('authentication.urls')),
    path('agenda/', include('agenda.urls')),
    path('ask-a-mentor/', include('ask_a_mentor.urls')),
    path('jadwal-belajar-bareng/', include('jadwal_belajar_bareng.urls')),
    path('notes/', include('notes.urls')),
    path('schedule-kuliah/', include('schedule_kuliah.urls')),
    path('study-communities/', include('study_communities.urls')),
    path('video-playlist/', include('video_playlist.urls'))
]
