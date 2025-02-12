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
            if(len(perfis) != 0):
                itensMercado = ItensMercado.objects.filter(id_Perfil=perfis[0].id_Perfil)
                serializerItensMercado = ItensMercadoSerializer(itensMercado, many=True)
                response["ItensMercado"] = serializerItensMercado.data

        else:
            perfis = Perfil.objects.all()

        serializerPerfil = PerfilSerializer(perfis, many=True)
        response["perfil"] = serializerPerfil.data
        
        return Response(response)
    
class perfilMidiaAPIView(APIView):
    serializer_class = MidiaSerializer

    def get(self, request, *args, **kwargs):
        response = {}
        if(request.query_params != {}):
            nameTagGet = request.query_params['nameTag']
            perfis = Perfil.objects.filter(nameTag=nameTagGet)
            if(len(perfis) != 0):
                midias = Midia.objects.filter(id_Perfil=perfis[0].id_Perfil)
                serializerMidia = MidiaSerializer(midias, many=True)
                response["Midia"] = serializerMidia.data
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

                    print(itensCompra, end="\n\n\n\n\n\n\n\n")
                    for itemCompra in itensCompra:
                        itemMercado   = ItensMercado.objects.get(id_ItemMercado=itemCompra.id_ItensMercado.id_ItemMercado)
                        perfilArtista = Perfil.objects.get(id_Perfil=itemMercado.id_Perfil.id_Perfil)

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
    
    def post(self, request, *args, **kwargs):

        perfilComprador = Perfil.objects.get(id_Perfil=request.data[0]["id_perfil_comprador"])
        compra = Compra.objects.create(perfilComprador=perfilComprador,
                                       metodoPagamento=request.data[0]["metodo_pagamento"])

        for data in request.data:
            itemMercado = ItensMercado.objects.get(id_ItemMercado=data["id_item_mercado"])

            itemCompra = Itemcompra.objects.create(id_Crompra      = compra,
                                                   id_ItensMercado = itemMercado,
                                                   detalhes        = data["detalhes"],
                                                   tipoCor         = data["tipo_cor"],
                                                   tipoFundo       = data["tipo_fundo"],
                                                   particao        = data["particao"],
                                                   cupom           = data["cupom"])
            
        return Response("OK")