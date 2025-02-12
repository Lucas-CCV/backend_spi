from django.db import models
from uuid import uuid4, uuid1

# Create your models here.

def enviar_imagem_perfil(instance, filename):
    return f"{instance.id_Perfil}_{filename}"

def enviar_imagem_midia(instance, filename):
    return f"{instance.id_Perfil.id_Perfil}_{instance.id_Midia}_{filename}"

def enviar_imagem_itenMercado(instance, filename):
    return f"{instance.id_Perfil.id_Perfil}_{instance.id_ItemMercado}_{filename}"

class Perfil(models.Model):
    id_Perfil   = models.AutoField(primary_key=True, editable=False)
    nome        = models.CharField(max_length=20)
    nameTag     = models.CharField(max_length=20)
    descricao   = models.CharField(max_length=300)
    estrelas    = models.FloatField(default=0)
    particao    = models.FloatField(default=0)
    foto        = models.ImageField(upload_to=enviar_imagem_perfil, blank=True, null=True)
    outrosSites = models.JSONField(default=dict, blank=True)
    tags        = models.JSONField(default=dict)

class midia(models.Model):
    id_Midia     = models.AutoField(primary_key=True, editable=False)
    id_Perfil    = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    foto         = models.ImageField(upload_to=enviar_imagem_midia, blank=True, null=True)
    dataPostagem = models.DateField(auto_now_add=True)

class ItensMercado(models.Model):
    id_ItemMercado = models.AutoField(primary_key=True, editable=False)
    id_Perfil      = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
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
    dataPedido      = models.DateField(auto_now_add=True)
    metodoPagamento = models.JSONField(default=dict)
    
class Itemcompra(models.Model):
    id_ItemCompra   = models.AutoField(primary_key=True, editable=False)
    id_Crompra      = models.ForeignKey(Compra, on_delete=models.DO_NOTHING)
    id_ItensMercado = models.ForeignKey(ItensMercado, on_delete=models.DO_NOTHING)
    dataEntrega     = models.DateField(blank=True)
    detalhes        = models.CharField(max_length=100)
    estatus         = models.CharField(max_length=20, blank=True)
    alerta          = models.CharField(max_length=20, blank=True)
    tipoCor         = models.CharField(max_length=20)
    tipoFundo       = models.CharField(max_length=20)
    particao        = models.FloatField(default=0)
    cupom           = models.FloatField(default=0)


"""

{
"twitter":"https://x.com/LouisLrnt"
}

{
"preto e branco":50,
"chapada":65,
"sombreado":85
}

{
"sem fundo":0,
"com fundo":15
}

{
"tipo":"pix",
"final":""
}


"""    