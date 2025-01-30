from django.urls import path
from . import views

urlpatterns = [
    path('getUser/', views.pegarPerfil),
    path('postUser/', views.criarPerfil),
]
