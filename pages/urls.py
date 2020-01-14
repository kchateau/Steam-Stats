from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('home', views.LoginView.as_view(), name='on_login'),
]