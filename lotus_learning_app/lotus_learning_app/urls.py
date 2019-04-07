from django.urls import include, path  # For django versions from 2.0 and up
from django.conf.urls import include, url  # For django versions before 2.0
from django.conf import settings
from django.contrib import admin
from django.urls import path
from lotus_logic.views import HomeView, NewVideo, LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('new_video/', NewVideo.as_view())
]
