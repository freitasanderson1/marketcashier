from rest_framework import viewsets
from rest_framework.response import Response

from cadastro.models import Cliente
from controle.models import Venda
from controle.serializers import VendaSerializer

class VendasApiView(viewsets.ModelViewSet):
    serializer_class = VendaSerializer

    def get_queryset(self):
        return Venda.objects.filter(ativo=True)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        print(f'Kwargs: {kwargs}')
        print(f'Request: {request.data}')
        
        if pk:
            try:
                venda = Venda.objects.get(id=pk)
                venda.cliente = Cliente.objects.get(id=request.data.get('cliente')) if request.data.get('cliente') else None
                venda.finalizado = True
                venda.pago = True if request.data.get('pago') else False
                venda.save()

                # print(Venda, Venda.venda.id)

                responseData = {
                    'mensagem': 'A Venda foi finalizada.',
                    'venda': venda.id,
                }

                status=200
            except:
                responseData = {'mensagem': 'O ID da Venda não existe.'}
                status=400
        else:
            responseData = {'mensagem': 'A API não recebeu os parâmetros necessários.'}
            status=412     

        return Response(responseData,status=status)