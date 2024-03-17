from django.http import JsonResponse
from django.views import View

from cadastro.models import Cliente
from controle.models import Venda, Pagamento
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
            ativo=True, 
        )

        listVendas = list()
        valores = list()

        for venda in vendas:
            if not venda.check_pago():
                if venda.pagamentosVenda.all():
                    listPagamentos = list()

                    [listPagamentos.append(pagamento.valor) for pagamento in venda.pagamentosVenda.all()]

                    valorTotal = round(venda.valor,2)
                    valorPago = round(sum(listPagamentos),2)
                    resta = round(valorTotal - valorPago,2)
                else:
                    resta = round(venda.valor,2)
                
                if resta > 0.0000:
                    dictVenda = {
                        'info': f'ID: {venda.id} - {cliente.nomeCompleto.split(" ")[0]} deve R${resta} de uma compra em {venda.dataCadastro.strftime("%d/%m/%Y")}',
                        'valor': resta,
                        'dataAlteracao': venda.dataAlteracao
                    }
                    valores.append(resta)
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
        
        print(f'Request: {request.POST}')

        pk = kwargs.get('cpf')
        cliente = Cliente.objects.get(Q(cpf=pk)|Q(id=pk))

        valor = float(request.POST.get('valor'))
        tipo = int(request.POST.get('tipo'))

        vendas = Venda.objects.filter(
            cliente=cliente, 
            finalizado=True, 
            ativo=True, 
        )

        for venda in vendas:

            if not venda.check_pago():
            
                if valor > 0.00:

                    if venda.pagamentosVenda.all():
                        listPagamentos = list()

                        [listPagamentos.append(pagamento.valor) for pagamento in venda.pagamentosVenda.all()]

                        soma = sum(listPagamentos)

                        resta = venda.valor - soma
                    else:
                        resta = venda.valor

                    if valor >= resta:
                        valor -= resta

                        novoPagamento = Pagamento()

                        novoPagamento.valor = round(resta,2)
                        novoPagamento.tipo = tipo
                        novoPagamento.venda = venda

                        novoPagamento.save()



                    else:
                        novoPagamento = Pagamento()

                        novoPagamento.valor = round(valor,2)
                        novoPagamento.tipo = tipo
                        novoPagamento.venda = venda
                        novoPagamento.save()

                        valor = 0


                        print(f'Dessa venda ainda falta: {venda.valor}')

                    venda.save()

            print(f'{cliente.nomeCompleto} ainda tem {valor}')
            
        valores = list()

        for venda in vendas:
            if not venda.check_pago():
                listPagamentos = list()

                [listPagamentos.append(pagamento.valor) for pagamento in venda.pagamentosVenda.all()]

                resta = round((venda.valor - sum(listPagamentos)),2)

                valores.append(resta)

        soma = float(sum(valores)) if valores else 0

        response = {
            'pago':float(request.POST.get('valor')),
            'resta': float(soma),
        }

        return JsonResponse(response)
