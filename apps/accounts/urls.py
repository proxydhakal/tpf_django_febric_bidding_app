from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from apps.accounts.views import profile
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path('profile/', profile, name='profile'),
    # path('<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
]
