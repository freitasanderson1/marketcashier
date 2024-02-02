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
    
    def create(self, request, *args, **kwargs):
        data = request.POST

        # print(f'request: {data}')

        try:
            existeCliente = Cliente.objects.get(cpf=data.get('cpf'))

            responseData = {'mensagem': 'O CPF desse Cliente já está cadastrado.'}

            status = 409

        except:
            novoCliente = Cliente()

            novoCliente.nomeCompleto = data.get('nomeCompleto')
            novoCliente.cpf = data.get('cpf')
            novoCliente.celular = data.get('celular')
            novoCliente.endereco = data.get('endereco')
            novoCliente.dataNascimento = data.get('dataNascimento')
            novoCliente.nomeCompleto = data.get('nomeCompleto')

            novoCliente.save()

            queryset = Cliente.objects.filter(id=novoCliente.id)

            Cliente_serialized = ClienteSerializer(queryset, many=True)
            
            queryset = Cliente.objects.filter(id=novoCliente.id)
            Cliente_serialized = ClienteSerializer(queryset, many=True)
            responseData = Cliente_serialized.data[0]

            # print(f'Dados Serializados: {responseData}')

            status=200

        return Response(responseData,status=status)