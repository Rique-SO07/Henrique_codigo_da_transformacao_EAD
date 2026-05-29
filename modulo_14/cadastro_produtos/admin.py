from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Exibe as colunas organizadas dentro do painel do Django
    list_display = ('nome', 'preco', 'quantidade')
    # Adiciona uma barra de pesquisa pelo nome do produto
    search_fields = ('nome',)