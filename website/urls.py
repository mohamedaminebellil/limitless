from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', views.signIN, name='signIN'),
    path('sign-up/', views.register, name='register'),
    path('netflix/', views.netflix_page, name='netflix_page'),
    path('spotify/', views.spotify_page, name='spotify_page'),
    path('about/', views.about, name='about'),
]
