from django.db import models

from controle.models import Produto, Venda

class ItemVenda(models.Model):

    id = models.BigAutoField(primary_key=True)

    produto = models.ForeignKey(Produto, verbose_name='Produto',null=True, on_delete=models.SET_NULL)

    venda = models.ForeignKey(Venda, verbose_name='Venda', related_name='itens', null=True, on_delete=models.CASCADE)

    quantidade = models.FloatField(u'Quantidade', null=False, blank=False, default=1.00)

    valorTotal = models.FloatField(u'Valor da Total', null=False, blank=False, default=1.00)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = 'Item da venda'
        verbose_name_plural = 'Itens das vendas'
        ordering = ['id']

    def __str__(self):
        return f'Item: {self.id} - {self.produto} - {self.quantidade} - {self.valorTotal}'
    
    def save(self):

        self.valorTotal = round((self.produto.preco * self.quantidade), 2)

        super(ItemVenda, self).save()
