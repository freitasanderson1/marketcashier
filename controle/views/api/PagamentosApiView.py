from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Q

import json

from controle.models import Pagamento
from controle.serializers import PagamentoSerializer

class PagamentosApiView(viewsets.ModelViewSet):
    serializer_class = PagamentoSerializer

    def get_queryset(self):

        queryset = Pagamento.objects.filter(ativo=True)
        
        listPagamentos = {
            'dinheiro': list(),
            'pix': list(),
            'debito': list(),
            'credito': list()
        }
        
        for pagamento in queryset:
            match pagamento.tipo:
                case 1:
                    listPagamentos['dinheiro'].append(round(pagamento.valor,2))
                case 2:
                    listPagamentos['pix'].append(round(pagamento.valor,2))
                case 3:
                    listPagamentos['debito'].append(round((pagamento.valor*0.9801),2))
                case 4:
                    listPagamentos['credito'].append(round((pagamento.valor*0.9502),2))
                case _:
                    return
        Pagamento_Serialized = PagamentoSerializer(queryset, many=True)


        responseData = {
            'pagamentos':listPagamentos,
            'lista': Pagamento_Serialized.data
        }

        # print(f'Dados Serializados: {responseData}')

        return responseData

    def retrieve(self, request, *args, **kwargs):
        # print(f'Kwargs: {kwargs}')
        # print(f'Request: {request}')

        data = kwargs.get('pk').split('-')
        
        if data:
            try:
                data[1] = f'0{data[1]}' if len(data[1]) == 1 else data[1]

                # print(f'Data de Hoje: {data}')

                queryset = Pagamento.objects.filter(dataCadastro__year=data[2], 
                    dataCadastro__month=data[1],
                    dataCadastro__day=data[0],
                    ativo=True
                    ).order_by('dataCadastro')
                
                listPagamentos = {
                    'dinheiro': list(),
                    'pix': list(),
                    'debito': list(),
                    'credito': list()
                }

                for pagamento in queryset:
                    match pagamento.tipo:
                        case 1:
                            listPagamentos['dinheiro'].append(round(pagamento.valor,2))
                        case 2:
                            listPagamentos['pix'].append(round(pagamento.valor,2))
                        case 3:
                            listPagamentos['debito'].append(round((pagamento.valor*0.9801),2))
                        case 4:
                            listPagamentos['credito'].append(round((pagamento.valor*0.9502),2))
                        case _:
                            return
                Pagamento_Serialized = PagamentoSerializer(queryset, many=True)


                responseData = {
                    'pagamentos':listPagamentos,
                    'lista': Pagamento_Serialized.data
                }

                # print(f'Dados Serializados: {responseData}')

                status=200
            except:
                responseData = {'mensagem': 'Não existe Pagamentos.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     
                                                                                                                                                                                          
        return Response(responseData,status=status)