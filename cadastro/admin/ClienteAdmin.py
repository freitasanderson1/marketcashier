from django.contrib import admin

from cadastro.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nomeCompleto','cpf','celular','endereco','ativo')
    search_fields = ('cpf','nomeCompleto','celular')
    exclude = ('id',)