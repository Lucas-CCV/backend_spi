from rest_framework import viewsets
from perfil import models
from API import serializers

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PerfilSerializer
    queryset = models.Perfil.objects.all()
    lookup_field = 'nameTag'
