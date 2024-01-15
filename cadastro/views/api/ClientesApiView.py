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

    def retrieve(self, request, *args, **kwargs):
        term = kwargs.get('pk')

        # print(f'Kwargs: {kwargs}')
        
        if term:
            try:
                queryset = Cliente.objects.filter(
                    Q(nomeCompleto__icontains=term)|
                    Q(cpf__icontains=term)
                )
                Cliente_serialized = ClienteSerializer(queryset, many=True)
                
                responseData = {
                    'clientes': Cliente_serialized.data,
                }

                # print(f'Dados Serializados: {responseData}')

                status=200
            except:
                responseData = {'mensagem': 'O ID do Cliente não existe.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     
                                                                                                                                                                                          
        return Response(responseData,status=status)