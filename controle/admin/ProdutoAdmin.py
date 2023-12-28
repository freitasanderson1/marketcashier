from django.contrib import admin

from controle.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    search_fields = ['nome','estoque','preco']
    list_display = ('id', 'nome','codigo','estoque','preco','unidadePeso','ativo')
