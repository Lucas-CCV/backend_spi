from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

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

        itemCarrinho.detalhes        = data.get("detalhes", itemCarrinho.detalhes)
        itemCarrinho.tipoCor         = data.get("tipoCor", itemCarrinho.tipoCor)
        itemCarrinho.tipoFundo       = data.get("tipoFundo", itemCarrinho.tipoFundo)

        itemCarrinho.save()

        serialzer = ItensCarrinhoSerializer(itemCarrinho)
        return Response(serialzer.data)
    
class perfilCompraAPIView(APIView):
    serializer_class = {"perfil":PerfilSerializer, "itensMercado" :ItensMercadoSerializer, "itensCompra": ItemCompraSerializer}

    def get(self, request, *args, **kwargs):
        response = {}
        if(request.query_params != {}):
            nameTagGet = request.query_params['nameTag']
            perfis = Perfil.objects.filter(nameTag=nameTagGet)
            if(len(perfis) != 0):
                compras = Compra.objects.filter(perfilComprador=perfis[0].id_perfil)
                response["Compras"] = []

                for compra in compras:
                    ItensCompra = Itemcompra.objects.filter(id_Crompra=compra.id_Crompra)

                    serializerCompra = ComprasSerializer(compra)
                    serializerItensCompra = ItemCompraSerializer(ItensCompra, many=True)

                    response["Compras"].append([serializerCompra.data, serializerItensCompra.data])

        return Response(response)        