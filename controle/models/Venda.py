from django.db import models

from django.contrib.auth.models import User

from cadastro.models import Cliente


class Venda(models.Model):
    
    id = models.BigAutoField(primary_key=True)

    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', null=True, on_delete=models.SET_NULL)
    
    vendedor = models.ForeignKey(User, verbose_name='Vendedor', null=True, on_delete=models.SET_NULL)

    valor = models.FloatField(u'Valor da Compra', null=False, blank=False, default=1.00)

    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)

    finalizado = models.BooleanField(verbose_name=u'Finalizado?', default=False, editable=True)
    
    pago = models.BooleanField(verbose_name=u'Pago?', default=False, editable=True)
    
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['id','dataCadastro']

    def __str__(self):
        cliente = self.cliente if self.cliente else 'Cliente sem Cadastro'
        string = f'Venda {self.id} - {cliente} comprou R${self.valor} em {self.dataCadastro.strftime("%d/%m/%Y às %H:%M")}'
        return string
    
    # def save(self):
    #     super(Venda, self).save()
        
    #     produtos = self.itens.filter(ativo=True).values('valorTotal')
        
    #     listaValores = list()

    #     [listaValores.append(float(valor['valorTotal'])) for valor in produtos]

    #     # print(listaValores)

    #     if produtos:
    #         self.valor = sum(listaValores)

    #     self.finalizarVenda()

    #     super(Venda, self).save()

    
    def finalizarVenda(self):

        itens = self.itens.filter(ativo=True)

        for item in itens:
            
            if item.produto.unidadePeso:
                item.produto.estoque -= item.quantidade
                item.produto.save()

        self.finalizado = True
        
        return