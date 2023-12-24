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
        print(f'Request: {request.POST}')
        return super().create(request, *args, **kwargs)