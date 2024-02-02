from django.contrib import admin

from controle.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    search_fields = ['nome','codigo','estoque','preco']
    list_display = ('id', 'nome','codigo','estoque','preco','unidadePeso','ativo')
