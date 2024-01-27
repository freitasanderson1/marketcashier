from rest_framework import serializers
from controle.models import Pagamento

from controle.serializers import VendaSerializer

class PagamentoSerializer(serializers.ModelSerializer):
    # venda = VendaSerializer()
    
    class Meta:

        model = Pagamento
        fields = '__all__'