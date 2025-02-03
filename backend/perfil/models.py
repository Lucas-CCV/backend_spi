from django.db import models
from uuid import uuid4, uuid1

# Create your models here.

def enviar_imagem_perfil(instance, filename):
    return f"{instance.id_perfil}_{filename}"

def enviar_imagem_itenMercado(instance, filename):
    return f"{instance.id_ItemMercado}_{filename}"

class Perfil(models.Model):
    id_perfil   = models.AutoField(primary_key=True, editable=False)
    nome        = models.CharField(max_length=20)
    nameTag     = models.CharField(max_length=20)
    descricao   = models.CharField(max_length=300)
    estrelas    = models.FloatField(default=0)
    particao    = models.IntegerField(default=100)
    foto        = models.ImageField(upload_to=enviar_imagem_perfil, blank=True, null=True)
    outrosSites = models.JSONField(default=dict, blank=True)
    tags        = models.JSONField(default=dict)

class ItensMercado(models.Model):
    id_ItemMercado = models.AutoField(primary_key=True, editable=False)
    perfil         = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    nome           = models.CharField(max_length=20)
    descricao      = models.CharField(max_length=100)
    preco          = models.FloatField(default=0)
    foto           = models.ImageField(upload_to=enviar_imagem_itenMercado, blank=True, null=True)
    tiposCor       = models.JSONField(default=dict, blank=True)
    tiposFundo     = models.JSONField(default=dict, blank=True)

class ItensCarrinho(models.Model):
    id_ItemCarrinho = models.AutoField(primary_key=True, editable=False)
    itensMercado    = models.ForeignKey(ItensMercado, on_delete=models.DO_NOTHING)
    perfilComprador = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    detalhes        = models.CharField(max_length=100)
    tipoCor         = models.CharField(max_length=20)
    tipoFundo       = models.CharField(max_length=20)

class Compra(models.Model):
    id_Crompra      = models.AutoField(primary_key=True, editable=False)
    perfilComprador = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    valorPago       = models.FloatField(default=0)
    dataPedido      = models.DateField(auto_now_add=True)
    dataEntrega     = models.DateField(blank=True, null=True)
    particao        = models.IntegerField(default=100)
    estatus         = models.CharField(max_length=20)
    alerta          = models.CharField(max_length=20, blank=True)

class Itemcompra(models.Model):
    id_ItemCompra   = models.AutoField(primary_key=True, editable=False)
    id_Crompra      = models.ForeignKey(Compra, on_delete=models.DO_NOTHING)
    itensMercado    = models.ForeignKey(ItensMercado, on_delete=models.DO_NOTHING)
    detalhes        = models.CharField(max_length=100)
    tipoCor         = models.CharField(max_length=20)
    tipoFundo       = models.CharField(max_length=20)