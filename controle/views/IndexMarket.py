from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from controle.models import Venda

class IndexMarket(LoginRequiredMixin,TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context