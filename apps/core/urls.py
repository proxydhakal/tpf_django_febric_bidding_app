from django.urls import path
from apps.core import views
from apps.core.views import ListCreateView

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('febrics/', views.FebricList.as_view(), name='febrics'),
    path('submit-list/', views.ListCreateView.as_view(), name="submit-list"),
    path('ajax/load-child/', views.load_list, name='ajax_load_lists'), # AJAX


]