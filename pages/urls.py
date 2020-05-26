from django.urls import path
from . import views
from .views import HomePageView, FriendsView, GamesView


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('home', views.LoginView.as_view(), name='on_login'),
    path('friends', views.FriendsView.as_view(), name='friends'),
    path('games', views.GamesView.as_view(), name='games')
]