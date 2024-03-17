from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q

from cadastro.models import Cliente
from controle.models import Venda, Pagamento
from controle.serializers import VendaSerializer

class VendasApiView(viewsets.ModelViewSet):
    serializer_class = VendaSerializer

    def get_queryset(self):
        return Venda.objects.filter(ativo=True).order_by('dataCadastro')

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        data = request.data

        # print(f'Kwargs: {kwargs}')
        # print(f'Request: {data}')

        if pk:
            try:
                venda = Venda.objects.get(id=pk)
                venda.cliente = Cliente.objects.get(id=data.get('cliente')) if data.get('cliente') else None
                venda.finalizado = True

                venda.valor = float(data.get('valorCompra')) if data.get('valorCompra') else venda.valor 
                
                if data.get('tipo'):
                    novoPagamento = Pagamento()

                    novoPagamento.valor = venda.valor if data.get('pago') == 'true' else float(data.get('valor'))
                    novoPagamento.tipo = data.get('tipo')
                    novoPagamento.venda = venda

                    novoPagamento.save()

                    

                venda.finalizarVenda()

                venda.save()

            # {'cliente': ['1'], 'pago': ['false'], 'valor': ['10'], 'tipo': ['1']}>

                # print(Venda, Venda.venda.id)
                if venda.pagamentosVenda.all():
                    listPagamentos = list()

                    for pagamento in venda.pagamentosVenda.all():
                        listPagamentos.append(round(pagamento.valor,2)) 
                    valorTotal = venda.valor

                    venda.valor = round(venda.valor + ((5/100)*venda.valor),2)
                    resta = round((venda.valor - sum(listPagamentos)),2)
                    desconto = round((venda.valor - valorTotal)-((5/100)*sum(listPagamentos)),2)

                else:
                    resta = venda.valor
                    valorTotal = round(resta + ((5/100)*resta),2)
                    desconto = round(valorTotal - resta,2)

                responseData = {
                    'mensagem': 'A Venda foi finalizada.',
                    'venda': venda.id,
                    'pago': resta,
                    'desconto': desconto
                }

                status=200
            except:
                responseData = {'mensagem': 'O ID da Venda não existe.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     

        return Response(responseData,status=status)
    
    def retrieve(self, request, *args, **kwargs):
        # print(f'Kwargs: {kwargs}')
        # print(f'Request: {request}')

        data = kwargs.get('pk').split('-')
        
        if data:
            try:
                data[1] = f'0{data[1]}' if len(data[1]) == 1 else data[1]

                # print(f'Data de Hoje: {data}')

                queryset = Venda.objects.filter(dataCadastro__year=data[2], 
                    dataCadastro__month=data[1],
                    dataCadastro__day=data[0],
                    finalizado=True,
                    ativo=True
                    ).order_by('dataCadastro')

                Venda_Serialized = VendaSerializer(queryset, many=True)

                responseData = Venda_Serialized.data

                # print(f'Dados Serializados: {responseData}')

                status=200
            except:
                responseData = {'mensagem': 'Não existe vendas.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     
                                                                                                                                                                                          
        return Response(responseData,status=status)