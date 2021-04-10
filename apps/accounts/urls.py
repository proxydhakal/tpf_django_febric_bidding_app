from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from apps.accounts.views import profile, SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    # path('signup/success/', views.success, name='success'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', SignUpView.as_view(), name='register'),

   
]
