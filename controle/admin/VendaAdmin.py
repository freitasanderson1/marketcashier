from django.contrib import admin

from controle.models import Venda, ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

    autocomplete_fields = ('produto',)

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    search_fields = ['cliente']
    list_display = ('id', 'cliente','vendedor','valor','dataCadastro', 'finalizado','pago','ativo')
    inlines = [
        ItemVendaInline    
    ]
