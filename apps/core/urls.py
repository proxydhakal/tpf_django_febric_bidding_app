from django.urls import path
from apps.core import views
from apps.core.views import index

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('submit-list', views.submit_a_listing, name="submit-list"),

]