from django.contrib import admin
from django.urls import path
from lotus_logic.views import HomeView, MainView, NewVideo, LoginView, RegisterView

urlpatterns = [
    path('', MainView.as_view()),
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view()),
    path('welcome/', MainView.as_view()),
    path('signin/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('new_video/', NewVideo.as_view())
]
