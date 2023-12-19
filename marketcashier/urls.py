from django.contrib import admin
from django.urls import path

from cadastro.views import LoginView, SairView
from controle.views import IndexMarket

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexMarket.as_view(), name='index'),

    #Logins views
    path('login/', LoginView.as_view(), name='login'),
    path('sair/', SairView.as_view(), name='sair'),
]
