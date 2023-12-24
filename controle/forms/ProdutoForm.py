from django import forms

from controle.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','estoque','preco','unidadePeso']
        
    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'