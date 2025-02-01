from django.db import models
from uuid import uuid4

# Create your models here.

def enviar_imagem_perfil(instance, filename):
    return f"{instance.perfil.id_perfil}_{filename}"

def enviar_imagem_itenMercado(instance, filename):
    return f"{instance.perfil}_{filename}"

class Perfil(models.Model):
    id_perfil = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome      = models.CharField(max_length=20)
    nameTag   = models.CharField(max_length=20)
    estrelas  = models.IntegerField(default=0)
    descricao = models.CharField(max_length=100)
    foto      = models.ImageField(upload_to=enviar_imagem_perfil, blank=True, null=True)

class ItensMercado(models.Model):
    nome      = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    preco     = models.FloatField(default=-1)
    foto      = models.ImageField(upload_to=enviar_imagem_perfil, blank=True, null=True)
    perfil    = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)