from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Perfil, ItensMercado, ItensCarrinho
from .serializers import PerfilSerializer, ItensMercadoSerializer, ItensCarrinhoSerializer

# Create your views here.

class perfilMercadoAPIView(APIView):
    serializer_class = {"perfil":PerfilSerializer, "itensMercado" :ItensMercadoSerializer}

    def get(self, request, *args, **kwargs):
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

class perfilCarrinhoAPIView(APIView):
    serializer_class = {"perfil":PerfilSerializer, "itensMercado" :ItensMercadoSerializer, "itensCarrinho": ItensCarrinhoSerializer}

    def get(self, request, *args, **kwargs):
        response = {}
        if(request.query_params != {}):
            nameTagGet = request.query_params['nameTag']
            perfis = Perfil.objects.filter(nameTag=nameTagGet)
            if(len(perfis) != 0):
                itensCarrinho = ItensCarrinho.objects.filter(perfilComprador=perfis[0].id_perfil)
                serializerItensCarrinho = ItensCarrinhoSerializer(itensCarrinho, many=True)
                response["ItensCarrinhos"] = serializerItensCarrinho.data

        return Response(response)
    
    def patch(self, request, *args, **kwargs):
        id = request.query_params["id"]
        itemCarrinho = ItensCarrinho.objects.get(id_ItemCarrinho=id)

        data = request.data

        itemCarrinho.id_ItemCarrinho = data.get("id_ItemCarrinho", itemCarrinho.id_ItemCarrinho)
        itemCarrinho.itensMercado    = data.get("itensMercado", itemCarrinho.itensMercado)
        itemCarrinho.perfilComprador = data.get("perfilComprador", itemCarrinho.perfilComprador)
        itemCarrinho.detalhes        = data.get("detalhes", itemCarrinho.detalhes)
        itemCarrinho.tipoCor         = data.get("tipoCor", itemCarrinho.tipoCor)
        itemCarrinho.tipoFundo       = data.get("tipoFundo", itemCarrinho.tipoFundo)

        itemCarrinho.save()

        serialzer = ItensCarrinhoSerializer(itemCarrinho)
        return Response(serialzer.data)