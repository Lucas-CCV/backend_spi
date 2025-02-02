from rest_framework import serializers
from .models import Perfil, ItensMercado, ItensCarrinho

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class ItensMercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensMercado
        fields = '__all__'

class ItensCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCarrinho
        fields = '__all__'