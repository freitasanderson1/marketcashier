from django.contrib.auth.models import User
from django.db import models


class Cliente(models.Model):

    nomeCompleto= models.CharField(verbose_name=u'Nome Completo',max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=False, unique=True)

    celular = models.CharField('Celular com DDD',max_length=255, null=True, blank=True, help_text='Fone de contato com DDD (74) 98765-4321', default=None)
    
    endereco= models.CharField(verbose_name=u'Endereço',max_length=1000)

    dataNascimento = models.DateField('Data de Nascimento', null=True, blank=True)

    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)
    dataUltimaAlteracao = models.DateTimeField('Última alteração', null=True, blank=True, auto_now=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?',default=True, editable=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nomeCompleto','ativo']

    def natural_key(self):
        return self.nomeCompleto
	
    def retornoComCpf(self):
        
        numeroCpf = self.cpf
        parte0 = '***.'
        parte1 = numeroCpf[3:6]+"."#01164334182
        parte2 = numeroCpf[6:9]+"-"        
        parte3 = '**'
        numero = parte0+parte1+parte2+parte3

        return self.nomeCompleto+' - '+numero

    def retornoCpfFormatado(self):
        numeroCpf = self.cpf
        parte0 = numeroCpf[0:3]+"."#01164334182
        parte1 = numeroCpf[3:6]+"."#01164334182
        parte2 = numeroCpf[6:9]+"-"
        parte3 = numeroCpf[9:11]
        numero = parte0+parte1+parte2+parte3

        return numero

    def __str__(self):

        try:
            return self.retornoComCpf()
        except:
            return self.nomeCompleto
