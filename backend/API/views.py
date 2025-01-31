from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from perfil.models import Perfil
from .serializers import PerfilSerializer

# Create your views here.

@api_view(['GET'])
def pegarPerfil(request):
    print(request.query_params)
    if(request.query_params != {}):
        nameTagGet = request.query_params['nameTag']
        perfis = Perfil.objects.filter(nameTag=nameTagGet)
    else:
        perfis = Perfil.objects.all()

    serializer = PerfilSerializer(perfis, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criarPerfil(request):
    serializer = PerfilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer)