from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Q

import json

from cadastro.models import Cliente
from cadastro.serializers import ClienteSerializer

class ClientesApiView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(ativo=True).order_by('nomeCompleto')
