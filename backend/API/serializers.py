from rest_framework import serializers
from perfil.models import Perfil, ItensMercado

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class ItensMercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensMercado
        fields = '__all__'