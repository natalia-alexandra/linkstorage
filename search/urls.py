from django.urls import path
from . import views


urlpatterns = [
    path('', views.search, name='search'),
    path('search_result/', views.search, name='search_result'),
]
