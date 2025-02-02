from django.urls import path
from . import views

urlpatterns = [
    path('perfilMercado', views.perfilMercadoAPIView.as_view()),
    path('perfilCarrinho', views.perfilCarrinhoAPIView.as_view()),
    path('perfilCompras', views.perfilCompraAPIView.as_view())
]
