from django.http import JsonResponse
from django.views import View

from bs4 import BeautifulSoup
import requests

class GetProductNameView(View):

    def get(self, request, *args, **kwargs):
        
        barcode = kwargs.get('barcode')
        # Site que será coletado
        site = f"https://go-upc.com/search?q={barcode.strip()}"

        # Coleta os dados do site
        html = requests.get(site).content

        # Formatando os dados
        dados = BeautifulSoup(html, 'html.parser')

        title = dados.find("h1", class_="product-name")

        # print(f'{title.text}')

        product = {
            "name": title.text,
            "barcode":barcode
        }
        
        return JsonResponse(product)