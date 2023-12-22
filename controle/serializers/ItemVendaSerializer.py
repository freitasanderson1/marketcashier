from rest_framework import serializers
from controle.models import ItemVenda

from controle.serializers import ProdutoSerializer, VendaSerializer

class ItemVendaSerializer(serializers.ModelSerializer):

    produto = ProdutoSerializer()
    # venda = VendaSerializer()

    class Meta:

        model = ItemVenda
        fields = '__all__'