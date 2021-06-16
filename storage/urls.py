from django.urls import path
from storage import views


urlpatterns = [
    path('', views.links, name='storage'),
    path('add_link/', views.add_link, name='add_link'),
    path('delete_link/<int:pk>/', views.delete_link, name='delete_link'),
    path('update_link/<int:pk>/', views.update_link, name='update_link'),
    path('favorite_link/<int:pk>/', views.favorite, name='favorite_link'),
    path('favorites/', views.all_favorites, name='favorites'),
]
