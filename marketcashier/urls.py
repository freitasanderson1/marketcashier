from django.contrib import admin
from django.urls import path

from cadastro.views import LoginView, SairView, ClientesApiView
from controle.views import IndexMarket, GetProductNameView, GetContaClienteView

from controle.views import VendasApiView, ProdutosApiView, ItemVendaApiView, PagamentosApiView

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexMarket.as_view(), name='index'),
    path('product/<str:barcode>', GetProductNameView.as_view(), name='getProductName'),
    path('cliente/<str:cpf>', GetContaClienteView.as_view(), name='getClienteConta'),


    #Logins views
    path('login/', LoginView.as_view(), name='login'),
    path('sair/', SairView.as_view(), name='sair'),
]

router = DefaultRouter(trailing_slash=False)
router.register(r'api/dados_vendas',VendasApiView, basename='VendasApi')
router.register(r'api/dados_produtos',ProdutosApiView, basename='ProdutosApi')
router.register(r'api/dados_pagamentos',PagamentosApiView, basename='PagamentosApi')
router.register(r'api/dados_item_venda',ItemVendaApiView, basename='ItemVendaApi')

router.register(r'api/dados_clientes',ClientesApiView, basename='ClientesApi')


urlpatterns += router.urls