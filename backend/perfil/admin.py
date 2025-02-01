from django.contrib import admin
from .models import Perfil, ItensMercado

# Register your models here.

admin.site.register([Perfil, ItensMercado])