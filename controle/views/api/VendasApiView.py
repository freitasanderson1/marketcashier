from rest_framework import viewsets

from controle.models import Venda
from controle.serializers import VendaSerializer

class VendasApiView(viewsets.ModelViewSet):
    serializer_class = VendaSerializer

    def get_queryset(self):
        return Venda.objects.filter(ativo=True)
