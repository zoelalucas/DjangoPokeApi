from django.urls import path
from . import views


urlpatterns = [
    path('pokemon/<str:pk>/', views.pokemon, name='pokemon'),
    path('', views.pokemonhome),
]