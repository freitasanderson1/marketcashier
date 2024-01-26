from django.http import JsonResponse
from django.views import View

from controle.models import Produto

from bs4 import BeautifulSoup
import requests

class GetProductNameView(View):

    def get(self, request, *args, **kwargs):
        
        barcode = kwargs.get('barcode').strip()
        
        
        try:
            produto = Produto.objects.get(codigo=barcode, ativo=True)

        except:
            produto = None

        if produto:

            product = {
                "name": "Produto já Cadastrado!",
                "barcode": barcode
            }
            
            return JsonResponse(product)

        url = f'https://api.cosmos.bluesoft.com.br/gtins/{barcode}.json'

        headers = {
            'X-Cosmos-Token': 'E5WjrXs-0DeTA9kbiMoFPQ',
            'Content-Type': 'application/json',
            'User-Agent': 'Cosmos-API-Request'
        }
        
        resp = requests.get(url, headers=headers).json()

        title = resp.get('description')

        if title:
            product = {
                "name": title,
                "barcode":barcode
            }
            return JsonResponse(product)
        
        # Site que será coletado
        site = f"https://go-upc.com/search?q={barcode}"

        # Coleta os dados do site
        html = requests.get(site).content

        # Formatando os dados
        dados = BeautifulSoup(html, 'html.parser')
        try:
            title = dados.find("h1", class_="product-name")
        except:
            title = None

        if title:
            product = {
                "name": title.text,
                "barcode":barcode
            }
            return JsonResponse(product)

        
        url = f"https://big-product-data.p.rapidapi.com/gtin/{barcode}"

        headers = {
            "X-RapidAPI-Key": "d3df2dfa78msh5f722f36d9e9a17p17165djsncf5f4aba2697",
            "X-RapidAPI-Host": "big-product-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        dados = response.json()
        try:
            title = dados['properties']['title'][0]
        except:
            title = None
        # print(title)
        
        if title:
            product = {
                "name": title,
                "barcode":barcode
            }

            return JsonResponse(product)

        url = "https://barcodes1.p.rapidapi.com/"

        querystring = {"query":barcode}

        headers = {
            "X-RapidAPI-Key": "d3df2dfa78msh5f722f36d9e9a17p17165djsncf5f4aba2697",
            "X-RapidAPI-Host": "barcodes1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        dados = response.json()
        try:
            title = dados['product']['title']
        except:
            title = None
        
        # print(title)
        
        if title:
            product = {
                "name": title,
                "barcode":barcode
            }

            return JsonResponse(product)

        url = "https://barcode-lookup.p.rapidapi.com/v3/products"

        querystring = {"barcode":barcode}

        headers = {
            "X-RapidAPI-Key": "d3df2dfa78msh5f722f36d9e9a17p17165djsncf5f4aba2697",
            "X-RapidAPI-Host": "barcode-lookup.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        
        dados = response.json()
        try:
            title = dados['products'][0]['title']
        except:
            title = None
        
        # print(title)
        # [print(f'{t} e Index: {index}\n') for t,index in enumerate(title)]
        
        if title:
            product = {
                "name": title,
                "barcode":barcode
            }

            return JsonResponse(product)

        url = "https://amazon-product10.p.rapidapi.com/amazon-product-data"

        payload = {
            "output": "json",
            "id": barcode,
            "type": "ean",
            "amazon_domain": "amazon.com"
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "d3df2dfa78msh5f722f36d9e9a17p17165djsncf5f4aba2697",
            "X-RapidAPI-Host": "amazon-product10.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        dados = response.json()

        try:
            title = dados['product']['title']
        except:
            title = None
        
        # print(title)
        # [print(f'{t} e Index: {index}\n') for t,index in enumerate(title)]
        
        if title:
            product = {
                "name": title,
                "barcode":barcode
            }

        else:
            product = {
                "name": 'Produto não encontrado!',
                "barcode":barcode
            }

        return JsonResponse(product)