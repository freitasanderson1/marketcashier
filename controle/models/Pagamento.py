from django.db import models

from controle.models import Venda

TIPO_PAGAMENTO = (
        (1, 'Dinheiro'),
        (2, 'Pix'),
        (3, 'Débito'),
        (4, 'Crédito'),
)

class Pagamento(models.Model):
    
    id = models.BigAutoField(primary_key=True)

    valor = models.FloatField(u'Valor da Compra', null=False, blank=False, default=0.00)

    venda = models.ForeignKey(Venda, verbose_name='Venda', related_name='pagamentosVenda', null=True, on_delete=models.CASCADE)

    tipo = models.IntegerField('Tipo do Pagamento', choices=TIPO_PAGAMENTO, null=False, default=1)

    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)
    
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id','dataCadastro']