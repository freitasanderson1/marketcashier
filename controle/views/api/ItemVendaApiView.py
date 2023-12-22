from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Q

import json

from controle.models import ItemVenda
from controle.serializers import ItemVendaSerializer

class ItemVendaApiView(viewsets.ModelViewSet):
    serializer_class = ItemVendaSerializer

    def get_queryset(self):
        return ItemVenda.objects.filter(ativo=True)
