from django.db import models
from uuid import uuid4, uuid1

# Create your models here.

def enviar_imagem_perfil(instance, filename):
    return f"{instance.id_perfil}_{filename}"

def enviar_imagem_itenMercado(instance, filename):
    return f"{instance.perfil}_{filename}"


class Perfil(models.Model):
    id_perfil = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome      = models.CharField(max_length=20)
    nameTag   = models.CharField(max_length=20)
    estrelas  = models.FloatField(default=0)
    descricao = models.CharField(max_length=100)
    foto      = models.ImageField(upload_to=enviar_imagem_perfil, blank=True, null=True)

class ItensMercado(models.Model):
    id_ItemMercado = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    nome           = models.CharField(max_length=20)
    descricao      = models.CharField(max_length=100)
    preco          = models.FloatField(default=-1)
    foto           = models.ImageField(upload_to=enviar_imagem_itenMercado, blank=True, null=True)
    tiposCor       = models.JSONField(default=dict, blank=True)
    tiposFundo     = models.JSONField(default=dict, blank=True)
    perfil         = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)

class ItensCarrinho(models.Model):
    id_ItemCarrinho = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    itensMercado    = models.ForeignKey(ItensMercado, on_delete=models.DO_NOTHING)
    perfilComprador = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    detalhes        = models.CharField(max_length=100)
    tipoCor         = models.IntegerField(default=0)
    tipoFundo       = models.IntegerField(default=0)