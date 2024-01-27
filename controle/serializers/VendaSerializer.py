from rest_framework import serializers
from controle.models import Venda

from cadastro.serializers import ClienteSerializer
class VendaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(required=False)
    class Meta:

        model = Venda
        fields = '__all__'