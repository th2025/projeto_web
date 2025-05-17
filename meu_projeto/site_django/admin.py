from django.contrib import admin
from .models import Produto, Usuario

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)    
