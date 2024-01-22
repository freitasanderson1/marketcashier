from django.http import JsonResponse
from django.views import View

from cadastro.models import Cliente
from controle.models import Venda
from django.db.models import Q

from cadastro.serializers import ClienteSerializer

class GetContaClienteView(View):

    def get(self, request, *args, **kwargs):
        
        # print(f'Kwargs: {kwargs}')

        pk = kwargs.get('cpf')
        cliente = Cliente.objects.get(Q(cpf=pk)|Q(id=pk))

        # print(f'Cliente; {cliente}')

        vendas = Venda.objects.filter(
            cliente=cliente, 
            finalizado=True, 
            pago=False,
            ativo=True, 
        )

        listVendas = list()
        valores = list()

        for venda in vendas:
            dictVenda = {
                'info': f'Venda {venda.id} - {cliente} comprou R${venda.valor} em {venda.dataCadastro.strftime("%d/%m/%Y às %H:%M")}',
                'valor': venda.valor,
                'dataAlteracao': venda.dataAlteracao
            }
            valores.append(venda.valor)
            listVendas.append(dictVenda)

        soma = float(sum(valores))

        dict_cliente = {
                'nome': cliente.nomeCompleto,
                'cpf': cliente.cpf,
                'debito': soma,
                'vendas': listVendas,
            }
        
        # print(f'Valor do débito: {soma}')

        return JsonResponse(dict_cliente)