from django.db import models


class Produto(models.Model):

    id = models.BigAutoField(primary_key=True)

    nome = models.TextField(u'Nome do Produto', max_length=255)
    
    estoque = models.FloatField(u'Estoque do Produto', null=False, blank=False, default=1.00)
    
    preco = models.FloatField(u'Valor do Quilo ou Unidade', null=False, blank=False, default=1.00)

    unidadePeso =  models.BooleanField(verbose_name=u'Unidade?', default=True, editable=True) #Unidade ou peso, se for no peso == False

    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome','id']

    def __str__(self):
        retorno = f'{self.nome} QTD: {self.estoque}'
        retorno += ' Unidades' if self.unidadePeso else ' Kgs'

        return retorno
