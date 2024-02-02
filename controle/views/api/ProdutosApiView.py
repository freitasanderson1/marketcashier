from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Q

import json

from controle.models import Produto
from controle.serializers import ProdutoSerializer

class ProdutosApiView(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        return Produto.objects.filter(ativo=True)

    def retrieve(self, request, *args, **kwargs):
        barcode = kwargs.get('pk')

        if barcode:
            # print(f"BARCODE do Produto: {barcode}")
            try:
                queryset = Produto.objects.filter(
                    Q(nome__icontains=barcode)|
                    Q(codigo__icontains=barcode)
                )
                Produto_serialized = ProdutoSerializer(queryset, many=True)
                responseData = Produto_serialized.data
                # print(f'Dados Serializados: {responseData}')
                status=200
            except:
                responseData = {'mensagem': 'O ID do Produto não existe.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     
                                                                                                                                                                                          
        return Response(responseData,status=status)
    
    def create(self, request, *args, **kwargs):

        # print(f'Request Create: {request.POST}')
        
        data = request.POST

        try:
            produto = Produto.objects.get(codigo=data.get('codigo'))
            
            responseData = {'mensagem': 'Já existe um Produto com esse código Cadastrado!',}
            status=409	 

        except:
            produto = Produto()

            produto.nome = data.get('nome').strip()
            produto.codigo = data.get('codigo')
            produto.unidadePeso = True if data.get('unidadePeso') == 'true' else False
            produto.estoque = data.get('estoque')
            produto.preco = data.get('preco')
            produto.ativo = True
            produto.save()

            responseData = {'mensagem': 'Produto Cadastrado!',}
            status=201  

        return Response(responseData,status=status)
    
    def update(self, request, *args, **kwargs):

        # print(f'Request Update: {request.POST}')

        data = request.POST

        produto = Produto.objects.get(id=data.get('id'))

        produto.nome = data.get('nome')
        produto.codigo = data.get('codigo')
        produto.estoque = data.get('estoque')
        produto.preco = data.get('preco')

        produto.save()

        responseData = {'mensagem': 'Produto Editado!',}
        status=201  

        return Response(responseData,status=status)