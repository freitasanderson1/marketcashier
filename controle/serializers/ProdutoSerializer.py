from rest_framework import serializers
from controle.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = '__all__'