from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Q

import json

from controle.models import ItemVenda, Produto, Venda
from controle.serializers import ItemVendaSerializer

class ItemVendaApiView(viewsets.ModelViewSet):
    serializer_class = ItemVendaSerializer

    def get_queryset(self):
        return ItemVenda.objects.filter(ativo=True)

    def create(self, request, *args, **kwargs):

        # print(f'Request Create: {request.POST}')
        data = request.POST
        
        produto = Produto.objects.get(id=data.get('produto'))

        # print(f'Produto: {produto}')


        novoItem = ItemVenda()
        novoItem.produto = produto
        novoItem.venda = Venda.objects.get(id=data.get('venda'))
        novoItem.quantidade = float(data.get('quantidade'))
        novoItem.valorTotal = float(data.get('quantidade')) * float(produto.preco)
        novoItem.save()

        queryset = ItemVenda.objects.filter(id=novoItem.id)
        ItemVenda_serialized = ItemVendaSerializer(queryset, many=True)
        responseData = ItemVenda_serialized.data[0]

        # print(f'Dados Serializados: {responseData}')

        # responseData = {'mensagem': 'Item Adicionado!',}
        status=201  

        return Response(responseData,status=status)
    
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            try:
                queryset = ItemVenda.objects.filter(venda__id=pk)
                ItemVenda_serialized = ItemVendaSerializer(queryset, many=True)
                soma = float(sum(item.valorTotal for item in queryset.filter(ativo=True)))
                # print(f'Soma: {soma}')
                
                venda = Venda.objects.get(id=pk)
                venda.valor = soma
                venda.save()

                responseData = {
                    'itens': ItemVenda_serialized.data,
                    'valor' : soma
                }

                # print(f'Dados Serializados: {responseData["valor"]}')

                status=200
            except:
                responseData = {'mensagem': 'O ID do ItemVenda não existe.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     
                                                                                                                                                                                          
        return Response(responseData,status=status)
    
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        # print(f'Kwargs: {kwargs}')
        
        if pk:
            try:
                itemVenda = ItemVenda.objects.get(id=pk)
                itemVenda.ativo = False

                itemVenda.save()

                # print(itemVenda, itemVenda.venda.id)

                responseData = {
                    'mensagem': 'O Item foi removido.',
                    'venda': itemVenda.venda.id,
                }

                status=200
            except:
                responseData = {'mensagem': 'O ID do ItemVenda não existe.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     

        return Response(responseData,status=status)
    