from django.contrib import admin
from .models import Perfil, ItensMercado, ItensCarrinho

# Register your models here.

admin.site.register([Perfil, ItensMercado, ItensCarrinho])