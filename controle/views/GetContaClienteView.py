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
                'info': f'ID: {venda.id} - {cliente.nomeCompleto.split(' ')[0]} comprou R${venda.valor} em {venda.dataCadastro.strftime("%d/%m/%Y")}',
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
    
    def post(self, request, *args, **kwargs):
        
        # print(f'Request: {kwargs}')

        pk = kwargs.get('cpf')
        cliente = Cliente.objects.get(Q(cpf=pk)|Q(id=pk))

        valor = float(request.POST.get('valor'))

        vendas = Venda.objects.filter(
            cliente=cliente, 
            finalizado=True, 
            pago=False,
            ativo=True, 
        )

        for venda in vendas:

            # print(f'Valor da Venda: {venda.valor}')
            
            if valor > 0.00:

                if valor >= venda.valor:
                    valor -= venda.valor
                    venda.pago = True
                else:
                    valor -= venda.valor
                    venda.valor = valor * (-1)
                    valor = 0

                    # print(f'Dessa venda ainda falta: {venda.valor}')

                venda.save()

            # print(f'{cliente.nomeCompleto} ainda tem {valor}')
        valores = list()

        for venda in vendas.filter(pago=False):
            valores.append(venda.valor)

        soma = float(sum(valores))

        response = {
            'pago':float(request.POST.get('valor')),
            'resta': float(soma),
        }

        return JsonResponse(response)
