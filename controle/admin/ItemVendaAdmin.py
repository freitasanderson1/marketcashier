from django.contrib import admin

from controle.models import ItemVenda

@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    search_fields = ['produto','quantidade','valorTotal']
    autocomplete_fields = ['produto']
    list_display = ('id', 'produto','quantidade', 'valorTotal','ativo')
