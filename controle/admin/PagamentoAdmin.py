from django.contrib import admin

from controle.models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):

    search_fields = ['id','tipo','valor']
    list_display = ('id', 'tipo','valor','ativo', 'dataCadastro', 'dataAlteracao')
