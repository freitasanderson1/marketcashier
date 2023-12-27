from django.views.generic import TemplateView

from controle.models import Produto

class CreateProductView(TemplateView):
    model = Produto
    template_name = 'cadastrarProduto.html'