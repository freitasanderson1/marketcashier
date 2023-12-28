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

    def create(self, request, *args, **kwargs):

        # print(f'Request Create: {request.POST}')
        
        data = request.POST

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
        produto.estoque = data.get('estoque')
        produto.preco = data.get('preco')

        produto.save()

        responseData = {'mensagem': 'Produto Editado!',}
        status=201  

        return Response(responseData,status=status)