from rest_framework import serializers
from .models import *

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

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class ItemCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemcompra
        fields = '__all__'

class MidiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = midia
        fields = '__all__'