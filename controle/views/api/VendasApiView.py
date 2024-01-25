from rest_framework import viewsets
from rest_framework.response import Response

from cadastro.models import Cliente
from controle.models import Venda, Pagamento
from controle.serializers import VendaSerializer

class VendasApiView(viewsets.ModelViewSet):
    serializer_class = VendaSerializer

    def get_queryset(self):
        return Venda.objects.filter(ativo=True)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        data = request.data

        # print(f'Kwargs: {kwargs}')
        # print(f'Request: {data}')

        if pk:
            try:
                venda = Venda.objects.get(id=pk)
                venda.cliente = Cliente.objects.get(id=data.get('cliente')) if data.get('cliente') else None
                venda.finalizado = True

                if data.get('tipo'):
                    novoPagamento = Pagamento()

                    novoPagamento.valor = venda.valor if data.get('pago') == 'true' else float(data.get('valor'))
                    novoPagamento.tipo = data.get('tipo')
                    novoPagamento.save()

                    venda.pagamento = novoPagamento

                venda.save()

            # {'cliente': ['1'], 'pago': ['false'], 'valor': ['10'], 'tipo': ['1']}>

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