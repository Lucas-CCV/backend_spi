from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import copy

# Create your views here.

class perfilMercadoAPIView(APIView):
    serializer_class = ItensMercadoSerializer

    def get(self, request, *args, **kwargs):
        response = {}
        if(request.query_params != {}):
            nameTagGet = request.query_params['nameTag']
            perfis = Perfil.objects.filter(nameTag=nameTagGet)
            print(perfis)
            if(len(perfis) != 0):
                itensMercado = ItensMercado.objects.filter(id_Perfil=perfis[0].id_Perfil)
                serializerItensMercado = ItensMercadoSerializer(itensMercado, many=True)
                response["ItensMercado"] = serializerItensMercado.data

        else:
            perfis = Perfil.objects.all()

        serializerPerfil = PerfilSerializer(perfis, many=True)
        response["perfil"] = serializerPerfil.data
        
        return Response(response)

class perfilCarrinhoAPIView(APIView):
    serializer_class = ItensCarrinhoSerializer

    def get(self, request, *args, **kwargs):
        response = {}
        if(request.query_params != {}):
            nameTagGet = request.query_params['nameTag']
            perfis = Perfil.objects.filter(nameTag=nameTagGet)
            if(len(perfis) != 0):
                itensCarrinho = ItensCarrinho.objects.filter(perfilComprador=perfis[0].id_Perfil)
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
    
    def post(self, request, *args, **kwargs):

        itemMercado = ItensMercado.objects.get(id_ItemMercado=request.data["itensMercado"])
        perfilComprador = Perfil.objects.get(id_Perfil=request.data["perfilComprador"])
        
        itemCarrinho = ItensCarrinho.objects.create(itensMercado    = itemMercado,
                                                    perfilComprador = perfilComprador,
                                                    detalhes        = request.data["detalhes"],
                                                    tipoCor         = request.data["tipoCor"],
                                                    tipoFundo       = request.data["tipoFundo"])

        serializer = ItensCarrinhoSerializer(itemCarrinho)

        return Response(serializer.data)
    
class perfilCompraAPIView(APIView):
    serializer_class = ComprasSerializer

    def get(self, request, *args, **kwargs):
        response = {}
        if(request.query_params != {}):
            nameTagGet = request.query_params['nameTag']
            perfis = Perfil.objects.filter(nameTag=nameTagGet)
            if(len(perfis) != 0):
                compras = Compra.objects.filter(perfilComprador=perfis[0].id_Perfil)
                response["Compras"] = []

                for compra in compras:
                    itensCompra = Itemcompra.objects.filter(id_Crompra=compra.id_Crompra)

                    for itemCompra in itensCompra:
                        itemMercado   = ItensMercado.objects.get(id_ItemMercado=itemCompra.id_ItensMercado.id_ItemMercado)
                        perfilArtista = Perfil.objects.get(id_Perfil=itemMercado.id_Perfil.id_Perfil)

                        print(itemMercado.foto.name)

                        compraDict = {}

                        compraDict["id"]               = itemCompra.id_Crompra.id_Crompra
                        compraDict["imagem"]           = F"/media/{itemMercado.foto.name}"
                        compraDict["data_pedido"]      = compra.dataPedido
                        compraDict["data_entrega"]     = itemCompra.dataEntrega
                        compraDict["nome_artista"]     = perfilArtista.nome
                        compraDict["status"]           = itemCompra.estatus
                        compraDict["alerta"]           = itemCompra.alerta
                        compraDict["metodo_pagamento"] = compra.metodoPagamento
                        compraDict["tipo_pedido"]      = itemMercado.nome
                        compraDict["preco_pedido"]     = itemMercado.preco
                        compraDict["adicionais"]       = [{"nome":itemCompra.tipoCor, "valor":itemMercado.tiposCor[itemCompra.tipoCor]},
                                                          {"nome":itemCompra.tipoFundo, "valor":itemMercado.tiposFundo[itemCompra.tipoFundo]}]
                        compraDict["detalhes_pedido"]  = {"particao": itemCompra.particao, "cupom":itemCompra.cupom}

                    response["Compras"].append(compraDict)

        return Response(response)        