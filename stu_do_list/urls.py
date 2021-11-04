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
import authentication.urls as login
import agenda.urls as agenda
import ask_a_mentor.urls as ask_a_mentor
import jadwal_belajar_bareng.urls as jadwal_belajar_bareng
import notes.urls as notes
import schedule_kuliah.urls as schedule_kuliah
import study_communities.urls as study_communities
import video_playlist.urls as video_playlist
import authentication.views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', include(login)),
    path('agenda/', include(agenda)),
    path('ask-a-mentor/', include(ask_a_mentor)),
    path('jadwal-belajar-bareng/', include(jadwal_belajar_bareng)),
    path('notes/', include(notes)),
    path('schedule-kuliah/', include(schedule_kuliah)),
    path('study-communities/', include(study_communities)),
    path('video-playlist/', include(video_playlist)),
    # path("register", login_views.register_request, name="register")
]
