from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.pegarPerfil),
    path('user/', views.criarPerfil),
]
