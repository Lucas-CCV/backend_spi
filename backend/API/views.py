from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from perfil.models import Perfil, ItensMercado
from .serializers import PerfilSerializer, ItensMercadoSerializer

# Create your views here.

@api_view(['GET'])
def pegarPerfil(request):
    print(request.query_params)
    response = {}
    if(request.query_params != {}):
        nameTagGet = request.query_params['nameTag']
        perfis = Perfil.objects.filter(nameTag=nameTagGet)
        print(perfis)
        if(len(perfis) != 0):
            itensMercado = ItensMercado.objects.filter(perfil=perfis[0].id_perfil)
            serializerItensMercado = ItensMercadoSerializer(itensMercado, many=True)
            response["ItensMercado"] = serializerItensMercado.data

    else:
        perfis = Perfil.objects.all()

    serializerPerfil = PerfilSerializer(perfis, many=True)
    response["perfil"] = serializerPerfil.data
    
    return Response(response)

@api_view(['POST'])
def criarPerfil(request):
    serializer = PerfilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer)